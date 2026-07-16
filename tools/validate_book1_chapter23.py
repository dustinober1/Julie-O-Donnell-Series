#!/usr/bin/env python3
"""Permanent validation for accepted Book 1 through Chapter 23."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "c4dca2aa7781709b6ba78f41abe5a35f14b13280"
EXPECTED_TOTAL = 121417
EXPECTED_ACT_III = 57762
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"
REVIEW = "books/book-01/control/47-chapter-23-acceptance-review.md"
CH23 = "books/book-01/manuscript/chapters/chapter-23.md"
DRAFT = "books/book-01/drafts/chapter-23.md"
EXPECTED_MANIFEST_BLOB = "022ce4585cb07421549b6749f3ca1b8f60221307"
EXPECTED_LOCK_BLOB = "c8c5be7e9ee5a902c7187697cf1bc70c8a5ce30a"
EXPECTED_REVIEW_BLOB = "c876854075ad1f686ac663018983fd34f0064e2c"
CH23_BLOB = "1f511d36404450f201b34a075f441d350eb7cc52"

EXPECTED_CHAPTERS = {
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
    CH23: (4610, CH23_BLOB),
}

STATE_FILES = [
    "PROJECT_STATE.yaml", "README.md", "books/book-01/manuscript/STATUS.md",
    "books/book-01/drafts/README.md", "books/book-01/control/README.md",
    "books/book-01/control/00-overview.md", "books/book-01/control/02-current-project-state.md",
    "books/book-01/control/04-source-of-truth-canon-locks.md", "books/book-01/control/05-master-timeline.md",
    "books/book-01/control/06-character-state-ledger.md", "books/book-01/control/07-relationship-and-trust-matrix.md",
    "books/book-01/control/08-evidence-and-chain-of-custody-ledger.md",
    "books/book-01/control/09-knowledge-and-information-control-matrix.md",
    "books/book-01/control/10-technology-and-system-rules.md",
    "books/book-01/control/11-organizations-authorities-and-institutional-control.md",
    "books/book-01/control/12-location-and-security-architecture.md",
    "books/book-01/control/13-antagonist-objectives-and-conspiracy-model.md",
    "books/book-01/control/14-public-narrative-versus-actual-record.md",
    "books/book-01/control/15-open-plot-threads-and-payoff-matrix.md",
    "books/book-01/control/16-chapter-by-chapter-status-record.md",
    "books/book-01/control/18-act-iii-entry-state.md", "books/book-01/control/20-control-pack-maintenance-rules.md",
    "books/book-01/control/22-book-1-ending-contract.md",
    "books/book-01/control/23-word-budget-and-act-iii-architecture.md",
    "books/book-01/control/24-thread-disposition-matrix.md", "series/recurring-character-ledger.md",
]
ALLOWED_CHANGED = set(STATE_FILES) | {
    ".github/workflows/book1-manuscript-validation.yml", MANIFEST, LOCK, REVIEW, DRAFT, CH23,
    "tools/validate_book1_chapter22.py", "tools/validate_book1_chapter23_mission_lock.py",
    "tools/validate_book1_chapter23_draft.py", "tools/validate_book1_chapter23.py",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], cwd=ROOT, text=True).strip()


def words(path: str) -> int:
    return len((ROOT / path).read_text(encoding="utf-8").split())


for path, (expected_words, expected_blob) in EXPECTED_CHAPTERS.items():
    if not (ROOT / path).is_file() or words(path) != expected_words or blob(path) != expected_blob:
        fail(f"accepted chapter mismatch: {path}")
if sum(v[0] for v in EXPECTED_CHAPTERS.values()) != EXPECTED_ACT_III:
    fail("Act III subtotal constant mismatch")
for path, expected_blob in ((MANIFEST, EXPECTED_MANIFEST_BLOB), (LOCK, EXPECTED_LOCK_BLOB), (REVIEW, EXPECTED_REVIEW_BLOB)):
    if blob(path) != expected_blob:
        fail(f"protected blob mismatch: {path}")

review = (ROOT / REVIEW).read_text(encoding="utf-8")
for phrase in ("## 25. Explicit verdict\n\n**ACCEPT**", "## 20. Review-authorized prose repair\n\n**None.**", CH23_BLOB, "**4,610**", "121,417"):
    if phrase not in review:
        fail(f"review missing: {phrase}")
for phrase in ("basically accepted", "provisionally canon", "accepted pending cleanup", "mostly ready"):
    if phrase in review.lower():
        fail(f"ambiguous verdict phrase present: {phrase}")

manifest = (ROOT / MANIFEST).read_text(encoding="utf-8")
for phrase in ("accepted_words: 121417", "chapter: 23", 'eastern: "14:24:44 EDT"', 'india: "23:54:44 IST"', 'path: "books/book-01/manuscript/chapters/chapter-23.md"'):
    if phrase not in manifest:
        fail(f"manifest missing: {phrase}")
if subprocess.run([sys.executable, "tools/count_book1_words.py", "--expect", str(EXPECTED_TOTAL)], cwd=ROOT).returncode:
    fail("accepted-manuscript word count")

tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
if (ROOT / DRAFT).exists():
    fail("Chapter 23 draft remains")
duplicates = [p for p in tracked if (ROOT / p).is_file() and blob(p) == CH23_BLOB]
if duplicates != [CH23]:
    fail(f"Chapter 23 duplicate paths: {duplicates}")
artifacts = [p for p in tracked if "chapter-23" in p.lower() and p.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/"))]
if artifacts != [LOCK, REVIEW, CH23]:
    fail(f"unexpected Chapter 23 artifacts: {artifacts}")
for path in tracked:
    lower = path.lower()
    if "chapter-24" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
        fail(f"Chapter 24 artifact exists: {path}")
    if ("remainder" in lower and "outline" in lower) or ("act-iii" in lower and "outline" in lower):
        fail(f"complete remainder outline exists: {path}")

project = (ROOT / "PROJECT_STATE.yaml").read_text(encoding="utf-8")
for phrase in ("chapters: 1-23", "accepted_words: 121417", "maximum_words_remaining: 3583", "active_chapter_drafts: []", EXPECTED_REVIEW_BLOB, CH23, "No Chapter 24 artifact exists."):
    if phrase not in project:
        fail(f"PROJECT_STATE.yaml missing: {phrase}")
for path in STATE_FILES:
    text = (ROOT / path).read_text(encoding="utf-8")
    if not any(token in text for token in ("Chapter 23", "121,417", "accepted_words: 121417", "14:24:44")):
        fail(f"{path} lacks accepted Chapter 23 state")
    lower = text.lower()
    for stale in ("chapter 23 acceptance review has not been created", "formal acceptance review not created", "formal acceptance review pending", "accepted canon: prologue and chapters 1–22", "accepted canon: prologue and chapters 1-22", "no chapter 23 prose or mission lock"):
        if stale in lower:
            fail(f"{path} retains stale state: {stale}")

protected = ["books/book-01/manuscript/prologue.md"] + [f"books/book-01/manuscript/chapters/chapter-{i:02d}.md" for i in range(1, 23)] + ["books/book-01/control/44-chapter-22-mission-lock.md", "books/book-01/control/45-chapter-22-acceptance-review.md", LOCK]
if subprocess.run(["git", "diff", "--quiet", BASE, "--", *protected], cwd=ROOT).returncode:
    fail("protected accepted prose or controls changed")

changed = set()
output = subprocess.check_output(["git", "diff", "--name-status", "--find-renames", BASE, "--"], cwd=ROOT, text=True)
for line in output.splitlines():
    fields = line.split("\t")
    if fields[0].startswith(("R", "C")):
        changed.update(fields[1:])
    elif len(fields) == 2:
        changed.add(fields[1])
    else:
        fail(f"unexpected diff entry: {line}")
unexpected = changed - ALLOWED_CHANGED
if unexpected:
    fail(f"unexpected changed files: {sorted(unexpected)}")
for required in (REVIEW, MANIFEST, CH23, "tools/validate_book1_chapter23.py"):
    if required not in changed:
        fail(f"required acceptance change missing: {required}")
for path in changed:
    name = Path(path).name.lower()
    if any(token in name for token in ("tmp", "temp", "helper", "payload", "runner", "debug", "apply", "latest", "backup")) or name.endswith((".orig", ".rej")):
        fail(f"forbidden artifact: {path}")
if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode:
    fail("git diff --check")
print("PASS: accepted Book 1 through Chapter 23 is synchronized and protected")
