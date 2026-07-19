# VERIDRIFT — Controlled Publication Corrections, Passes 0–2

This directory records the completed first three stages of the final publication correction plan. It is a **controlled correction pass**, not a developmental rewrite.

## Scope completed

- Pass 0: canonical-master control and obsolete-draft isolation.
- Pass 1: chronology, custody, geography, and house-style decisions locked.
- Pass 2: chronology and custody findings C01–C05 corrected with true Word tracked changes.

The tracked Word master contains 12 insertions and 12 deletions. Each revision author field carries the applicable ledger ID.

## Reviewable material in this PR

- `SOURCE_CORRECTIONS.patch` — exact source-level representation of C01–C05 against the accepted Markdown manuscript.
- `CHANGE_LOG.md` — deleted and inserted wording for every correction.
- `STYLE_AND_CONTINUITY.md` — locked date, custody, geography, and house-style decisions.
- `VERIFICATION_REPORT.md` — structural, tracked-change, search, checksum, and visual-QA results.
- `CHECKSUMS.sha256` and `BINARY_ARTIFACTS.md` — identities of the controlled Word/EPUB artifacts produced during this pass.

The accepted Markdown manuscript files are intentionally not changed by this audit PR. The source patch is retained so the corrections can be applied atomically after the tracked changes are accepted and before regenerated publication proofs are approved.

## Binary working artifacts

The full tracked publication master, style-sheet DOCX, preserved EPUB baseline, and archived obsolete draft were produced and verified outside Git. They are not duplicated as binary blobs in this PR. Their exact SHA-256 identities are recorded in `BINARY_ARTIFACTS.md`.

## Verification

- Full 25-unit manuscript structure verified against the reviewed EPUB.
- All chapter openings, endings, and paragraph sequences matched before correction.
- OOXML package integrity passed.
- Tracked-change structure passed.
- Corrected target-phrase audit passed.
- The 442-page working master and one-page style sheet were rendered and visually inspected.

## Status

Passes 0–2 are complete. This is not yet a retailer-upload package. Pass 3 will repair the Chapter 2 scene transitions and dialogue paragraph findings D01–D38.
