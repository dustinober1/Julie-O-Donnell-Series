# Book 1 Production Proofs

This directory contains reproducible production proofs for *Veridrift*.

## Source authority

Only the 25 prose files listed in `../ACCEPTED_MANUSCRIPT.yaml`, in manifest order, are used. Generated proofs are derivatives and never become manuscript authority.

## Build

```bash
python -m pip install -r requirements-production.txt
python tools/build_book1_production.py
python -m unittest tools.test_book1_production -v
```

The permanent builder validates manifest version, readiness, file inventory, per-file hashes and counts, the 105,157-word total, Chapter 20 locks, chapter order, Chapter 25 absence, and the final line before generating any proof.

## Outputs

- `proofs/Veridrift_INTERIOR_PROOF.docx`
- `proofs/Veridrift_EPUB_PROOF.epub`
- `proofs/Veridrift_PRINT_PROOF.pdf`

## Status

These are production proofs pending manual author approval. Publication readiness remains `proofread_and_production_required`.
