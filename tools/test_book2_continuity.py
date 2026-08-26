#!/usr/bin/env python3
"""Book 2 continuity tooling: negative controls and Book 1 non-regression.

Two things must hold. The Book 2 wiring has to actually fire on the defects it
exists to catch, and the shared engine must not have moved Book 1 by a byte.
"""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import book_profiles
import check_book1_detail_rules as rules
import count_book2_words as counter

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
CH01 = ROOT / "books/book-02/manuscript/chapter-01.md"
CH02 = ROOT / "books/book-02/manuscript/chapter-02.md"


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=ROOT,
                          capture_output=True, text=True)


def book2_findings(rule: str) -> list[str]:
    """Re-extract Book 2 and return this rule's finding lines."""
    run(str(TOOLS / "extract_book1_detail_index.py"), "--book", "2", "--quiet")
    proc = run(str(TOOLS / "check_book1_detail_rules.py"), "--book", "2", "--rule", rule)
    out = proc.stdout
    return [ln.strip() for ln in out.splitlines() if ln.strip().startswith("- ")]


class ProfileTests(unittest.TestCase):
    def test_book1_offset_is_nine_thirty(self):
        self.assertEqual(book_profiles.profile(1).offset_label(), "+09:30")

    def test_book2_offset_is_seven_hours(self):
        # outline/07: "Canadian locations use PDT (UTC-7) during this period."
        self.assertEqual(book_profiles.profile(2).offset_label(), "+07:00")

    def test_unknown_book_is_refused(self):
        with self.assertRaises(SystemExit):
            book_profiles.profile(9)

    def test_longest_alias_wins(self):
        # "Eastern" must not shadow "Eastern Daylight Time".
        alt = book_profiles.profile(1).zone_alternation()
        self.assertLess(alt.index("Eastern\\ Daylight\\ Time"), alt.index("|Eastern|"))


class Book1NonRegressionTests(unittest.TestCase):
    def test_detail_index_is_byte_identical(self):
        committed = ROOT / "artifacts/book1-detail-index.json"
        out = ROOT / "artifacts/.book1-index-check.json"
        try:
            proc = run(str(TOOLS / "extract_book1_detail_index.py"),
                       "--quiet", "--output", str(out))
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(out.read_bytes(), committed.read_bytes())
        finally:
            out.unlink(missing_ok=True)

    def test_derived_chronology_is_byte_identical(self):
        committed = ROOT / "artifacts/book1-derived-chronology.md"
        out = ROOT / "artifacts/.book1-chron-check.md"
        try:
            run(str(TOOLS / "check_book1_detail_rules.py"), "--chronology", str(out))
            self.assertEqual(out.read_bytes(), committed.read_bytes())
        finally:
            out.unlink(missing_ok=True)

    def test_book1_hard_rules_still_clean(self):
        proc = run(str(TOOLS / "check_book1_detail_rules.py"))
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("no hard-rule findings", proc.stdout)


class Book2WiringTests(unittest.TestCase):
    def test_book2_index_covers_the_drafted_prose(self):
        run(str(TOOLS / "extract_book1_detail_index.py"), "--book", "2", "--quiet")
        index = json.loads((ROOT / "artifacts/book2-detail-index.json").read_text())
        self.assertEqual(index["source"], "books/book-02/MANUSCRIPT_STATUS.yaml")
        self.assertEqual(len(index["units"]), 2)

    def test_r2_anchors_on_book2_inline_times(self):
        # Book 2 states narrative-present time inline. Before the inline anchor
        # existed R2 found nothing at all, which made the rule inert.
        run(str(TOOLS / "extract_book1_detail_index.py"), "--book", "2", "--quiet")
        proc = run(str(TOOLS / "check_book1_detail_rules.py"), "--book", "2", "--rule", "R2")
        self.assertRegex(proc.stdout, r"\[R2\]\s+REVIEW\s+([1-9]\d*)")

    def test_r2_ignores_forward_references(self):
        # "set for 09:00 the following morning" is an appointment, not the
        # narrative present; anchoring on it would invent a backward step.
        self.assertIsNone(rules._inline_time_re(book_profiles.profile(2))
                          .match("The proposed session was set for 09:00 the following morning."))
        self.assertIsNotNone(rules._inline_time_re(book_profiles.profile(2))
                             .match("At 15:34, Julie asked a question."))

    def test_book2_is_currently_clean(self):
        self.assertEqual(book2_findings("R9"), [])


class R9NegativeControlTests(unittest.TestCase):
    """R9 is the rule that caught the Dhaliwal contradiction. Prove it fires."""

    def inject(self, path: Path, old: str, new: str, expect: str) -> None:
        original = path.read_text(encoding="utf-8")
        self.assertIn(old, original)
        try:
            path.write_text(original.replace(old, new, 1), encoding="utf-8")
            findings = book2_findings("R9")
            self.assertTrue(
                any(expect in f for f in findings),
                f"R9 did not fire; got {findings}",
            )
        finally:
            path.write_text(original, encoding="utf-8")
        self.assertEqual(book2_findings("R9"), [])

    def test_catches_a_second_given_name(self):
        self.inject(CH02, "Amrita Dhaliwal sat", "Deepa Dhaliwal sat", "given name")

    def test_catches_a_second_rank(self):
        self.inject(CH02, "under Inspector Dhaliwal", "under Superintendent Dhaliwal", "rank")

    def test_rank_forms_collapse_but_real_promotions_survive(self):
        """Two-directional, against Book 1's real prose.

        Book 1 writes both "Agent Grant" and "Special Agent Grant" -- one rank
        written two lengths, which must not be reported. It also writes "Major
        Marcus Reed" in the prologue and "Colonel Marcus Reed" six years later
        -- a real promotion, which must be.
        """
        index = json.loads((ROOT / "artifacts/book1-detail-index.json").read_text())
        findings = rules.Findings()
        rules.PROFILE = book_profiles.profile(1)
        rules.rule_r9(index["records"], findings)
        summaries = [f["summary"] for f in findings.for_rule("R9")]

        self.assertFalse([s for s in summaries if s.startswith("'Grant'")],
                         f"'Special Agent' was reported as a second rank: {summaries}")
        self.assertTrue([s for s in summaries if s.startswith("'Reed'") and "rank" in s],
                        f"Reed's Major -> Colonel promotion was not reported: {summaries}")


class CounterTests(unittest.TestCase):
    def test_provenance_block_is_not_counted_as_prose(self):
        raw = CH01.read_text(encoding="utf-8")
        self.assertTrue(raw.lstrip().startswith("<!--"))
        self.assertLess(counter.count(CH01), len(raw.split()))

    def test_recorded_totals_match_the_prose(self):
        proc = run(str(TOOLS / "count_book2_words.py"), "--expect", "5597")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_sync_is_idempotent(self):
        before = (ROOT / "books/book-02/MANUSCRIPT_STATUS.yaml").read_bytes()
        run(str(TOOLS / "count_book2_words.py"), "--sync")
        self.assertEqual((ROOT / "books/book-02/MANUSCRIPT_STATUS.yaml").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
