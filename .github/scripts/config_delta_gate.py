#!/usr/bin/env python3
"""Compare built site trees after removing the staging URL prefix."""

import argparse
import difflib
import os
import sys


def collect_files(root):
    """Return paths for all files under root."""
    files = {}
    if not os.path.isdir(root):
        return files
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            files[rel] = full
    return files


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def is_binary(raw):
    """A file is treated as binary (byte-compared, not normalized) when it
    contains NUL bytes. HTML/text files occasionally hold a stray non-UTF-8
    byte but never NUL, so they still get normalized via a latin-1 decode."""
    return b"\x00" in raw


def read_normalized(raw, baseurl):
    return raw.decode("latin-1").replace(baseurl, "")


def short_diff(rel, a_lines, b_lines):
    """Return a short unified-diff excerpt for reporting."""
    diff = list(
        difflib.unified_diff(
            a_lines, b_lines, fromfile=f"staging/{rel}", tofile=f"production/{rel}",
            lineterm="",
        )
    )
    if len(diff) > 40:
        diff = diff[:40] + ["... [truncated] ..."]
    return "\n".join(diff)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Config delta gate.")
    parser.add_argument("--staging", required=True, help="staging site tree")
    parser.add_argument("--production", required=True, help="production site tree")
    parser.add_argument("--baseurl", required=True, help="staging baseurl prefix")
    args = parser.parse_args(argv)

    staging = collect_files(args.staging)
    production = collect_files(args.production)

    if not staging or not production:
        print("FAIL: both build trees must contain files.", file=sys.stderr)
        return 1

    staging_paths = set(staging)
    production_paths = set(production)

    only_staging = sorted(staging_paths - production_paths)
    only_production = sorted(production_paths - staging_paths)

    if only_staging or only_production:
        if only_staging:
            print("FAIL: files only in staging:", file=sys.stderr)
            for p in only_staging:
                print("  + " + p, file=sys.stderr)
        if only_production:
            print("FAIL: files only in production:", file=sys.stderr)
            for p in only_production:
                print("  - " + p, file=sys.stderr)
        return 1

    failures = 0
    for rel in sorted(staging_paths):
        s_raw = read_bytes(staging[rel])
        p_raw = read_bytes(production[rel])

        # Binary files (images, fonts, ...): compare raw bytes.
        if is_binary(s_raw) or is_binary(p_raw):
            if s_raw != p_raw:
                print("FAIL: binary file differs outside config delta: " + rel, file=sys.stderr)
                failures += 1
            continue

        s_norm = read_normalized(s_raw, args.baseurl)
        p_norm = read_normalized(p_raw, args.baseurl)
        if s_norm != p_norm:
            print("FAIL: difference outside enumerated config delta: " + rel, file=sys.stderr)
            print(short_diff(rel, s_norm.splitlines(), p_norm.splitlines()), file=sys.stderr)
            failures += 1

    if failures:
        print(f"\n{failures} file(s) differ outside the config delta.", file=sys.stderr)
        return 1

    print("PASS: staging and production differ only within the enumerated config delta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
