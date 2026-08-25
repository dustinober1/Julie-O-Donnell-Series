# EPUB Validation

- File: `books/book-01/production/proofs/Veridrift_EPUB_PROOF.epub`
- Size: 299,194 bytes
- SHA-256: `fe78362ae4707e549a1d3a25d6f816288cdfca827a220586d9f35d3e5993fd36`
- EPUB mimetype first and uncompressed: PASS
- Spine entries: 27 (2 proof front-matter sections + 25 accepted sections)
- TOC entries: 25 — PASS
- Chapter 25 absent: PASS
- Remote resources: none
- JavaScript: none
- Independent XHTML paragraph extraction comparison: PASS
- EPUBCheck: populated by workflow in `epubcheck.txt`; every production-owned error must be resolved.
- Independent reader: workflow invokes Pandoc against the EPUB when available.
- Kindle Previewer: unavailable on the Linux CI runner; manual Kindle Previewer review remains required.
- Approved cover: missing; EPUB cover metadata intentionally omitted.

## Extraction findings

- No missing, duplicated, reordered, or altered body paragraph detected.
