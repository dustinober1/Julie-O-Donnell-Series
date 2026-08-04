# 72. Book 1 Detail Continuity Audit — Final Report

**Plan:** `70-detail-continuity-audit-plan.md`
**Findings register:** `71-detail-continuity-findings.md`
**Audit head commit:** `08e1b7df53624a8bbea1bbfd7c18062c6f0f84bb`
**Date:** 2026-08-04

---

## 1. Verdict

# ACCEPTED PROSE PASSES. THREE CONTROL DEFECTS FOUND AND REPAIRED.

No accepted prose file was changed. The manifest, word count, and all
twenty-five SHA-256 values are unchanged from the frozen publication master.

Every defect this audit found was in a control document that had fallen out of
sync with prose that was already correct.

## 2. Why the audit was run this way

Book 1 carried extensive quality control before this pass, and all of it was
passing. Those controls verify **format, inventory, integrity, and style**.
The controls that do address story fact — the seven continuity ledgers and the
audit at `59-` — were built top-down: a fact had to be noticed before it could
be recorded, and a fact that was never recorded cannot fail a ledger check.

This audit ran the other direction. It extracted every mechanically checkable
detail out of the prose first and tested the ledgers against it.

That choice is what produced the results. All three defects sat in files that
earlier top-down passes had read and found clean — because those passes were
checking the facts someone had already thought to write down.

## 3. Coverage

| Class | Rule | Scope reached | Result |
|---|---|---|---|
| D1 clock | R1 zone offset | 6 paired statements | clean |
| D1 clock | R2 scene chronology | 68 scene headers, whole book | clean after adjudication |
| D1 clock | R3 countdown monotonicity | 29 values, 5 concurrent clocks | clean |
| D1 clock | R4 sub-second restatement | 12 values across 5 chapters | clean |
| D3 codes | R5 designator form | 76 designators | clean |
| D2 names | R6 near-miss variants | 149 recurring names | clean after adjudication |
| D8 quantities | R7 anchored facts | 4 load-bearing facts | clean |
| D2/D3 | R8 first-mention index | 1,179 entries | recorded |
| D5 objects | R9 possession chain | Ch 5–14 targeted | clean |
| D6 injury | R10 capability ceilings | Ch 5–14 targeted | clean |
| D7 knowledge | R11 ordering | index-level, whole book | clean |
| D4 space | R12 physical transit | one real-geography window | clean |
| D9 surface | R13 surface continuity | **not run** | — |
| proof | R14 proof ceilings | Ch 15–24 | clean |

**Not covered:** the full per-chapter scene cards, R13 surface continuity
across the book, and scene-level R9/R10 over Chapters 15–24. Those remain
available if wanted; on the evidence below, the expected yield is low.

## 4. The three defects

| ID | Defect | Class | State |
|---|---|---|---|
| **DC-01** | Control documents compressed two calendar days into one. The prose opens October 12, crosses midnight inside Chapter 5, and puts the climax on October 13; the master timeline filed 10:43 through 22:18 under a single October 13 heading. | LEDGER-STALE | repaired |
| **DC-02** | A superseded `15:41–16:14` re-entry row survived in the master timeline, describing the pre-repair 16:xx architecture and contradicting a note three lines beneath it. Both were marked LOCKED. | CONTRADICTION | repaired |
| **DC-03** | The 02:14 identity construction — the book's central unresolved thread — was filed under October 13 in the series handoff. Chapter 2 places it "that morning," on October 12. | CONTRADICTION | repaired |

**DC-02 and DC-03 were only reachable once DC-01 was repaired.** DC-02 sat
exactly on the day boundary. DC-03 was perfectly self-consistent under the
wrong reading: with every scene filed under October 13, "02:14 that morning"
and the 04:50 climax sat on the same day and contradicted nothing.

That dependency is the argument for the bottom-up direction, stated as
compactly as it can be. Fixing the calendar did not just correct a heading; it
made two further defects visible that no amount of top-down checking had
surfaced.

## 5. What the audit found about the drafting

Stated plainly, because it is the answer to the question that prompted this
work.

The detail tracking in the accepted prose is strong:

- **285 timestamp occurrences**, 219 distinct, with no ordering defect and no
  zone-conversion error.
- **12 sub-second forensic timestamps** re-cited across Chapters 12, 13, 14,
  19, and 22 — `07:08:09.442`, `07:10:08.021`, `07:52:12.117` — every
  restatement matches its origin exactly.
- **76 designators** with zero format drift, including the ones most prone to
  it: `APX-DIR-0019`, `SSO-NS-004`, `DIA-SAR-PRICE-01`, `PCF-27`, `L3-7`.
- **Five concurrent countdown clocks** in Act II, interleaved on the page,
  each decreasing correctly. The external commit clock's arithmetic lands
  exactly on its 05:00 anchor.
- **Possession chains** that survive scrutiny, including the tool bag whose
  scattered contents in Chapter 6 were each established in Chapter 5.
- **An injury acquired on the page** in Chapter 6 and respected by every
  subsequent action through Chapter 24, including an unremarked switch from
  two-handed to left-handed driving.
- **Proof ceilings held explicitly**, with the book's central distinction —
  the later release versus the original construction — stated and re-stated at
  every point where a lesser draft would have let it collapse.

The concern that prompted this audit was that detail tracking during drafting
had been poor. The evidence does not support that. What drifted was the
paperwork about the book, not the book.

## 6. Durable outcome

The audit leaves behind a repeatable check rather than a one-time result.

| Artifact | Path |
|---|---|
| Extractor | `tools/extract_book1_detail_index.py` |
| Rule checker | `tools/check_book1_detail_rules.py` |
| Tests | `tools/test_book1_detail_rules.py` (14 tests) |
| Derived chronology | `artifacts/book1-derived-chronology.md` |
| Rule results | `artifacts/book1-detail-findings.json` |
| CI workflow | `.github/workflows/book1-detail-continuity.yml` |

The workflow fails the build if the chronology derived from the prose stops
matching the committed one. That is the specific guard whose absence allowed
DC-01 to persist: nothing in the repository compared a stated date against the
number of midnights the prose actually crosses.

Both tools carry no third-party dependencies, matching the other permanent
Book 1 validators.

## 7. Effect on publication state

None. The publication package remains frozen and cleared as recorded in
`66-publication-master-freeze.md` and PR #92. This audit changed no accepted
prose, no manifest value, no word count, and no checksum, so no rebuild,
revalidation, or re-freeze is required.

The required next steps in `PROJECT_STATE.yaml` are unchanged: perform a
retailer-specific preview immediately before upload, and record retailer
upload or release status when it occurs.
