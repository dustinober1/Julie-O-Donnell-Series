# VERIDRIFT — Pass 0–2 Binary Artifact Manifest

The following binary artifacts were produced during the controlled correction pass and verified locally. They are not duplicated as binary blobs in this audit PR; their identities are fixed here so a later repository upload or publication build can be checked byte-for-byte.

| Artifact | Purpose | Bytes | SHA-256 |
|---|---|---:|---|
| `Veridrift_Publication_Master_v1.docx` | Full Prologue + Chapters 1–24 working master with C01–C05 as true tracked changes | 397,243 | `78737ffa248c4d8cb08e60b26be5a6aabcedcdc2a2aea7964c842a72ad6f01dd` |
| `Veridrift_Style_and_Continuity_Sheet_v1.docx` | Locked date, custody, geography, and house-style decisions | 38,187 | `1a1794112e89f40aea79ef85249979fe5d10f5d51fc14526b064db5793dc72fd` |
| `Veridrift_EPUB_PROOF_REVIEWED_NOT_FOR_UPLOAD.epub` | Unchanged reviewed proof baseline | 291,517 | `9ffc13c0ec2d58f8eede73405fa1c5a8485aefb2630c6e70db9e25e017526c37` |
| `Veridrift_OBSOLETE_12-Chapter_Draft.docx` | Archived incomplete source retained only for provenance | 253,490 | `22c91d97c5b44b9927f0a87ffc32215e1da4a0c60f587bd1280381c144aec382` |

## Structural facts

- Working master: 25 navigable manuscript units, Prologue plus Chapters 1–24.
- Tracked revisions: 12 insertions and 12 deletions, authored by ledger IDs C01–C05.
- Working-master render: 442 pages.
- Style-sheet render: 1 page.
- Preserved EPUB checksum matches the production proof merged through PR #86.
