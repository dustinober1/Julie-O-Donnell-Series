# 68 — Production Proof Query Log

## Status key

- `OPEN`
- `FIXED IN PRODUCTION`
- `METADATA REQUIRED`
- `AUTHOR DECISION REQUIRED`
- `ACCEPTED PROOF LIMITATION`

## Queries

| ID | Status | Area | Query / finding | Disposition |
|---|---|---|---|---|
| PPQ-001 | METADATA REQUIRED | Author | No locked author or pen name was found. | Proof-only author placeholder; publication blocked. |
| PPQ-002 | METADATA REQUIRED | Copyright | Copyright holder and year are not locked. | Omitted; publication blocked. |
| PPQ-003 | METADATA REQUIRED | Publisher | Publisher/imprint and publisher logo are not locked. | Omitted; publication blocked. |
| PPQ-004 | METADATA REQUIRED | Edition / ISBN | Edition statement and format ISBNs are not locked. | Omitted; publication blocked. |
| PPQ-005 | AUTHOR DECISION REQUIRED | Trim | No locked trim size was found. | Proof default is 6 x 9 inches. Confirm before final production. |
| PPQ-006 | METADATA REQUIRED | Cover | No repository asset is explicitly identified as the final approved cover. | No cover embedded; EPUB and full print production blocked. |
| PPQ-007 | METADATA REQUIRED | Front/back matter | Dedication, acknowledgments, and additional approved matter are not locked. | Not invented or included. |
| PPQ-008 | ACCEPTED PROOF LIMITATION | EPUB | Kindle Previewer is unavailable on the Linux runner. | Manual Kindle Previewer test required. |
| PPQ-009 | ACCEPTED PROOF LIMITATION | DOCX | Microsoft Word-specific pagination, field refresh, and blank-page handling cannot be fully certified by LibreOffice. | Manual Word review required. |
| PPQ-010 | ACCEPTED PROOF LIMITATION | PDF | Recto chapter starts were not forced in the PDF proof to avoid malformed parity pagination. | Author/production decision required before final print interior. |
| PPQ-011 | FIXED IN PRODUCTION | Cross-format | Production headings, scene ornaments, navigation, and running furniture were excluded from prose comparison. | Independent DOCX/EPUB/PDF extraction comparison implemented. |
| PPQ-012 | FIXED IN PRODUCTION | PDF validation | Initial PDF normalization treated a numeric prose-only line as a folio and did not account for a wrapped chapter heading. | Validator made page-aware; exact normalized PDF body now matches the manifest source hash. |

## Prose defects

No manuscript-prose correction was made. Any prose issue discovered during manual review must be logged here and routed through a new editorial exception rather than silently repaired in production.
