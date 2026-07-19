from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/build_book1_production.py"
spec = importlib.util.spec_from_file_location("book1_production", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules["book1_production"] = mod
assert spec and spec.loader
spec.loader.exec_module(mod)


class ProductionProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx = mod.load_context(
            ROOT,
            mod.EXPECTED_SOURCE_COMMIT,
            "agent/book1-production-package",
            "test-head",
        )
        cls.proofs = ROOT / mod.PROOF_DIR_REL
        cls.docx = cls.proofs / "Veridrift_INTERIOR_PROOF.docx"
        cls.epub = cls.proofs / "Veridrift_EPUB_PROOF.epub"
        cls.pdf = cls.proofs / "Veridrift_PRINT_PROOF.pdf"

    def test_source_inventory_is_exact(self):
        self.assertEqual(len(self.ctx.entries), 25)
        self.assertIsNone(self.ctx.entries[0].number)
        self.assertEqual([e.number for e in self.ctx.entries[1:]], list(range(1, 25)))
        self.assertEqual(sum(e.words for e in self.ctx.entries), 105157)
        self.assertFalse(any(e.number == 25 for e in self.ctx.entries))

    def test_outputs_exist_and_nonzero(self):
        for path in (self.docx, self.epub, self.pdf):
            self.assertTrue(path.is_file(), path)
            self.assertGreater(path.stat().st_size, 1000, path)

    def test_docx_structure_and_text(self):
        info = mod.docx_structure(self.docx, self.ctx.entries)
        self.assertTrue(info["headings_match"])
        self.assertEqual(info["heading_count"], 25)
        self.assertFalse(info["has_chapter_25"])
        extracted = mod.extract_docx_body(self.docx, self.ctx.entries)
        self.assertEqual(mod.validate_exact_structured(self.ctx, extracted, "DOCX"), [])

    def test_epub_structure_navigation_and_text(self):
        info = mod.epub_structure(self.epub, self.ctx.entries)
        self.assertTrue(info["mimetype_first"])
        self.assertTrue(info["chapter_nav_match"])
        self.assertEqual(len(info["nav_entries"]), 25)
        self.assertFalse(info["has_chapter_25"])
        extracted = mod.extract_epub_body(self.epub, self.ctx.entries)
        self.assertEqual(mod.validate_exact_structured(self.ctx, extracted, "EPUB"), [])

    def test_pdf_preflight_and_text(self):
        info = mod.pdf_structure(self.pdf)
        self.assertTrue(info["trim_6x9"])
        self.assertFalse(info["encrypted"])
        self.assertEqual(info["unembedded_fonts"], [])
        self.assertEqual(info["final_line_count"], 1)
        self.assertTrue(info["last_page_contains_final_line"])
        self.assertFalse(info["chapter_25"])
        ok, expected_hash, actual_hash = mod.validate_pdf_chars(self.ctx, mod.extract_pdf_text(self.pdf))
        self.assertTrue(ok, (expected_hash, actual_hash))

    def test_build_manifest_has_hashes_and_metadata_blockers(self):
        path = ROOT / mod.REPORT_DIR_REL / "production-build-manifest.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["source_commit"], mod.EXPECTED_SOURCE_COMMIT)
        self.assertEqual(data["manifest_version"], 2)
        self.assertEqual(data["accepted_file_count"], 25)
        self.assertEqual(data["accepted_word_count"], 105157)
        self.assertEqual(len(data["sources"]), 25)
        self.assertEqual(len(data["outputs"]), 3)
        self.assertIn("author_or_pen_name", data["unresolved_metadata_blockers"])
        for output in data["outputs"]:
            self.assertRegex(output["sha256"], r"^[0-9a-f]{64}$")

    def test_locked_endings(self):
        ch20 = next(e for e in self.ctx.entries if e.number == 20)
        self.assertEqual(ch20.words, 2363)
        self.assertEqual(ch20.sha256, mod.EXPECTED_CH20_SHA)
        self.assertEqual(ch20.paragraphs[-1], mod.EXPECTED_CH20_END)
        self.assertEqual(self.ctx.entries[-1].paragraphs[-1], mod.EXPECTED_FINAL_LINE)


if __name__ == "__main__":
    unittest.main()
