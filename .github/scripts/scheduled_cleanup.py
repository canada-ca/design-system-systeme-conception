#!/usr/bin/env python3
"""Authoritative reconciliation sweep for the PR-preview host.

Deletes stale pr-<n> directories under the preview/prod-artifact path
families whose PR number is not among the source repo's currently open
pull requests. Backstops the PR-close-triggered preview-cleanup.yml,
which is best-effort (missed events, disabled workflow, outages, etc.
all leave orphaned directories that only a periodic sweep can recover).
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

PATH_FAMILIES = (
    "design-system/pr-preview",
    "systeme-conception/pr-preview",
    "design-system/prod-artifact",
    "systeme-conception/prod-artifact",
)


def parse_open_prs(raw: str) -> set[str]:
    return {part.strip() for part in raw.split(",") if part.strip()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview-host", required=True)
    parser.add_argument("--open-prs", default="")
    args = parser.parse_args()

    host = Path(args.preview_host)
    open_prs = parse_open_prs(args.open_prs)

    deleted = 0
    for family in PATH_FAMILIES:
        family_dir = host / family
        if not family_dir.is_dir():
            continue
        for entry in sorted(family_dir.iterdir()):
            if not entry.is_dir() or not entry.name.startswith("pr-"):
                continue
            pr_number = entry.name[len("pr-"):]
            if pr_number in open_prs:
                continue
            try:
                shutil.rmtree(entry)
            except OSError as exc:
                print(f"ERROR: failed to remove {entry}: {exc}", file=sys.stderr)
                return 1
            print(f"removed {entry}")
            deleted += 1

    print(f"Swept {deleted} stale preview director{'y' if deleted == 1 else 'ies'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
