#!/usr/bin/env python3
"""Permanent validation for accepted Julie O'Donnell Book 1 through Chapter 24."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "d8adea11828fbd1ec0a8924e072b566f0fc62bcd"
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
PROJECT = "PROJECT_STATE.yaml"
CH23 = "books/book-01/manuscript/chapters/chapter-23.md"
CH23_LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"
CH23_REVIEW = "books/book-01/control/47-chapter-23-acceptance-review.md"
CH24 = "books/book-01/manuscript/chapters/chapter-24.md"
CH24_LOCK = "books/book-01/control/48-chapter-24-mission-lock.md"
CH24_REVIEW = "books/book-01/control/49-chapter-24-acceptance-review.md"
CH24_DRAFT = "books/book-01/drafts/chapter-24.md"

EXPECTED_TOTAL = 124779
EXPECTED_ACT_III = 61124
EXPECTED_MANIFEST_BLOB = "cae7c37803acf96ecb856af562ecd522e6696499"
EXPECTED_CH23_BLOB = "1f511d36404450f201b34a075f441d350eb7cc52"
EXPECTED_CH23_LOCK_BLOB = "c8c5be7e9ee5a902c7187697cf1bc70c8a5ce30a"
EXPECTED_CH23_REVIEW_BLOB = "c876854075ad1f686ac663018983fd34f0064e2c"
EXPECTED_CH24_BLOB = "abce3cbea04a7afd798b5022ba09ce665a9cc923"
EXPECTED_CH24_LOCK_BLOB = "260186500b448b5154858f7df47f113dc8d6fbfa"
EXPECTED_CH24_REVIEW_BLOB = "f734346a7e959d1b265167130903d44f19512e17"

ACT_III = {
    "books/book-01/manuscript/chapters/chapter-13.md": (6175, "e7d04921431e571aab434f2f4b808655e363d30c"),
    "books/book-01/manuscript/chapters/chapter-14.md": (5763, "78f7fff02cd271fecbc94f7daf7151dbebbd5c6d"),
    "books/book-01/manuscript/chapters/chapter-15.md": (5993, "b8e7e2ae573a6c25ea096121c75acee867f3fad2"),
    "books/book-01/manuscript/chapters/chapter-16.md": (6024, "dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8"),
    "books/book-01/manuscript/chapters/chapter-17.md": (5888, "1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1"),
    "books/book-01/manuscript/chapters/chapter-18.md": (4478, "6f5873d6e975ec74646af152aad22ea84545fc01"),
    "books/book-01/manuscript/chapters/chapter-19.md": (5393, "1c7cc22fc7c480cb247efa1f6a2c0d0b1e1b1baf"),
    "books/book-01/manuscript/chapters/chapter-20.md": (4307, "0bd12f43beeef48d5e897ee1fa78a333bd23099b"),
    "books/book-01/manuscript/chapters/chapter-21.md": (4415, "866d4210b7fc808aef48144a91a58280f38fc99c"),
    "books/book-01/manuscript/chapters/chapter-22.md": (4716, "034ab496794594427d8409d03e7c6659d41b6a91"),
    CH23: (4610, EXPECTED_CH23_BLOB),
    CH24: (3362, EXPECTED_CH24_BLOB),
}

EXPECTED_CHANGED = {
    ".github/workflows/book1-manuscript-validation.yml",
    PROJECT,
    "README.md",
    MANIFEST,
    "books/book-01/control/00-overview.md",
    "books/book-01/control/02-current-project-state.md",
    "books/book-01/control/15-open-plot-threads-and-payoff-matrix.md",
    "books/book-01/control/16-chapter-by-chapter-status-record.md",
    "books/book-01/control/18-act-iii-entry-state.md",
    "books/book-01/control/20-control-pack-maintenance-rules.md",
    "books/book-01/control/22-book-1-ending-contract.md",
    "books/book-01/control/23-word-budget-and-act-iii-architecture.md",
    "books/book-01/control/24-thread-disposition-matrix.md",
    CH24_REVIEW,
    "books/book-01/control/README.md",
    "books/book-01/drafts/README.md",
    "books/book-01/manuscript/STATUS.md",
    CH24,
    "series/recurring-character-ledger.md",
    "tools/validate_book1_chapter23.py",
    "tools/validate_book1_chapter24.py",
    "tools/validate_book1_chapter24_mission_lock.py",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(*args: str) -> str:
    try:
        return subprocess.check_output(
            args, cwd=ROOT, text=True, stderr=subprocess.PIPE
        ).strip()
    except subprocess.CalledProcessError as exc:
        fail(
            f"command `{' '.join(args)}` failed with exit code {exc.returncode}:\n"
            f"{exc.stderr.strip()}"
        )
    except FileNotFoundError:
        fail(f"command `{args[0]}` was not found")
    raise AssertionError("unreachable")


def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        fail(f"missing {path}")
    return target.read_text(encoding="utf-8")


def blob(path: str) -> str:
    return run("git", "hash-object", path)


def word_count(path: str) -> int:
    return len(read(path).split())


def require(text: str, phrases: tuple[str, ...], label: str) -> None:
    for phrase in phrases:
        if phrase not in text:
            fail(f"{label} missing `{phrase}`")


def changed_files() -> set[str]:
    result: set[str] = set()
    output = run("git", "diff", "--name-status", "--find-renames", BASE, "--")
    for line in output.splitlines():
        fields = line.split("\t")
        if fields[0].startswith(("R", "C")) and len(fields) == 3:
            result.add(fields[2])
        elif len(fields) == 2:
            result.add(fields[1])
        else:
            fail(f"unexpected diff entry: {line}")
    return result


def validate_hashes_and_counts() -> None:
    exact = {
        MANIFEST: EXPECTED_MANIFEST_BLOB,
        CH23: EXPECTED_CH23_BLOB,
        CH23_LOCK: EXPECTED_CH23_LOCK_BLOB,
        CH23_REVIEW: EXPECTED_CH23_REVIEW_BLOB,
        CH24: EXPECTED_CH24_BLOB,
        CH24_LOCK: EXPECTED_CH24_LOCK_BLOB,
        CH24_REVIEW: EXPECTED_CH24_REVIEW_BLOB,
    }
    for path, expected in exact.items():
        actual = blob(path)
        if actual != expected:
            fail(f"blob mismatch for {path}: {actual} != {expected}")

    subtotal = 0
    for path, (expected_words, expected_blob) in ACT_III.items():
        actual_words = word_count(path)
        actual_blob = blob(path)
        if actual_words != expected_words or actual_blob != expected_blob:
            fail(
                f"accepted Act III mismatch for {path}: "
                f"words={actual_words}, blob={actual_blob}"
            )
        subtotal += actual_words
    if subtotal != EXPECTED_ACT_III:
        fail(f"Act III subtotal mismatch: {subtotal}")

    protected = ["books/book-01/manuscript/prologue.md"] + [
        f"books/book-01/manuscript/chapters/chapter-{n:02d}.md"
        for n in range(1, 13)
    ]
    if subprocess.run(
        ["git", "diff", "--quiet", BASE, "--", *protected], cwd=ROOT
    ).returncode:
        fail("accepted Prologue or Chapters 1–12 changed")

    if subprocess.run(
        [sys.executable, "tools/count_book1_words.py", "--expect", str(EXPECTED_TOTAL)],
        cwd=ROOT,
    ).returncode:
        fail("accepted Book 1 total mismatch")


def validate_manifest_and_navigation() -> None:
    require(
        read(MANIFEST),
        (
            "accepted_words: 124779",
            "chapter: 24",
            'eastern: "08:14:44 EDT"',
            'india: "17:44:44 IST"',
            'title: "The Terms of Return"',
            f'path: "{CH24}"',
            "Book 1 structural completion does not equal publication readiness",
        ),
        MANIFEST,
    )
    require(
        read(PROJECT),
        (
            "schema_version: 17",
            "structurally_complete: true",
            "publication_ready: false",
            "accepted_words: 124779",
            "maximum_words_remaining: 221",
            "accepted_act_iii_words: 61124",
            "chapters: 1-24",
            "active_chapter_drafts: []",
            "verdict: ACCEPT",
            f"reviewed_blob_sha: {EXPECTED_CH24_BLOB}",
            f"acceptance_review_blob_sha: {EXPECTED_CH24_REVIEW_BLOB}",
            "chapter_25_and_later: not authorized for Book 1",
            "publication-readiness and final quality-assurance review",
        ),
        PROJECT,
    )

    synchronized = (
        "README.md",
        "books/book-01/control/00-overview.md",
        "books/book-01/control/02-current-project-state.md",
        "books/book-01/control/15-open-plot-threads-and-payoff-matrix.md",
        "books/book-01/control/16-chapter-by-chapter-status-record.md",
        "books/book-01/control/18-act-iii-entry-state.md",
        "books/book-01/control/20-control-pack-maintenance-rules.md",
        "books/book-01/control/22-book-1-ending-contract.md",
        "books/book-01/control/23-word-budget-and-act-iii-architecture.md",
        "books/book-01/control/24-thread-disposition-matrix.md",
        "books/book-01/control/README.md",
        "books/book-01/drafts/README.md",
        "books/book-01/manuscript/STATUS.md",
        "series/recurring-character-ledger.md",
    )
    for path in synchronized:
        text = read(path)
        if path != "series/recurring-character-ledger.md" and "124,779" not in text:
            fail(f"synchronized accepted total missing from {path}")
        if path not in (
            "series/recurring-character-ledger.md",
            "books/book-01/manuscript/STATUS.md",
        ) and "Chapter 25" not in text:
            fail(f"Chapter 25 prohibition missing from {path}")


def validate_chapter24() -> None:
    text = read(CH24)
    expected_opening = (
        "15:04:44 EDT / 00:34:44 IST\n\n"
        "# Chapter 24 - The Terms of Return\n\n"
        "Secure MPD Evidence Intake\nWashington, D.C.\n"
    )
    if not text.startswith(expected_opening):
        fail("Chapter 24 opening identity changed")
    if text.count("\n\n---\n\n") != 3:
        fail("Chapter 24 does not contain exactly four causal movements")
    movements = [len(part.split()) for part in text.split("\n\n---\n\n")]
    if movements != [800, 739, 673, 1147]:
        fail(f"Chapter 24 movement counts changed: {movements}")
    if word_count(CH24) != 3362:
        fail(f"Chapter 24 word count changed: {word_count(CH24)}")
    if not text.rstrip().endswith("The bubble stayed centered."):
        fail("Chapter 24 final line changed")

    required = (
        "26-MJ-187463-ER",
        "CHARGING: UNRESOLVED",
        "Possible personal contact",
        "It was not repaired.",
        "None of the choices were safe",
        "Then it remains no.",
        "Leland Price was alive",
        "restricted administrative status",
        "independent source-integrity practice",
        "evidence architecture",
        "case-specific written mandate",
        "source original with its lawful custodian",
        "merged universal truth file",
        "proof ceilings",
        "stop or refusal right",
        "Civilian and source protection",
        "retain counsel, consent, and custody",
        "own unresolved criminal",
        "MPD-901441` through `MPD-901447",
        "136 sealed files, 47 incomplete files, and 311 excluded files",
        "SSO-NS-004` powered down, isolated, closed, unused",
        "LSS-SL-90418",
        "LSS-IDR-90418-01",
        "At exactly 08:14:44 EDT / 17:44:44 IST",
    )
    lower = text.lower()
    for phrase in required:
        if phrase.lower() not in lower:
            fail(f"Chapter 24 missing required element: {phrase}")

    prohibited = (
        "Sterling ordered",
        "Sterling commanded",
        "Vance was the original 02:14 operator",
        "Vance was the sole architect",
        "Tariq was physically",
        "WSS plaintext showed",
        "Julie was fully exonerated",
        "Elias was granted immunity",
        "Price was cleared",
        "opened SSO-NS-004",
        "operated SSO-NS-004",
        "# Chapter 25",
        "TODO",
        "TBD",
    )
    for phrase in prohibited:
        if phrase.lower() in lower:
            fail(f"Chapter 24 contains prohibited conclusion: {phrase}")


def validate_review_and_artifacts() -> None:
    require(
        read(CH24_REVIEW),
        (
            "## 16. Explicit verdict\n\n**ACCEPT**",
            "## 13. Review-authorized prose repair\n\n**None.**",
            EXPECTED_CH24_BLOB,
            "3,362",
            "800 / 739 / 673 / 1,147",
            "124,779",
            "61,124",
            "221 words",
            "No Chapter 25 artifact",
        ),
        CH24_REVIEW,
    )
    if (ROOT / CH24_DRAFT).exists():
        fail("Chapter 24 draft still exists")

    tracked = run("git", "ls-files").splitlines()
    chapter24_artifacts = sorted(
        path
        for path in tracked
        if "chapter-24" in path.lower()
        and path.startswith(
            (
                "books/book-01/control/",
                "books/book-01/drafts/",
                "books/book-01/manuscript/",
            )
        )
    )
    if chapter24_artifacts != sorted((CH24_LOCK, CH24_REVIEW, CH24)):
        fail(f"unexpected Chapter 24 artifacts: {chapter24_artifacts}")

    for path in tracked:
        lower = path.lower()
        if "chapter-25" in lower and path.startswith(
            (
                "books/book-01/control/",
                "books/book-01/drafts/",
                "books/book-01/manuscript/",
            )
        ):
            fail(f"Chapter 25 artifact exists: {path}")
        if ("remainder" in lower and "outline" in lower) or (
            "act-iii" in lower and "outline" in lower
        ):
            fail(f"complete remainder outline exists: {path}")
        if path.startswith(("books/book-01/", "tools/")) and lower.endswith(
            (".bak", ".tmp", ".orig", "~")
        ):
            fail(f"temporary or backup artifact exists: {path}")

    for obsolete in (
        "tools/validate_book1_chapter23.py",
        "tools/validate_book1_chapter24_mission_lock.py",
        "tools/validate_book1_chapter24_draft.py",
    ):
        if (ROOT / obsolete).exists():
            fail(f"obsolete validator remains: {obsolete}")


def validate_scope_and_diff() -> None:
    actual = changed_files()
    if actual != EXPECTED_CHANGED:
        fail(f"changed-file scope mismatch: {sorted(actual)}")
    if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode:
        fail("git diff --check failed")


def main() -> None:
    validate_hashes_and_counts()
    validate_manifest_and_navigation()
    validate_chapter24()
    validate_review_and_artifacts()
    validate_scope_and_diff()
    print(
        "PASS: Book 1 accepted through Chapter 24 at 124,779 words; "
        "structurally complete, source-limited, and scope-protected"
    )


if __name__ == "__main__":
    main()
