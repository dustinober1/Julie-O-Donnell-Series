#!/usr/bin/env python3
"""Compile the full manuscript by concatenating the accepted files listed in the manifest."""

from __future__ import annotations

import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
OUTPUT_PATH = REPO_ROOT / "books/book-01/manuscript/full-manuscript.md"


def main() -> int:
    if not MANIFEST_PATH.is_file():
        print(f"Error: Manifest file not found at {MANIFEST_PATH}", file=sys.stderr)
        return 1

    try:
        manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Error reading manifest: {exc}", file=sys.stderr)
        return 1

    accepted_files = manifest.get("accepted_files", [])
    if not accepted_files:
        print("Error: No accepted files listed in the manifest.", file=sys.stderr)
        return 1

    parts = []
    for entry in accepted_files:
        path_str = entry.get("path")
        if not path_str:
            print(f"Error: Missing path in manifest entry {entry}", file=sys.stderr)
            return 1

        file_path = REPO_ROOT / path_str
        if not file_path.is_file():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            return 1

        try:
            content = file_path.read_text(encoding="utf-8")
            parts.append(content)
            print(f"Read {file_path.name}")
        except Exception as exc:
            print(f"Error reading {file_path}: {exc}", file=sys.stderr)
            return 1

    # Concatenate the files exactly as they are
    combined_content = "".join(parts)

    try:
        OUTPUT_PATH.write_text(combined_content, encoding="utf-8")
        print(f"Successfully compiled and wrote full manuscript to {OUTPUT_PATH}")
    except Exception as exc:
        print(f"Error writing output file: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
