#!/usr/bin/env python3
"""Validate the authorized Chapter 23 mission-lock gate transition."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "ddc52a379ab4e0440555dab194aa3474be839123"
LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"
EXPECTED_LOCK_BLOB = "c8c5be7e9ee5a902c7187697cf1bc70c8a5ce30a"
CH22 = "books/book-01/manuscript/chapters/chapter-22.md"
CH22_LOCK = "books/book-01/control/44-chapter-22-mission-lock.md"
CH22_REVIEW = "books/book-01/control/45-chapter-22-acceptance-review.md"
MANIFEST = "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
CH22_VALIDATOR = "tools/validate_book1_chapter22.py"
WORKFLOW = ".github/workflows/book1-manuscript-validation.yml"
EXPECTED_CH22_BLOB = "034ab496794594427d8409d03e7c6659d41b6a91"
EXPECTED_CH22_LOCK_BLOB = "9bd255ac7b09a1490dc70be4506ba29183756788"
EXPECTED_CH22_REVIEW_BLOB = "f0261e728600b58a4efada77b39874977f347ade"
EXPECTED_MANIFEST_BLOB = "faae57d468a4a599dc14ee753c74b5257e946ec8"
EXPECTED_CHANGED = {
    WORKFLOW,
    LOCK,
    CH22_VALIDATOR,
    "tools/validate_book1_chapter23_mission_lock.py",
}


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


lock = read(LOCK)
if blob(LOCK) != EXPECTED_LOCK_BLOB:
    fail("Chapter 23 mission-lock blob mismatch")

required_headings = [
    "## 1. Repository and baseline verification",
    "## 2. Chapter number and working title",
    "## 3. Dominant dramatic function",
    "## 4. Mission statement",
    "## 5. Opening time and location",
    "## 6. Opening character and custody states",
    "## 7. Primary objective",
    "## 8. Secondary objectives",
    "## 9. Success condition",
    "## 10. Failure condition",
    "## 11. Concrete abort condition",
    "## 12. POV structure",
    "## 13. Cutaway decision",
    "## 14. Required cast and character functions",
    "## 15. Antagonist and institutional pressure",
    "## 16. Disclosure forum and authority mechanism",
    "## 17. Evidence available",
    "## 18. Evidence that must remain sealed",
    "## 19. Authentication method",
    "## 20. Chain-of-custody rules",
    "## 21. Technology and system constraints",
    "## 22. Knowledge boundaries",
    "## 23. Proof ceilings",
    "## 24. Public-narrative fracture",
    "## 25. Scene-by-scene blueprint",
    "## 26. Injury and physical constraints",
    "## 27. Relationship movement",
    "## 28. Word-count target, range, hard ceiling, and reserve",
    "## 29. Mandatory emotional turn",
    "## 30. Required irreversible consequence",
    "## 31. Chapter endpoint",
    "## 32. Minimum unresolved handoff question for the final chapter",
    "## 33. Explicit prohibitions",
    "## 34. Drafting instructions",
    "## 35. Validation checklist",
    "## 36. Final lock verdict",
]
for heading in required_headings:
    if heading not in lock:
        fail(f"mission lock missing heading: {heading}")

required_phrases = (
    "**The Official Correction**",
    "**Combined authenticated public fracture and bounded institutional consequence.**",
    "**13:12:44 EDT / 22:42:44 IST**",
    "**14:24:44 EDT / 23:54:44 IST**",
    "**Primary and sole POV:** Julie O’Donnell",
    "**No cutaway is authorized.**",
    "**Preferred target:** **4,700 words**",
    "**Acceptable range:** **4,400–5,000 words**",
    "**Hard ceiling:** **5,200 words**",
    "**Absolute minimum reserve after the hard ceiling:** **2,993 words**",
    "Vance personal finding limited to the later remote release",
    "Sterling personal command not established",
    "`MPD-901441` through `MPD-901447`",
    "`LSS-SL-90418`",
    "**LOCKED FOR CHAPTER 23 DRAFTING**",
)
for phrase in required_phrases:
    if phrase not in lock:
        fail(f"mission lock missing required phrase: {phrase}")

if lock.count("### Scene ") != 6:
    fail("mission lock must contain exactly six scene blueprints")
if "Chapter 23 prose" not in lock:
    fail("mission lock must preserve Chapter 23 prose boundary")
if "complete remainder outline" not in lock:
    fail("mission lock must preserve remainder-outline boundary")
if "book-bible.md" not in lock or "outline.md" not in lock:
    fail("authorized nonexistent-bible/outline resolution missing")
if "Google Doc" not in lock:
    fail("external/Google Doc source prohibition missing")
if "Chapter 24 Mission Lock" in lock or "# Chapter 24" in lock:
    fail("Chapter 24 planning appears in Chapter 23 mission lock")
for phrase in ("basically locked", "provisionally locked", "draft attached", "sample scene", "opening paragraph"):
    if phrase in lock.lower():
        fail(f"ambiguous or prose-like mission-lock phrase present: {phrase}")

if blob(CH22) != EXPECTED_CH22_BLOB:
    fail("accepted Chapter 22 prose blob changed")
if blob(CH22_LOCK) != EXPECTED_CH22_LOCK_BLOB:
    fail("accepted Chapter 22 mission-lock blob changed")
if blob(CH22_REVIEW) != EXPECTED_CH22_REVIEW_BLOB:
    fail("accepted Chapter 22 review blob changed")
if blob(MANIFEST) != EXPECTED_MANIFEST_BLOB:
    fail("accepted manifest blob changed")

manifest = read(MANIFEST)
for phrase in (
    "accepted_words: 116807",
    "chapter: 22",
    'eastern: "13:12:44 EDT"',
    'india: "22:42:44 IST"',
):
    if phrase not in manifest:
        fail(f"accepted manifest missing: {phrase}")
if "chapter-23.md" in manifest:
    fail("Chapter 23 was added to accepted manifest")

ch22_validator = read(CH22_VALIDATOR)
for phrase in (
    'CH23_LOCK = "books/book-01/control/46-chapter-23-mission-lock.md"',
    'CH23_VALIDATOR = "tools/validate_book1_chapter23_mission_lock.py"',
    "authorized_ch23 = {CH23_LOCK}",
    'if "chapter-24" in lower',
):
    if phrase not in ch22_validator:
        fail(f"Chapter 22 validator gate transition missing: {phrase}")

workflow = read(WORKFLOW)
for phrase in (
    "python3 tools/count_book1_words.py --expect 116807",
    "python3 tools/validate_book1_chapter22.py",
    "python3 tools/validate_book1_chapter23_mission_lock.py",
    f"git diff --check {BASE} --",
):
    if phrase not in workflow:
        fail(f"workflow missing: {phrase}")

tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
chapter23_artifacts = []
for path in tracked:
    lower = path.lower()
    if "chapter-23" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
        chapter23_artifacts.append(path)
    if "chapter-24" in lower and path.startswith(("books/book-01/control/", "books/book-01/drafts/", "books/book-01/manuscript/")):
        fail(f"Chapter 24 artifact exists: {path}")
    if ("remainder" in lower and "outline" in lower) or ("act-iii" in lower and "outline" in lower):
        fail(f"complete remainder outline artifact exists: {path}")

if chapter23_artifacts != [LOCK]:
    fail(f"unexpected Chapter 23 artifacts: {chapter23_artifacts}")
for forbidden in (
    "books/book-01/drafts/chapter-23.md",
    "books/book-01/manuscript/chapters/chapter-23.md",
    "books/book-01/control/47-chapter-23-acceptance-review.md",
):
    if (ROOT / forbidden).exists():
        fail(f"forbidden Chapter 23 artifact exists: {forbidden}")

protected = [
    MANIFEST,
    CH22,
    CH22_LOCK,
    CH22_REVIEW,
    "books/book-01/manuscript/prologue.md",
] + [f"books/book-01/manuscript/chapters/chapter-{index:02d}.md" for index in range(1, 22)]
if subprocess.run(["git", "diff", "--quiet", BASE, "--", *protected], cwd=ROOT).returncode:
    fail("accepted manifest, accepted prose, or Chapter 22 controls changed")

changed_output = subprocess.check_output(
    ["git", "diff", "--name-status", "--find-renames", BASE, "--"],
    cwd=ROOT,
    text=True,
)
changed = set()
for line in changed_output.splitlines():
    fields = line.split("\t")
    status = fields[0]
    if status.startswith(("R", "C")):
        if len(fields) != 3:
            fail(f"unexpected rename/copy diff entry: {line}")
        changed.update(fields[1:])
    else:
        if len(fields) != 2:
            fail(f"unexpected diff entry: {line}")
        changed.add(fields[1])
if changed != EXPECTED_CHANGED:
    fail(f"changed-file scope mismatch: expected {sorted(EXPECTED_CHANGED)}, got {sorted(changed)}")
for path in changed:
    name = Path(path).name.lower()
    if any(token in name for token in ("tmp", "temp", "helper", "payload", "runner", "debug", "apply", "latest", "backup")):
        fail(f"forbidden temporary/helper artifact: {path}")
    if name.endswith((".orig", ".rej")):
        fail(f"forbidden rejected/original artifact: {path}")

if subprocess.run(["git", "diff", "--check", BASE, "--"], cwd=ROOT).returncode:
    fail("git diff --check")

print("PASS: Chapter 23 mission lock is authorized, complete, and scope-protected")
