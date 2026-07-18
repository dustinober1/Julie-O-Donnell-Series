#!/usr/bin/env python3
"""Unit tests for the accepted-manifest Book 1 compiler."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

from test_validate_book1_publication_readiness import ValidatorFixture, validator

sys.modules["validate_book1_publication_readiness"] = validator
COMPILER_PATH = Path(__file__).with_name("compile_book1_from_manifest.py")
SPEC = importlib.util.spec_from_file_location("book1_compiler", COMPILER_PATH)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


class ManifestCompilerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.fixture = ValidatorFixture(self.root)
        self.fixture.build()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_compiler_concatenates_only_accepted_sources(self) -> None:
        output = self.root / "compiled/Veridrift_ACCEPTED.md"
        total, output_sha = compiler.compile_book(
            self.root,
            output,
            target_min=0,
            target_max=1_000_000,
        )

        expected = "\n\n".join(
            (self.root / path).read_text(encoding="utf-8").rstrip()
            for path, _title, _words, _sha in self.fixture.entries
        ) + "\n"
        self.assertEqual(output.read_text(encoding="utf-8"), expected)
        self.assertEqual(total, sum(entry[2] for entry in self.fixture.entries))
        self.assertEqual(len(output_sha), 64)

        sidecar = json.loads(
            output.with_suffix(output.suffix + ".build.json").read_text(encoding="utf-8")
        )
        self.assertEqual(sidecar["book"], "Veridrift")
        self.assertEqual(sidecar["accepted_words"], total)
        self.assertEqual(sidecar["output_sha256"], output_sha)
        self.assertEqual(
            sidecar["accepted_files"], [entry[0] for entry in self.fixture.entries]
        )
        self.assertIn("review compilation only", sidecar["authority"])

    def test_compiler_refuses_stale_control_metadata(self) -> None:
        control = self.fixture.control / "README.md"
        control.write_text(
            control.read_text(encoding="utf-8") + "Accepted words: 124,779\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(validator.ValidationError, "stale control metadata"):
            compiler.compile_book(
                self.root,
                self.root / "compiled.md",
                target_min=0,
                target_max=1_000_000,
            )


if __name__ == "__main__":
    unittest.main()
