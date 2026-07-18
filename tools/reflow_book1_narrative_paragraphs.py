#!/usr/bin/env python3
"""Conservatively combine adjacent one-sentence narrative paragraphs without changing words."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"
TARGETS = ("chapter-04.md", "chapter-05.md", "chapter-12.md", "chapter-13.md", "chapter-14.md")

SCENE_TERMS = (
    "Eastern Daylight Time",
    "Eastern Standard Time",
    "Indian Standard Time",
    "Washington, D.C.",
    "Kashmir",
    "Virginia",
)


def eligible(paragraph: str) -> bool:
    if "\n" in paragraph:
        return False
    stripped = paragraph.strip()
    if not stripped or stripped.startswith(("#", "“", '"', "-", "*", "•")):
        return False
    if stripped.endswith(":"):
        return False
    if any(term in stripped for term in SCENE_TERMS):
        return False
    words = stripped.split()
    if not 8 <= len(words) <= 48:
        return False
    letters = "".join(ch for ch in stripped if ch.isalpha())
    if letters and letters.upper() == letters:
        return False
    sentence_marks = len(re.findall(r"[.!?](?:[”\"])?$", stripped))
    return sentence_marks == 1


def reflow(text: str) -> str:
    paragraphs = text.split("\n\n")
    out: list[str] = []
    index = 0
    while index < len(paragraphs):
        current = paragraphs[index]
        if not eligible(current):
            out.append(current)
            index += 1
            continue

        merged = current.strip()
        merged_count = 1
        cursor = index + 1
        while cursor < len(paragraphs) and merged_count < 3 and eligible(paragraphs[cursor]):
            candidate = paragraphs[cursor].strip()
            if len((merged + " " + candidate).split()) > 105:
                break
            merged += " " + candidate
            merged_count += 1
            cursor += 1

        out.append(merged)
        index = cursor
    return "\n\n".join(out)


def main() -> None:
    for name in TARGETS:
        path = CHAPTER_DIR / name
        original = path.read_text(encoding="utf-8")
        updated = reflow(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
