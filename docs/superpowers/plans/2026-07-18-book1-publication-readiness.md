# Book 1 Publication Readiness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move *Veridrift* from developmentally revised to a controlled publication candidate without changing the locked story, ending, or deliberate series carryovers.

**Architecture:** `books/book-01/ACCEPTED_MANUSCRIPT.yaml` remains the sole canonical prose inventory. Work proceeds through source reconciliation, specialist review intake, approved corrections, continuity reconstruction, targeted compression, line/copyedit, and production validation. Every change is made on a review branch and must preserve source ownership, proof limits, evidence chronology, and the final line.

**Tech Stack:** Markdown manuscript files, YAML canon manifest, Python validators, GitHub issues and pull requests.

## Global Constraints

- Canon is the prologue plus Chapters 1–24 listed in `books/book-01/ACCEPTED_MANUSCRIPT.yaml`.
- Accepted baseline is 105,081 words before publication-readiness corrections.
- No Chapter 25 may be created.
- Plot, chapter order, POV order, timeline outcomes, clues, evidence, technology functions, dialogue meaning, and ending are content locked except where a critical specialist correction requires the smallest possible repair.
- Preserve the eleven-point-two-second interval, environmental deviation finding, impossible path through granite, Payload 88, APX-DIR-0019, K-17, no-fire outcome, Vance's later authenticated release, unresolved original constructor, unresolved Sterling personal command, Julie's terms of work, Marcus's incomplete correction, Elias's consent boundary, and the final line `The bubble stayed centered.`
- External specialist approval may never be invented or inferred. Unreviewed areas remain publication blockers until a qualified reviewer signs off.

---

### Task 1: Reconcile the canonical state

**Files:**
- Modify: `books/book-01/control/README.md`
- Modify: `books/book-01/ACCEPTED_MANUSCRIPT.yaml` only if generated hashes or counts change
- Create: `books/book-01/control/51-publication-readiness-status.md`
- Modify: `README.md` if repository status changes

- [ ] Replace stale 124,779-word and obsolete endpoint claims with the current accepted manifest state.
- [ ] State explicitly that generated compilations and historical Word exports are noncanonical.
- [ ] Record the publication gate as external specialist review, approved corrections, continuity validation, copyedit, proofread, and production export.
- [ ] Verify all active control files agree on title, chapter count, word count, ending, and open series threads.

### Task 2: Strengthen automated canon validation

**Files:**
- Modify: `tools/validate_book1_publication_readiness.py`
- Create: `tools/test_validate_book1_publication_readiness.py`

- [ ] Parse accepted titles, word counts, and hashes from the manifest.
- [ ] Verify each file's actual word count and SHA-256 against the manifest.
- [ ] Verify the manifest total equals the summed file totals.
- [ ] Verify control-pack status does not contain stale accepted totals or obsolete endpoint claims.
- [ ] Verify the final line and deliberate unresolved threads remain present.
- [ ] Add fixture-driven tests for count drift, hash drift, stale control metadata, missing files, heading errors, and final-line changes.

### Task 3: Create specialist review tracking

**Files:**
- Modify: `books/book-01/control/50-specialist-review-brief.md`
- Create: `books/book-01/control/52-specialist-review-register.md`
- Create: `books/book-01/control/review-packets/README.md`
- Create seven review packet files for SIGINT, targeting/JAG, facility/fire, PKI/forensics, federal legal process, Indian Army/South Asia, and trauma medicine.

- [ ] Give each area an owner, status, review date, findings count, and approval ceiling.
- [ ] Require critical/material/minor/preference severity and the smallest story-preserving correction.
- [ ] State that no review is complete until a named qualified reviewer supplies a dated deliverable.
- [ ] Open one GitHub issue per specialist area.

### Task 4: Create continuity ledgers

**Files:**
- Create: `books/book-01/control/continuity/00-readme.md`
- Create: `01-master-timeline.md`
- Create: `02-evidence-custody-ledger.md`
- Create: `03-injury-ledger.md`
- Create: `04-knowledge-ledger.md`
- Create: `05-authority-ledger.md`
- Create: `06-technology-ledger.md`
- Create: `07-public-narrative-ledger.md`

- [ ] Record the controlling facts already established by the accepted manuscript.
- [ ] Mark every field that must be revalidated after specialist corrections.
- [ ] Preserve the difference between registered authority, physical possession, personal operation, command, and motive.

### Task 5: Intake and adjudicate specialist findings

**Files:**
- Create: `books/book-01/control/53-specialist-findings-ledger.md`

- [ ] Enter every finding with area, chapter, severity, explanation, smallest correction, downstream impact, decision, and status.
- [ ] Accept critical findings unless disproved by stronger evidence.
- [ ] Accept material corrections when they preserve the locked story.
- [ ] Batch minor terminology corrections into copyedit.
- [ ] Reject unsupported preference edits.

### Task 6: Apply approved technical corrections

**Files:**
- Modify only affected accepted manuscript chapters and relevant control files.

- [ ] Correct military/SIGINT foundations first.
- [ ] Correct PKI and hardware-evidence mechanisms second.
- [ ] Correct facility, fire, and suppression mechanisms third.
- [ ] Correct Indian Army and artillery procedure fourth.
- [ ] Correct federal custody and legal procedure fifth.
- [ ] Correct injury capability and treatment last.
- [ ] Regenerate manifest counts and hashes after each approved correction set.

### Task 7: Reconstruct continuity after technical corrections

**Files:**
- Modify all continuity ledgers.
- Modify: `tools/validate_book1_publication_readiness.py`

- [ ] Reconcile EDT/IST and all local clock offsets.
- [ ] Reconcile evidence custody, seal state, derivatives, and original-source location.
- [ ] Reconcile injuries and physical capability chapter by chapter.
- [ ] Reconcile character knowledge and proof ceilings.
- [ ] Reconcile institutional authority and public narrative chronology.

### Task 8: Tighten the late procedural act

**Files:**
- Modify as necessary: Chapters 15–23.
- Create: `books/book-01/control/54-late-act-compression-report.md`

- [ ] Remove repeated full inventories after common custody is stable.
- [ ] Reduce repeated explanations of registered authority versus physical possession.
- [ ] Reduce repeated camera, visible-hands, and clock protocol after the procedure is established.
- [ ] Preserve the MPD handoff, board examination, K-17 local record, Hartwell production, signer custody exception, Price finding, construction/release split, Vance release, and aborted public overclaim.
- [ ] Record before/after word counts and every retained story function.

### Task 9: Differentiate dialogue voices and reduce cast load

**Files:**
- Modify affected dialogue only.
- Create: `books/book-01/control/55-character-voice-and-cast-report.md`

- [ ] Keep Julie grounded in physical cause and proof limits.
- [ ] Keep Marcus grounded in command, responsibility, and access.
- [ ] Keep Elias grounded in mechanisms, fear, consent, and identity ownership.
- [ ] Keep Sarah grounded in categories, order, and defensible procedure.
- [ ] Keep Grant grounded in narrow questions and replicable method.
- [ ] Keep Ortiz grounded in observable scene facts and custody.
- [ ] Keep Sharma grounded in terrain, soldiers, and local command.
- [ ] Add role reminders for late-returning secondary characters and merge only roles with no distinct story function.

### Task 10: Strengthen Vance's institutional credibility

**Files:**
- Modify the smallest suitable early chapter passage.

- [ ] Add no more than two brief references showing why competent officials considered Argus or Vance valuable before the crisis.
- [ ] Do not add a villain monologue, personal backstory, original-constructor proof, or Sterling-command proof.

### Task 11: Complete line/copyedit and production proof

**Files:**
- Modify accepted manuscript files.
- Create: `books/book-01/control/56-copyedit-style-sheet.md`
- Create: `books/book-01/control/57-production-proof-report.md`

- [ ] Remove remaining repetitive AI cadence and excessive isolated beats.
- [ ] Standardize ranks, agencies, time notation, serials, headings, system displays, punctuation, and spelling.
- [ ] Generate Word, EPUB, PDF, and Markdown review outputs from the accepted inventory.
- [ ] Verify print layout, EPUB reflow, headings, scene breaks, and final line.
- [ ] Feed every production correction back into canonical source files before regenerating outputs.

### Task 12: Final publication gate

**Files:**
- Modify: `books/book-01/control/51-publication-readiness-status.md`
- Modify: `README.md`

- [ ] Confirm all seven specialist areas have named dated dispositions.
- [ ] Confirm all critical findings are fixed and material findings are fixed or intentionally accepted.
- [ ] Confirm validators pass against the final manifest.
- [ ] Confirm the immediate crisis and Julie's Book 1 arc are resolved while the original constructor and Sterling's personal command remain open.
- [ ] Confirm the manuscript still ends with `The bubble stayed centered.`
- [ ] Mark publication readiness only after copyedit and production proof are complete.
