#!/usr/bin/env python3
"""Patch the reviewed repair map to preserve Chapter 12's closing line."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "tools/build_book1_one_sentence_repair_map.py"
text = PATH.read_text(encoding="utf-8")

old_keep = '''    ("books/book-01/manuscript/chapters/chapter-12.md", 248): "preserve field-endpoint reveal before display",
}'''
new_keep = '''    ("books/book-01/manuscript/chapters/chapter-12.md", 248): "preserve field-endpoint reveal before display",
    ("books/book-01/manuscript/chapters/chapter-12.md", 393): "preserve isolated chapter-closing line",
}'''
old_counts = '''        "attach_next_dialogue": 167,
        "keep": 60,'''
new_counts = '''        "attach_next_dialogue": 166,
        "keep": 61,'''

if new_keep not in text:
    if old_keep not in text:
        raise RuntimeError("expected Chapter 12 keep block not found")
    text = text.replace(old_keep, new_keep, 1)
if new_counts not in text:
    if old_counts not in text:
        raise RuntimeError("expected action count block not found")
    text = text.replace(old_counts, new_counts, 1)
PATH.write_text(text, encoding="utf-8")
print("patched Chapter 12 ending protection")
