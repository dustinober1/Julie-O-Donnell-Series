#!/usr/bin/env python3
"""Focused validation for the Chapter 24 final-chapter mission lock."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "07162d09f9a8a429909eb0e9227530315c7c7664"
LOCK = "books/book-01/control/48-chapter-24-mission-lock.md"
LOCK_BLOB = "260186500b448b5154858f7df47f113dc8d6fbfa"
CH23 = "books/book-01/manuscript/chapters/chapter-23.md"
CH23_BLOB = "1f511d36404450f201b34a075f441d350eb7cc52"
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
MANIFEST_BLOB = "022ce4585cb07421549b6749f3ca1b8f60221307"
CH23_LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"
CH23_LOCK_BLOB = "c8c5be7e9ee5a902c7187697cf1bc70c8a5ce30a"
CH23_REVIEW = "books/book-01/control/47-chapter-23-acceptance-review.md"
CH23_REVIEW_BLOB = "c876854075ad1f686ac663018983fd34f0064e2c"
EXPECTED_CHANGED = {
    ".github/workflows/book1-manuscript-validation.yml",
    "PROJECT_STATE.yaml",
    "README.md",
    "books/book-01/control/00-overview.md",
    "books/book-01/control/02-current-project-state.md",
    "books/book-01/control/16-chapter-by-chapter-status-record.md",
    "books/book-01/control/18-act-iii-entry-state.md",
    LOCK,
    "books/book-01/control/README.md",
    "books/book-01/drafts/README.md",
    "books/book-01/manuscript/STATUS.md",
    "tools/validate_book1_chapter23.py",
    "tools/validate_book1_chapter24_mission_lock.py",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], cwd=ROOT, text=True).strip()


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


for path, expected in (
    (LOCK, LOCK_BLOB), (CH23, CH23_BLOB), (MANIFEST, MANIFEST_BLOB),
    (CH23_LOCK, CH23_LOCK_BLOB), (CH23_REVIEW, CH23_REVIEW_BLOB),
):
    if not (ROOT / path).is_file() or blob(path) != expected:
        fail(f"protected blob mismatch: {path}")

lock = read(LOCK)
sections = re.findall(r"^## (\d+)\. ", lock, flags=re.MULTILINE)
if sections != [str(i) for i in range(1, 39)]:
    fail(f"mission-lock sections are not exactly 1-38: {sections}")
if lock.count("### Movement ") != 4:
    fail("mission lock must contain exactly four movement blueprints")

required_phrases = (
    "# Chapter 24 Mission Lock — The Terms of Return",
    "**The Terms of Return**",
    "final chapter of Julie O'Donnell Book 1",
    "15:04:44 EDT / 00:34:44 IST",
    "40 minutes exactly",
    "Julie O'Donnell close third, past tense, for the entire chapter",
    "No cutaway is authorized",
    "Preferred target:** **3,300 words",
    "Acceptable range:** **3,150–3,450 words",
    "Hard maximum:** **3,583 words",
    "exactly four causal movements",
    "independent source-integrity and evidence-architecture practice",
    "permits future contact outside rank and command",
    "Elias controls future contact and technical participation",
    "MPD-901441` through `MPD-901447",
    "136 sealed / 47 incomplete / 311 excluded",
    "LSS-SL-90418",
    "original 02:14 human operator",
    "human constructor of the borrowed request path",
    "Sterling's knowledge, intent, direction, or command",
    "No Chapter 25 is authorized or implied",
    "It drafted no Chapter 24 prose",
    "no complete chapter-by-chapter remainder-of-book outline",
)
for phrase in required_phrases:
    if phrase.lower() not in lock.lower():
        fail(f"mission lock missing required phrase: {phrase}")

for forbidden in (
    "books/book-01/drafts/chapter-24.md",
    "books/book-01/manuscript/chapters/chapter-24.md",
    "books/book-01/control/49-chapter-24-acceptance-review.md",
):
    if (ROOT / forbidden).exists():
        fail(f"forbidden Chapter 24 prose/review exists: {forbidden}")

tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
artifacts24 = [p for p in tracked if "chapter-24" in p.lower() and p.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/"))]
if artifacts24 != [LOCK]:
    fail(f"unexpected Chapter 24 artifacts: {artifacts24}")
for path in tracked:
    lower = path.lower()
    if "chapter-25" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
        fail(f"Chapter 25 artifact exists: {path}")
    if ("remainder" in lower and "outline" in lower) or ("act-iii" in lower and "outline" in lower):
        fail(f"complete remainder outline exists: {path}")

project = read("PROJECT_STATE.yaml")
for phrase in (
    "schema_version: 15", "accepted_words: 121417", "maximum_words_remaining: 3583",
    "title: The Terms of Return", f"mission_lock: {LOCK}", "status: mission locked; undrafted and non-canon",
    "preferred_words: 3300", "acceptable_words: 3150-3450", "hard_maximum_words: 3583",
    "chapter_25_and_later: not authorized for Book 1", "active_chapter_drafts: []",
):
    if phrase not in project:
        fail(f"PROJECT_STATE.yaml missing: {phrase}")

for path in (
    "README.md", "books/book-01/manuscript/STATUS.md", "books/book-01/drafts/README.md",
    "books/book-01/control/README.md", "books/book-01/control/00-overview.md",
    "books/book-01/control/02-current-project-state.md", "books/book-01/control/16-chapter-by-chapter-status-record.md",
    "books/book-01/control/18-act-iii-entry-state.md",
):
    text = read(path)
    for phrase in ("The Terms of Return", "3,583"):
        if phrase not in text:
            fail(f"{path} missing synchronized Chapter 24 state: {phrase}")

protected = [MANIFEST, CH23, CH23_LOCK, CH23_REVIEW, "books/book-01/manuscript/prologue.md"] + [f"books/book-01/manuscript/chapters/chapter-{i:02d}.md" for i in range(1, 23)]
if subprocess.run(["git", "diff", "--quiet", BASE, "--", *protected], cwd=ROOT).returncode:
    fail("accepted manuscript or Chapter 23 controls changed")
if subprocess.run([sys.executable, "tools/count_book1_words.py", "--expect", "121417"], cwd=ROOT).returncode:
    fail("accepted manuscript count changed")

changed: set[str] = set()
output = subprocess.check_output(["git", "diff", "--name-status", "--find-renames", BASE, "--"], cwd=ROOT, text=True)
for line in output.splitlines():
    fields = line.split("\t")
    if fields[0].startswith(("R", "C")):
        changed.update(fields[1:])
    elif len(fields) == 2:
        changed.add(fields[1])
    else:
        fail(f"unexpected diff entry: {line}")
if changed != EXPECTED_CHANGED:
    fail(f"changed-file scope mismatch: expected {sorted(EXPECTED_CHANGED)}, got {sorted(changed)}")
for path in changed:
    name = Path(path).name.lower()
    if any(token in name for token in ("tmp", "temp", "helper", "payload", "runner", "debug", "apply", "latest", "backup")) or name.endswith((".orig", ".rej")):
        fail(f"forbidden artifact: {path}")
if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode:
    fail("git diff --check")
print("PASS: Chapter 24 final-chapter mission lock is exact, bounded, and prose-free")
