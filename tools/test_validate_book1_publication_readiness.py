#!/usr/bin/env python3
"""Unit tests for the Book 1 publication-readiness validator."""
from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("validate_book1_publication_readiness.py")
SPEC = importlib.util.spec_from_file_location("book1_validator", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ValidatorFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.book = root / "books/book-01"
        self.manuscript = self.book / "manuscript"
        self.chapters = self.manuscript / "chapters"
        self.control = self.book / "control"
        self.chapters.mkdir(parents=True)
        self.control.mkdir(parents=True)
        self.entries: list[tuple[str, str, int, str]] = []

    @staticmethod
    def _word_count(text: str) -> int:
        return len(text.split())

    @staticmethod
    def _sha(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def write_sources(self) -> None:
        prologue = "# Prologue - Six Years Ago\n\nOpening source text.\n"
        prologue_path = self.manuscript / "prologue.md"
        prologue_path.parent.mkdir(parents=True, exist_ok=True)
        prologue_path.write_text(prologue, encoding="utf-8")
        self.entries.append(
            (
                "books/book-01/manuscript/prologue.md",
                "Six Years Ago",
                self._word_count(prologue),
                self._sha(prologue),
            )
        )

        for number in range(1, 25):
            title = "The Terms of Return" if number == 24 else f"Test Chapter {number}"
            ending = "\nThe bubble stayed centered.\n" if number == 24 else "\nBody text.\n"
            text = f"# Chapter {number} — {title}\n{ending}"
            path = self.chapters / f"chapter-{number:02d}.md"
            path.write_text(text, encoding="utf-8")
            self.entries.append(
                (
                    f"books/book-01/manuscript/chapters/chapter-{number:02d}.md",
                    title,
                    self._word_count(text),
                    self._sha(text),
                )
            )

    def write_manifest(self) -> None:
        total = sum(entry[2] for entry in self.entries)
        lines = [
            "version: 2",
            "book: 1",
            'title: "Veridrift"',
            'status: "developmentally_revised"',
            'publication_readiness: "specialist_review_and_copyedit_required"',
            f"total_accepted_words: {total}",
            "accepted_files:",
        ]
        for path, title, words, sha in self.entries:
            lines.extend(
                [
                    f'  - path: "{path}"',
                    f'    title: "{title}"',
                    '    accepted_on: "2026-07-18"',
                    f"    words: {words}",
                    f'    sha256: "{sha}"',
                ]
            )
        lines.extend(
            [
                "excluded_from_canon:",
                '  - path: "archive/"',
                '    reason: "Historical only."',
            ]
        )
        (self.book / "ACCEPTED_MANUSCRIPT.yaml").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )

    def write_controls(self) -> None:
        total = sum(entry[2] for entry in self.entries)
        (self.root / "README.md").write_text(
            "# Julie O'Donnell Series\n\n"
            f"Accepted revised manuscript: **{total:,} words**.\n"
            "Original 02:14 construction remains unresolved.\n"
            "Sterling's personal knowledge or command remains unresolved.\n",
            encoding="utf-8",
        )
        (self.control / "README.md").write_text(
            "# Book 1 Control Pack\n\n"
            "- Book title: **Veridrift**\n"
            "- Accepted canon: **Prologue and Chapters 1–24**\n"
            f"- Accepted baseline: **{total:,} words**\n"
            "- Preserved ending: **The bubble stayed centered.**\n",
            encoding="utf-8",
        )
        (self.control / "51-publication-readiness-status.md").write_text(
            "# Book 1 Publication-Readiness Status\n\n"
            f"**Accepted baseline:** {total:,} words  \n"
            "**Accepted structure:** Prologue + Chapters 1–24  \n"
            "Original 02:14 construction remains unresolved.\n"
            "Senator Sterling's personal command remains unresolved.\n"
            "The bubble stayed centered.\n",
            encoding="utf-8",
        )

    def build(self) -> None:
        self.write_sources()
        self.write_manifest()
        self.write_controls()


class PublicationReadinessValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.fixture = ValidatorFixture(self.root)
        self.fixture.build()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def validate(self) -> int:
        return validator.validate_repository(
            self.root, target_min=0, target_max=1_000_000
        )

    def test_valid_fixture_passes(self) -> None:
        total = self.validate()
        self.assertGreater(total, 0)

    def test_hash_drift_fails(self) -> None:
        path = self.fixture.chapters / "chapter-03.md"
        path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "sha256 mismatch"):
            self.validate()

    def test_manifest_word_count_drift_fails(self) -> None:
        manifest = self.fixture.book / "ACCEPTED_MANUSCRIPT.yaml"
        text = manifest.read_text(encoding="utf-8").replace("    words: 8", "    words: 9", 1)
        manifest.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "word-count mismatch"):
            self.validate()

    def test_stale_control_total_fails(self) -> None:
        control = self.fixture.control / "README.md"
        control.write_text(
            control.read_text(encoding="utf-8") + "Accepted words: 124,779\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(validator.ValidationError, "stale control metadata"):
            self.validate()

    def test_changed_final_line_fails(self) -> None:
        path = self.fixture.chapters / "chapter-24.md"
        path.write_text("# Chapter 24 — The Terms of Return\n\nDifferent ending.\n", encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "must end"):
            self.validate()

    def test_chapter_25_artifact_fails(self) -> None:
        (self.fixture.chapters / "chapter-25.md").write_text(
            "# Chapter 25 — Unauthorized\n\nNo.\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(validator.ValidationError, "Chapter 25"):
            self.validate()

    def test_heading_title_mismatch_fails(self) -> None:
        path = self.fixture.chapters / "chapter-02.md"
        path.write_text("# Chapter 2 — Wrong Title\n\nBody text.\n", encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "title mismatch"):
            self.validate()


if __name__ == "__main__":
    unittest.main()
