# Book 1 Production Package

This directory contains reproducible production-proof records, final-package evidence, validation reports, and external-asset provenance for *Veridrift*.

## Source authority

Only the 25 prose files listed in `../ACCEPTED_MANUSCRIPT.yaml`, in manifest order, are canonical prose. Generated DOCX, EPUB, PDF, cover, compilation, and archive files are derivatives and never become independently editable manuscript authority.

## Historical proof build

The following proof files record the intermediate production stage completed before final-package signoff:

- `proofs/Veridrift_INTERIOR_PROOF.docx`
- `proofs/Veridrift_EPUB_PROOF.epub`
- `proofs/Veridrift_PRINT_PROOF.pdf`

Their build and approval history is retained in `../control/67-production-package-build.md`, `../control/68-production-proof-query-log.md`, and `../control/69-production-proof-approval.md`.

## Final package

PR #92 completed and cleared the final publication package at merge commit `9708fdd86e9292a75b7683152c7746567f015cc6`.

Final-package records are under `final/`, including:

- package manifest;
- final publication review;
- correction ledger;
- metadata;
- validation reports;
- SHA-256 checksums.

Large final binaries remain outside ordinary Git history. Their filenames, storage observations, formats, checksums, and approval states are recorded in `EXTERNAL_ASSETS.yaml`.

## Current status

- Publication readiness: `publication_ready_upload_ready`.
- Accepted prose: frozen.
- Final package: generated, validated, and cleared.
- Open manuscript or package defects: none.
- Retail release: not established by repository evidence.

A retailer-specific preview immediately before upload is an operational safeguard, not a pending production gate.

## Reproducible validation

```bash
python -m pip install -r requirements-production.txt
python tools/build_book1_production.py
python -m unittest tools.test_book1_production -v
```

The permanent builder validates the accepted inventory, per-file hashes and counts, the 105,157-word total, Chapter 20 locks, chapter order, Chapter 25 absence, and the final line before generating proof derivatives.
