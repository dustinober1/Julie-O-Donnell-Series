#!/usr/bin/env python3
"""Run the automatable detail-continuity rules (R1-R8).

Consumes the detail index produced by ``tools/extract_book1_detail_index.py``
and applies the rule sets defined in
``books/book-01/control/70-detail-continuity-audit-plan.md``. Pass ``--book 2``
to run Book 2; per-book zones and paths live in ``tools/book_profiles.py``.
This file keeps its Book 1 name because frozen Book 1 control records cite it
by path.

    R1  every cross-zone pair states exactly the book's declared offset
    R2  timestamps are non-decreasing within a chapter, allowing declared
        rollovers, flashbacks, and restatements
    R3  countdown runs decrease monotonically
    R4  sub-second timestamps agree across every chapter that restates them
    R5  each designator appears in exactly one canonical form
    R6  no near-miss spelling or casing variants of recurring entity names
    R7  quantities that state the same fact agree
    R8  first-mention index for every entity and designator
    R9  each recurring surname pairs with one given name and one rank

R1, R3, R4, and R5 are hard rules: a violation is a defect. R2, R6, and R7 are
reporting rules that surface candidates for human adjudication, because
legitimate prose routinely reorders time, introduces new names, and restates
numbers in different units. R8 produces no findings; it feeds the knowledge-
ordering review (R11), which is judgment-only.

Exit status is 1 only when a hard rule fails, so this can gate CI without
turning every legitimate flashback into a build failure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from book_profiles import REPO_ROOT, BookProfile, add_book_argument, profile

# Set by main() once the book is known; Book 1 stays the default so existing
# invocations and Book 1's committed chronology are unchanged.
PROFILE: BookProfile = profile(1)

HARD_RULES = {"R1", "R3", "R4", "R5"}


def _clock_re(prof: BookProfile) -> re.Pattern:
    return re.compile(
        r"^(\d{2}):(\d{2})(?::(\d{2})(\.\d+)?)?"
        r"(?:\s+(" + "|".join(z.canon for z in prof.zones) + r"))?$"
    )


CLOCK = _clock_re(PROFILE)


def parse_clock(normalized: str) -> tuple[float, str] | None:
    m = CLOCK.match(normalized)
    if not m:
        return None
    seconds = int(m.group(1)) * 3600 + int(m.group(2)) * 60
    if m.group(3):
        seconds += int(m.group(3))
    if m.group(4):
        seconds += float(m.group(4))
    return seconds, (m.group(5) or "")


def unit_order(unit: str) -> int:
    if unit == "prologue":
        return 0
    m = re.search(r"(\d+)", unit)
    return int(m.group(1)) if m else 999


class Findings:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, rule: str, severity: str, summary: str, citations: list[str]) -> None:
        self.items.append(
            {"rule": rule, "severity": severity, "summary": summary, "citations": citations}
        )

    def for_rule(self, rule: str) -> list[dict]:
        return [i for i in self.items if i["rule"] == rule]


def cite(record: dict) -> str:
    return f"{record['path']}:{record['line']} — {record['context']}"


# --------------------------------------------------------------------------
# R1: paired-zone offset
# --------------------------------------------------------------------------

def rule_r1(records: list[dict], findings: Findings) -> int:
    """Every line stating both of the book's zones must state the declared offset.

    Book 1 pairs EDT with IST at exactly +09:30. Book 2 pairs PDT with UTC at
    +07:00, per outline/07: "Canadian locations use PDT (UTC-7)."
    """
    if not PROFILE.zone_pair:
        return 0
    base, other = PROFILE.zone_pair
    expected = PROFILE.offset_between(base, other)
    expected_label = PROFILE.offset_label()

    by_line: dict[tuple[str, int], list[dict]] = defaultdict(list)
    for r in records:
        if r["kind"] == "timestamp":
            by_line[(r["path"], r["line"])].append(r)

    checked = 0
    for (_path, _line), group in sorted(by_line.items()):
        zoned = [(parse_clock(r["normalized"]), r) for r in group]
        base_recs = [(p[0], r) for p, r in zoned if p and p[1] == base]
        other_recs = [(p[0], r) for p, r in zoned if p and p[1] == other]
        if not base_recs or not other_recs:
            continue
        for base_seconds, base_rec in base_recs:
            for other_seconds, other_rec in other_recs:
                checked += 1
                delta = (other_seconds - base_seconds) % 86400
                if abs(delta - (expected % 86400)) > 0.0005:
                    hours, rem = divmod(delta, 3600)
                    findings.add(
                        "R1",
                        "hard",
                        f"{base}/{other} pair states +{int(hours):02d}:{int(rem // 60):02d}, "
                        f"expected {expected_label}: "
                        f"{base_rec['value']} {base} / {other_rec['value']} {other}",
                        [cite(base_rec)],
                    )
    return checked


# --------------------------------------------------------------------------
# R2: within-chapter ordering
# --------------------------------------------------------------------------

# A scene header is a standalone line carrying only a time (optionally with a
# zone, optionally paired) or only a date. Screen text always carries a prefix
# or suffix — "DISCHARGE IN 01:30", "COUNTER-BATTERY SUPPORT COMMIT: 05:00 EDT"
# — so anchoring on the whole line separates narrative present from displayed
# data without needing to understand either.
def _scene_time_re(prof: BookProfile) -> re.Pattern:
    zones = prof.zone_alternation()
    return re.compile(
        r"^(\d{1,2}):([0-5]\d)(?::([0-5]\d)(\.\d+)?)?"
        r"(?:\s+(" + zones + r"))?"
        r"(?:\s*/\s*(\d{1,2}):([0-5]\d)(?::([0-5]\d))?\s*(" + zones + r"))?$"
    )


def _inline_time_re(prof: BookProfile) -> re.Pattern | None:
    """Sentence-initial narrative-present time, for books that state it inline."""
    if not prof.inline_time_anchor:
        return None
    return re.compile(prof.inline_time_anchor.replace("ZONES", prof.zone_alternation()))


SCENE_TIME = _scene_time_re(PROFILE)
INLINE_TIME = _inline_time_re(PROFILE)
SCENE_DATE = re.compile(r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})$")


def scene_headers(records: list[dict]) -> list[dict]:
    """Walk the accepted files in order and pull the narrative-present anchors."""
    paths: list[tuple[int, str, str]] = []
    seen = set()
    for r in records:
        if r["path"] not in seen:
            seen.add(r["path"])
            paths.append((unit_order(r["unit"]), r["unit"], r["path"]))
    paths.sort()

    anchors: list[dict] = []
    for _order, unit, path in paths:
        lines = (REPO_ROOT / path).read_text(encoding="utf-8").splitlines()
        for lineno, raw in enumerate(lines, start=1):
            line = raw.strip()
            if not line:
                continue
            date_match = SCENE_DATE.match(line)
            if date_match:
                anchors.append(
                    {
                        "type": "date",
                        "unit": unit,
                        "path": path,
                        "line": lineno,
                        "value": line,
                        "month": date_match.group(1),
                        "day": int(date_match.group(2)),
                    }
                )
                continue
            time_match = SCENE_TIME.match(line)
            inline = False
            if time_match is None and INLINE_TIME is not None:
                time_match = INLINE_TIME.match(line)
                inline = time_match is not None
            if time_match:
                base = PROFILE.base_zone
                zone = ZONE_CANON.get((time_match.group(5) or base).lower(), base)
                seconds = int(time_match.group(1)) * 3600 + int(time_match.group(2)) * 60
                if time_match.group(3):
                    seconds += int(time_match.group(3))
                if zone != base:
                    # Normalize a headline stated in a secondary zone back to the
                    # book's base zone, so the whole book sits on one axis.
                    seconds = (seconds - PROFILE.offset_between(base, zone)) % 86400
                # A standalone header is the whole line; an inline anchor is
                # one clause inside a paragraph, so show only that clause.
                shown = line
                if inline:
                    clause = re.split(r"(?<=[.?!])\s", line, maxsplit=1)[0]
                    shown = clause if len(clause) <= 120 else clause[:117] + "..."
                anchors.append(
                    {
                        "type": "time",
                        "unit": unit,
                        "path": path,
                        "line": lineno,
                        "value": shown,
                        "seconds": seconds,
                    }
                )
    return anchors


ZONE_CANON = PROFILE.zone_canon()


DAYS_IN_MONTH = {
    "January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
    "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
    "November": 30, "December": 31,
}


def derive_chronology(records: list[dict], findings: Findings) -> tuple[int, list[dict]]:
    """Rebuild the book's calendar from the prose alone.

    Two distinct defects are reachable here. The first is a scene that steps
    backward without a date header to justify it. The second — the one no
    existing control could see — is a stated date that contradicts the number
    of midnights the prose has actually crossed since the last stated date.

    The returned chronology assigns every scene a day index, then anchors those
    indices to the calendar using the first date the prose states. Scenes that
    fall before any stated date get a back-calculated date, which is exactly
    where an unexamined control document can drift without contradiction.
    """
    anchors = scene_headers(records)
    checked = 0
    day_index = 0          # midnights crossed since the first scene
    previous_seconds = None
    pending_date: dict | None = None
    stated: list[tuple[int, dict]] = []
    scenes: list[dict] = []

    last_stated: dict | None = None
    inferred_since_date = 0

    for anchor in anchors:
        if anchor["type"] == "date":
            # A date header belongs to the scene it introduces, so hold it
            # until the scene's time anchor resolves which day that is.
            pending_date = anchor
            continue
        checked += 1
        seconds = anchor["seconds"]
        crossed_here = 0
        if previous_seconds is not None and seconds < previous_seconds:
            drop = previous_seconds - seconds
            if drop > 8 * 3600:
                # The only reading consistent with continuous narration.
                crossed_here = 1
            elif pending_date is None:
                findings.add(
                    "R2",
                    "review",
                    f"{anchor['unit']}: scene header {anchor['value']} steps back "
                    f"{drop / 3600:.2f}h with no date header",
                    [f"{anchor['path']}:{anchor['line']}"],
                )
        day_index += crossed_here

        if pending_date is not None:
            # A stated date is testable: the days it declares since the last
            # stated date must equal the midnights the prose actually crossed.
            if last_stated is not None and last_stated["month"] == pending_date["month"]:
                declared = pending_date["day"] - last_stated["day"]
                actual = inferred_since_date + crossed_here
                # Declaring more days than the prose narrates is an ordinary
                # scene cut across a night nobody describes. Declaring fewer is
                # the defect: the prose has crossed a midnight the dates deny.
                # A declared gap larger than the narrated one is a scene cut
                # across a night nobody describes. Advance the day counter to
                # match, so it keeps tracking real calendar days.
                if declared > actual:
                    day_index += declared - actual
                if declared < actual:
                    findings.add(
                        "R2",
                        "review",
                        f"Stated dates {last_stated['month']} {last_stated['day']} "
                        f"({last_stated['unit']}) and {pending_date['month']} {pending_date['day']} "
                        f"({pending_date['unit']}) declare {declared} day(s) apart, "
                        f"but the prose crosses {actual} midnight(s) between them",
                        [
                            f"{last_stated['path']}:{last_stated['line']}",
                            f"{pending_date['path']}:{pending_date['line']}",
                        ],
                    )
            stated.append((day_index, pending_date))
            last_stated = pending_date
            inferred_since_date = 0
            pending_date = None
        else:
            inferred_since_date += crossed_here

        scenes.append(
            {
                "unit": anchor["unit"],
                "path": anchor["path"],
                "line": anchor["line"],
                "header": anchor["value"],
                "day_index": day_index,
                "stated_date": (
                    f"{stated[-1][1]['month']} {stated[-1][1]['day']}"
                    if stated and stated[-1][0] == day_index
                    else None
                ),
            }
        )
        previous_seconds = seconds

    # Anchor the relative day indices to the calendar using the first date the
    # prose states, so that scenes preceding it get an explicit derived date.
    if stated:
        base_index, base = stated[0]
        for scene in scenes:
            day = base["day"] + (scene["day_index"] - base_index)
            month = base["month"]
            if day < 1:
                day += DAYS_IN_MONTH.get(month, 30)
                month = "(previous month)"
            scene["derived_date"] = f"{month} {day}"
    return checked, scenes


def rule_r2(records: list[dict], findings: Findings) -> int:
    checked, scenes = derive_chronology(records, findings)
    rule_r2.scenes = scenes
    return checked


# --------------------------------------------------------------------------
# R3: countdown runs
# --------------------------------------------------------------------------

# Act II runs several countdown clocks at once — the external counter-battery
# commit, the volatile sanitization timer, the Indian execution timer, and the
# suppression discharge timer — and the prose interleaves reads from all of
# them. Checking them as one sequence produces nothing but false positives, so
# each read is attributed to the clock its own line names. An unlabelled read
# ("The clock reached 00:27") inherits the last clock explicitly named.
# Labels must name the instrument, not merely share a word with it. "discharge"
# alone also matches the stormwater discharge in Chapter 5, which is weather,
# not a countdown.
CLOCK_LABELS = (
    ("suppression", re.compile(r"discharge in|suppression (?:clock|display|countdown)|countdown above the gate", re.I)),
    ("sanitization", re.compile(r"sanitization (?:clock|timer)", re.I)),
    ("execution", re.compile(r"execution in", re.I)),
    ("indian_support", re.compile(r"american release|smaller timer", re.I)),
    ("buffer_retention", re.compile(r"buffer retention", re.I)),
    ("external_commit", re.compile(r"external (?:commit|clock|queue)|release (?:clock|queue)", re.I)),
)


def label_clock(line_text: str) -> str | None:
    for label, pattern in CLOCK_LABELS:
        if pattern.search(line_text):
            return label
    return None


def rule_r3(records: list[dict], findings: Findings) -> int:
    """Remaining-time reads must decrease within each named countdown clock.

    A countdown read is a sub-two-hour value written with a leading 00 or 01
    hour field. Runs are keyed by clock rather than by chapter, because the
    suppression discharge legitimately spans the Chapter 8 to Chapter 9 break.
    """
    candidates = []
    for r in records:
        if r["kind"] != "timestamp":
            continue
        parsed = parse_clock(r["normalized"])
        if not parsed or parsed[1]:
            continue
        if parsed[0] < 3600 * 2 and r["value"].startswith(("00:", "01:")):
            candidates.append((parsed[0], r))

    line_cache: dict[str, list[str]] = {}

    def source_line(record: dict) -> str:
        lines = line_cache.get(record["path"])
        if lines is None:
            lines = (REPO_ROOT / record["path"]).read_text(encoding="utf-8").splitlines()
            line_cache[record["path"]] = lines
        idx = record["line"] - 1
        return lines[idx] if 0 <= idx < len(lines) else ""

    candidates.sort(key=lambda item: (unit_order(item[1]["unit"]), item[1]["line"]))
    runs: dict[str, list[tuple[float, dict]]] = defaultdict(list)
    current = None
    current_unit = None
    for seconds, record in candidates:
        # Attribution never crosses a chapter boundary. Chapter 5 carries
        # absolute post-midnight wall-clock reads (00:18, 03:57) that share the
        # shape of a countdown but are not one, and a run that legitimately
        # spans chapters — the suppression discharge across the 8/9 break —
        # names its clock again on the far side.
        if record["unit"] != current_unit:
            current_unit = record["unit"]
            current = None
        explicit = label_clock(source_line(record))
        if explicit:
            current = explicit
        if current:
            runs[current].append((seconds, record))

    checked = 0
    for label in sorted(runs):
        run = runs[label]
        if len(run) < 3:
            checked += len(run)
            continue
        previous = None
        for seconds, record in run:
            checked += 1
            if previous is not None and seconds > previous[0]:
                findings.add(
                    "R3",
                    "hard",
                    f"{label} countdown rises from {previous[1]['value']} to {record['value']}",
                    [cite(previous[1]), cite(record)],
                )
            previous = (seconds, record)
    return checked


# --------------------------------------------------------------------------
# R4: sub-second restatement agreement
# --------------------------------------------------------------------------

def rule_r4(records: list[dict], findings: Findings) -> int:
    """Sub-second timestamps restated in later chapters must match exactly.

    The failure this catches is a near-miss restatement: 07:08:09.442 in one
    chapter and 07:08:09.422 in another. Those are indistinguishable to a
    reader scanning for contradictions and fatal to a forensic plot.
    """
    subsecond = [r for r in records if r["kind"] == "timestamp" and "." in r["value"]]
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in subsecond:
        seconds = parse_clock(r["normalized"])
        if seconds:
            groups[f"{seconds[0]:.3f}"].append(r)

    keys = sorted(groups, key=float)
    for i, key in enumerate(keys):
        for other in keys[i + 1:]:
            gap = abs(float(other) - float(key))
            if 0 < gap <= 1.0:
                a, b = groups[key][0], groups[other][0]
                findings.add(
                    "R4",
                    "hard",
                    f"Near-miss sub-second values {a['value']} and {b['value']} differ by {gap:.3f}s",
                    [cite(a), cite(b)],
                )
    return len(subsecond)


# --------------------------------------------------------------------------
# R5: designator canonical form
# --------------------------------------------------------------------------

def rule_r5(records: list[dict], findings: Findings) -> int:
    """Each designator must appear in exactly one surface form."""
    groups: dict[str, set[str]] = defaultdict(set)
    examples: dict[tuple[str, str], dict] = {}
    for r in records:
        if r["kind"] != "designator":
            continue
        groups[r["normalized"]].add(r["value"])
        examples.setdefault((r["normalized"], r["value"]), r)

    for normalized, variants in sorted(groups.items()):
        if len(variants) > 1:
            citations = [cite(examples[(normalized, v)]) for v in sorted(variants)]
            findings.add(
                "R5",
                "hard",
                f"Designator {normalized} appears as {sorted(variants)}",
                citations,
            )
    return len(groups)


# --------------------------------------------------------------------------
# R6: entity near-miss variants
# --------------------------------------------------------------------------

def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]


def rule_r6(records: list[dict], findings: Findings, min_count: int = 3) -> int:
    """Surface single-edit variants among recurring entity names."""
    counts: dict[str, int] = defaultdict(int)
    examples: dict[str, dict] = {}
    for r in records:
        # Only mid-sentence capitals are evidence of a name. Counting
        # sentence-initial ones turns every "Close"/"Closed" pair into a
        # finding and buries the real ones.
        if r["kind"] != "entity" or not r.get("mid_sentence"):
            continue
        counts[r["value"]] += 1
        examples.setdefault(r["value"], r)

    recurring = sorted(name for name, count in counts.items() if count >= min_count)
    for i, a in enumerate(recurring):
        for b in recurring[i + 1:]:
            if abs(len(a) - len(b)) > 1 or a.lower() == b.lower():
                continue
            if levenshtein(a, b) == 1:
                findings.add(
                    "R6",
                    "review",
                    f"Near-miss entity names '{a}' ({counts[a]}x) and '{b}' ({counts[b]}x)",
                    [cite(examples[a]), cite(examples[b])],
                )
    return len(recurring)


# --------------------------------------------------------------------------
# R7: quantity registry
# --------------------------------------------------------------------------

NUMBER_WORD_VALUES = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100,
}


def numeric_value(token: str) -> float | None:
    """Normalize 'eleven', '11', 'eleven-point-two', and '11.2' to one axis."""
    text = token.lower().strip().replace("‐", "-").replace("–", "-")
    try:
        return float(text)
    except ValueError:
        pass
    if "point" in text:
        whole, _, frac = text.partition("point")
        whole_value = numeric_value(whole.strip(" -"))
        frac_value = numeric_value(frac.strip(" -"))
        if whole_value is None or frac_value is None:
            return None
        return whole_value + frac_value / 10
    parts = [p for p in re.split(r"[-\s]+", text) if p]
    total = 0.0
    seen = False
    for part in parts:
        if part not in NUMBER_WORD_VALUES:
            return None
        value = NUMBER_WORD_VALUES[part]
        seen = True
        total = total * value if value == 100 else total + value
    return total if seen else None


# The quantities the plot actually rests on. Each pattern captures the number
# wherever the manuscript states that fact; every capture must agree.
#
# This list is deliberately curated and deliberately short. A generic pattern
# produces confident nonsense: "every two seconds" is a status light blinking,
# not the carrier cadence, and "Eight years ago" is an inventory number, not the
# strike. Only facts that are single-valued *by construction* belong here, and
# each pattern is written tightly enough that a wrong value would still match.
# Extend it as later passes identify more load-bearing quantities.
ANCHORED_FACTS = {
    "civilians killed in the strike":
        r"\b([\w-]+)\s+civilians?\s+(?:were\s+|[\w\s]{0,20}remained\s+)?(?:dead|died|killed)",
    "children among the dead":
        r"\b([\w-]+)\s+(?:were|was)\s+children\b",
    # Always stated in decimal form, which is what separates the carrier cadence
    # from every incidental "every two seconds" in the book.
    "carrier cadence (seconds)":
        r"(?:every|toward|at)\s+((?:\d+\.\d+)|(?:[\w]+-point-[\w]+))[\s-]seconds?\b",
    "custody package count":
        r"\b([\w-]+)[\s-]package\s+(?:structure|labels|custody|chest)\b",
}


def rule_r7(records: list[dict], findings: Findings) -> int:
    """Every statement of a load-bearing quantity must state the same value."""
    paths: list[tuple[int, str, str]] = []
    seen = set()
    for r in records:
        if r["path"] not in seen:
            seen.add(r["path"])
            paths.append((unit_order(r["unit"]), r["unit"], r["path"]))
    paths.sort()

    observed: dict[str, dict[float, dict]] = defaultdict(dict)
    for _order, unit, path in paths:
        for lineno, line in enumerate(
            (REPO_ROOT / path).read_text(encoding="utf-8").splitlines(), start=1
        ):
            for fact, pattern in ANCHORED_FACTS.items():
                for m in re.finditer(pattern, line, re.I):
                    value = numeric_value(m.group(1))
                    if value is None:
                        continue
                    observed[fact].setdefault(
                        value,
                        {
                            "path": path,
                            "line": lineno,
                            "unit": unit,
                            "context": m.group(0),
                        },
                    )

    for fact in sorted(observed):
        values = observed[fact]
        if len(values) > 1:
            rendered = ", ".join(
                f"{v:g} ({values[v]['unit']})" for v in sorted(values)
            )
            findings.add(
                "R7",
                "review",
                f"Anchored fact '{fact}' is stated with differing values: {rendered}",
                [f"{d['path']}:{d['line']} — {d['context']}" for d in values.values()],
            )
    return sum(len(v) for v in observed.values())


# --------------------------------------------------------------------------
# R9: one surname, one given name, one rank
# --------------------------------------------------------------------------

# R6 catches near-miss *spellings* of a recurring name. It cannot catch a
# character who keeps her surname but acquires a different given name or rank
# between chapters, because neither variant is a near-miss of the other and
# each may appear only once. That is exactly how Book 2's RCMP lead became
# "Inspector Amrita Dhaliwal" in accepted Chapter 1 and "Superintendent Deepa
# Dhaliwal" in drafted Chapter 2.
#
# Reporting, not hard: promotions happen, and relatives share surnames. The
# rule surfaces the pairing for adjudication.
RANKS = (
    "Inspector", "Superintendent", "Sergeant", "Constable", "Detective",
    "Corporal", "Commissioner", "Commander", "Captain", "Major", "Colonel",
    "General", "Lieutenant", "Admiral", "Officer", "Agent", "Director",
    "Deputy", "Chief", "Senator", "Congressman", "Congresswoman", "Governor",
    "Justice", "Judge", "Doctor", "Professor", "Secretary", "Ambassador",
    "Naib", "Subedar", "Naik", "Havildar", "Sepoy", "Rifleman", "Special",
)
RANK_ALT = "|".join(RANKS)

# "Inspector Amrita Dhaliwal", "Superintendent Dhaliwal", "Amrita Dhaliwal",
# "Naib Subedar Sethi". Up to two rank words, then an optional given name.
FULL_NAME = re.compile(
    r"\b(?:((?:" + RANK_ALT + r")(?:\s+(?:" + RANK_ALT + r"))?)\s+)?"
    r"(?:([A-Z][a-z]{2,})\s+)?"
    r"([A-Z][a-z]{2,})\b"
)


# Place and organization words that take a capitalized modifier and would
# otherwise read as surnames: "Apex Building", "Fairfax County", "Fenwick Annex".
NOT_A_SURNAME = {
    "Annex", "Agency", "Airport", "Army", "Avenue", "Bank", "Bridge", "Building",
    "Bureau", "Center", "Centre", "Command", "Corps", "County", "Court",
    "Department", "Division", "Facility", "Group", "Hall", "Hospital", "Hotel",
    "Criminal", "Institute", "Intelligence", "Navy", "Office", "Post", "Regiment",
    "Relay", "River", "Secure",
    "Road", "Room", "Service", "Services", "Station", "Street", "Suite",
    "Systems", "Trust", "University", "Valley", "Wing",
    # Number words: "Payload Eighty-Eight", "Core One", "Secure Suite Four".
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
    "Seventy", "Eighty", "Ninety", "Hundred",
}

# Capitalized by grammar rather than by being a name. Filtering on the word is
# more precise than filtering on sentence position, which would also discard a
# real given name that happens to open a sentence -- exactly the case this rule
# exists to catch ("Deepa Dhaliwal sat at the daughter's left.").
NOT_A_GIVEN_NAME = {
    "A", "After", "All", "Also", "And", "Another", "Any", "As", "At", "Because",
    "Before", "Both", "But", "By", "Can", "Could", "Did", "Do", "Does", "Each",
    "Even", "Every", "For", "Former", "From", "Had", "Has", "Have", "He", "Her",
    "Here", "His", "How", "If", "In", "Is", "It", "Its", "Just", "May", "Might",
    "More", "Most", "Must", "Neither", "New", "No", "None", "Not", "Now", "Of",
    "On", "One", "Only", "Or", "Other", "Our", "Over", "Same", "She", "Should",
    "So", "Some", "Still", "Such", "Than", "That", "The", "Their", "Then",
    "There", "These", "They", "This", "Those", "Through", "To", "Two", "Under",
    "Until", "Was", "We", "Were", "What", "When", "Where", "Which", "While",
    "Who", "Why", "Will", "With", "Without", "Would", "You", "Your",
}

_SENTENCE_END = '.?!"\u201c\u201d:;\u2014-'


def _sentence_initial(raw: str, match: re.Match) -> bool:
    prefix = raw[: match.start()].rstrip()
    return not prefix or prefix[-1] in _SENTENCE_END


def rule_r9(records: list[dict], findings: Findings, min_count: int = 3) -> int:
    """Flag a recurring surname that pairs with more than one given name or rank."""
    paths: list[tuple[int, str, str]] = []
    seen = set()
    for r in records:
        if r["path"] not in seen:
            seen.add(r["path"])
            paths.append((unit_order(r["unit"]), r["unit"], r["path"]))
    paths.sort()

    # Words the book also uses in lowercase. "Direct", "Control" and "Behind"
    # open sentences; "Deepa" and "Hannah" never appear lowercase anywhere. A
    # candidate is rejected only when both signals agree, so a real given name
    # that happens to open a sentence still counts.
    lowercase_vocab: set[str] = set()
    for _order, _unit, path in paths:
        for word in re.findall(r"[A-Za-z']+", (REPO_ROOT / path).read_text(encoding="utf-8")):
            if word[0].islower():
                lowercase_vocab.add(word.lower())

    surname_hits: dict[str, int] = defaultdict(int)
    ranks: dict[str, dict[str, dict]] = defaultdict(dict)
    givens: dict[str, dict[str, dict]] = defaultdict(dict)

    for _order, unit, path in paths:
        for lineno, raw in enumerate(
            (REPO_ROOT / path).read_text(encoding="utf-8").splitlines(), start=1
        ):
            for m in FULL_NAME.finditer(raw):
                rank, given, surname = m.group(1), m.group(2), m.group(3)
                if surname in RANKS or surname in NOT_A_SURNAME:
                    continue
                surname_hits[surname] += 1
                where = {"unit": unit, "path": path, "line": lineno,
                         "value": m.group(0),
                         "context": raw.strip()[:90]}
                if rank:
                    ranks[surname].setdefault(rank, where)
                positional = (
                    _sentence_initial(raw, m) and given.lower() in lowercase_vocab
                ) if given else False
                if (given and given not in RANKS
                        and given not in NOT_A_GIVEN_NAME and not positional):
                    givens[surname].setdefault(given, where)

    checked = 0
    for surname in sorted(surname_hits):
        if surname_hits[surname] < min_count:
            continue
        checked += 1
        for label, table in (("given name", givens), ("rank", ranks)):
            variants = dict(table.get(surname, {}))
            if label == "rank":
                # A longer form that contains a shorter one is the same rank
                # written out: "Special Agent" is not a second rank for "Agent".
                for short in sorted(variants, key=len):
                    for long in [v for v in variants if v != short]:
                        if long.endswith(short):
                            variants.pop(long, None)
            if len(variants) > 1:
                shown = ", ".join(f"{v!r}" for v in sorted(variants))
                findings.add(
                    "R9",
                    "review",
                    f"{surname!r} appears with {len(variants)} {label}s: {shown}",
                    [cite(w) for _, w in sorted(variants.items())],
                )
    return checked


# --------------------------------------------------------------------------
# R8: first-mention index
# --------------------------------------------------------------------------

def rule_r8(records: list[dict]) -> dict[str, dict]:
    """Record where each entity and designator first appears."""
    first: dict[str, dict] = {}
    ordered = sorted(records, key=lambda r: (unit_order(r["unit"]), r["line"]))
    for r in ordered:
        if r["kind"] not in {"entity", "designator"}:
            continue
        first.setdefault(r["value"], {"unit": r["unit"], "path": r["path"], "line": r["line"]})
    return first


# --------------------------------------------------------------------------

def main() -> None:
    global PROFILE, CLOCK, SCENE_TIME, INLINE_TIME, ZONE_CANON
    parser = argparse.ArgumentParser(description=__doc__)
    add_book_argument(parser)
    parser.add_argument("--index", type=Path, default=None)
    parser.add_argument("--json", type=Path, help="write full findings as JSON")
    parser.add_argument(
        "--chronology",
        type=Path,
        help="write the calendar derived from the prose alone",
    )
    parser.add_argument("--rule", action="append", help="run only these rules")
    args = parser.parse_args()

    PROFILE = profile(args.book)
    CLOCK = _clock_re(PROFILE)
    SCENE_TIME = _scene_time_re(PROFILE)
    INLINE_TIME = _inline_time_re(PROFILE)
    ZONE_CANON = PROFILE.zone_canon()
    if args.index is None:
        args.index = PROFILE.index_path

    if not args.index.exists():
        print(f"Missing {args.index}. Run tools/extract_book1_detail_index.py "
              f"--book {PROFILE.number} first.", file=sys.stderr)
        raise SystemExit(2)

    index = json.loads(args.index.read_text(encoding="utf-8"))
    records = index["records"]
    findings = Findings()
    selected = set(args.rule) if args.rule else None

    def enabled(rule: str) -> bool:
        return selected is None or rule in selected

    counts: dict[str, int] = {}
    if enabled("R1"):
        counts["R1"] = rule_r1(records, findings)
    if enabled("R2"):
        counts["R2"] = rule_r2(records, findings)
    if enabled("R3"):
        counts["R3"] = rule_r3(records, findings)
    if enabled("R4"):
        counts["R4"] = rule_r4(records, findings)
    if enabled("R5"):
        counts["R5"] = rule_r5(records, findings)
    if enabled("R6"):
        counts["R6"] = rule_r6(records, findings)
    if enabled("R7"):
        counts["R7"] = rule_r7(records, findings)
    if enabled("R9"):
        counts["R9"] = rule_r9(records, findings)
    first_mentions = rule_r8(records) if enabled("R8") else {}

    labels = {
        "R1": f"{PROFILE.zone_pair[0]}/{PROFILE.zone_pair[1]} offset pairs checked"
               if PROFILE.zone_pair else "cross-zone offset pairs checked",
        "R2": "chapter-ordered timestamps checked",
        "R3": "countdown values checked",
        "R4": "sub-second timestamps checked",
        "R5": "distinct designators checked",
        "R6": "recurring entity names checked",
        "R7": "anchored-fact statements checked",
        "R9": "recurring surnames checked for one given name and one rank",
    }

    hard_failures = 0
    for rule in ("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R9"):
        if rule not in counts:
            continue
        items = findings.for_rule(rule)
        severity = "HARD" if rule in HARD_RULES else "REVIEW"
        status = "clean" if not items else f"{len(items)} finding(s)"
        print(f"[{rule}] {severity:6} {counts[rule]:>6,} {labels[rule]:<38} {status}")
        for item in items:
            print(f"         - {item['summary']}")
            for citation in item["citations"]:
                print(f"           {citation}")
        if rule in HARD_RULES:
            hard_failures += len(items)

    if first_mentions:
        print(f"[R8] INDEX  {len(first_mentions):>6,} first mentions recorded")

    if args.chronology and getattr(rule_r2, "scenes", None):
        lines = [
            # Book 1's heading is reproduced verbatim: its chronology is a
            # committed artifact that CI diffs byte for byte.
            "# Book 1 chronology derived from the accepted prose"
            if PROFILE.number == 1
            else f"# Book {PROFILE.number} chronology derived from the prose",
            "",
            "Generated by `tools/check_book1_detail_rules.py --chronology`."
            if PROFILE.number == 1
            else f"Generated by `tools/check_book1_detail_rules.py --book "
                 f"{PROFILE.number} --chronology`.",
            "",
            "`Stated` is a date the prose names in a scene header. `Derived` is the",
            "date implied by counting midnights from the first stated date. Where the",
            "two columns disagree, or where a scene has a derived date and no stated",
            "one, a control document can drift without ever contradicting the prose.",
            "",
            "| Scene | Header | Day index | Stated | Derived |",
            "|---|---|---|---|---|",
        ]
        for scene in rule_r2.scenes:
            lines.append(
                f"| `{scene['unit']}`:{scene['line']} | {scene['header']} | "
                f"{scene['day_index']} | {scene['stated_date'] or '—'} | "
                f"{scene.get('derived_date', '—')} |"
            )
        args.chronology.parent.mkdir(parents=True, exist_ok=True)
        args.chronology.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote {args.chronology}")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "counts": counts,
            "findings": findings.items,
            "first_mentions": first_mentions,
        }
        args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {args.json}")

    print()
    if hard_failures:
        print(f"FAIL: {hard_failures} hard-rule finding(s)")
        raise SystemExit(1)
    review = len([i for i in findings.items if i["severity"] == "review"])
    print(f"PASS: no hard-rule findings; {review} item(s) flagged for review")


if __name__ == "__main__":
    main()
