# 26. REPOSITORY GOVERNANCE REPAIR RECORD

## Status

**Integrated by the commit containing this record.**

This repair changes repository organization and production controls. It does not alter accepted manuscript prose and does not accept Chapter 13.

## Problems corrected

### 1. Draft inside the accepted-manuscript directory

Chapter 13 existed under `manuscript/chapters/` while status files correctly called it unaccepted. Its location made accidental canon treatment likely.

**Repair:** Reuse the unchanged Chapter 13 blob at `drafts/chapter-13.md` and remove the manuscript-path entry.

### 2. Contradictory production status

Repository files disagreed about:

- whether Chapter 13 existed;
- whether its title was selected;
- whether Act III drafting had begun;
- accepted word count; and
- the next production action.

**Repair:** Make `PROJECT_STATE.yaml` the sole production-status authority. Replace duplicated status documents with concise derived summaries.

### 3. Stale accepted-manuscript inventory

The manuscript README contained chapter-level counts whose total conflicted with the later verified accepted total.

**Repair:** Create `ACCEPTED_MANUSCRIPT.yaml` as the controlling inventory, remove stale per-chapter counts from the README, and retain the accepted total of 61,118 words.

### 4. No explicit ending contract

The repository tracked many threads but did not separate Book 1 obligations from series carryovers.

**Repair:** Add `22-book-1-ending-contract.md`.

### 5. No controlled word architecture

The requested 100,000–125,000-word range was not connected to the accepted total or remaining chapter functions.

**Repair:** Add a 112,500-word planning target and provisional remaining architecture in `23-word-budget-and-act-iii-architecture.md`.

### 6. Duplicate and unclassified open threads

Several open-thread entries described the same underlying obligation, and none had a formal Book 1/series disposition.

**Repair:** Add `24-thread-disposition-matrix.md`, merge duplicates into controlling thread groups, and assign every thread a disposition.

### 7. No formal promotion gate

A complete draft could be mistaken for accepted prose.

**Repair:** Add `25-chapter-acceptance-gate.md` and make same-pass promotion mandatory.

### 8. No cross-book recurring-character control

The Book 1 character ledger tracked current state but not cross-book recurrence, no-retcon locks, return triggers, or intended end states.

**Repair:** Add `series/recurring-character-ledger.md`.

### 9. External source ambiguity

The former Google Doc and uploaded Word snapshot remained available as historical inputs without a dedicated archive policy.

**Repair:** Add `archive/legacy-sources/README.md`, identify the Word snapshot by hash, and explicitly prohibit either source from functioning as an active manuscript.

### 10. Chapter 13 review ambiguity

The draft structurally followed the mission lock, but no formal verdict separated structural promise from acceptance.

**Repair:** Add `27-chapter-13-acceptance-review.md` with a HOLD verdict pending a complete continuity, ledger, count, and style pass.

## Files deliberately not duplicated

Superseded status and planning versions remain recoverable through Git history. They are not copied into an active archive tree because duplicate Markdown files would recreate the same ambiguity this repair removes.

## Canon impact

- Accepted prose changed: **No**
- Accepted chapters changed: **No**
- Accepted endpoint changed: **No**
- Accepted word count changed: **No**
- Chapter 13 prose changed: **No**
- Chapter 13 accepted: **No**
- Source hierarchy clarified: **Yes**
- Draft/canon separation enforced: **Yes**
- Book and series production controls added: **Yes**
