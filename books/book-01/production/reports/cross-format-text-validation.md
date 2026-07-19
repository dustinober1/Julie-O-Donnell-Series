# Cross-Format Text Validation

## Source normalization

- Source: exactly 25 manifest-listed Markdown files in manifest order.
- Markdown heading markers are production structure, not body prose.
- Inline emphasis delimiters are removed while their text is preserved.
- Scene-break source markers are compared structurally and rendered as `* * *`.
- Whitespace is normalized only for PDF line-wrap comparison; DOCX and EPUB are compared paragraph by paragraph.
- Production-only title/notice matter, running heads, and folios are excluded.

## Results

- DOCX independent OOXML extraction: PASS
- EPUB independent ZIP/XHTML extraction: PASS
- PDF independent pypdf extraction with whitespace/header normalization: PASS
- Exactly one Prologue and 24 numbered chapters: PASS
- No Chapter 25: PASS
- Chapter 20 count/hash/end: PASS
- Complete-book final line: `The bubble stayed centered.` — PASS
- Overall: PASS
