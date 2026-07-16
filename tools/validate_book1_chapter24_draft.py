#!/usr/bin/env python3
"""Validate the sole non-canon Chapter 24 first draft and protect accepted Book 1."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "d8adea11828fbd1ec0a8924e072b566f0fc62bcd"
DRAFT = "books/book-01/drafts/chapter-24.md"
LOCK = "books/book-01/control/48-chapter-24-mission-lock.md"
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
CH23 = "books/book-01/manuscript/chapters/chapter-23.md"
CH23_LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"
CH23_REVIEW = "books/book-01/control/47-chapter-23-acceptance-review.md"
DRAFT_BLOB = "abce3cbea04a7afd798b5022ba09ce665a9cc923"
LOCK_BLOB = "260186500b448b5154858f7df47f113dc8d6fbfa"
MANIFEST_BLOB = "022ce4585cb07421549b6749f3ca1b8f60221307"
CH23_BLOB = "1f511d36404450f201b34a075f441d350eb7cc52"
CH23_LOCK_BLOB = "c8c5be7e9ee5a902c7187697cf1bc70c8a5ce30a"
CH23_REVIEW_BLOB = "c876854075ad1f686ac663018983fd34f0064e2c"
DRAFT_WORDS = 3362
EXPECTED_CHANGED = {
    ".github/workflows/book1-manuscript-validation.yml",
    "PROJECT_STATE.yaml",
    "books/book-01/drafts/README.md",
    DRAFT,
    "tools/validate_book1_chapter23.py",
    "tools/validate_book1_chapter24_mission_lock.py",
    "tools/validate_book1_chapter24_draft.py",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def blob(path: str) -> str:
    return run("git", "hash-object", path)


def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        fail(f"missing {path}")
    return target.read_text(encoding="utf-8")


def word_count(path: str) -> int:
    return len(read(path).split())


def changed_files() -> set[str]:
    changed: set[str] = set()
    output = run("git", "diff", "--name-status", "--find-renames", BASE, "--")
    for line in output.splitlines():
        fields = line.split("\t")
        if fields[0].startswith(("R", "C")) and len(fields) == 3:
            changed.update(fields[1:])
        elif len(fields) == 2:
            changed.add(fields[1])
        else:
            fail(f"unexpected diff entry: {line}")
    return changed


def validate_common() -> None:
    for path, expected in (
        (MANIFEST, MANIFEST_BLOB), (CH23, CH23_BLOB), (CH23_LOCK, CH23_LOCK_BLOB),
        (CH23_REVIEW, CH23_REVIEW_BLOB), (LOCK, LOCK_BLOB), (DRAFT, DRAFT_BLOB),
    ):
        if blob(path) != expected:
            fail(f"protected or draft blob mismatch: {path}")
    if word_count(DRAFT) != DRAFT_WORDS:
        fail(f"Chapter 24 word count mismatch: {word_count(DRAFT)}")
    if subprocess.run([sys.executable, "tools/count_book1_words.py", "--expect", "121417"], cwd=ROOT).returncode:
        fail("accepted Book 1 word count changed")

    manifest = read(MANIFEST)
    for phrase in ("accepted_words: 121417", "chapter: 23", 'eastern: "14:24:44 EDT"', 'india: "23:54:44 IST"'):
        if phrase not in manifest:
            fail(f"accepted manifest missing {phrase}")
    if "chapter-24.md" in manifest:
        fail("Chapter 24 appears in accepted manifest")

    text = read(DRAFT)
    opening = "15:04:44 EDT / 00:34:44 IST\n\n# Chapter 24 - The Terms of Return\n\nSecure MPD Evidence Intake\nWashington, D.C.\n"
    if not text.startswith(opening):
        fail("title, opening clock, or location changed")
    if text.count("\n\n---\n\n") != 3:
        fail("Chapter 24 must contain exactly four causal movements")
    movement_words = [len(part.split()) for part in text.split("\n\n---\n\n")]
    limits = ((700, 800), (650, 750), (600, 700), (1050, 1150))
    if any(not low <= count <= high for count, (low, high) in zip(movement_words, limits)):
        fail(f"movement word ranges invalid: {movement_words}")
    if "At exactly 08:14:44 EDT / 17:44:44 IST" not in text[-500:]:
        fail("locked farm endpoint missing")
    if not text.rstrip().endswith("The bubble stayed centered."):
        fail("final farm image changed")

    required = (
        "26-MJ-187463-ER", "CHARGING: UNRESOLVED", "Possible personal contact", "It was not repaired.",
        "None of the choices were safe", "Then it remains no.", "Leland Price was alive", "restricted administrative status",
        "independent source-integrity practice", "evidence architecture", "case-specific written mandate",
        "source original with its lawful custodian", "merged universal truth file", "proof ceilings", "stop or refusal right",
        "Civilian and source protection", "retain counsel, consent, and custody", "own unresolved criminal",
        "MPD-901441` through `MPD-901447", "136 sealed files, 47 incomplete files, and 311 excluded files",
        "SSO-NS-004` powered down, isolated, closed, unused", "LSS-SL-90418", "LSS-IDR-90418-01",
    )
    for phrase in required:
        if phrase.lower() not in text.lower():
            fail(f"required Chapter 24 element missing: {phrase}")
    prohibited = (
        "Sterling ordered", "Sterling commanded", "Vance was the original 02:14 operator", "Vance was the sole architect",
        "Tariq was physically", "WSS plaintext showed", "Julie was fully exonerated", "Elias was granted immunity",
        "Price was cleared", "opened SSO-NS-004", "operated SSO-NS-004", "# Chapter 25", "TODO", "TBD",
    )
    for phrase in prohibited:
        if phrase.lower() in text.lower():
            fail(f"prohibited conclusion or artifact present: {phrase}")

    project = read("PROJECT_STATE.yaml")
    for phrase in (
        "schema_version: 16", "accepted_words: 121417", "active_chapter_drafts:\n      - 24",
        "status: first draft complete; non-canon; formal acceptance review not created",
        f"draft_blob_sha: {DRAFT_BLOB}", f"draft_words: {DRAFT_WORDS}",
        "chapter_25_and_later: not authorized for Book 1",
    ):
        if phrase not in project:
            fail(f"PROJECT_STATE.yaml missing {phrase}")

    tracked = run("git", "ls-files").splitlines()
    artifacts24 = [p for p in tracked if "chapter-24" in p.lower() and p.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/"))]
    if artifacts24 != [LOCK, DRAFT]:
        fail(f"unexpected Chapter 24 artifacts: {artifacts24}")
    for forbidden in ("books/book-01/manuscript/chapters/chapter-24.md", "books/book-01/control/49-chapter-24-acceptance-review.md"):
        if (ROOT / forbidden).exists():
            fail(f"forbidden Chapter 24 artifact exists: {forbidden}")
    for path in tracked:
        lower = path.lower()
        if "chapter-25" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
            fail(f"Chapter 25 artifact exists: {path}")
        if ("remainder" in lower and "outline" in lower) or ("act-iii" in lower and "outline" in lower):
            fail(f"complete remainder outline exists: {path}")

    protected = [MANIFEST, CH23, CH23_LOCK, CH23_REVIEW, LOCK, "books/book-01/manuscript/prologue.md"] + [f"books/book-01/manuscript/chapters/chapter-{i:02d}.md" for i in range(1, 24)]
    if subprocess.run(["git", "diff", "--quiet", BASE, "--", *protected], cwd=ROOT).returncode:
        fail("accepted prose, manifest, review, or mission lock changed")
    changed = changed_files()
    if changed != EXPECTED_CHANGED:
        fail(f"changed-file scope mismatch: {sorted(changed)}")
    if MANIFEST in changed or any(path.startswith("books/book-01/manuscript/") for path in changed):
        fail("accepted manifest or manuscript changed")
    if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode:
        fail("git diff --check")


if __name__ == "__main__":
    validate_common()
    print("PASS: Chapter 24 first draft is exact, non-canon, source-limited, and scope-protected")
