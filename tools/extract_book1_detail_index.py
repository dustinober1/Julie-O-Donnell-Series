#!/usr/bin/env python3
"""Extract a bottom-up detail index from the accepted Book 1 prose.

The existing Book 1 controls verify format, inventory, integrity, and style.
They do not extract story fact. The seven continuity ledgers do hold story
fact, but they were written top-down: a fact had to be noticed before it could
be recorded, and a fact that was never recorded cannot fail a ledger check.

This tool runs the other direction. It reads the 25 accepted prose files named
in ``books/book-01/ACCEPTED_MANUSCRIPT.yaml`` and emits every mechanically
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

Output: ``artifacts/book1-detail-index.json``.

The tool reads only. It never writes to the accepted manuscript.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - environment guard
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
DEFAULT_OUTPUT = REPO_ROOT / "artifacts/book1-detail-index.json"

# --------------------------------------------------------------------------
# Patterns
# --------------------------------------------------------------------------

# 04:52, 04:52:19, 07:08:09.442. Anchored so that a bare "11.2" or a page
# number never reads as a clock value.
TIMESTAMP = re.compile(r"(?<![\d:.])(\d{1,2}):([0-5]\d)(?::([0-5]\d)(\.\d+)?)?(?![\d:])")

DATE = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\b")

# Zone marker immediately following a timestamp. The manuscript uses both the
# abbreviation and the spelled-out form, and pairs them in either order.
ZONE = re.compile(
    r"^\s*(?:hours\s+)?(EDT|IST|Eastern Daylight Time|Indian Standard Time|Eastern|Indian)\b",
    re.IGNORECASE,
)

ZONE_CANON = {
    "edt": "EDT",
    "eastern": "EDT",
    "eastern daylight time": "EDT",
    "ist": "IST",
    "indian": "IST",
    "indian standard time": "IST",
}

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


def load_manifest() -> list[dict]:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    return data["accepted_files"]


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
        "source": "books/book-01/ACCEPTED_MANUSCRIPT.yaml",
        "units": units,
        "totals": {"records": len(records), "by_class": dict(sorted(by_class.items()))},
        "records": [asdict(r) for r in records],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    index = build_index()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if not args.quiet:
        totals = index["totals"]
        print(f"Extracted {totals['records']:,} detail records from {len(index['units'])} accepted files")
        for detail_class, count in totals["by_class"].items():
            print(f"  {detail_class}: {count:,}")
        print(f"Wrote {args.output.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
