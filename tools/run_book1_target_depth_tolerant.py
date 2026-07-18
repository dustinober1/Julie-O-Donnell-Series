#!/usr/bin/env python3
"""Run the final depth pass while reporting any shifted editorial anchors."""
from __future__ import annotations

from pathlib import Path

import apply_book1_target_depth as target

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"


def main() -> None:
    revisions = {
        "chapter-15.md": target.revise_15,
        "chapter-16.md": target.revise_16,
        "chapter-17.md": target.revise_17,
        "chapter-18.md": target.revise_18,
        "chapter-19.md": target.revise_19,
        "chapter-20.md": target.revise_20,
        "chapter-21.md": target.revise_21,
        "chapter-22.md": target.revise_22,
        "chapter-23.md": target.revise_23,
        "chapter-24.md": target.revise_24,
    }
    failed: list[str] = []
    for name, revise in revisions.items():
        path = CHAPTER_DIR / name
        original = path.read_text(encoding="utf-8")
        try:
            updated = revise(original)
        except RuntimeError as exc:
            failed.append(f"{name}: {exc}")
            continue
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(path.relative_to(ROOT))

    if failed:
        print("SHIFTED ANCHORS:")
        for item in failed:
            print(f"- {item}")


if __name__ == "__main__":
    main()
