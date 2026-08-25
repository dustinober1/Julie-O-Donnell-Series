#!/usr/bin/env python3
"""Permanent guard on Book 1's ending and its two deliberate proof ceilings.

Replaces tools/validate_book1_chapter24.py, retired 2026-08-25. That validator
mixed two incompatible things: a one-shot scope gate for the Chapter 24
acceptance PR (pinned to a base commit, a changed-file set, and git blob
hashes) and a set of content invariants. The scope gate went stale the moment
the developmental revision landed, and it dragged the content checks down with
it -- 19 of its 24 "required elements" no longer existed in the rewritten
chapter, and its pinned word counts described a draft that has not existed
since. See books/book-01/control/79-chapter24-validator-retirement.md.

Nothing here is pinned to a word count, a blob, or a commit. Every check is a
content invariant that survives ordinary revision, which is the only kind of
check that stays useful. The prohibited-conclusion guard is now applied to the
whole accepted manuscript rather than to Chapter 24 alone.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "books/book-01/manuscript"
CH24 = MANUSCRIPT / "chapters/chapter-24.md"

FINAL_LINE = "The bubble stayed centered."

# Affirmative statements that would collapse a deliberate series thread or
# overclaim past the evidence the book establishes. Every entry is a literal,
# not a pattern: the prose repeatedly *denies* these propositions ("It does not
# prove Senator Sterling held it"), and a looser regex would fire on exactly the
# sentences that enforce the ceiling. Each was verified absent when added.
PROHIBITED = (
    # Sterling's personal knowledge, direction, possession, or command
    "Sterling ordered",
    "Sterling commanded",
    "Sterling directed",
    "Sterling instructed",
    "Sterling authorized",
    "Sterling had ordered",
    "proves Sterling held",
    "proves that Sterling",
    "opened SSO-NS-004",
    "operated SSO-NS-004",
    # the human or upstream instruction behind the original 02:14 construction
    "Vance was the original 02:14 operator",
    "Vance was the sole architect",
    "Vance directed",
    "Vance constructed",
    "Vance initiated",
    "identified the physical operator",
    "the physical operator was",
    # findings the book deliberately refuses to reach
    "Tariq was physically",
    "Tariq operated",
    "Tariq opened",
    "WSS plaintext showed",
    "Julie was fully exonerated",
    "Julie was exonerated",
    "Elias was granted immunity",
    "Price was cleared",
    "conclusively proved",
    "beyond any doubt",
    # drafting residue and a chapter that must not exist
    "# Chapter 25",
    "TODO",
    "TBD",
    "FIXME",
)

# Elements of Chapter 24 that carry the ending's argument and survived the
# developmental revision. Deliberately short: a long list of quoted fragments is
# a snapshot of one draft, not an invariant, which is how the retired validator
# rotted.
CH24_REQUIRED = (
    "CHARGING: UNRESOLVED",
    "It was not repaired.",
    "independent source-integrity practice",
    "evidence architecture",
    "Possible personal contact",
)

# Chapter 24 must leave both series carryovers explicitly open.
CH24_OPEN_THREADS = (
    "who initiated the original 02:14 construction",
    "Sterling personally knew or directed",
)

_failures: list[str] = []


def fail(message: str) -> None:
    _failures.append(message)


def accepted_files() -> list[Path]:
    return [MANUSCRIPT / "prologue.md"] + sorted(
        (MANUSCRIPT / "chapters").glob("chapter-*.md")
    )


def check_prohibited(paths: list[Path]) -> int:
    checked = 0
    for path in paths:
        lowered = path.read_text(encoding="utf-8").lower()
        for phrase in PROHIBITED:
            checked += 1
            if phrase.lower() in lowered:
                fail(
                    f"prohibited conclusion in {path.relative_to(ROOT)}: {phrase!r}"
                )
    return checked


def check_chapter_24() -> None:
    text = CH24.read_text(encoding="utf-8")

    # Structural identity, anchored on text rather than on bytes or counts.
    if not text.lstrip().startswith("# Chapter 24 "):
        fail("Chapter 24 does not open with its chapter heading")
    if "The Terms of Return" not in text.split("\n", 1)[0]:
        fail("Chapter 24 title changed")
    if "Secure MPD Evidence Intake" not in text:
        fail("Chapter 24 opening location changed")

    if not text.rstrip().endswith(FINAL_LINE):
        fail(f"Chapter 24 final line changed; must end {FINAL_LINE!r}")

    lowered = text.lower()
    for phrase in CH24_REQUIRED:
        if phrase.lower() not in lowered:
            fail(f"Chapter 24 missing required element: {phrase!r}")
    for phrase in CH24_OPEN_THREADS:
        if phrase.lower() not in lowered:
            fail(f"Chapter 24 no longer leaves a series thread open: {phrase!r}")


def check_no_chapter_25() -> None:
    strays = sorted(
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*chapter-25*")
        if p.is_file() and ".git/" not in p.as_posix()
    )
    if strays:
        fail("Chapter 25 artifact exists: " + ", ".join(strays))


def main() -> int:
    paths = accepted_files()
    if len(paths) != 25:
        fail(f"expected 25 accepted prose files, found {len(paths)}")

    checked = check_prohibited(paths)
    check_chapter_24()
    check_no_chapter_25()

    if _failures:
        for message in _failures:
            print(f"FAIL: {message}", file=sys.stderr)
        return 1

    print(
        f"PASS: Book 1 ending invariants; {len(PROHIBITED)} prohibited "
        f"conclusions checked across {len(paths)} files ({checked} assertions), "
        f"{len(CH24_REQUIRED) + len(CH24_OPEN_THREADS)} Chapter 24 elements intact, "
        f"final line preserved"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
