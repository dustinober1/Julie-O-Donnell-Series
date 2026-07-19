#!/usr/bin/env python3
"""Regression tests for Book 1 publication-master freeze invariants."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import book1_publication_readiness_core as core
import validate_book1_publication_readiness as validator


class PublicationMasterFreezeTests(unittest.TestCase):
    def test_final_pre_freeze_totals_are_guarded(self) -> None:
        self.assertIn("105,155", validator.STALE_CONTROL_LITERALS)
        self.assertIn("105155", validator.STALE_CONTROL_LITERALS)

    def test_unlisted_manuscript_markdown_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "books/book-01/manuscript/full-manuscript.md"
            path.parent.mkdir(parents=True)
            path.write_text("# Unauthorized compilation\n", encoding="utf-8")
            with self.assertRaisesRegex(
                validator.ValidationError, "unauthorized manuscript file"
            ):
                validator.validate_manuscript_inventory(root, [])

    def test_zero_open_proofread_queries_are_required(self) -> None:
        source = Path(core.__file__).read_text(encoding="utf-8")
        self.assertIn('"Open queries: **0**"', source)
        self.assertIn("open proofread queries remain", source)


if __name__ == "__main__":
    unittest.main()
