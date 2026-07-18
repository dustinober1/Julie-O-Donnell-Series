# Book 1 Developmental Revision Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a publication-ready 105,000–110,000-word revision of *Veridrift* that fixes all objective blockers, clarifies the poisoned-feed causality, rebalances character agency, and compresses the procedural final act while preserving the Book 1 series-opening resolution.

**Architecture:** Work on `agent/book1-developmental-revision` in gated passes. Objective defects and validation come first; developmental edits follow in chapter groups; metadata and accepted-manuscript controls update only after the prose passes verification. The prologue and current Chapter 1 remain unchanged unless validation finds an objective defect.

**Tech Stack:** UTF-8 Markdown manuscript files, YAML inventory/control files, Python validation utilities, GitHub feature branch and draft pull request.

## Global Constraints

- Current `main` accepted manuscript is the sole prose baseline.
- Preserve the prologue and current Chapter 1 publication-voice pass.
- Preserve the immediate crisis outcome, core evidence chain, principal set pieces, Marcus resolution, Elias boundary, Julie's independent-practice decision, and centered-bubble final image.
- Treat the book as a series opener; keep only one clean conspiracy carryover.
- Final accepted word count must be 105,000–110,000 words by the repository's whitespace-token method.
- Do not claim that external specialist review has occurred.
- Commit each independently reviewable pass.

---

### Task 1: Add publication-readiness validation

**Files:**
- Create: `tools/validate_book1_publication_readiness.py`
- Modify: none

**Produces:** A single command that checks accepted-file presence, heading syntax, metatext, duplicate thermostat markers, Markdown display artifacts, calendar/timestamp defects, final-line timestamp leakage, and total accepted word count.

- [ ] **Step 1:** Fetch `books/book-01/ACCEPTED_MANUSCRIPT.yaml` and reuse its accepted-file inventory and whitespace word-count definition.
- [ ] **Step 2:** Implement exact failures for these strings or patterns: `Chapter 11`, `scene card begun in Chapter 14`, `end of Chapter 21`, `Chapter 21 comparison`, `during Chapter 21`, `Chapter 22 had ended`, `On July thirteenth`, a heading joined to preceding prose, chapter headings using a hyphen instead of an em dash, and backticks surrounding uppercase system fields.
- [ ] **Step 3:** Count occurrences of `0088 / COMP-04 / CORE-01` in Chapters 4–5 and fail if the same full transmission scene remains duplicated.
- [ ] **Step 4:** Validate that the final manuscript ends with `The bubble stayed centered.` and that the final farm scene contains no exact clock timestamp.
- [ ] **Step 5:** Fail if accepted words are outside 105,000–110,000 after the revision; allow an explicit `--pre-revision` mode to report rather than fail during intermediate work.
- [ ] **Step 6:** Commit as `test: add Book 1 publication-readiness validator`.

### Task 2: Remove objective publication blockers

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-04.md`
- Modify: `books/book-01/manuscript/chapters/chapter-05.md`
- Modify: `books/book-01/manuscript/chapters/chapter-13.md`
- Modify: `books/book-01/manuscript/chapters/chapter-14.md`
- Modify: `books/book-01/manuscript/chapters/chapter-17.md`
- Modify: `books/book-01/manuscript/chapters/chapter-21.md`
- Modify: `books/book-01/manuscript/chapters/chapter-22.md`
- Modify: `books/book-01/manuscript/chapters/chapter-23.md`
- Modify: `books/book-01/manuscript/chapters/chapter-24.md`

- [ ] **Step 1:** Remove one duplicated Elias thermostat transmission, retaining a single complete transmission and converting any later reference into a brief consequence or acknowledgment.
- [ ] **Step 2:** Separate Chapter 13's heading from the preceding sentence.
- [ ] **Step 3:** Replace every in-world chapter/scene-card reference with story-world referents such as `the earlier intake`, `the comparison record`, or `the restraint position`.
- [ ] **Step 4:** Change the July report date to October and repair Chapter 23/24 timestamp ordering.
- [ ] **Step 5:** Standardize all affected chapter headings to `# Chapter N — Title`, remove leading spaces from scene headings, and remove backticks from system displays.
- [ ] **Step 6:** Run the validator in `--pre-revision` mode; all blocker checks must pass even though word count still exceeds target.
- [ ] **Step 7:** Commit as `fix: remove Book 1 publication blockers`.

### Task 3: Clarify the poisoned-feed mechanism and institutional setup

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-02.md`
- Modify: `books/book-01/manuscript/chapters/chapter-03.md`
- Modify: `books/book-01/manuscript/chapters/chapter-05.md`
- Modify: `books/book-01/manuscript/chapters/chapter-08.md`
- Modify: `books/book-01/manuscript/chapters/chapter-10.md`

- [ ] **Step 1:** In Chapter 2, add compact grounding for the classified bilateral pilot and Apex's delegated contractor authority without interrupting Julie's analysis.
- [ ] **Step 2:** In Chapters 2 and 5, distinguish messy Revision Eight from the post-archive derivative.
- [ ] **Step 3:** Make `SIGMA-NORMALIZE-4` the mechanism that flattens modeled irregularities, repeats reconstructed structure, and suppresses conflicting observations.
- [ ] **Step 4:** Replace any interface that states a complete thematic conclusion with raw lineage/event fields that characters must interpret.
- [ ] **Step 5:** Preserve the eleven-point-two-second interval, 0.07 percent deviation, impossible granite path, and all downstream crisis outcomes.
- [ ] **Step 6:** Commit as `edit: clarify Payload 88 deployment causality`.

### Task 4: Rebalance Julie, Elias, Sarah, and Vance

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-02.md`
- Modify: `books/book-01/manuscript/chapters/chapter-04.md`
- Modify: `books/book-01/manuscript/chapters/chapter-05.md`
- Modify: `books/book-01/manuscript/chapters/chapter-06.md`
- Modify: `books/book-01/manuscript/chapters/chapter-08.md`
- Modify: `books/book-01/manuscript/chapters/chapter-09.md`
- Modify: `books/book-01/manuscript/chapters/chapter-15.md`

- [ ] **Step 1:** Give Elias one ordinary family obligation before detention and one later reference to the personal cost of the public accusation.
- [ ] **Step 2:** Seed Sarah's integrity by showing her record Vance's restriction, resist premature sabotage language, and preserve a conflicting directive.
- [ ] **Step 3:** Revise Vance's Chapter 5 interview so he never explicitly confesses to manufacturing a controlled crisis; his strategic rationale remains inferable from defensible language and evidence.
- [ ] **Step 4:** During Chapter 8 reconciliation, let Julie choose an initially defensible but overbroad boundary that temporarily excludes a genuine K-17 observation. Elias catches it; Julie corrects the record and owns the limitation.
- [ ] **Step 5:** In Chapter 15, let Sarah's preserved record correct Julie's earlier judgment and let another professional originate a safeguard Julie would otherwise have supplied.
- [ ] **Step 6:** Commit as `edit: rebalance character agency and culpability`.

### Task 5: Tighten Chapters 4–14

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-04.md` through `chapter-14.md`

- [ ] **Step 1:** Cut 2,000–3,000 words from Chapters 4–5 by shortening the first failed approach, surveillance interval, motel/cutout setup repetition, and duplicated explanations.
- [ ] **Step 2:** Preserve Chapters 6–9's set pieces but trim repeated gate mechanics, countdown restatement, injury inventory, and proof-ceiling after-sentences.
- [ ] **Step 3:** Cut 2,000–3,000 words from Chapters 10–14 by compressing garage observation, repeated handling markers, and repeated explanations of what each fact does not prove.
- [ ] **Step 4:** Seed Northbridge/Sterling and the classified bilateral arrangement before they become a new conspiracy layer.
- [ ] **Step 5:** Add one concise line establishing Ortiz's relevant evidence/federal-liaison background when he enters.
- [ ] **Step 6:** Preserve every plot-bearing identifier and evidence object required by later chapters.
- [ ] **Step 7:** Commit as `edit: tighten Book 1 pursuit and Hartwell acts`.

### Task 6: Rebuild the final investigation across multiple days

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-15.md` through `chapter-23.md`

- [ ] **Step 1:** Establish October 13 as the apprehension and emergency-custody day.
- [ ] **Step 2:** Move Chapter 17's first independent examination and Chapter 18's Arjun authentication to October 14.
- [ ] **Step 3:** Move signer custody, borrowed-identity comparison, Vance's later release, and public correction to October 15.
- [ ] **Step 4:** Remove redundant exact times that invite unrealistic minute-by-minute auditing; retain times only when they control evidence order.
- [ ] **Step 5:** Compress Chapters 16–17 into a continuous custody-to-examination escalation while retaining both chapter files.
- [ ] **Step 6:** Compress Chapters 19–20 into one signer-custody/authority-chain discovery and Chapters 21–22 into one borrowed-identity/release comparison.
- [ ] **Step 7:** Reduce Chapter 23 to the failed broad correction, the three bounded releases, and immediate public consequence.
- [ ] **Step 8:** Remove or role-label nonessential late officials; retain only names required for later responsibility or series continuity.
- [ ] **Step 9:** Remove full SHA-256 strings except one abbreviated illustrative value.
- [ ] **Step 10:** Cut 10,000–13,000 words from Chapters 15–23 without removing the seven-object separation, board contradiction, Arjun independence, federal receiving authority, office signer custody, Price borrowed identity, Vance later release, or bounded correction.
- [ ] **Step 11:** Commit as `edit: compress and retime Book 1 final investigation`.

### Task 7: Tighten Chapter 24 and the series carryover

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-24.md`
- Modify: `series/recurring-character-ledger.md`
- Modify: `books/book-01/control/24-thread-disposition-matrix.md`

- [ ] **Step 1:** Move Chapter 24 to October 16.
- [ ] **Step 2:** Retain named release authority, physician-controlled treatment, Marcus's correction, Julie's refusal to equate correction with forgiveness, Elias's contact boundary, independent work decision, neighbor assistance, and centered bubble.
- [ ] **Step 3:** Remove repeated package status summaries, separate status reports for every minor official, and repeated legal language established in Chapters 19–23.
- [ ] **Step 4:** Reduce Julie's terms of work to three or four governing principles.
- [ ] **Step 5:** Remove the exact final timestamp and end exactly on `The bubble stayed centered.`
- [ ] **Step 6:** Compress the carryover list to the original 02:14 human direction and Sterling's personal knowledge/command.
- [ ] **Step 7:** Cut 700–1,000 words.
- [ ] **Step 8:** Commit as `edit: sharpen Book 1 resolution and carryover`.

### Task 8: Perform the manuscript-wide rhythm and voice pass

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-02.md` through `chapter-24.md`

- [ ] **Step 1:** Search every chapter for repeated `Not X. Not Y. Z.` and `That did not prove X. It proved Y.` constructions.
- [ ] **Step 2:** Keep only the strongest 20–30 percent of those rhetorical patterns.
- [ ] **Step 3:** Combine routine one-sentence paragraphs into fuller units, especially in Chapters 13–23.
- [ ] **Step 4:** Preserve short isolated paragraphs for countdowns, reversals, and emotional decisions.
- [ ] **Step 5:** Differentiate dialogue according to the design vocabulary for Julie, Marcus, Elias, Sharma, Sarah, Ortiz, Grant, and Alvarez.
- [ ] **Step 6:** Remove explanatory after-sentences when the displayed evidence or dialogue already carries the inference.
- [ ] **Step 7:** Commit as `edit: complete Book 1 publication voice pass`.

### Task 9: Create the specialist-review brief

**Files:**
- Create: `books/book-01/control/50-specialist-review-brief.md`

- [ ] **Step 1:** List the exact scenes and questions for SIGINT/ELINT review.
- [ ] **Step 2:** List the prologue strike-chain questions for UAS targeting/JAG review.
- [ ] **Step 3:** List Building Three fire, clean-agent, access, and contractor-authority questions.
- [ ] **Step 4:** List PKI/token, evidence-custody, and multi-day federal investigation questions.
- [ ] **Step 5:** List Indian Army/artillery, Northern Command, Line of Control, and bilateral-integration questions.
- [ ] **Step 6:** Mark each item `UNREVIEWED` rather than implying specialist approval.
- [ ] **Step 7:** Commit as `docs: add Book 1 specialist review brief`.

### Task 10: Update accepted-manuscript controls and verify

**Files:**
- Modify: `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
- Modify: `README.md`
- Modify: `PROJECT_STATE.yaml`
- Modify: `books/book-01/manuscript/STATUS.md`
- Modify: `books/book-01/control/00-overview.md`
- Modify: `books/book-01/control/16-chapter-by-chapter-status-record.md`
- Modify: materially affected chapter acceptance/control records

- [ ] **Step 1:** Recount accepted words using the exact whitespace-token method.
- [ ] **Step 2:** Update the endpoint to October 16 at Julie's farm without an exact final second.
- [ ] **Step 3:** Record that the manuscript is developmentally revised but still awaits external specialist review, copyediting, and proofreading.
- [ ] **Step 4:** Run all existing Book 1 validators plus `python tools/validate_book1_publication_readiness.py`.
- [ ] **Step 5:** Confirm total accepted words are 105,000–110,000 and every blocker check passes.
- [ ] **Step 6:** Compile the accepted files in manifest order and inspect every chapter boundary.
- [ ] **Step 7:** Commit as `chore: finalize Book 1 developmental revision controls`.

### Task 11: Review and publish the branch

**Files:**
- Review all branch changes against `main`.

- [ ] **Step 1:** Compare `agent/book1-developmental-revision` against `main` and inspect per-file word-count changes.
- [ ] **Step 2:** Verify no prologue or Chapter 1 prose changes occurred.
- [ ] **Step 3:** Verify all required plot-bearing evidence and identifiers remain.
- [ ] **Step 4:** Run the publication-readiness validator one final time.
- [ ] **Step 5:** Open a draft pull request titled `Revise Veridrift for publication readiness` with before/after word counts, structural summary, validation results, and unresolved specialist-review items.
