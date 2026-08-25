# Book 1 Control Pack

Accepted prose and `../ACCEPTED_MANUSCRIPT.yaml` control canon. This directory records continuity, evidence, knowledge, technology, institutional authority, proof ceilings, editorial history, publication validation, and production-package evidence.

## Current accepted state

- Book title: **Veridrift**
- Accepted canon: **Prologue and Chapters 1–24**
- Accepted prose files: **25**
- Accepted baseline: **109,498 words**
- Manifest version: **2**
- Controlled final proofread: **complete; PR #84 merged**
- Open proofreading queries: **0**
- Editorial state: **publication master re-frozen 2026-08-25 under `78-act-iii-correction-record.md`**
- Publication state: **prose frozen and validated; proofs rebuilt and verified; final package not yet promoted**
- Readiness field: `proofs_rebuilt_pending_author_visual_review`
- Prior package merge commit: `9708fdd86e9292a75b7683152c7746567f015cc6` (superseded prose, and built with the unfixed scene-header styling)
- Retail release state: **not established by repository evidence**
- Preserved ending: **The bubble stayed centered.**

`../ACCEPTED_MANUSCRIPT.yaml` is the sole canonical prose inventory. Historical drafts, archived files, the obsolete twelve-chapter Word export, generated review compilations, and prose outside the manifest inventory are not manuscript authority.

## Deliberate series carryovers

- The human or upstream instruction behind the original 02:14 construction remains unidentified.
- Senator Sterling's personal knowledge, direction, intent, possession, operation, or command remains unestablished.

These are deliberate series threads, not Book 1 continuity gaps.

## Current records

- Publication-readiness status: `51-publication-readiness-status.md`
- Specialist review register: `52-specialist-review-register.md`
- Specialist findings ledger: `53-specialist-findings-ledger.md`
- Production-proof report: `57-production-proof-report.md`
- Copyedit style sheet: `61-copyedit-style-sheet.md`
- Copyedit query log: `62-copyedit-query-log.md`
- Post-copyedit state reconciliation: `63-post-copyedit-publication-state-reconciliation.md`
- Final proofread report: `64-final-proofread-report.md`
- Final proofread query log: `65-final-proofread-query-log.md`
- Publication-master freeze: `66-publication-master-freeze.md`
- Production package build record: `67-production-package-build.md`
- Production proof approval: `69-production-proof-approval.md`
- Detail continuity audit plan: `70-detail-continuity-audit-plan.md`
- Detail continuity findings register: `71-detail-continuity-findings.md`
- Detail continuity audit report and verdict: `72-detail-continuity-audit-report.md`
- Complete editorial review of the accepted prose: `73-complete-editorial-review.md`
- Editorial correction record and current publication-master freeze: `74-editorial-correction-record.md`
- Act III thread-redistribution mission lock: `75-act-iii-thread-redistribution-lock.md`
- Production-quality pass: `76-production-quality-pass.md`
- Act III antagonist and compression mission lock: `77-act-iii-antagonist-and-compression-lock.md`
- Act III correction record and current publication-master freeze: `78-act-iii-correction-record.md`
- Paragraph render-style validator: `../../../tools/validate_book1_paragraph_styles.py`
- Chronology derived from the prose: `../../../artifacts/book1-derived-chronology.md`
- Final package manifest: `../production/final/Veridrift_Final_Package_Manifest.json`
- Final publication review: `../production/final/Veridrift_Final_Publication_Review.md`
- Final package checksums: `../production/final/CHECKSUMS.sha256`
- External asset provenance: `../production/EXTERNAL_ASSETS.yaml`

## Future prose-change policy

Any later accepted-prose change requires:

1. a new editorial exception record;
2. explicit author approval;
3. updated per-file word count and SHA-256;
4. an updated total accepted count;
5. complete revalidation;
6. a new publication-master freeze record.

## Next authorized stage

**Review the rebuilt proofs, then promote them.** The package was rebuilt and both production defects are confirmed fixed in the binaries: 190 scene headers correctly styled with none in monospace, and `PAK_RELAY_17A` intact in DOCX, EPUB and print PDF. `tools/test_book1_production.py` passes with the production dependencies present.

Remaining before retailer upload:

1. Author review of the visual contact sheets — the build marks visual inspection `PENDING AUTHOR REVIEW` by design.
2. Promote the verified proofs into `../production/final/`, regenerating `CHECKSUMS.sha256` and the package manifest. That directory still carries the superseded records.
3. The retailer-specific preview.

See `78-act-iii-correction-record.md` §6.
