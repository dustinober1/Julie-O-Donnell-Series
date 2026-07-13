from pathlib import Path
import hashlib

old_blob = "73b387872d3c4937f6598b20d4bcc90d6c46f415"
correction_baseline = "b4f654aca10e9ce7e7ebdb6256ad25e210fd7633"
chapter_path = Path("books/book-01/manuscript/chapters/chapter-15.md")
chapter = chapter_path.read_text(encoding="utf-8")
old_sentence = "No camera guaranteed truth. Batteries failed. angles missed hands. files could later be challenged."
new_sentence = "No camera guaranteed truth. Batteries failed. Angles missed hands. Files could later be challenged."
if chapter.count(old_sentence) != 1:
    raise SystemExit(f"expected one capitalization defect, found {chapter.count(old_sentence)}")
before_count = len(chapter.split())
chapter = chapter.replace(old_sentence, new_sentence, 1)
after_count = len(chapter.split())
if before_count != 5993 or after_count != 5993:
    raise SystemExit((before_count, after_count))
chapter_path.write_text(chapter, encoding="utf-8")

data = chapter.encode("utf-8")
new_blob = hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()
if new_blob == old_blob:
    raise SystemExit("blob did not change")

text_suffixes = {".md", ".yaml", ".yml"}
for path in Path(".").rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in text_suffixes:
        continue
    text = path.read_text(encoding="utf-8")
    if old_blob in text:
        path.write_text(text.replace(old_blob, new_blob), encoding="utf-8")

def replace_once(path_str: str, old: str, new: str) -> None:
    path = Path(path_str)
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one occurrence of {old!r}, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

replace_once(
    "PROJECT_STATE.yaml",
    '      prose_changed_during_review: false\n      reviewed_blob_sha: "' + new_blob + '"',
    '      prose_changed_during_review: true\n      reviewed_blob_sha: "' + new_blob + '"',
)
replace_once(
    "PROJECT_STATE.yaml",
    '    chapter_15: "accepted and promoted unchanged"',
    '    chapter_15: "accepted and promoted after one capitalization copyedit"',
)
replace_once(
    "PROJECT_STATE.yaml",
    '    status: "accepted unchanged; canon"',
    '    status: "accepted after one capitalization copyedit; canon"',
)
replace_once(
    "PROJECT_STATE.yaml",
    '    verdict: "ACCEPT"\n    prose_changed_during_review: false\n    next_gate:',
    '    verdict: "ACCEPT"\n    prose_changed_during_review: true\n    next_gate:',
)
replace_once(
    "PROJECT_STATE.yaml",
    '    status: "ACCEPT; promoted unchanged"',
    '    status: "ACCEPT; promoted after one capitalization copyedit"',
)
replace_once(
    "PROJECT_STATE.yaml",
    '  - "Chapter 15 is accepted unchanged at 5993 words and lives only under the manuscript path."',
    '  - "Chapter 15 is accepted after one capitalization-only copyedit at 5993 words and lives only under the manuscript path."',
)

replace_once(
    "README.md",
    '- Chapter 15, **The Split Record**: accepted unchanged at **5,993 words**',
    '- Chapter 15, **The Split Record**: accepted after one capitalization-only copyedit at **5,993 words**',
)
replace_once(
    "books/book-01/drafts/README.md",
    'Chapter 15 — **The Split Record** — was accepted unchanged and moved to:',
    'Chapter 15 — **The Split Record** — was accepted after one capitalization-only copyedit and moved to:',
)
replace_once(
    "books/book-01/manuscript/STATUS.md",
    '- Chapter 15 verdict: **ACCEPT**, unchanged at 5,993 words',
    '- Chapter 15 verdict: **ACCEPT**, after one capitalization-only copyedit at 5,993 words',
)
replace_once(
    "books/book-01/control/30-chapter-15-mission-lock.md",
    'The locked mission was fully dramatized by `books/book-01/manuscript/chapters/chapter-15.md` and accepted unchanged at 5,993 words.',
    'The locked mission was fully dramatized by `books/book-01/manuscript/chapters/chapter-15.md` and accepted after one capitalization-only copyedit at 5,993 words.',
)
replace_once(
    "books/book-01/control/16-chapter-by-chapter-status-record.md",
    '- **Reviewed blob:** `' + new_blob + '`.\n- **Exact word count:** 5,993 whitespace-delimited Markdown words.',
    '- **Reviewed blob:** `' + new_blob + '`.\n- **Review prose change:** One capitalization-only copyedit in the body-camera paragraph; word count unchanged.\n- **Exact word count:** 5,993 whitespace-delimited Markdown words.',
)

review_path = Path("books/book-01/control/31-chapter-15-acceptance-review.md")
review = review_path.read_text(encoding="utf-8")
review = review.replace(
    "Chapter 15 — **The Split Record** — satisfies the approved mission lock, the Chapter 15 acceptance gate, accepted-manuscript continuity, evidence and knowledge limits, injury mechanics, institutional realism, Narrative House Style v2.2, and the Book 1 ending contract. No prose revision was required. The reviewed 5,993-word draft is promoted unchanged into the accepted manuscript.",
    "Chapter 15 — **The Split Record** — satisfies the approved mission lock, the Chapter 15 acceptance gate, accepted-manuscript continuity, evidence and knowledge limits, injury mechanics, institutional realism, Narrative House Style v2.2, and the Book 1 ending contract. One capitalization-only copyedit was required in the body-camera paragraph: `angles` and `files` were capitalized after periods. The reviewed 5,993-word draft is accepted with that word-count-neutral correction.",
    1,
)
review = review.replace("- Prose revisions: **none**", "- Prose revisions: **one capitalization-only copyedit**", 1)
review = review.replace(
    "- **Optional polish:** none authorized\n- **No change:** complete chapter prose",
    "- **Required copyedit:** one capitalization-only correction in the body-camera paragraph\n- **No further change:** all other chapter prose",
    1,
)
review = review.replace(
    "1. Move the unchanged Chapter 15 blob to `books/book-01/manuscript/chapters/chapter-15.md`.",
    "1. Retain the corrected Chapter 15 blob at `books/book-01/manuscript/chapters/chapter-15.md`.",
    1,
)
addendum_marker = "Chapter 16 was not drafted. Chapter 16 and later prose do not exist.\n"
addendum = f"""

## Corrective acceptance addendum — 2026-07-13

- Correction baseline on `main`: `{correction_baseline}` (PR #31 had already accepted and promoted Chapter 15).
- Drift handling: the prior acceptance work was preserved; this pass corrected its one missed mandatory copyedit rather than reverting or duplicating the promotion.
- Pre-correction accepted blob: `{old_blob}`.
- Final reviewed/accepted blob: `{new_blob}`.
- Exact prose change: `Batteries failed. angles missed hands. files could later be challenged.` became `Batteries failed. Angles missed hands. Files could later be challenged.`
- Pre-correction and post-correction word counts: **5,993 / 5,993**.
- Verdict remains **ACCEPT**; accepted scope, 81,586-word total, opening, endpoint, custody state, evidence limits, and Chapter 16 prohibition are unchanged.
"""
if "## Corrective acceptance addendum" in review:
    raise SystemExit("corrective addendum already present")
if addendum_marker not in review:
    raise SystemExit("review addendum insertion point missing")
review = review.replace(addendum_marker, addendum_marker + addendum, 1)
review_path.write_text(review, encoding="utf-8")

workflow_path = Path(".github/workflows/book1-manuscript-validation.yml")
workflow = workflow_path.read_text(encoding="utf-8")
needle = "          assert 'Chapter 16' not in text\n"
inserted = (
    needle
    + "          assert 'No camera guaranteed truth. Batteries failed. Angles missed hands. Files could later be challenged.' in text\n"
    + "          assert 'Batteries failed. angles missed hands. files could later be challenged.' not in text\n"
)
if workflow.count(needle) != 1:
    raise SystemExit("workflow insertion point missing")
workflow = workflow.replace(needle, inserted, 1)
workflow = workflow.replace(
    "          assert 'Chapter 16 and later prose do not exist' in review.read_text(encoding='utf-8')\n",
    "          review_text = review.read_text(encoding='utf-8')\n          assert 'Chapter 16 and later prose do not exist' in review_text\n          assert 'one capitalization-only copyedit' in review_text\n",
    1,
)
workflow_path.write_text(workflow, encoding="utf-8")

occurrences = []
for path in Path(".").rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in text_suffixes:
        continue
    text = path.read_text(encoding="utf-8")
    if old_blob in text:
        occurrences.append(str(path))
if occurrences != ["books/book-01/control/31-chapter-15-acceptance-review.md"]:
    raise SystemExit(f"unexpected old blob references: {occurrences}")

print(f"new Chapter 15 blob: {new_blob}")
print(f"word count: {after_count}")
