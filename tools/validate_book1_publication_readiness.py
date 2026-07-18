#!/usr/bin/env python3
"""Manuscript-wide publication-readiness checks for Julie O'Donnell Book 1."""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_MIN = 105_000
TARGET_MAX = 110_000
FINAL_LINE = "The bubble stayed centered."

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
    re.compile(r"\bscene card (?:begun|started|continued) in Chapter\s+\d+\b", re.IGNORECASE),
    re.compile(r"\bend of Chapter\s+\d+\b", re.IGNORECASE),
    re.compile(r"\bduring Chapter\s+\d+\b", re.IGNORECASE),
    re.compile(r"\bChapter\s+\d+ comparison\b", re.IGNORECASE),
)

CHAPTER_HEADING_RE = re.compile(r"^# Chapter (\d+) — (.+)$")
PROLOGUE_HEADING_RE = re.compile(r"^# Prologue (?:-|—) (.+)$")
BACKTICK_DISPLAY_RE = re.compile(r"`[A-Z0-9][A-Z0-9 _:/.-]{3,}`")
JOINED_HEADING_RE = re.compile(r"[^\n]# Chapter \d+")
TIMESTAMP_RE = re.compile(r"\b\d{2}:\d{2}(?::\d{2})?\s+(?:EDT|EST|IST)\b")

ENTRY_RE = re.compile(
    r'^[ \t]*-[ \t]+path:[ \t]*"([^"]+)"[ \t]*$\n'
    r'^[ \t]+title:[ \t]*"([^"]+)"[ \t]*$\n'
    r'^[ \t]+accepted_on:[ \t]*"([^"]+)"[ \t]*$\n'
    r'^[ \t]+words:[ \t]*(\d+)[ \t]*$\n'
    r'^[ \t]+sha256:[ \t]*"([0-9a-f]{64})"[ \t]*$',
    re.MULTILINE,
)

STALE_CONTROL_LITERALS = (
    "124,779",
    "61,124",
    "08:14:44 EDT / 17:44:44 IST",
    "Publication-ready state: not yet determined",
)


class ValidationError(RuntimeError):
    """A publication-readiness invariant failed."""


@dataclass(frozen=True)
class ManifestEntry:
    path: str
    title: str
    accepted_on: str
    words: int
    sha256: str


def fail(message: str) -> None:
    raise ValidationError(message)


def _read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing {path}")
    return path.read_text(encoding="utf-8")


def parse_manifest(root: Path) -> tuple[list[ManifestEntry], int, str]:
    manifest = root / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
    text = _read(manifest)
    accepted_block = text.split("\nexcluded_from_canon:", 1)[0]

    entries = [
        ManifestEntry(path, title, accepted_on, int(words), sha256)
        for path, title, accepted_on, words, sha256 in ENTRY_RE.findall(accepted_block)
    ]
    if len(entries) != 25:
        fail(f"expected 25 accepted prose files, found {len(entries)}")
    if len({entry.path for entry in entries}) != len(entries):
        fail("accepted manifest contains duplicate paths")

    total_match = re.search(
        r"^total_accepted_words:[ \t]*(\d+)[ \t]*$", text, re.MULTILINE
    )
    if not total_match:
        fail("manifest missing total_accepted_words")
    total = int(total_match.group(1))

    title_match = re.search(r'^title:[ \t]*"([^"]+)"', text, re.MULTILINE)
    if not title_match or title_match.group(1) != "Veridrift":
        fail("manifest title must be Veridrift")

    if 'status: "developmentally_revised"' not in text:
        fail("manifest status must be developmentally_revised")
    if 'publication_readiness: "specialist_review_and_copyedit_required"' not in text:
        fail("manifest publication readiness must require specialist review and copyedit")

    if sum(entry.words for entry in entries) != total:
        fail(
            "manifest total does not equal the sum of accepted entry word counts: "
            f"{total:,} vs {sum(entry.words for entry in entries):,}"
        )
    return entries, total, text


def validate_heading(path: Path, title: str, text: str) -> None:
    lines = text.splitlines()
    first = lines[0] if lines else ""
    relative = path.as_posix()

    if relative.endswith("/manuscript/prologue.md"):
        match = PROLOGUE_HEADING_RE.fullmatch(first)
        if not match:
            fail(f"nonstandard prologue heading in {relative}: {first!r}")
        if match.group(1) != title:
            fail(
                f"title mismatch in {relative}: manifest={title!r}, heading={match.group(1)!r}"
            )
        return

    if "/manuscript/chapters/" not in relative:
        fail(f"accepted prose path is outside manuscript inventory: {relative}")

    match = CHAPTER_HEADING_RE.fullmatch(first)
    if not match:
        fail(f"nonstandard chapter heading in {relative}: {first!r}")
    expected_number = int(path.stem.split("-")[-1])
    if int(match.group(1)) != expected_number:
        fail(f"chapter number mismatch in {relative}")
    if match.group(2) != title:
        fail(
            f"title mismatch in {relative}: manifest={title!r}, heading={match.group(2)!r}"
        )


def validate_text(path: Path, title: str, text: str) -> None:
    label = path.as_posix()
    validate_heading(path, title, text)

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
            if re.search(
                r"(?:Virginia|Washington, D\.C\.|Kashmir|Eastern Daylight Time|Indian Standard Time)$",
                line.strip(),
            ):
                fail(f"leading space on scene heading in {label}:{line_number}")


def validate_manifest_files(
    root: Path, entries: list[ManifestEntry], texts: dict[str, str]
) -> int:
    actual_total = 0
    for entry in entries:
        path = root / entry.path
        text = texts[entry.path]
        actual_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if actual_sha != entry.sha256:
            fail(
                f"sha256 mismatch for {entry.path}: "
                f"manifest={entry.sha256}, actual={actual_sha}"
            )
        actual_words = len(text.split())
        if actual_words != entry.words:
            fail(
                f"word-count mismatch for {entry.path}: "
                f"manifest={entry.words}, actual={actual_words}"
            )
        actual_total += actual_words
    return actual_total


def validate_thermostat_scene(root: Path) -> None:
    chapter_4 = _read(root / "books/book-01/manuscript/chapters/chapter-04.md")
    chapter_5 = _read(root / "books/book-01/manuscript/chapters/chapter-05.md")
    combined = chapter_4 + "\n" + chapter_5
    marker = "0088 / COMP-04 / CORE-01"
    if marker not in combined:
        fail("thermostat message marker is missing")

    detailed_scene_anchors = (
        "He generated a compressor fault.",
        "He bridged the contacts eight times.",
    )
    detailed_count = sum(anchor in combined for anchor in detailed_scene_anchors)
    if detailed_count != 1:
        fail(
            "expected one detailed thermostat transmission scene across Chapters 4–5, "
            f"found {detailed_count}"
        )


def validate_final_scene(root: Path, text: str) -> None:
    if not text.rstrip().endswith(FINAL_LINE):
        fail(f"Chapter 24 must end with `{FINAL_LINE}`")
    final_section = text.rsplit("\n\n---\n\n", 1)[-1]
    if TIMESTAMP_RE.search(final_section):
        fail("final farm section still contains an exact clock timestamp")


def validate_no_chapter_25(root: Path, manifest_text: str) -> None:
    book_root = root / "books/book-01"
    artifacts = [
        path
        for path in book_root.rglob("chapter-25*")
        if path.is_file() and "archive" not in path.parts
    ]
    if artifacts:
        labels = ", ".join(str(path.relative_to(root)) for path in artifacts)
        fail(f"unauthorized Chapter 25 artifact found: {labels}")
    if re.search(r"chapter-25", manifest_text, re.IGNORECASE):
        fail("accepted manifest references an unauthorized Chapter 25")


def validate_control_metadata(root: Path, total: int) -> None:
    files = (
        root / "README.md",
        root / "books/book-01/control/README.md",
        root / "books/book-01/control/51-publication-readiness-status.md",
    )
    texts = {path: _read(path) for path in files}
    combined = "\n".join(texts.values())

    for literal in STALE_CONTROL_LITERALS:
        if literal in combined:
            fail(f"stale control metadata remains: {literal!r}")

    formatted_total = f"{total:,}"
    for path, text in texts.items():
        if formatted_total not in text:
            fail(
                f"control metadata in {path.relative_to(root)} does not contain "
                f"accepted total {formatted_total}"
            )

    control = texts[root / "books/book-01/control/README.md"]
    status = texts[root / "books/book-01/control/51-publication-readiness-status.md"]
    if "Prologue and Chapters 1–24" not in control:
        fail("control README does not identify Prologue and Chapters 1–24")
    if "Prologue + Chapters 1–24" not in status:
        fail("publication status does not identify Prologue + Chapters 1–24")
    if FINAL_LINE not in control or FINAL_LINE not in status:
        fail("control files do not preserve the final line")

    lower = combined.lower()
    if "original 02:14" not in lower:
        fail("control metadata does not preserve the original 02:14 open thread")
    if "sterling" not in lower or "personal" not in lower or "unresolved" not in lower:
        fail("control metadata does not preserve Sterling's unresolved personal-command thread")


def validate_repository(
    root: Path,
    *,
    target_min: int = TARGET_MIN,
    target_max: int = TARGET_MAX,
    pre_revision: bool = False,
) -> int:
    root = root.resolve()
    entries, manifest_total, manifest_text = parse_manifest(root)

    texts: dict[str, str] = {}
    for entry in entries:
        path = root / entry.path
        text = _read(path)
        texts[entry.path] = text
        validate_text(path, entry.title, text)

    chapter_24_path = "books/book-01/manuscript/chapters/chapter-24.md"
    if chapter_24_path not in texts:
        fail("accepted inventory is missing Chapter 24")
    validate_final_scene(root, texts[chapter_24_path])
    validate_no_chapter_25(root, manifest_text)
    validate_thermostat_scene(root)

    actual_total = validate_manifest_files(root, entries, texts)
    if actual_total != manifest_total:
        fail(
            f"actual accepted total {actual_total:,} does not match manifest total "
            f"{manifest_total:,}"
        )

    if not target_min <= actual_total <= target_max:
        message = (
            f"accepted word count {actual_total:,} is outside "
            f"{target_min:,}–{target_max:,}"
        )
        if pre_revision:
            print(f"WARN: {message}")
        else:
            fail(message)

    validate_control_metadata(root, actual_total)
    return actual_total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pre-revision",
        action="store_true",
        help="report an out-of-range word count without failing while revision is in progress",
    )
    args = parser.parse_args()

    try:
        total = validate_repository(ROOT, pre_revision=args.pre_revision)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(f"PASS: Book 1 publication-readiness checks; accepted words={total:,}")


if __name__ == "__main__":
    main()
