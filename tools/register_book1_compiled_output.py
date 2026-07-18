#!/usr/bin/env python3
"""Register the revised compiled manuscript as generated, non-canonical output."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
RELATIVE = "books/book-01/compiled/current/Julie_O_Donnell_Book_1_REVISED.md"


def main() -> None:
    text = MANIFEST.read_text(encoding="utf-8")
    if RELATIVE in text:
        return
    addition = (
        f'  - path: "{RELATIVE}"\n'
        '    reason: "Generated compilation for review; canonical prose remains the accepted file inventory."\n'
    )
    if not text.endswith("\n"):
        text += "\n"
    MANIFEST.write_text(text + addition, encoding="utf-8")
    print(f"registered {RELATIVE}")


if __name__ == "__main__":
    main()
