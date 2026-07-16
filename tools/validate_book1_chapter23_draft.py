#!/usr/bin/env python3
"""Permanent validation for the sole non-canon Chapter 23 first draft."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "c4dca2aa7781709b6ba78f41abe5a35f14b13280"
DRAFT = "books/book-01/drafts/chapter-23.md"
LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
CH22 = "books/book-01/manuscript/chapters/chapter-22.md"
CH22_LOCK = "books/book-01/control/44-chapter-22-mission-lock.md"
CH22_REVIEW = "books/book-01/control/45-chapter-22-acceptance-review.md"
EXPECTED_DRAFT_BLOB = "1f511d36404450f201b34a075f441d350eb7cc52"
EXPECTED_DRAFT_WORDS = 4610
EXPECTED_LOCK_BLOB = "c8c5be7e9ee5a902c7187697cf1bc70c8a5ce30a"
EXPECTED_MANIFEST_BLOB = "faae57d468a4a599dc14ee753c74b5257e946ec8"
EXPECTED_CH22_BLOB = "034ab496794594427d8409d03e7c6659d41b6a91"
EXPECTED_CH22_LOCK_BLOB = "9bd255ac7b09a1490dc70be4506ba29183756788"
EXPECTED_CH22_REVIEW_BLOB = "f0261e728600b58a4efada77b39874977f347ade"
EXPECTED_CHANGED = {
    ".github/workflows/book1-manuscript-validation.yml",
    "PROJECT_STATE.yaml",
    "books/book-01/drafts/README.md",
    DRAFT,
    "tools/validate_book1_chapter22.py",
    "tools/validate_book1_chapter23_mission_lock.py",
    "tools/validate_book1_chapter23_draft.py",
}
SCENE_MARKERS = [
    "13:12:44 EDT / 22:42:44 IST",
    "13:22:00 EDT / 22:52:00 IST",
    "13:36:00 EDT / 23:06:00 IST",
    "13:53:00 EDT / 23:23:00 IST",
    "14:04:00 EDT / 23:34:00 IST",
    "14:17:00 EDT / 23:47:00 IST",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], cwd=ROOT, text=True).strip()


def read(path: str) -> str:
    file_path = ROOT / path
    if not file_path.is_file():
        fail(f"missing {path}")
    return file_path.read_text(encoding="utf-8")


def words(path: str) -> int:
    return len(read(path).split())


for path, expected in (
    (LOCK, EXPECTED_LOCK_BLOB),
    (MANIFEST, EXPECTED_MANIFEST_BLOB),
    (CH22, EXPECTED_CH22_BLOB),
    (CH22_LOCK, EXPECTED_CH22_LOCK_BLOB),
    (CH22_REVIEW, EXPECTED_CH22_REVIEW_BLOB),
):
    if blob(path) != expected:
        fail(f"protected blob mismatch: {path}")

manifest = read(MANIFEST)
for phrase in (
    "accepted_words: 116807",
    "chapter: 22",
    'eastern: "13:12:44 EDT"',
    'india: "22:42:44 IST"',
    'path: "books/book-01/manuscript/chapters/chapter-22.md"',
):
    if phrase not in manifest:
        fail(f"accepted manifest missing: {phrase}")
if "chapter-23.md" in manifest:
    fail("Chapter 23 appears in accepted manifest")

count_result = subprocess.run(
    [sys.executable, "tools/count_book1_words.py", "--expect", "116807"],
    cwd=ROOT,
)
if count_result.returncode:
    fail("accepted manuscript total changed")

text = read(DRAFT)
if blob(DRAFT) != EXPECTED_DRAFT_BLOB:
    fail("Chapter 23 draft blob mismatch")
count = words(DRAFT)
if count != EXPECTED_DRAFT_WORDS:
    fail(f"Chapter 23 word count mismatch: expected {EXPECTED_DRAFT_WORDS}, found {count}")
if not 4400 <= count <= 5200:
    fail(f"Chapter 23 outside authorized range: {count}")
if count > 5000:
    print(f"NOTE: Chapter 23 is above preferred range but below hard ceiling: {count}")

expected_opening = (
    "13:12:44 EDT / 22:42:44 IST\n\n"
    "# Chapter 23 - The Official Correction\n\n"
    "Secure MPD Evidence Intake\nWashington, D.C.\n"
)
if not text.startswith(expected_opening):
    fail("Chapter 23 title, opening clock, or location changed")
for marker in SCENE_MARKERS:
    if text.count(marker) != 1:
        fail(f"scene marker count invalid: {marker} = {text.count(marker)}")
if text.count("14:24:44 EDT / 23:54:44 IST") != 1:
    fail("Chapter 23 endpoint count invalid")
if "At exactly 14:24:44 EDT / 23:54:44 IST" not in text[-1200:]:
    fail("Chapter 23 exact endpoint not near chapter end")

required = (
    "VANCE PERSONAL FINDING: LIMITED TO THE LATER REMOTE RELEASE",
    "STERLING PERSONAL COMMAND: NOT ESTABLISHED",
    "ARGUS-PI-187463-01",
    "DCIS-ISC-187463-01",
    "LSS-ACK-90418-01",
    "PUBLICATION HASH:",
    "PUBLIC RECEIPT:",
    "LSS-IDR-90418-01",
    "Rachel Nwosu",
    "Miriam Alvarez",
    "Marisol Vega",
    "COMPLETE BOUNDED CORRECTION — NOT EXCULPATORY ADVOCACY",
    "Abort the release",
    "Release halted",
    "At mine",
    "K-17 local authentication had failed and written zero records",
    "later remote reconstruction was separate",
    "did not support the claim that Julie, Marcus, Elias, or Price had originated the poisoned source",
    "It did not use cleared",
    "It did not use innocent",
    "It did not say released",
    "SSO-NS-004",
    "Martin Vann",
    "LSS-SL-90418",
    "seven MPD packages remained in the chest",
    "136",
    "47",
    "311",
    "WSS plaintext",
    "Marcus remained in guarded medical care on four liters of oxygen",
    "Elias remained in separate guarded medical custody",
    "Julie remained detained",
    "The truth no longer depended on her carrying it.",
)
missing = [phrase for phrase in required if phrase not in text]
if missing:
    fail(f"Chapter 23 required element missing: {missing}")

if text.count("PUBLICATION HASH:") != 3:
    fail("Chapter 23 must contain exactly three publication hashes")
if text.count("PUBLIC RECEIPT:") != 3:
    fail("Chapter 23 must contain exactly three public receipts")
if text.count("13:12:44 EDT / 22:42:44 IST") != 1:
    fail("opening marker duplicated")

prohibited = (
    "# Chapter 24",
    "Chapter 24 -",
    "Sterling personally commanded the operation.",
    "Sterling ordered Vance",
    "Vance created the original deployment",
    "Vance was the original 02:14 operator",
    "Vance was the sole architect",
    "Price constructed the request",
    "Elias was the original signer",
    "Tariq was physically at K-17",
    "WSS plaintext showed",
    "opened SSO-NS-004",
    "operated SSO-NS-004",
    "opened MPD-901",
    "mounted MPD-901",
    "imaged MPD-901",
    "reconstructed the 47 incomplete files",
    "recovered the 311 excluded files",
    "Julie was fully exonerated",
    "Marcus was fully exonerated",
    "Elias was granted immunity",
    "Price was cleared of all conduct",
    "Julie was released",
)
present = [phrase for phrase in prohibited if phrase in text]
if present:
    fail(f"Chapter 23 prohibited conclusion or action present: {present}")
for artifact in ("TODO", "TBD", "DRAFTING NOTE", "ALTERNATE VERSION", "PLACEHOLDER", "SAMPLE PROSE"):
    if artifact in text:
        fail(f"drafting artifact remains: {artifact}")

project = read("PROJECT_STATE.yaml")
for phrase in (
    "accepted_words: 116807",
    "chapters: 1-22",
    "active_chapter_drafts:\n      - 23",
    "status: first draft complete; non-canon; formal acceptance review not created",
    f"draft_blob_sha: {EXPECTED_DRAFT_BLOB}",
    f"draft_words: {EXPECTED_DRAFT_WORDS}",
    f"mission_lock_blob_sha: {EXPECTED_LOCK_BLOB}",
    "chapter_24_and_later: undrafted and individually mission unlocked",
):
    if phrase not in project:
        fail(f"PROJECT_STATE.yaml missing: {phrase}")

drafts_readme = read("books/book-01/drafts/README.md")
for phrase in (
    "23 — The Official Correction",
    EXPECTED_DRAFT_BLOB,
    "4,610",
    "formal acceptance review not created",
    "No Chapter 24 artifact exists",
):
    if phrase not in drafts_readme:
        fail(f"draft navigation missing: {phrase}")

tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
ch23_prose = [
    path for path in tracked
    if "chapter-23" in path.lower()
    and path.startswith(("books/book-01/drafts/", "books/book-01/manuscript/"))
    and path.endswith(".md")
]
if ch23_prose != [DRAFT]:
    fail(f"Chapter 23 prose placement/duplication invalid: {ch23_prose}")
if (ROOT / "books/book-01/control/47-chapter-23-acceptance-review.md").exists():
    fail("Chapter 23 acceptance review exists")
for path in tracked:
    lower = path.lower()
    if "chapter-24" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
        fail(f"Chapter 24 artifact exists: {path}")
    if ("remainder" in lower and "outline" in lower) or ("act-iii" in lower and "outline" in lower):
        fail(f"complete remainder outline exists: {path}")

protected_paths = [
    MANIFEST,
    CH22,
    CH22_LOCK,
    CH22_REVIEW,
    LOCK,
    "books/book-01/manuscript/prologue.md",
] + [f"books/book-01/manuscript/chapters/chapter-{index:02d}.md" for index in range(1, 22)]
if subprocess.run(["git", "diff", "--quiet", BASE, "--", *protected_paths], cwd=ROOT).returncode:
    fail("accepted prose, accepted controls, manifest, or Chapter 23 mission lock changed")

changed_output = subprocess.check_output(
    ["git", "diff", "--name-status", "--find-renames", BASE, "--"],
    cwd=ROOT,
    text=True,
)
changed = set()
for line in changed_output.splitlines():
    fields = line.split("\t")
    if fields[0].startswith(("R", "C")):
        if len(fields) != 3:
            fail(f"unexpected rename/copy entry: {line}")
        changed.update(fields[1:])
    else:
        if len(fields) != 2:
            fail(f"unexpected diff entry: {line}")
        changed.add(fields[1])
if changed != EXPECTED_CHANGED:
    fail(f"changed-file scope mismatch: expected {sorted(EXPECTED_CHANGED)}, got {sorted(changed)}")
if MANIFEST in changed or any(path.startswith("books/book-01/manuscript/") for path in changed):
    fail("accepted manifest or manuscript changed")
for path in changed:
    lower = Path(path).name.lower()
    if any(token in lower for token in ("tmp", "temp", "helper", "payload", "runner", "debug", "apply", "latest", "backup")):
        fail(f"temporary/helper artifact in changed scope: {path}")
    if lower.endswith((".orig", ".rej")):
        fail(f"rejected/original artifact in changed scope: {path}")

if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode:
    fail("git diff --check")

print("PASS: Chapter 23 first draft is exact, non-canon, source-limited, and scope-protected")
