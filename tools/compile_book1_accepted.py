#!/usr/bin/env python3
"""Compile Book 1 strictly from the accepted-manuscript inventory."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
OUTPUT = ROOT / "books/book-01/compiled/current/Julie_O_Donnell_Book_1_REVISED.md"
PATH_RE = re.compile(r'^\s+(?:-\s+)?path:\s*"([^"]+)"\s*$')


def accepted_paths() -> list[Path]:
    text = MANIFEST.read_text(encoding="utf-8")
    block = text.split("\nexcluded_from_canon:", 1)[0]
    values = [
        match.group(1)
        for line in block.splitlines()
        if (match := PATH_RE.match(line))
    ]
    if len(values) != 25:
        raise RuntimeError(f"expected 25 accepted prose files, found {len(values)}")
    return [ROOT / value for value in values]


def main() -> None:
    paths = accepted_paths()
    sections = [path.read_text(encoding="utf-8").rstrip() for path in paths]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"compiled {len(paths)} files -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
