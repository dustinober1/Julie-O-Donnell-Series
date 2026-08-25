# Julie O'Donnell Series

Canonical repository for the contemporary geopolitical techno-thriller series centered on Julie O'Donnell.

## Source of truth

GitHub is the sole active source of truth for manuscript prose, accepted chapters, canon and continuity records, mission locks, outlines, research controls, project state, and editorial or publication tracking.

Google Drive is limited to archived snapshots, review copies generated from GitHub, large production binaries, and files shared with nontechnical collaborators. A Drive copy does not supersede GitHub merely because it has a later modified timestamp.

## Book 1: *Veridrift*

- Prologue plus Chapters 1–24.
- Accepted Markdown publication master: **109,498 words** across exactly **25 accepted prose files**.
- Canonical manifest: `books/book-01/ACCEPTED_MANUSCRIPT.yaml`, version 2.
- Accepted prose is frozen. Changes require an explicit correction record and reviewable pull request.
- Final Book 1 line remains locked: **The bubble stayed centered.**
- The original 02:14 constructor remains unidentified.
- Senator Sterling's personal knowledge, direction, intent, possession, operation, or command remains unestablished.

## Publication state

PR #92, merged as commit `9708fdd86e9292a75b7683152c7746567f015cc6`, completed and froze the final publication package.

The following outputs were generated, validated, and cleared as the frozen publication package:

- `Veridrift_Publication_Master_FINAL.docx`
- `Veridrift_FINAL.epub`
- `Veridrift_PRINT_INTERIOR_FINAL.pdf`
- `Veridrift_Cover_1600x2560_RGB.jpg`
- `Veridrift_Final_Publication_Package.zip`

The final validation records, package manifest, correction ledger, metadata, and SHA-256 checksums are under `books/book-01/production/final/`. Large binaries remain external to ordinary Git history and are tracked by provenance and checksum records.

**Supported status:** publication-ready and upload-ready, with no open manuscript or package defect. A retailer-specific Kindle Previewer inspection remains prudent immediately before upload. The repository does not establish whether the book has already been released to retailers.

## Canonical authority

`books/book-01/ACCEPTED_MANUSCRIPT.yaml` and its listed files are the canonical Book 1 prose inventory. The production DOCX, EPUB, PDF, and generated compilations are derived outputs, not independently editable prose authorities.

Historical drafts, archived sources, obsolete Word exports, generated review compilations, and prose outside the accepted manifest are excluded from authority.

## Required workflow

1. Create or update the governing mission lock or control record.
2. Draft on a branch.
3. Review through a pull request.
4. Accept explicitly.
5. Add accepted prose to the accepted-manuscript manifest.
6. Update canon and state ledgers in the same pull request.
7. Generate Drive review copies only from GitHub.
