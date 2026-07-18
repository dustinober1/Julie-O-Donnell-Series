#!/usr/bin/env python3
"""Patch the one-sentence repair verifier to compare protected blocks directly."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "tools/apply_book1_one_sentence_repair.py"
OLD = '''    updated_paragraphs = split_paragraphs(updated)
    updated_protected = [p for p in updated_paragraphs if kind(p) in {"meta", "display"}]
    if updated_protected != original_protected:
        raise RuntimeError(f"scene metadata or system display changed in {path.relative_to(ROOT)}")
'''
NEW = '''    updated_paragraphs = split_paragraphs(updated)
    protected_cursor = 0
    for protected in original_protected:
        try:
            protected_cursor = updated_paragraphs.index(protected, protected_cursor) + 1
        except ValueError as exc:
            raise RuntimeError(
                f"scene metadata or system display changed in {path.relative_to(ROOT)}: {protected!r}"
            ) from exc
'''

text = PATH.read_text(encoding="utf-8")
if NEW in text:
    print("verifier patch already applied")
elif OLD not in text:
    raise RuntimeError("expected verifier block not found")
else:
    PATH.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
    print("patched protected-block verifier")
