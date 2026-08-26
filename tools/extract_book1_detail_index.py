#!/usr/bin/env python3
"""Extract a bottom-up detail index from a book's prose.

The existing controls verify format, inventory, integrity, and style.
They do not extract story fact. The seven continuity ledgers do hold story
fact, but they were written top-down: a fact had to be noticed before it could
be recorded, and a fact that was never recorded cannot fail a ledger check.

This tool runs the other direction. It reads the prose files named by the
book's source of truth and emits every mechanically
extractable concrete detail as a citation-carrying record, so that the prose
becomes the ground truth the ledgers are tested against.

It covers the detail classes that pattern matching can reach:

    D1  clock and calendar
    D2  named entities
    D3  designators and codes
    D8  quantities

D4 (space and movement), D5 (objects and custody), D6 (injury and capability),
D7 (knowledge state), and D9 (surface continuity) cannot be pattern matched and
are handled by the per-chapter scene cards instead.

Output: the book profile's index path, ``artifacts/book1-detail-index.json`` by
default. Pass ``--book 2`` for Book 2; per-book settings live in
``tools/book_profiles.py``. This file keeps its Book 1 name because frozen
Book 1 control records cite it by path.

The tool reads only. It never writes to the accepted manuscript.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path

from book_profiles import REPO_ROOT, BookProfile, add_book_argument, profile

# Set by main() once the book is known. Book 1 stays the default everywhere, so
# existing invocations and Book 1's committed artifacts are unchanged.
PROFILE: BookProfile = profile(1)

# --------------------------------------------------------------------------
# Patterns
# --------------------------------------------------------------------------

# 04:52, 04:52:19, 07:08:09.442. Anchored so that a bare "11.2" or a page
# number never reads as a clock value.
TIMESTAMP = re.compile(r"(?<![\d:.])(\d{1,2}):([0-5]\d)(?::([0-5]\d)(\.\d+)?)?(?![\d:])")

DATE = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\b")

# Zone marker immediately following a timestamp. The manuscript uses both the
# abbreviation and the spelled-out form, and pairs them in either order.
def _zone_re(prof: BookProfile) -> re.Pattern:
    return re.compile(
        r"^\s*(?:hours\s+)?(" + prof.zone_alternation() + r")\b",
        re.IGNORECASE,
    )


ZONE = _zone_re(PROFILE)

ZONE_CANON = PROFILE.zone_canon()

# Designators: APX-DIR-0019, SSO-NS-004, K-17, PCF-27, L3-7, VAL-088,
# DIA-SAR-PRICE-01, SIGMA-NORMALIZE-4, COMP-04, CORE-01, WSS-4, H-3.
# Hyphen class covers the en dash, because a dash swap is exactly the kind of
# silent drift rule R5 exists to catch.
DESIGNATOR = re.compile(r"\b([A-Z][A-Z0-9]{0,11}(?:[-‐-―][A-Z0-9]{1,11}){1,4})\b")

# "Payload 88", "Partition B", "Building Three", "Zone H-3" — a capitalized
# label carrying a number or single-letter suffix.
LABELLED_NUMBER = re.compile(r"\b([A-Z][a-z]{2,15})\s+((?:\d{1,4})|[A-Z])\b")

NUMERAL = re.compile(r"(?<![\w:.-])(\d+(?:\.\d+)?)(?![\w:.-])")

NUMBER_WORDS = (
    "zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty "
    "thirty forty fifty sixty seventy eighty ninety hundred thousand million "
    "first second third fourth fifth sixth seventh eighth ninth tenth"
).split()
NUMBER_WORD = re.compile(
    r"\b((?:" + "|".join(NUMBER_WORDS) + r")(?:[-‐-―](?:" + "|".join(NUMBER_WORDS) + r"))*)\b",
    re.IGNORECASE,
)

# Durations, which the ledgers never captured and which carry as much
# continuity load as the absolute clock does.
DURATION = re.compile(
    r"\b((?:\d+(?:\.\d+)?|" + "|".join(NUMBER_WORDS) + r")(?:[-‐-―](?:" + "|".join(NUMBER_WORDS) + r"))*)"
    r"[\s‐-―]+(second|seconds|minute|minutes|hour|hours|day|days|week|weeks|month|months|year|years)\b",
    re.IGNORECASE,
)

CAPITALIZED = re.compile(r"\b([A-Z][a-zA-Z’']{2,})\b")

# Words that start a sentence or a line of dialogue and are not proper nouns.
# Kept deliberately broad; a false negative here only costs a review line.
STOPWORDS = {
    "the", "and", "but", "for", "not", "yes", "you", "she", "her", "his", "him",
    "they", "them", "their", "that", "this", "these", "those", "then", "there",
    "here", "what", "when", "where", "which", "who", "whom", "whose", "why",
    "how", "with", "without", "from", "into", "onto", "over", "under", "after",
    "before", "because", "while", "until", "unless", "though", "although",
    "nothing", "nobody", "none", "neither", "either", "every", "each", "any",
    "all", "some", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "eleven", "twelve", "twenty", "thirty", "forty",
    "fifty", "sixty", "hundred", "first", "second", "third", "last", "next",
    "her", "she", "it", "its", "was", "were", "had", "has", "have", "did",
    "does", "can", "could", "would", "should", "will", "shall", "may", "might",
    "must", "are", "is", "am", "be", "been", "being", "his", "our", "your",
    "let", "get", "got", "put", "say", "said", "tell", "told", "ask", "asked",
    "now", "still", "just", "only", "even", "also", "too", "very", "more",
    "most", "less", "least", "again", "once", "twice", "never", "always",
    "sometimes", "somewhere", "someone", "something", "anyone", "anything",
    "everyone", "everything", "if", "so", "as", "at", "by", "in", "of", "on",
    "or", "to", "up", "no", "nor", "an", "a", "i", "we", "he", "do", "don",
    "outside", "inside", "above", "below", "beyond", "beneath", "between",
    "behind", "across", "against", "along", "around", "through", "toward",
    "towards", "upon", "within", "off", "out", "down", "back", "away", "both",
    "same", "other", "another", "such", "own", "few", "many", "much",
}


@dataclass
class Record:
    """One extracted detail, always carrying enough to cite it."""

    detail_class: str
    kind: str
    value: str
    normalized: str
    path: str
    line: int
    unit: str
    context: str
    # True when the token is capitalized in a position where capitalization
    # carries information. "Clear" opening a line of dialogue proves nothing;
    # "Clear" mid-sentence would be a name.
    mid_sentence: bool = False


# Parsed by regex rather than PyYAML so this runs in the same bare CI job as
# the other permanent Book 1 validators, which carry no third-party
# dependencies. Mirrors the shape used by book1_publication_readiness_core.
MANIFEST_ENTRY = re.compile(
    r'^  - path: "([^"]+)"\n'
    r'    title: "([^"]+)"\n'
    r'    accepted_on: "[^"]+"\n'
    r"    words: (\d+)\n"
    r'    sha256: "([0-9a-f]{64})"',
    re.MULTILINE,
)


# Book 2 records narrative units rather than an accepted-file manifest, and a
# unit may be undrafted (path: null) or drafted but not yet accepted. Drafted
# prose is included deliberately: catching a contradiction before acceptance is
# the entire point of running this during drafting.
UNIT_ENTRY = re.compile(
    r'^  - unit: "([^"]+)"\n'
    r'    title: "([^"]+)"\n'
    r"    path: (null|\"[^\"]+\")\n"
    r'    status: "([^"]+)"',
    re.MULTILINE,
)


def load_accepted_manifest(prof: BookProfile) -> list[dict]:
    text = prof.source_of_truth.read_text(encoding="utf-8")
    accepted_block = text.split("\nexcluded_from_canon:", 1)[0]
    return [
        {"path": path, "title": title, "words": int(words), "sha256": sha256}
        for path, title, words, sha256 in MANIFEST_ENTRY.findall(accepted_block)
    ]


def load_narrative_units(prof: BookProfile) -> list[dict]:
    text = prof.source_of_truth.read_text(encoding="utf-8")
    entries = []
    for unit, title, raw_path, status in UNIT_ENTRY.findall(text):
        if raw_path == "null":
            continue
        path = raw_path.strip('"')
        if not (REPO_ROOT / path).exists():
            raise SystemExit(f"{prof.key}: {unit} names a missing file: {path}")
        entries.append({"path": path, "title": title, "words": None,
                        "sha256": None, "status": status})
    return entries


def load_manifest(prof: BookProfile | None = None) -> list[dict]:
    prof = prof or PROFILE
    if prof.source_kind == "accepted-manifest":
        entries = load_accepted_manifest(prof)
    elif prof.source_kind == "narrative-units":
        entries = load_narrative_units(prof)
    else:
        raise SystemExit(f"unknown source kind {prof.source_kind!r}")
    if not entries:
        raise SystemExit(f"{prof.key}: no prose files found in {prof.source_of_truth}")
    if prof.expected_units is not None and len(entries) != prof.expected_units:
        raise SystemExit(
            f"{prof.key}: expected {prof.expected_units} prose files, found {len(entries)}"
        )
    return entries


def unit_name(path: str) -> str:
    """Short label used to order and group findings."""
    stem = Path(path).stem
    if stem == "prologue":
        return "prologue"
    match = re.search(r"(\d+)", stem)
    return f"ch{int(match.group(1)):02d}" if match else stem


def unit_order(unit: str) -> int:
    if unit == "prologue":
        return 0
    match = re.search(r"(\d+)", unit)
    return int(match.group(1)) if match else 999


def snippet(line: str, start: int, end: int, width: int = 70) -> str:
    lo = max(0, start - width)
    hi = min(len(line), end + width)
    text = line[lo:hi].strip()
    return ("…" if lo > 0 else "") + text + ("…" if hi < len(line) else "")


def to_seconds(hh: str, mm: str, ss: str | None, frac: str | None) -> float:
    total = int(hh) * 3600 + int(mm) * 60 + (int(ss) if ss else 0)
    return total + (float(frac) if frac else 0.0)


def format_clock(hh: str, mm: str, ss: str | None, frac: str | None) -> str:
    text = f"{int(hh):02d}:{mm}"
    if ss:
        text += f":{ss}"
    if frac:
        text += frac
    return text


def extract_clock(line: str, path: str, lineno: int, unit: str) -> list[Record]:
    out: list[Record] = []
    for m in TIMESTAMP.finditer(line):
        hh, mm, ss, frac = m.group(1), m.group(2), m.group(3), m.group(4)
        if int(hh) > 23:
            continue
        zone_match = ZONE.match(line[m.end():])
        zone = ZONE_CANON[zone_match.group(1).lower()] if zone_match else ""
        out.append(
            Record(
                detail_class="D1",
                kind="timestamp",
                value=m.group(0),
                normalized=format_clock(hh, mm, ss, frac) + (f" {zone}" if zone else ""),
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    for m in DATE.finditer(line):
        out.append(
            Record(
                detail_class="D1",
                kind="date",
                value=m.group(0),
                normalized=f"{m.group(1)} {int(m.group(2))}",
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    for m in DURATION.finditer(line):
        unit_word = m.group(2).lower().rstrip("s")
        out.append(
            Record(
                detail_class="D1",
                kind="duration",
                value=m.group(0),
                normalized=f"{m.group(1).lower()} {unit_word}",
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    return out


def extract_designators(line: str, path: str, lineno: int, unit: str) -> list[Record]:
    out: list[Record] = []
    for m in DESIGNATOR.finditer(line):
        value = m.group(1)
        # Normalize dash variants and case so that R5 can group true variants.
        normalized = re.sub(r"[‐-―]", "-", value).upper()
        out.append(
            Record(
                detail_class="D3",
                kind="designator",
                value=value,
                normalized=normalized,
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    for m in LABELLED_NUMBER.finditer(line):
        out.append(
            Record(
                detail_class="D3",
                kind="labelled_number",
                value=m.group(0),
                normalized=f"{m.group(1).lower()} {m.group(2).lower()}",
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    return out


def extract_entities(line: str, path: str, lineno: int, unit: str) -> list[Record]:
    out: list[Record] = []
    for m in CAPITALIZED.finditer(line):
        value = m.group(1)
        if value.lower() in STOPWORDS:
            continue
        if value.isupper():
            # All-caps runs are screen and document text, already covered by D3.
            continue
        before = line[:m.start()].rstrip()
        # Sentence-initial and dialogue-initial capitals are grammatical, not
        # onomastic. Only a capital following a word character mid-clause is
        # evidence of a proper noun.
        mid = bool(before) and before[-1] not in '.!?"“”‘’—–-:;' and not before.endswith(",")
        out.append(
            Record(
                detail_class="D2",
                kind="entity",
                value=value,
                normalized=value.lower().replace("’", "'"),
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end(), width=40),
                mid_sentence=mid,
            )
        )
    return out


def extract_quantities(line: str, path: str, lineno: int, unit: str) -> list[Record]:
    out: list[Record] = []
    masked = TIMESTAMP.sub(lambda m: " " * len(m.group(0)), line)
    for m in NUMERAL.finditer(masked):
        out.append(
            Record(
                detail_class="D8",
                kind="numeral",
                value=m.group(1),
                normalized=m.group(1),
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    for m in NUMBER_WORD.finditer(masked):
        out.append(
            Record(
                detail_class="D8",
                kind="number_word",
                value=m.group(1),
                normalized=m.group(1).lower(),
                path=path,
                line=lineno,
                unit=unit,
                context=snippet(line, m.start(), m.end()),
            )
        )
    return out


def extract_file(path: str) -> list[Record]:
    unit = unit_name(path)
    text = (REPO_ROOT / path).read_text(encoding="utf-8")
    records: list[Record] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        records.extend(extract_clock(line, path, lineno, unit))
        records.extend(extract_designators(line, path, lineno, unit))
        records.extend(extract_entities(line, path, lineno, unit))
        records.extend(extract_quantities(line, path, lineno, unit))
    return records


def build_index() -> dict:
    entries = load_manifest()
    records: list[Record] = []
    units: list[dict] = []
    for entry in entries:
        path = entry["path"]
        file_records = extract_file(path)
        records.extend(file_records)
        units.append(
            {
                "unit": unit_name(path),
                "path": path,
                "title": entry["title"],
                "words": entry["words"],
                "records": len(file_records),
            }
        )
    units.sort(key=lambda u: unit_order(u["unit"]))
    by_class: dict[str, int] = {}
    for record in records:
        by_class[record.detail_class] = by_class.get(record.detail_class, 0) + 1
    return {
        "source": PROFILE.source_of_truth.relative_to(REPO_ROOT).as_posix(),
        "units": units,
        "totals": {"records": len(records), "by_class": dict(sorted(by_class.items()))},
        "records": [asdict(r) for r in records],
    }


def main() -> None:
    global PROFILE, ZONE, ZONE_CANON
    parser = argparse.ArgumentParser(description=__doc__)
    add_book_argument(parser)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    PROFILE = profile(args.book)
    ZONE = _zone_re(PROFILE)
    ZONE_CANON = PROFILE.zone_canon()
    if args.output is None:
        args.output = PROFILE.index_path

    index = build_index()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if not args.quiet:
        totals = index["totals"]
        print(f"Extracted {totals['records']:,} detail records from "
              f"{len(index['units'])} {PROFILE.key} prose files")
        for detail_class, count in totals["by_class"].items():
            print(f"  {detail_class}: {count:,}")
        try:
            shown = args.output.resolve().relative_to(REPO_ROOT)
        except ValueError:
            shown = args.output
        print(f"Wrote {shown}")


if __name__ == "__main__":
    main()
