# Book 1 Control Pack

Accepted prose and `../ACCEPTED_MANUSCRIPT.yaml` control canon. This directory records continuity, evidence, knowledge, technology, institutional authority, proof ceilings, editorial history, publication validation, and production-package evidence.

## Current accepted state

- Book title: **Veridrift**
- Accepted canon: **Prologue and Chapters 1–24**
- Accepted prose files: **25**
- Accepted baseline: **108,672 words**
- Manifest version: **2**
- Controlled final proofread: **complete; PR #84 merged**
- Open proofreading queries: **0**
- Editorial state: **publication master re-frozen 2026-08-25 under `76-production-quality-pass.md`**
- Publication state: **prose frozen and validated; production package STALE and requires rebuild**
- Readiness field: `prose_frozen_package_rebuild_required`
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
- Production-quality pass and current publication-master freeze: `76-production-quality-pass.md`
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

**Rebuild the production package.** It is stale twice over: the accepted prose has changed substantially, and it was built with an `identify_scene_meta()` that rendered 54 of the book's 64 scene headers in monospace. Book 1 is not upload-ready until it is rebuilt, `tools/test_book1_production.py` passes rather than skips, scene headers are visually confirmed as centred small-caps in all three formats, and checksums and the package manifest are regenerated. See `76-production-quality-pass.md` §10.

Then perform a retailer-specific preview immediately before upload and record retailer upload or release status when it occurs.

The prose itself is correct and frozen. The stale outputs are a build state, not a manuscript defect.
