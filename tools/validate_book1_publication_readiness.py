#!/usr/bin/env python3
"""Manuscript-wide publication-readiness checks for Julie O'Donnell Book 1."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
TARGET_MIN = 105_000
TARGET_MAX = 110_000

FORBIDDEN_LITERAL = (
    "the scene card begun in Chapter 14",
    "the end of Chapter 21",
    "the Chapter 21 comparison",
    "during Chapter 21",
    "the same restraint geometry in which Chapter 22 had ended",
    "On July thirteenth",
)

FORBIDDEN_META_PATTERNS = (
    re.compile(r"\bthe answer matched Chapter\s+\d+\b", re.IGNORECASE),
    re.compile(r"\bscene card\b", re.IGNORECASE),
    re.compile(r"\bend of Chapter\s+\d+\b", re.IGNORECASE),
    re.compile(r"\bduring Chapter\s+\d+\b", re.IGNORECASE),
    re.compile(r"\bChapter\s+\d+ comparison\b", re.IGNORECASE),
)

HEADING_RE = re.compile(r"^# Chapter (\d+) — .+$")
BACKTICK_DISPLAY_RE = re.compile(r"`[A-Z0-9][A-Z0-9 _:/.-]{3,}`")
JOINED_HEADING_RE = re.compile(r"[^\n]# Chapter \d+")
TIMESTAMP_RE = re.compile(r"\b\d{2}:\d{2}(?::\d{2})?\s+(?:EDT|EST|IST)\b")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def manifest_paths() -> list[Path]:
    if not MANIFEST.is_file():
        fail(f"missing {MANIFEST.relative_to(ROOT)}")
    text = MANIFEST.read_text(encoding="utf-8")
    paths = [ROOT / value for value in re.findall(r'^\s+path:\s+"([^"]+)"\s*$', text, re.MULTILINE)]
    if len(paths) != 25:
        fail(f"expected 25 accepted prose files, found {len(paths)}")
    for path in paths:
        if not path.is_file():
            fail(f"missing accepted prose file {path.relative_to(ROOT)}")
    return paths


def word_count(paths: list[Path]) -> int:
    return sum(len(path.read_text(encoding="utf-8").split()) for path in paths)


def validate_chapter_heading(path: Path, text: str) -> None:
    if "manuscript/chapters/" not in path.as_posix():
        return
    first = text.splitlines()[0] if text.splitlines() else ""
    match = HEADING_RE.fullmatch(first)
    if not match:
        fail(f"nonstandard chapter heading in {path.relative_to(ROOT)}: {first!r}")
    expected = int(path.stem.split("-")[-1])
    if int(match.group(1)) != expected:
        fail(f"chapter number mismatch in {path.relative_to(ROOT)}")


def validate_text(path: Path, text: str) -> None:
    label = path.relative_to(ROOT)
    validate_chapter_heading(path, text)

    if JOINED_HEADING_RE.search(text):
        fail(f"chapter heading attached to prose in {label}")

    for phrase in FORBIDDEN_LITERAL:
        if phrase in text:
            fail(f"drafting artifact in {label}: {phrase!r}")

    for pattern in FORBIDDEN_META_PATTERNS:
        match = pattern.search(text)
        if match:
            fail(f"chapter metatext in {label}: {match.group(0)!r}")

    match = BACKTICK_DISPLAY_RE.search(text)
    if match:
        fail(f"backtick system-display artifact in {label}: {match.group(0)!r}")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith(" ") and line.strip() and not line.startswith("    "):
            if re.search(r"(?:Virginia|Washington, D\.C\.|Kashmir|Eastern Daylight Time|Indian Standard Time)$", line.strip()):
                fail(f"leading space on scene heading in {label}:{line_number}")


def validate_thermostat_scene() -> None:
    chapter_4 = (ROOT / "books/book-01/manuscript/chapters/chapter-04.md").read_text(encoding="utf-8")
    chapter_5 = (ROOT / "books/book-01/manuscript/chapters/chapter-05.md").read_text(encoding="utf-8")
    marker = "0088 / COMP-04 / CORE-01"
    if marker not in chapter_4 + chapter_5:
        fail("thermostat message marker is missing")
    if marker in chapter_4 and marker in chapter_5:
        fail("thermostat transmission remains duplicated across Chapters 4 and 5")


def validate_final_scene() -> None:
    path = ROOT / "books/book-01/manuscript/chapters/chapter-24.md"
    text = path.read_text(encoding="utf-8")
    if not text.rstrip().endswith("The bubble stayed centered."):
        fail("Chapter 24 must end with `The bubble stayed centered.`")
    final_section = text.rsplit("\n\n---\n\n", 1)[-1]
    if TIMESTAMP_RE.search(final_section):
        fail("final farm section still contains an exact clock timestamp")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pre-revision",
        action="store_true",
        help="report an out-of-range word count without failing while revision is in progress",
    )
    args = parser.parse_args()

    paths = manifest_paths()
    for path in paths:
        validate_text(path, path.read_text(encoding="utf-8"))
    validate_thermostat_scene()
    validate_final_scene()

    total = word_count(paths)
    if not TARGET_MIN <= total <= TARGET_MAX:
        message = f"accepted word count {total:,} is outside {TARGET_MIN:,}–{TARGET_MAX:,}"
        if args.pre_revision:
            print(f"WARN: {message}")
        else:
            fail(message)

    print(f"PASS: Book 1 publication-readiness checks; accepted words={total:,}")


if __name__ == "__main__":
    main()
