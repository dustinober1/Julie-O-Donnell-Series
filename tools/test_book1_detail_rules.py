#!/usr/bin/env python3
"""Tests for the Book 1 detail-continuity extractor and rule checker.

These lock in the behaviour that took several iterations to get right: the
rules must fire on real defects and stay silent on the legitimate prose
patterns that superficially resemble them. Every "must not fire" case below
corresponds to a false positive an earlier version of these rules produced
against the accepted manuscript.
"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "tools" / filename)
    module = importlib.util.module_from_spec(spec)
    # Registered before execution because @dataclass resolves annotations
    # through sys.modules and fails on an unregistered module.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


extract = _load("extract_book1_detail_index", "extract_book1_detail_index.py")
rules = _load("check_book1_detail_rules", "check_book1_detail_rules.py")


def record(**kwargs) -> dict:
    base = {
        "detail_class": "D1",
        "kind": "timestamp",
        "value": "05:00",
        "normalized": "05:00",
        "path": "books/book-01/manuscript/chapters/chapter-08.md",
        "line": 1,
        "unit": "ch08",
        "context": "",
        "mid_sentence": False,
    }
    base.update(kwargs)
    return base


class TestClockParsing(unittest.TestCase):
    def test_parses_zoned_and_subsecond_values(self):
        self.assertEqual(rules.parse_clock("05:00 EDT"), (18000, "EDT"))
        self.assertEqual(rules.parse_clock("07:08:09.442")[0], 25689.442)

    def test_rejects_non_clock_text(self):
        self.assertIsNone(rules.parse_clock("11.2"))


class TestR1ZoneOffset(unittest.TestCase):
    def _check(self, edt: str, ist: str) -> int:
        findings = rules.Findings()
        rules.rule_r1(
            [
                record(value=edt, normalized=f"{edt} EDT"),
                record(value=ist, normalized=f"{ist} IST"),
            ],
            findings,
        )
        return len(findings.for_rule("R1"))

    def test_accepts_the_manuscripts_fixed_offset(self):
        self.assertEqual(self._check("05:00", "14:30"), 0)
        self.assertEqual(self._check("07:46:00", "17:16:00"), 0)

    def test_rejects_a_wrong_offset(self):
        # The failure this exists to catch: a nine-hour conversion.
        self.assertEqual(self._check("05:00", "14:00"), 1)


class TestR3Countdowns(unittest.TestCase):
    def test_labels_name_the_instrument_not_the_weather(self):
        # "the stormwater discharge rose" is Chapter 5 weather, not a countdown.
        self.assertIsNone(rules.label_clock("At 18:06, the stormwater discharge rose."))
        self.assertEqual(rules.label_clock("DISCHARGE IN 01:30"), "suppression")
        self.assertEqual(
            rules.label_clock("The external commit clock showed 00:18."), "external_commit"
        )
        self.assertEqual(
            rules.label_clock("The sanitization clock showed 00:22."), "sanitization"
        )


class TestR5Designators(unittest.TestCase):
    def test_flags_a_dash_variant(self):
        findings = rules.Findings()
        rules.rule_r5(
            [
                record(kind="designator", value="L3-7", normalized="L3-7"),
                record(kind="designator", value="L3–7", normalized="L3-7"),
            ],
            findings,
        )
        self.assertEqual(len(findings.for_rule("R5")), 1)

    def test_accepts_a_single_consistent_form(self):
        findings = rules.Findings()
        rules.rule_r5(
            [
                record(kind="designator", value="APX-DIR-0019", normalized="APX-DIR-0019"),
                record(kind="designator", value="APX-DIR-0019", normalized="APX-DIR-0019"),
            ],
            findings,
        )
        self.assertEqual(findings.for_rule("R5"), [])


class TestR6MidSentenceFilter(unittest.TestCase):
    def test_sentence_initial_capitals_are_not_names(self):
        records = extract.extract_entities(
            "“Clear the partition,” one of his operators said.", "p", 1, "ch09"
        )
        clear = [r for r in records if r.value == "Clear"]
        self.assertTrue(clear)
        self.assertFalse(clear[0].mid_sentence)

    def test_mid_sentence_capitals_are_names(self):
        records = extract.extract_entities(
            "The noise was generated in a lab at Fort Belvoir.", "p", 1, "prologue"
        )
        fort = [r for r in records if r.value == "Fort"]
        self.assertTrue(fort and fort[0].mid_sentence)


class TestR7NumericNormalization(unittest.TestCase):
    def test_words_and_digits_compare_equal(self):
        self.assertEqual(rules.numeric_value("eleven"), rules.numeric_value("11"))
        self.assertEqual(rules.numeric_value("eleven-point-two"), 11.2)
        self.assertEqual(rules.numeric_value("ninety-nine"), 99)

    def test_rejects_non_numeric_tokens(self):
        self.assertIsNone(rules.numeric_value("package"))


class TestAcceptedManuscript(unittest.TestCase):
    """The rules must stay clean against the frozen manuscript."""

    @classmethod
    def setUpClass(cls):
        cls.index = extract.build_index()
        cls.records = cls.index["records"]

    def test_extracts_all_accepted_files(self):
        self.assertEqual(len(self.index["units"]), 25)

    def test_hard_rules_are_clean(self):
        findings = rules.Findings()
        rules.rule_r1(self.records, findings)
        rules.rule_r3(self.records, findings)
        rules.rule_r4(self.records, findings)
        rules.rule_r5(self.records, findings)
        hard = [i for i in findings.items if i["severity"] == "hard"]
        self.assertEqual(hard, [], f"hard-rule findings: {hard}")

    def test_derived_chronology_places_the_crisis_across_two_calendar_days(self):
        """The prose crosses midnight inside Chapter 5.

        Chapter 15 states October 13 for a scene one midnight after the
        Chapter 5 crossing, which places Chapters 1 through the first half of
        Chapter 5 on October 12. Book 1's control documents file all of it
        under a single October 13 heading. This test pins the prose-derived
        reading so that the discrepancy cannot silently reverse.
        """
        findings = rules.Findings()
        _checked, scenes = rules.derive_chronology(self.records, findings)
        by_scene = {(s["unit"], s["line"]): s for s in scenes}

        # Chapter 5 opens before midnight and its later scenes fall after it.
        self.assertEqual(by_scene[("ch05", 7)]["derived_date"], "October 12")
        self.assertEqual(by_scene[("ch05", 393)]["derived_date"], "October 13")

        # The stated dates from Chapter 15 onward agree with the derivation.
        for unit, line, expected in (
            ("ch15", 4, "October 13"),
            ("ch17", 4, "October 14"),
            ("ch20", 4, "October 15"),
            ("ch24", 4, "October 16"),
        ):
            scene = by_scene[(unit, line)]
            self.assertEqual(scene["stated_date"], expected)
            self.assertEqual(scene["derived_date"], expected)


if __name__ == "__main__":
    unittest.main()
