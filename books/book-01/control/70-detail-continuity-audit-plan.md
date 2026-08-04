# 70. Book 1 Detail Continuity Audit — Plan

**Status:** Executed 2026-08-04. Findings in `71-detail-continuity-findings.md`; verdict in `72-detail-continuity-audit-report.md`. R1–R12 and R14 run to the coverage stated in `72-` §3; the full scene-card pass and R13 remain available.
**Author request:** Independent re-verification of Book 1 concrete detail, on the concern that detail tracking during original drafting was incomplete
**Manuscript under audit:** Prologue + Chapters 1–24, `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
**Manuscript state:** `prose_frozen: true`, publication package cleared under PR #92
**Plan date:** 2026-08-04

---

## 1. Why a new pass is justified

Book 1 already carries substantial quality control. All of it currently passes:

| Existing control | Result at plan date |
|---|---|
| `tools/count_book1_words.py` | 105,157 words, matches manifest |
| `tools/validate_book1_publication_readiness.py` | PASS |
| Per-file SHA-256 vs. `ACCEPTED_MANUSCRIPT.yaml` | 25 of 25 match, 0 mismatches |
| `59-post-research-continuity-audit.md` | PASS WITH MINOR REPAIRS |
| `64-final-proofread-report.md` | Complete |
| `66-publication-master-freeze.md` | Frozen |

None of that is evidence that story detail is correct. Those controls verify **format, inventory, integrity, and style**. The continuity work that does address story fact — the seven ledgers under `control/continuity/` and the audit at `59-` — was performed **top-down**: it began from a known correction or a ledger assertion and searched the prose for anything that contradicted it.

That direction of travel has a structural blind spot. It verifies the facts someone already thought to write down. A detail that was never recorded in a ledger cannot fail a ledger check. A detail that drifted between Chapter 6 and Chapter 19 without ever entering a ledger is invisible to every control listed above.

This audit inverts the direction: **extract every concrete detail out of the accepted prose first, then check the extraction against itself and against the ledgers.** The prose becomes the source of ground truth for the index; the ledgers become a thing to be tested, not the test.

The already-resolved Chapter 5-to-6 defect is the proof that this class of error occurs here: two accepted chapters carried mutually exclusive physical states and both sat in the controlling manuscript at once. It was found by a targeted read, not by any automated control. There is no reason to assume it was the only one.

## 2. Scope

### In scope

The 25 accepted prose files only. Every concrete, checkable assertion in them.

### Out of scope

- Prose quality, pacing, voice, and line editing. Those are closed (`51-`, `54-`, `55-`, `61-`).
- External specialist adjudication of real-world technical accuracy. That gate is separately waived and recorded (`52-`, `60-`); this audit checks *internal* consistency, not real-world plausibility.
- Production binaries, cover, metadata, retailer preview. Derived outputs; they follow the prose.
- Historical records, superseded drafts, one-shot scripts, and archived material. These may legitimately contain stale values and must not be "corrected."

### Explicitly not in scope for change

Accepted prose. This audit **produces findings, not edits**. Any prose change is a separate, author-approved action under the policy in §7.

## 3. Detail classes to be extracted

Nine classes. Each maps to a rule set in §5.

| # | Class | What gets extracted | Volume observed in survey |
|---|---|---|---|
| D1 | Clock and calendar | Every timestamp, date, day reference, duration, countdown value, elapsed-time claim | 285 timestamp occurrences, 219 distinct values |
| D2 | Named entities | People, ranks, titles, organizations, facilities, place names | ~40 recurring proper nouns above 30 occurrences |
| D3 | Designators and codes | `APX-DIR-0019`, `K-17`, `Payload 88`, `SIGMA-NORMALIZE-4`, `PCF-27`, `L3-7`, `COMP-04`, `0088`, checksum and cadence identifiers | Registry to be built |
| D4 | Physical space and movement | Rooms, routes, levels, doors, vehicles, distances, and every transit between them | Per-scene |
| D5 | Objects and custody | Who physically holds what, in every scene; the seven-package structure; seals, cases, cartridges, boards, bags | Per-scene |
| D6 | Injury and capability | Injury acquisition, symptom progression, and what each character can and cannot physically do afterward | Julie, Marcus, Elias primary |
| D7 | Knowledge state | What each character knows, when they learned it, and from whom | All named principals |
| D8 | Quantities | Counts, measurements, temperatures, money, durations stated in words | e.g. eleven civilians, five children, four seconds, 11.2-second cadence, ninth checksum, forty-three seconds |
| D9 | Surface continuity | Clothing, weather, light level, injuries visible, phone and battery state, vehicle state | Per-scene |

D7 and D5 are the two classes most likely to hold undetected defects, because neither can be checked by pattern matching and neither was extracted bottom-up in any prior pass.

D9 matters more than usual here because Chapter 5 runs continuously from 15:41 EDT through 04:51 EDT the following morning. Every light, visibility, fatigue, and exterior-darkness cue across that span has to hold together, and no existing control looks at it.

## 4. Method

### Phase 0 — Baseline and freeze verification

Re-run and record, so that findings are anchored to an exact manuscript state:

```bash
python3 tools/count_book1_words.py
python3 tools/validate_book1_publication_readiness.py
python3 -m unittest discover -s tools -p 'test_*.py'
```

Plus a fresh per-file SHA-256 comparison against `ACCEPTED_MANUSCRIPT.yaml`. Record the audit head commit. All findings cite this baseline.

**Exit:** baseline recorded, all checks green, head commit fixed.

### Phase 1 — Bottom-up extraction

Build a machine-readable detail index from the accepted prose. One record per extracted detail, each carrying: class (D1–D9), value, file, line, surrounding quote, and scene identifier.

Two complementary extractors:

1. **Mechanical** — a new tool, `tools/extract_book1_detail_index.py`, emitting `artifacts/book1-detail-index.json`. Handles D1, D2, D3, D8 by pattern: timestamps, dates, durations, capitalized tokens, designator formats, numerals, and spelled-out numbers. This is repeatable, diffable, and cheap to re-run after any future change.
2. **Reading** — a per-chapter scene card for D4, D5, D6, D7, D9, which cannot be pattern-matched. Each of the 25 files gets a card recording, per scene: participants present, location, entry and exit time, objects held by whom, injuries active, knowledge newly acquired by whom, and observable surface state on exit.

The scene cards are the expensive part and the part that actually finds things. They are the deliverable that Book 1 has never had.

**Exit:** `artifacts/book1-detail-index.json` plus 25 scene cards under `books/book-01/control/detail-audit/`.

### Phase 2 — Rule execution

Run the §5 rule sets against the index and the cards. Every rule produces either a clean result or a candidate finding with a citation.

**Exit:** raw candidate-finding list, unfiltered.

### Phase 3 — Adjudication

Every candidate is read in full context and classified into exactly one of:

| Class | Meaning | Default disposition |
|---|---|---|
| **CONTRADICTION** | Two accepted-prose statements cannot both be true | Escalate to author |
| **IMPOSSIBILITY** | A single statement is internally impossible (travel time, countdown arithmetic, capability ceiling) | Escalate to author |
| **LEDGER-STALE** | Prose is correct; a control document is wrong or out of date | Repair the control; no prose change |
| **UNDERSPECIFIED** | Not wrong, but a detail a reader could reasonably track and the text leaves ambiguous | Author judgment |
| **DELIBERATE** | Intended open thread or intended institutional misstatement | Confirm it is recorded in `24-thread-disposition-matrix.md`; no change |
| **NO ISSUE** | False positive | Record and close |

The DELIBERATE class matters here. Book 1 deliberately contains false statements — Apex's armed-saboteur and hostage classifications, Sterling's public accusations, the pre-correction official record. An auditor working bottom-up will flag these as contradictions. They must be separated from real defects, and the register that governs them is `07-public-narrative-ledger.md` and `24-thread-disposition-matrix.md`.

**Exit:** every candidate classified, with citation and reasoning.

### Phase 4 — Disposition

Findings are reported to the author with a recommendation. Nothing is applied to accepted prose without approval. See §7.

## 5. Rule sets

### Automatable (become permanent regression checks)

| Rule | Check |
|---|---|
| R1 | Every EDT/IST pair states exactly +09:30. The survey confirms the convention holds at the pairs sampled; the audit checks all of them. |
| R2 | Timestamps are non-decreasing within a scene and across chapters, allowing for declared day rollovers and explicitly marked flashbacks or replays. |
| R3 | Countdown sequences decrease monotonically and their deltas match elapsed wall-clock time. Chapters 8 and 9 carry long countdown runs; this is arithmetic and should be proven, not trusted. |
| R4 | Sub-second timestamps (`07:08:09.442`, `07:27:14.118`) are consistent every time the same event is restated in a later chapter. Chapters 12, 13, 14, 19, and 22 all re-cite predawn timestamps; each restatement must match its origin exactly. |
| R5 | Designator registry: each code appears in exactly one canonical form, everywhere. Flags `L3-7` vs `L3–7`, `APX-DIR-0019` vs `APX-DIR-19`, and similar drift. |
| R6 | Entity-name registry: near-miss spelling and casing variants of every recurring proper noun. |
| R7 | Quantity registry: every stated count and measurement, with all variants of the same fact grouped for comparison. |
| R8 | First-mention index: the first appearance of every proper noun and designator, which feeds the D7 knowledge review. |

### Judgment-only (per-chapter reading)

| Rule | Check |
|---|---|
| R9 | **Possession chain.** Every object has a continuous holder. An object cannot be used by someone who was not last recorded holding it. Priority targets: the sealed aluminum case, Elias's administrator-token board, the canvas tool bag, the signed recovery cartridge, the paper custody log, the PCF-27 module. |
| R10 | **Capability ceiling.** No character performs an action their recorded injuries preclude. Priority targets: Julie's right hand and wrist, Marcus's ribs and concussion monitoring, Elias's hip and index finger. |
| R11 | **Knowledge order.** No character acts on, references, or reasons from information before the text gives it to them. This is the single most common failure mode in a multi-POV thriller and the least covered by existing controls. |
| R12 | **Physical transit.** Every movement between locations is possible in the stated elapsed time, by the stated route, in the stated physical condition. |
| R13 | **Surface continuity.** Clothing, light, weather, vehicle, and device state persist correctly across scene and chapter boundaries. |
| R14 | **Proof-ceiling discipline.** The `00-readme.md` proof-category rule — registered authority, institutional custody, physical possession, physical operation, personal authentication, command, motive — is not silently violated by narration or dialogue. A lower category must never read as proving a higher one. |

R14 is the rule most specific to this book. The entire third act turns on what the evidence can and cannot prove, and a single loose line of narration can collapse a distinction the plot depends on.

## 6. Sequencing

Five batches, cut on act structure rather than evenly, so that each batch is a coherent stretch of story time.

| Batch | Files | Story span | Notes |
|---|---|---|---|
| B1 | Prologue, Ch 1–4 | Six years prior; Oct 13 morning to ~15:36 EDT | Establishes nearly every entity, designator, and quantity. Build the registries here. |
| B2 | Ch 5–9 | 15:41 EDT Oct 13 through 05:14:36 EDT Oct 14 | Highest risk. Overnight span, the repaired 5-to-6 seam, dense countdown arithmetic, three-person movement through a facility. |
| B3 | Ch 10–14 | 05:15 to 07:49 EDT Oct 14 | Densest timestamp region, heaviest sub-second cross-referencing, custody structure forms here. |
| B4 | Ch 15–19 | Oct 14 daytime | Custody, examination, and record-splitting; proof-ceiling discipline is critical. |
| B5 | Ch 20–24 | Oct 15–16 | Release mechanism, public correction, ending contract. Cross-check against `22-book-1-ending-contract.md` and `series/recurring-character-ledger.md`. |

Batches run in order. B1 must complete before the others, because it produces the registries every later batch checks against.

After all five: a **cross-batch pass** covering the checks no single batch can see — full-book knowledge ordering, the complete possession chain, cumulative injury progression, and the seven-package custody structure end to end.

## 7. Disposition policy

The manuscript is frozen. This audit does not change that, and does not assume permission to change it.

- **LEDGER-STALE findings** are repaired directly in the control documents. Controls are living records; keeping them accurate is maintenance, not a prose change.
- **CONTRADICTION and IMPOSSIBILITY findings** are reported with severity, exact citations, and a recommended minimal repair. **No accepted prose file is touched without explicit author approval.**
- Any approved prose change follows the existing policy in `control/README.md` in full: editorial exception record, author approval, updated per-file word count and SHA-256, updated total, complete revalidation, and a new publication-master freeze record. It also requires rebuilding the production package, because the current package is cleared against the current prose.
- **Historical records are never rewritten.** Files that document a past state legitimately contain superseded values.

The likeliest and most desirable outcome is that most findings are LEDGER-STALE or UNDERSPECIFIED and the frozen prose stands. The audit is worth running regardless, because the alternative is discovering a contradiction after retail upload.

## 8. Deliverables

| Artifact | Path |
|---|---|
| Detail index (machine-readable) | `artifacts/book1-detail-index.json` |
| Extraction tool | `tools/extract_book1_detail_index.py` |
| Automated rule checker | `tools/check_book1_detail_rules.py` |
| Per-chapter scene cards | `books/book-01/control/detail-audit/` (25 files) |
| Findings register | `books/book-01/control/71-detail-continuity-findings.md` |
| Final audit report and verdict | `books/book-01/control/72-detail-continuity-audit-report.md` |

The two tools are the durable output. After this audit, R1–R8 become a repeatable check that can be added to the existing GitHub workflows, so no future correction can silently reintroduce a clock, designator, or quantity drift.

## 9. Known items to resolve during the audit

Recorded now so they are not lost:

1. **Stated accepted-word totals differ across control documents.** `59-post-research-continuity-audit.md` states 105,144; the current manifest, `PROJECT_STATE.yaml`, and the validator all state 105,157. The difference is consistent with the copyedit that merged after that audit, and `59-` is a dated historical record that should retain its own value. Confirm this explanation and verify no *current-status* file still carries a superseded total.
2. **Chapter 5 carries the widest time span in the book**, 15:41 EDT to 04:51:06 EDT. It is also the chapter that was structurally repaired. It deserves the most careful single-file read in the audit.
3. **Timestamps in Chapters 20 and 21 run non-monotonically** on the surface (09:06, 06:54, 10:32, 06:41:18, 05:45, 07:00). These are almost certainly later-day scenes citing earlier predawn events, which is legitimate — but each citation must be verified against its origin timestamp under R4.
4. **Chapter 2 states 05:00 and 02:14 alongside 16:30.** Confirm each is correctly attributed to certification time, deployment attribution, and support commit respectively, per the accepted architecture in `repairs/chapter-05-to-06-continuity-repair/README.md`.

## 10. Effort and staging

Phase 0 and the mechanical half of Phase 1 are inexpensive and produce immediate signal — the registries alone will surface any designator or quantity drift within the first pass. The scene cards are the bulk of the work and are the reason the audit is worth doing.

Recommended staging: run Phase 0 and mechanical Phase 1 across the whole book first, review what the registries surface, and only then commit to the full scene-card pass. If the registries come back clean, that is real evidence the drafting was tighter than remembered, and the scene-card pass can be prioritized toward B2 and B3 rather than run exhaustively.

## 11. Approval gate

This plan changes nothing on its own. Execution begins only on author instruction, and §7 governs everything the execution is permitted to touch.
