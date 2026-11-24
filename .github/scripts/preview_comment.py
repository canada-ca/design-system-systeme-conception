#!/usr/bin/env python3
"""Build the PR preview markdown comment body."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit


START_MARKER = "<!-- preview-urls:start -->"
END_MARKER = "<!-- preview-urls:end -->"
PAGE_EXTENSIONS = {".md", ".markdown", ".html"}
POST_RE = re.compile(r"^_posts/(\d{4})-(\d{2})-(\d{2})-([^/]+)\.(md|markdown|html)$")
MAX_OTHER_FILES = 15


@dataclass(frozen=True)
class PreviewTarget:
    base_url: str
    staging_dir: Path


@dataclass(frozen=True)
class PagePreview:
    source_path: str
    language: str
    built_path: str
    url: str
    alternate_built_path: str | None


class AlternateLinkParser(HTMLParser):
    def __init__(self, other_language: str) -> None:
        super().__init__()
        self.other_language = other_language
        self.in_head = False
        self.href: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "head":
            self.in_head = True
            return

        if not self.in_head or tag != "link" or self.href is not None:
            return

        attributes = {name.lower(): value for name, value in attrs if value is not None}
        rel_values = set(attributes.get("rel", "").lower().split())
        if "alternate" in rel_values and attributes.get("hreflang", "").lower() == self.other_language:
            self.href = attributes.get("href")

    def handle_endtag(self, tag: str) -> None:
        if tag == "head":
            self.in_head = False


def markdown_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")


def url_path(value: str) -> str:
    return quote(value, safe="/:@")


def markdown_link(label: str, url: str) -> str:
    return f"[{markdown_text(label)}]({url})"


def built_relative_path(language_relative_path: str) -> str | None:
    extension = Path(language_relative_path).suffix.lower()
    if extension not in PAGE_EXTENSIONS:
        return None

    post_match = POST_RE.match(language_relative_path)
    if post_match:
        year, month, day, slug = post_match.groups()[:4]
        return f"{year}/{month}/{day}/{slug}.html"

    if extension in {".md", ".markdown"}:
        return f"{language_relative_path[: -len(extension)]}.html"

    return language_relative_path


def alternate_built_relative_path(html_path: Path, other_language: str, other_base_url: str) -> str | None:
    parser = AlternateLinkParser(other_language)
    try:
        parser.feed(html_path.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return None

    if not parser.href:
        return None

    base_parts = urlsplit(other_base_url.rstrip("/"))
    href_parts = urlsplit(parser.href)
    base_path = base_parts.path.rstrip("/") + "/"

    if href_parts.scheme or href_parts.netloc:
        if href_parts.scheme != base_parts.scheme or href_parts.netloc != base_parts.netloc:
            return None
        href_path = href_parts.path
    else:
        href_path = href_parts.path

    if not href_path.startswith(base_path):
        return None

    relative_path = unquote(href_path[len(base_path) :])
    return relative_path or None


def classify_path(path: str, repo: str, sha: str, en: PreviewTarget, fr: PreviewTarget) -> tuple[str, PagePreview | str]:
    target: PreviewTarget | None = None
    other_target: PreviewTarget | None = None
    language_relative_path: str | None = None
    language: str | None = None
    other_language: str | None = None

    if path.startswith("en/"):
        target = en
        other_target = fr
        language_relative_path = path[3:]
        language = "en"
        other_language = "fr"
    elif path.startswith("fr/"):
        target = fr
        other_target = en
        language_relative_path = path[3:]
        language = "fr"
        other_language = "en"

    if (
        target is not None
        and other_target is not None
        and language_relative_path is not None
        and language is not None
        and other_language is not None
    ):
        built_path = built_relative_path(language_relative_path)
        built_file = target.staging_dir / Path(*built_path.split("/")) if built_path else None
        if built_path and built_file and built_file.is_file():
            url = f"{target.base_url}/{url_path(built_path)}"
            alternate_built_path = alternate_built_relative_path(built_file, other_language, other_target.base_url)
            return "page", PagePreview(path, language, built_path, url, alternate_built_path)

    blob_url = f"https://github.com/{repo}/blob/{sha}/{url_path(path)}"
    return "other", markdown_link(path, blob_url)


def build_other_rows(other_files: list[str]) -> list[str]:
    shown = other_files[:MAX_OTHER_FILES]
    rows = [f"| {item} |" for item in shown]
    overflow = len(other_files) - len(shown)
    if overflow > 0:
        overflow_word = "file" if overflow == 1 else "files"
        rows.append(f"| *...and {overflow} more {overflow_word}* |")
    return rows


def build_page_rows(page_previews: list[PagePreview], en_base: str, fr_base: str) -> list[str]:
    changed_pages: dict[tuple[str, str], PagePreview] = {}

    for preview in page_previews:
        key = (preview.language, preview.built_path)
        existing = changed_pages.get(key)
        if existing is None or preview.source_path < existing.source_path:
            changed_pages[key] = preview

    rows = [
        f"| Site home | {markdown_link(f'{en_base}/', f'{en_base}/')} | {markdown_link(f'{fr_base}/', f'{fr_base}/')} |"
    ]
    preview_rows: list[tuple[str, PagePreview | None, PagePreview | None]] = []
    rendered: set[tuple[str, str]] = set()

    for key in sorted(changed_pages):
        if key in rendered:
            continue

        preview = changed_pages[key]
        other_language = "fr" if preview.language == "en" else "en"
        other_preview = (
            changed_pages.get((other_language, preview.alternate_built_path))
            if preview.alternate_built_path is not None
            else None
        )

        if other_preview is not None and other_preview.alternate_built_path == preview.built_path:
            en_preview = preview if preview.language == "en" else other_preview
            fr_preview = preview if preview.language == "fr" else other_preview
            identity = en_preview.built_path
            preview_rows.append((identity, en_preview, fr_preview))
            rendered.add((en_preview.language, en_preview.built_path))
            rendered.add((fr_preview.language, fr_preview.built_path))
            continue

        identity = preview.built_path
        en_preview = preview if preview.language == "en" else None
        fr_preview = preview if preview.language == "fr" else None
        preview_rows.append((identity, en_preview, fr_preview))
        rendered.add(key)

    for identity, en_preview, fr_preview in sorted(
        preview_rows,
        key=lambda row: (
            row[0],
            row[1].built_path if row[1] else "",
            row[2].built_path if row[2] else "",
        ),
    ):
        en_cell = markdown_link(en_preview.built_path, en_preview.url) if en_preview else "—"
        fr_cell = markdown_link(fr_preview.built_path, fr_preview.url) if fr_preview else "—"
        rows.append(f"| {markdown_text(identity)} | {en_cell} | {fr_cell} |")

    return rows


def build_comment(
    *,
    pr_number: str,
    repo: str,
    sha: str,
    preview_host: str,
    en_dir: str,
    fr_dir: str,
    staging_en: str,
    staging_fr: str,
    changed_paths: list[str],
) -> str:
    preview_host = preview_host.rstrip("/")
    en_base = f"{preview_host}/{en_dir}/pr-preview/pr-{pr_number}"
    fr_base = f"{preview_host}/{fr_dir}/pr-preview/pr-{pr_number}"
    en = PreviewTarget(en_base, Path(staging_en))
    fr = PreviewTarget(fr_base, Path(staging_fr))

    page_previews: list[PagePreview] = []
    other_files: list[str] = []

    for path in changed_paths:
        if not path:
            continue
        kind, preview_or_link = classify_path(path, repo, sha, en, fr)
        if kind == "page":
            if isinstance(preview_or_link, PagePreview):
                page_previews.append(preview_or_link)
        else:
            if isinstance(preview_or_link, str):
                other_files.append(preview_or_link)

    page_rows = build_page_rows(page_previews, en_base, fr_base)
    other_rows = build_other_rows(other_files)
    short_sha = sha[:7]

    lines = [
        START_MARKER,
        "## 🚀 PR Preview",
        "",
        f"Latest commit: {markdown_link(short_sha, f'https://github.com/{repo}/commit/{sha}')}",
        "",
        "| Page | English | French |",
        "| --- | --- | --- |",
        *page_rows,
        "",
        "## 📁 Other changed files",
        "",
    ]
    if other_rows:
        lines.extend(["| File |", "| --- |", *other_rows, ""])
    else:
        lines.extend(["_None_", ""])

    lines.extend([
        "---",
        "",
        "<sub><em>Preview updates automatically with each commit.</em></sub>",
        END_MARKER,
    ])
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--sha", required=True)
    parser.add_argument("--preview-host", required=True)
    parser.add_argument("--en-dir", required=True)
    parser.add_argument("--fr-dir", required=True)
    parser.add_argument("--staging-en", required=True)
    parser.add_argument("--staging-fr", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    changed_paths = [line.rstrip("\r\n") for line in sys.stdin]
    sys.stdout.write(
        build_comment(
            pr_number=args.pr,
            repo=args.repo,
            sha=args.sha,
            preview_host=args.preview_host,
            en_dir=args.en_dir,
            fr_dir=args.fr_dir,
            staging_en=args.staging_en,
            staging_fr=args.staging_fr,
            changed_paths=changed_paths,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
