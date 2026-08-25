#!/usr/bin/env python3
"""Negative controls for the ending-invariant guard.

A guard that cannot fail is not a guard. Each test injects a defect the
validator exists to catch, confirms it fires, and confirms the manuscript is
restored afterwards.
"""
from __future__ import annotations

import importlib
import unittest
from pathlib import Path

import validate_book1_ending_invariants as mod

ROOT = Path(__file__).resolve().parents[1]
CH24 = ROOT / "books/book-01/manuscript/chapters/chapter-24.md"
CH01 = ROOT / "books/book-01/manuscript/chapters/chapter-01.md"


class EndingInvariantTests(unittest.TestCase):
    def setUp(self) -> None:
        importlib.reload(mod)

    def run_validator(self) -> int:
        importlib.reload(mod)
        return mod.main()

    def assert_clean(self) -> None:
        self.assertEqual(self.run_validator(), 0, "manuscript should pass as-is")

    def inject(self, path: Path, mutate) -> None:
        """Apply mutate() to path, assert the validator fails, then restore."""
        original = path.read_text(encoding="utf-8")
        try:
            path.write_text(mutate(original), encoding="utf-8")
            self.assertEqual(self.run_validator(), 1, "validator failed to fire")
        finally:
            path.write_text(original, encoding="utf-8")
        self.assert_clean()

    def test_manuscript_is_clean(self) -> None:
        self.assert_clean()

    def test_catches_changed_final_line(self) -> None:
        self.inject(CH24, lambda t: t.rstrip()[: -len(mod.FINAL_LINE)] + "The bubble drifted.\n")

    def test_catches_prohibited_conclusion_in_chapter_24(self) -> None:
        self.inject(CH24, lambda t: t + "\n\nSterling ordered the construction.\n")

    def test_catches_prohibited_conclusion_anywhere_in_the_book(self) -> None:
        # The retired validator only inspected Chapter 24; an overclaim planted
        # in Chapter 1 would have passed it.
        self.inject(CH01, lambda t: t + "\n\nJulie was exonerated.\n")

    def test_catches_closed_series_thread(self) -> None:
        self.inject(CH24, lambda t: t.replace("who initiated the original 02:14 construction", "who signed the order"))

    def test_catches_missing_required_element(self) -> None:
        self.inject(CH24, lambda t: t.replace("It was not repaired.", "It was repaired."))

    def test_catches_drafting_residue(self) -> None:
        self.inject(CH24, lambda t: t + "\n\nTODO: rewrite this.\n")

    def test_catches_changed_chapter_24_title(self) -> None:
        self.inject(CH24, lambda t: t.replace("# Chapter 24 — The Terms of Return", "# Chapter 24 — The Return"))

    def test_every_prohibited_phrase_is_absent_from_the_manuscript(self) -> None:
        # Guards against adding a phrase that legitimate prose already contains,
        # which would make the validator permanently red.
        blob = "".join(p.read_text(encoding="utf-8") for p in mod.accepted_files()).lower()
        for phrase in mod.PROHIBITED:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase.lower(), blob)

    def test_no_pinned_counts_or_hashes(self) -> None:
        # The retired validator died of pinned word counts, blob hashes, and a
        # base commit. Keep this one free of them.
        source = Path(mod.__file__).read_text(encoding="utf-8")
        body = source.split('"""', 2)[-1]
        import re
        self.assertIsNone(re.search(r"\b[0-9a-f]{40}\b", body), "git blob/commit hash pinned")
        self.assertIsNone(re.search(r"\b[0-9a-f]{64}\b", body), "sha256 pinned")
        self.assertIsNone(re.search(r"word_count|\b\d{4,}\b", body), "word count pinned")


if __name__ == "__main__":
    unittest.main()
