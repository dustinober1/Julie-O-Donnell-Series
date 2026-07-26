# Migration Conflict Log

## Status values

- **resolved** — authority and disposition established.
- **isolated** — both sources preserved; no authoritative overwrite applied.
- **pending comparison** — exported and checksummed; detailed comparison belongs to the next focused PR.
- **requires author decision** — substantive prose correction is not applied automatically.

## C-001 — Stale Book 1 publication status

**Status:** resolved in `migration/reconcile-book1-status`  
**GitHub baseline:** `9708fdd86e9292a75b7683152c7746567f015cc6`  
**Evidence:** PR #92 final package manifest, validations, publication review, change log, closed ledger, and checksums.

Several state files still said production proofs were pending. PR #92 records that the final DOCX, EPUB, print PDF, cover, metadata, ledger, and package archive were generated, validated, and cleared. The stale state files are reconciled without changing accepted manuscript prose.

## C-002 — Drive-native Book 1 Prologue

**Status:** isolated; normalized line comparison pending the series-bible PR  
**Drive source:** `prologue`, file ID `1upUvx5RV-ToSFLLc5k_mQQZhjerethTDWi5PiXPEoAg`, modified `2026-07-21T02:39:35.504Z`  
**Drive export SHA-256:** `ddb58d8162c32ba1e573e7308c69f0e79e4e687e6f390b93408126457ed91699`  
**GitHub source:** `books/book-01/manuscript/prologue.md` at baseline commit `9708fdd86e9292a75b7683152c7746567f015cc6`  
**Accepted manifest SHA-256:** `9f1285a83b3379b8f34ced719ad7b2d9d79b645a8eb5587aa38822710683506e`

Known substantive candidate: Drive says `At 0214 hours`; the publication master says `At 0214`. No change is applied automatically.

## C-003 — Drive-native Book 1 Chapter 1

**Status:** isolated; normalized line comparison pending the series-bible PR  
**Drive source:** `chapter-01`, file ID `1cUkrfYZ8093yVZCjOIz2wsiLPXebMIWLzxNcU3Vzfgw`, modified `2026-07-21T02:46:16.857Z`  
**Drive export SHA-256:** `b13fff8fe3242b28775501e0b5396c908235f55d7198d7aec1f58f72acdb1ed8`  
**GitHub source:** `books/book-01/manuscript/chapters/chapter-01.md` at baseline commit `9708fdd86e9292a75b7683152c7746567f015cc6`  
**Accepted manifest SHA-256:** `36a1dc970b84ab0e2b76c856f83dd4d35dff405bfd9219854d8fbbd2f8d0c8c7`

No Drive text is promoted until the normalized comparison identifies each difference and its authority classification.

## C-004 — Drive rectangular cover differs from approved package cover

**Status:** resolved as distinct external asset  
**Drive file:** `cover.jpg`, ID `123KLeaO9TTCk57vRmOzbB62ZvJggV1OZ`  
**Drive SHA-256:** `60dcd6293a0338ac40db5f281d8a6178c69d31e26dd6d7928ab01264cf2a23a3`  
**Approved PR #92 cover SHA-256:** `3e20c8e44fb6a4541fc3cb8729cf87641043434b439c3c9c1a40624508dc8e6d`

The Drive file is 1600 × 2560 RGB JPEG but is not byte-identical to the approved package cover. It is tracked as an external distribution/review asset and must not silently replace the approved cover.

## C-005 — Drive-era authority statements conflict with migration decision

**Status:** resolved by explicit supersession  
**Affected Drive documents:** Series Bible Authority README, Book 1 Series Continuity README, and Book 2 Control Center.

Statements declaring Drive the sole authority are preserved as historical source text but are superseded by the 2026-07-25 migration decision. Imported active documents will state GitHub authority while retaining exact Drive IDs and export checksums in provenance records.

## C-006 — Duplicate Drive controls

**Status:** resolved at byte-identity level; GitHub counterpart comparison pending where applicable

- Book 1 canon handoff and Book 2 canon handoff export to the same SHA-256: `327b7bdbf963eb0599d7e23b36dd2e12d07560af398e6c536d786d077a9774f0`.
- Two Drive recurring-character ledger DOCX files share SHA-256 `d40a7dffb38cd65127491bde9c66fc4c6ddafed57c2848d5aaf3e4602a311187`.
- Two Drive open-plot-thread DOCX files share SHA-256 `10ed9b568e876032d4eec66ecdfea9222224f26bb6f4d4609adebd34b1192455`.
- Two Drive master-timeline DOCX files share SHA-256 `7375de11050af3a1340762fc1f6e01f117e6fb5b46654d731bd871e90c75026d`.
- Two Drive antagonist-objective DOCX files share SHA-256 `da4258454d0d5219b8e35eba773d26796ae077b5a18fb7f023276248e63389c6`.

Duplicate Drive copies will not become duplicate active GitHub controls.
