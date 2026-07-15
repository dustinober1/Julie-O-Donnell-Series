#!/usr/bin/env python3
"""Permanent validation for accepted Book 1 through Chapter 22."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "3ed760050f7e74ad152d0f46ede7db16164030b0"
EXPECTED_TOTAL = 116807
EXPECTED_ACT_III = 53152
EXPECTED_MANIFEST_BLOB = "faae57d468a4a599dc14ee753c74b5257e946ec8"
EXPECTED_REVIEW_BLOB = "9de6c47b5984875339e8c6244ffca25f49394d9c"
EXPECTED_LOCK_BLOB = "9bd255ac7b09a1490dc70be4506ba29183756788"
CH22_BLOB = "034ab496794594427d8409d03e7c6659d41b6a91"
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
    "books/book-01/manuscript/chapters/chapter-22.md": (4716, CH22_BLOB),
}
REVIEW = "books/book-01/control/45-chapter-22-acceptance-review.md"
LOCK = "books/book-01/control/44-chapter-22-mission-lock.md"
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
STATE_FILES = [
    "PROJECT_STATE.yaml",
    "README.md",
    "books/book-01/manuscript/STATUS.md",
    "books/book-01/drafts/README.md",
    "books/book-01/control/README.md",
    "books/book-01/control/00-overview.md",
    "books/book-01/control/02-current-project-state.md",
    "books/book-01/control/04-source-of-truth-canon-locks.md",
    "books/book-01/control/05-master-timeline.md",
    "books/book-01/control/06-character-state-ledger.md",
    "books/book-01/control/07-relationship-and-trust-matrix.md",
    "books/book-01/control/08-evidence-and-chain-of-custody-ledger.md",
    "books/book-01/control/09-knowledge-and-information-control-matrix.md",
    "books/book-01/control/10-technology-and-system-rules.md",
    "books/book-01/control/11-organizations-authorities-and-institutional-control.md",
    "books/book-01/control/12-location-and-security-architecture.md",
    "books/book-01/control/13-antagonist-objectives-and-conspiracy-model.md",
    "books/book-01/control/14-public-narrative-versus-actual-record.md",
    "books/book-01/control/15-open-plot-threads-and-payoff-matrix.md",
    "books/book-01/control/16-chapter-by-chapter-status-record.md",
    "books/book-01/control/18-act-iii-entry-state.md",
    "books/book-01/control/20-control-pack-maintenance-rules.md",
    "books/book-01/control/22-book-1-ending-contract.md",
    "books/book-01/control/23-word-budget-and-act-iii-architecture.md",
    "books/book-01/control/24-thread-disposition-matrix.md",
    "series/recurring-character-ledger.md",
]
ALLOWED_CHANGED = set(STATE_FILES) | {
    ".github/workflows/book1-manuscript-validation.yml",
    MANIFEST,
    "books/book-01/drafts/chapter-22.md",
    "books/book-01/manuscript/chapters/chapter-22.md",
    REVIEW,
    "tools/validate_book1_chapter22.py",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], cwd=ROOT, text=True).strip()


def words(path: str) -> int:
    return len((ROOT / path).read_text(encoding="utf-8").split())


for path, (expected_words, expected_blob) in EXPECTED_CHAPTERS.items():
    if not (ROOT / path).is_file():
        fail(f"missing {path}")
    if words(path) != expected_words:
        fail(f"word count mismatch for {path}")
    if blob(path) != expected_blob:
        fail(f"blob mismatch for {path}")

if sum(count for count, _ in EXPECTED_CHAPTERS.values()) != EXPECTED_ACT_III:
    fail("Act III subtotal constant mismatch")
if blob(MANIFEST) != EXPECTED_MANIFEST_BLOB:
    fail("accepted manifest blob mismatch")
if blob(REVIEW) != EXPECTED_REVIEW_BLOB:
    fail("Chapter 22 acceptance-review blob mismatch")
if blob(LOCK) != EXPECTED_LOCK_BLOB:
    fail("Chapter 22 mission-lock blob mismatch")

review = (ROOT / REVIEW).read_text(encoding="utf-8")
if "## 25. Explicit verdict\n\n**ACCEPT**" not in review:
    fail("explicit ACCEPT verdict missing")
for phrase in ("basically accepted", "provisionally canon", "accepted pending cleanup", "mostly ready"):
    if phrase in review.lower():
        fail(f"ambiguous verdict phrase present: {phrase}")

manifest = (ROOT / MANIFEST).read_text(encoding="utf-8")
for required in (
    "accepted_words: 116807",
    "chapter: 22",
    'eastern: "13:12:44 EDT"',
    'india: "22:42:44 IST"',
    'path: "books/book-01/manuscript/chapters/chapter-22.md"',
):
    if required not in manifest:
        fail(f"manifest missing: {required}")

count_result = subprocess.run(
    [sys.executable, "tools/count_book1_words.py", "--expect", str(EXPECTED_TOTAL)],
    cwd=ROOT,
)
if count_result.returncode:
    fail("accepted-manuscript word count")

if (ROOT / "books/book-01/drafts/chapter-22.md").exists():
    fail("Chapter 22 draft remains")
tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
duplicates = [path for path in tracked if (ROOT / path).is_file() and blob(path) == CH22_BLOB]
if duplicates != ["books/book-01/manuscript/chapters/chapter-22.md"]:
    fail(f"Chapter 22 duplicate paths: {duplicates}")

for path in tracked:
    lower = path.lower()
    if "chapter-23" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
        fail(f"Chapter 23 artifact exists: {path}")
    if ("remainder" in lower and "outline" in lower) or ("act-iii" in lower and "outline" in lower):
        fail(f"complete remainder outline artifact exists: {path}")

stale_phrases = (
    "accepted_words: 112091",
    "accepted-manuscript length: **112,091 words**",
    "formal acceptance review pending",
    "first draft complete; non-canon",
    "chapter 22 acceptance review: not created",
    "chapter 22 has no acceptance review yet",
    "active book 1 drafts: chapter 22 only",
)
for path in STATE_FILES:
    file_path = ROOT / path
    if not file_path.is_file():
        fail(f"missing synchronized state file: {path}")
    text = file_path.read_text(encoding="utf-8")
    if not any(token in text for token in ("Chapter 22", "116,807", "accepted_words: 116807", "13:12:44")):
        fail(f"{path} lacks accepted Chapter 22 state")
    lower = text.lower()
    for phrase in stale_phrases:
        if phrase in lower:
            fail(f"{path} retains stale state: {phrase}")

project_state = (ROOT / "PROJECT_STATE.yaml").read_text(encoding="utf-8")
for required in ("chapters: 1-22", "accepted_words: 116807", "maximum_words_remaining: 8193", "active_chapter_drafts: []"):
    if required not in project_state:
        fail(f"PROJECT_STATE.yaml missing: {required}")

protected = ["books/book-01/manuscript/prologue.md"] + [
    f"books/book-01/manuscript/chapters/chapter-{index:02d}.md" for index in range(1, 22)
]
if subprocess.run(["git", "diff", "--quiet", BASE, "--", *protected], cwd=ROOT).returncode != 0:
    fail("accepted Prologue or Chapters 1-21 changed")

changed = set(subprocess.check_output(["git", "diff", "--name-only", BASE, "--"], cwd=ROOT, text=True).splitlines())
unexpected = changed - ALLOWED_CHANGED
if unexpected:
    fail(f"unexpected changed files: {sorted(unexpected)}")
required_changed = {REVIEW, MANIFEST, "books/book-01/drafts/chapter-22.md", "books/book-01/manuscript/chapters/chapter-22.md", "tools/validate_book1_chapter22.py"}
if not required_changed.issubset(changed):
    fail(f"missing required changed files: {sorted(required_changed - changed)}")

for path in changed:
    name = Path(path).name.lower()
    if any(token in name for token in ("tmp", "temp", "helper", "payload", "runner", "debug", "apply", "latest", "backup")):
        fail(f"forbidden temporary/helper artifact: {path}")
    if name.endswith((".orig", ".rej")):
        fail(f"forbidden rejected/original artifact: {path}")

if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode != 0:
    fail("git diff --check")

print("PASS: accepted Book 1 through Chapter 22 is synchronized and protected")
