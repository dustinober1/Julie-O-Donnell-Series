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

### Task 1: Reconcile the canonical state — COMPLETE

**Files:**
- Modify: `books/book-01/control/README.md`
- Create: `books/book-01/control/51-publication-readiness-status.md`
- Modify: `README.md`

- [x] Replace stale 124,779-word and obsolete endpoint claims with the current accepted manifest state.
- [x] State explicitly that generated compilations and historical Word exports are noncanonical.
- [x] Record the publication gate as external specialist review, approved corrections, continuity validation, copyedit, proofread, and production export.
- [x] Verify active control files agree on title, chapter count, word count, ending, and open series threads through automated validation.

### Task 2: Strengthen automated canon validation — COMPLETE

**Files:**
- Modify: `tools/validate_book1_publication_readiness.py`
- Create: `tools/test_validate_book1_publication_readiness.py`
- Create: `tools/test_compile_book1_from_manifest.py`
- Create: `.github/workflows/book1-publication-readiness.yml`

- [x] Parse accepted titles, word counts, and hashes from the manifest.
- [x] Verify each file's actual word count and SHA-256 against the manifest.
- [x] Verify the manifest total equals the summed file totals.
- [x] Verify control-pack status does not contain stale accepted totals or obsolete endpoint claims.
- [x] Verify the final line and deliberate unresolved threads remain present.
- [x] Add fixture-driven tests for count drift, hash drift, stale control metadata, headings, final-line changes, and Chapter 25 creation.
- [x] Add CI to run tests, validation, diagnostics, manifest compilation, and final-line verification.

### Task 3: Create specialist review tracking — COMPLETE; EXTERNAL REVIEWS OPEN

**Files:**
- Modify: `books/book-01/control/50-specialist-review-brief.md`
- Create: `books/book-01/control/52-specialist-review-register.md`
- Create: `books/book-01/control/review-packets/README.md`
- Create seven specialist packet files.

- [x] Give each area an issue owner, status, review fields, and approval ceiling.
- [x] Require critical/material/minor/preference severity and the smallest story-preserving correction.
- [x] State that no review is complete until a named qualified reviewer supplies a dated deliverable.
- [x] Open one GitHub issue per specialist area: #70–#76.
- [ ] Obtain the seven external deliverables. **BLOCKED: requires named qualified human reviewers.**

### Task 4: Create continuity ledgers — COMPLETE BASELINE

**Files:**
- Create: `books/book-01/control/continuity/00-readme.md`
- Create: `01-master-timeline.md`
- Create: `02-evidence-custody-ledger.md`
- Create: `03-injury-ledger.md`
- Create: `04-knowledge-ledger.md`
- Create: `05-authority-ledger.md`
- Create: `06-technology-ledger.md`
- Create: `07-public-narrative-ledger.md`

- [x] Record controlling facts already established by the accepted manuscript.
- [x] Mark fields requiring revalidation after specialist corrections.
- [x] Preserve the difference between registered authority, institutional custody, physical possession, personal operation, command, and motive.
- [ ] Reconcile the ledgers against future accepted specialist corrections. **BLOCKED: no findings yet.**

### Task 5: Intake and adjudicate specialist findings — INFRASTRUCTURE COMPLETE

**Files:**
- Create: `books/book-01/control/53-specialist-findings-ledger.md`

- [x] Create fields for area, chapter, severity, explanation, smallest correction, downstream impact, decision, and status.
- [x] Define acceptance, modified acceptance, copyedit deferral, reconciliation, rejection, and content-lock reopening decisions.
- [ ] Enter and adjudicate findings. **BLOCKED: external findings not yet received.**

### Task 6: Apply approved technical corrections — BLOCKED

**Files:**
- Modify only affected accepted manuscript chapters and relevant control files.

- [ ] Correct military/SIGINT foundations first.
- [ ] Correct PKI and hardware-evidence mechanisms second.
- [ ] Correct facility, fire, and suppression mechanisms third.
- [ ] Correct Indian Army and artillery procedure fourth.
- [ ] Correct federal custody and legal procedure fifth.
- [ ] Correct injury capability and treatment last.
- [ ] Regenerate manifest counts and hashes after each approved correction set.

**Blocker:** Applying unreviewed technical changes would invent expert approval and could create new cross-domain errors.

### Task 7: Reconstruct continuity after technical corrections — BASELINE COMPLETE / FINAL PASS BLOCKED

- [x] Create baseline EDT/IST and local-clock timeline.
- [x] Create baseline evidence custody, seal, derivative, and source-original map.
- [x] Create baseline injury capability map.
- [x] Create baseline character knowledge and proof-ceiling map.
- [x] Create baseline institutional authority and public narrative maps.
- [ ] Reconcile all ledgers after technical corrections. **BLOCKED by Task 6.**

### Task 8: Tighten the late procedural act — AUDIT COMPLETE / PROSE EDIT BLOCKED

**Files:**
- Create: `books/book-01/control/54-late-act-compression-report.md`
- Create: `tools/analyze_book1_publication_style.py`

- [x] Identify repeated inventory, proof-ceiling, camera, visible-hands, clock, and objection patterns.
- [x] Protect the MPD handoff, board examination, K-17 local record, Hartwell production, signer custody exception, Price finding, construction/release split, Vance release, and aborted public overclaim.
- [x] Set a controlled 1,200–1,800-word preferred reduction rather than an unsafe quota.
- [ ] Apply the chapter edits and record before/after counts. **BLOCKED until legal, PKI, and provenance corrections stabilize the language.**

### Task 9: Differentiate dialogue voices and reduce cast load — DESIGN COMPLETE / PROSE EDIT BLOCKED

**Files:**
- Create: `books/book-01/control/55-character-voice-and-cast-report.md`

- [x] Define Julie's physical-cause/proof-limit voice.
- [x] Define Marcus's command/responsibility/access voice.
- [x] Define Elias's mechanism/consent/identity voice.
- [x] Define Sarah's category/order/procedure voice.
- [x] Define Grant's narrow-question/replication voice.
- [x] Define Ortiz's observable-scene/custody voice.
- [x] Define Sharma's terrain/soldiers/local-command voice.
- [x] Define role reminders and strict consolidation criteria.
- [ ] Apply dialogue-only changes. **BLOCKED until specialist terminology and compression stabilize.**

### Task 10: Strengthen Vance's institutional credibility — DEFERRED

- [x] Define the permitted addition: at most two brief references showing why competent officials valued Argus or Vance.
- [x] Prohibit villain monologue, personal backstory, original-constructor proof, and Sterling-command proof.
- [ ] Add the smallest approved passage. **DEFERRED until specialist corrections identify the safest early location and authentic terminology.**

### Task 11: Complete line/copyedit and production proof — CONTROLS COMPLETE / EXECUTION BLOCKED

**Files:**
- Create: `books/book-01/control/56-copyedit-style-sheet.md`
- Create: `books/book-01/control/57-production-proof-report.md`
- Create: `tools/compile_book1_from_manifest.py`

- [x] Create the full copyedit style sheet and proof-language rules.
- [x] Create print, EPUB, Word, Markdown, checksum, layout, and device-proof gates.
- [x] Create manifest-driven Markdown compiler with build-provenance sidecar.
- [ ] Apply final line/copyedit to accepted prose. **BLOCKED by technical corrections and continuity pass.**
- [ ] Generate final Word, EPUB, PDF, and Markdown production outputs. **BLOCKED by copyedit.**
- [ ] Complete human print/device proof. **BLOCKED by outputs.**

### Task 12: Final publication gate — STATUS CONTROL COMPLETE / APPROVAL BLOCKED

**Files:**
- Modify: `books/book-01/control/51-publication-readiness-status.md`
- Modify: `README.md`

- [x] Record completed infrastructure and active blockers.
- [x] Confirm the immediate crisis and Julie's Book 1 arc resolve while the original constructor and Sterling's personal command remain open.
- [x] Lock the final line in validator and control files.
- [ ] Confirm all seven specialist areas have named dated dispositions.
- [ ] Confirm all critical findings are fixed and material findings are fixed or intentionally accepted.
- [ ] Confirm validators pass against the post-correction final manifest.
- [ ] Mark publication readiness only after copyedit and production proof are complete.

## Current implementation verdict

All work that can be completed honestly before external specialist findings has been implemented on `agent/book1-publication-readiness`. Remaining unchecked tasks are not deferred for convenience: they require evidence that does not yet exist—qualified external reviews—or depend sequentially on those reviews. The branch must remain a draft publication-readiness program, not a claim that the book is already publication approved.
