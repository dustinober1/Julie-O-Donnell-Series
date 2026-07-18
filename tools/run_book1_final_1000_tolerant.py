#!/usr/bin/env python3
"""Run the final thousand-word pass while reporting shifted anchors."""
from __future__ import annotations

from pathlib import Path

import apply_book1_final_1000 as final_pass


def tolerant_patch(path: Path, anchor: str, replacement: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    if anchor not in text:
        print(f"SHIFTED ANCHOR: {path.name}: {marker}")
        return
    path.write_text(text.replace(anchor, replacement, 1), encoding="utf-8")
    print(path.relative_to(final_pass.ROOT))


def main() -> None:
    final_pass.patch = tolerant_patch
    final_pass.main()


if __name__ == "__main__":
    main()
