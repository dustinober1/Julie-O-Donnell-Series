# EPUB Validation

- File: `books/book-01/production/proofs/Veridrift_EPUB_PROOF.epub`
- Size: 291,517 bytes
- SHA-256: `9ffc13c0ec2d58f8eede73405fa1c5a8485aefb2630c6e70db9e25e017526c37`
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
