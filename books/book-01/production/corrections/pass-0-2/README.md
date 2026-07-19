# VERIDRIFT — Controlled Publication Corrections, Passes 0–2

This directory records the completed first three stages of the final publication correction plan. It is a **controlled correction pass**, not a developmental rewrite.

## Scope completed

- Pass 0: canonical-master control and obsolete-draft isolation.
- Pass 1: chronology, custody, geography, and house-style decisions locked.
- Pass 2: chronology and custody findings C01–C05 corrected with true Word tracked changes.

The tracked master contains 12 insertions and 12 deletions. Each revision author field carries the applicable ledger ID.

## Working authority

- `Veridrift_Publication_Master_v1.docx` — full Prologue plus Chapters 1–24; sole editable correction master.
- `Veridrift_Style_and_Continuity_Sheet_v1.docx` — locked editorial decisions.
- `STYLE_AND_CONTINUITY.md` — reviewable text equivalent of the style sheet.
- `SOURCE_CORRECTIONS.patch` — reviewable source-level representation of C01–C05. The accepted Markdown manuscript files are not changed by this PR; the patch is retained so those changes can be applied atomically when the tracked corrections are accepted.

## Baseline and obsolete files

- `Veridrift_EPUB_PROOF_REVIEWED_NOT_FOR_UPLOAD.epub` — unchanged reviewed proof baseline.
- `Veridrift_OBSOLETE_12-Chapter_Draft.docx` — incomplete draft, retained only for provenance; never use for publication.

## Audit material

- `CHANGE_LOG.md`
- `VERIFICATION_REPORT.md`
- `verification-data.json`
- `CHECKSUMS.sha256`

## Verification

- Full 25-unit manuscript structure verified against the reviewed EPUB.
- All chapter openings, endings, and paragraph sequences matched before correction.
- OOXML package integrity passed.
- Tracked-change structure passed.
- Corrected target-phrase audit passed.
- The 442-page working master and one-page style sheet were rendered and visually inspected.

## Status

Passes 0–2 are complete. This is not yet a retailer-upload package. Pass 3 will repair the Chapter 2 scene transitions and dialogue paragraph findings D01–D38.
