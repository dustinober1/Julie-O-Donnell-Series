# House Style v2.2 Line-Density Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Narrative House Style v2.2 and apply a second line-density pass to Chapters 1 and 2 without altering canon, evidence strength, continuity, or crisis rhythm.

**Architecture:** Treat the style supplement, Chapter 1, Chapter 2, and repository tracking as four independently reviewable units. Revise quiet and explanatory passages toward denser close-third narrative while preserving direct dialogue and isolated paragraphs where wording, authority, countdown, or irreversible action creates suspense.

**Tech Stack:** GitHub Markdown manuscript, YAML project tracking, GitHub contents API, manual continuity and page-shape validation.

## Global Constraints

- Work only in `dustinober1/Julie-O-Donnell-Series` on `main`.
- GitHub Markdown remains the sole manuscript source of truth.
- Preserve the current Chapter 3 design commit and do not revise Chapter 3 prose.
- House Style v2.0 remains the complete base guide; v2.1 and v2.2 are progressively more specific supplements.
- Do not imitate or closely emulate a living author.
- Do not change plot, chronology, evidence, custody, injuries, knowledge boundaries, technology rules, or accepted endings.
- Prioritize 10–18 percent physical-line reduction and 3–7 percent word reduction per chapter, subordinate to dramatic clarity.

---

### Task 1: Add the v2.2 line-density supplement

**Files:**
- Create: `docs/Julie_ODonnell_Narrative_House_Style_v2_2.md`

**Consumes:**
- `docs/Julie_ODonnell_Narrative_House_Style_v2.md`
- `docs/Julie_ODonnell_Narrative_House_Style_v2_1.md`
- approved design at `docs/superpowers/specs/2026-07-12-house-style-v2-2-line-density-design.md`

**Produces:**
- controlling rules for dialogue-chain review, indirect dialogue, screen-field density, paragraph joining, and second-pass validation.

- [ ] **Step 1: Draft the supplement**

Include exact sections for authority, dialogue chains, question-to-exposition conversion, indirect dialogue, screen fields, paragraph joining, crisis exceptions, quantitative audits, and Chapter 1–2 calibration.

- [ ] **Step 2: Verify authority language**

Confirm the supplement states that accepted manuscript and canon controls outrank craft guidance and that v2.0/v2.1 remain active except where v2.2 is more specific.

- [ ] **Step 3: Commit**

Commit message:

```text
Add Julie O'Donnell house style v2.2
```

### Task 2: Apply the Chapter 1 second pass

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-01.md`
- Create: `artifacts/book-01-chapter-01-house-style-v2-2-line-density-revision-note.md`

**Consumes:**
- revised Prologue
- current Chapter 1
- current Chapter 2 opening
- v2.1 Chapter 1 revision note
- v2.2 supplement

**Produces:**
- denser Chapter 1 with unchanged plot and handoff.

- [ ] **Step 1: Record baseline**

Record current Chapter 1 word count, physical lines, dialogue-start paragraphs, and isolated one-sentence paragraphs from the v2.1 note.

- [ ] **Step 2: Revise farm and Marcus arrival**

Consolidate low-pressure maintenance, phone, vehicle, and approach paragraphs while preserving the honest-causality opening and Marcus arriving alone.

- [ ] **Step 3: Revise telemetry and decision dialogue**

Retain relationship wounds and consequential challenges. Convert routine calibration, review-cell, tracking, and access answers into close-third narrative.

- [ ] **Step 4: Revise Reston and Room 402B**

Compress visitor-lobby small talk, repeated corporate-control observations, and procedural dialogue after the 11:39 profile establishes Vance’s authority. Preserve phone/fob custody, mechanical key, exact access fields, and final line.

- [ ] **Step 5: Validate boundaries and canon**

Confirm the revised Prologue still supports the opening and Chapter 2 can still begin in Room 402B with Julie trying to prove herself wrong.

- [ ] **Step 6: Count and document**

Create the v2.2 Chapter 1 revision note with exact second-pass counts, dialogue deliberately retained, material converted to narrative, canon checks, and remaining risks.

- [ ] **Step 7: Commit manuscript and note separately**

Commit messages:

```text
Apply Chapter 1 line-density second pass
Document Chapter 1 v2.2 line-density revision
```

### Task 3: Apply the Chapter 2 second pass

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-02.md`
- Create: `artifacts/book-01-chapter-02-house-style-v2-2-line-density-revision-note.md`

**Consumes:**
- revised Chapter 1 ending
- current Chapter 2
- Chapter 3 opening
- v2.1 Chapter 2 revision note
- v2.2 supplement

**Produces:**
- denser Chapter 2 with preserved parallel POV architecture and exact 85-percent handoff.

- [ ] **Step 1: Record baseline**

Use the v2.1 Chapter 2 note for current word, line, dialogue-start, and isolated-paragraph counts.

- [ ] **Step 2: Consolidate Julie’s investigation**

Compress the Price call, archive-authority argument, authorship similarity list, ninth-checksum dialogue, and routine screen fields after each controlling fact is established.

- [ ] **Step 3: Consolidate Elias’s discovery**

Compress Package 88 development history and channel-choice analysis. Preserve the three safeguards, production state, 02:14 false authorization, APX-DIR-0019, Keller confrontation, memory-board concealment, and unresolved 91-percent copy.

- [ ] **Step 4: Protect containment rhythm**

Keep the 29-to-85-percent sequence visually fast. Remove only commentary or dialogue that repeats a visible state without changing action.

- [ ] **Step 5: Validate boundaries and canon**

Confirm the Chapter 1 opening state and Chapter 3 deadbolt/85-percent opening state require no repair.

- [ ] **Step 6: Count and document**

Create the v2.2 Chapter 2 revision note with exact second-pass counts, preserved dialogue, compressed material, canon checks, and remaining risks.

- [ ] **Step 7: Commit manuscript and note separately**

Commit messages:

```text
Apply Chapter 2 line-density second pass
Document Chapter 2 v2.2 line-density revision
```

### Task 4: Update repository tracking

**Files:**
- Modify: `PROJECT_STATE.yaml`
- Modify: `books/book-01/manuscript/STATUS.md`

**Consumes:**
- final Chapter 1 and 2 counts
- v2.2 guide and revision-note paths

**Produces:**
- accurate style version, revision ledger, approximate accepted-manuscript total, and next recommended action.

- [ ] **Step 1: Update project state**

Set style version to 2.2, add guide/supplement relationships, record Chapters 1 and 2 as receiving v2.2 second passes, add both note paths, and update the approximate accepted-manuscript total.

- [ ] **Step 2: Update manuscript status**

Record the v2.2 craft control and second-pass completion while preserving Chapter 13 draft/not-accepted status and the existing Chapter 3 design.

- [ ] **Step 3: Set next action**

Keep Chapter 3 as the next manuscript revision target, now under v2.2 line-density rules.

- [ ] **Step 4: Commit**

Commit messages:

```text
Update project state for House Style v2.2
Update manuscript status for House Style v2.2
```

### Task 5: Final verification

**Files:**
- Verify all files changed since the implementation-plan commit.

- [ ] **Step 1: Compare commits**

Confirm only the v2.2 guide, Chapters 1–2, two revision notes, project state, and manuscript status changed.

- [ ] **Step 2: Verify exact boundaries**

Confirm Chapter 1 retains its exact final line and Chapter 2 retains its exact final two lines.

- [ ] **Step 3: Verify canon checklist**

Recheck every locked fact in the two v2.1 revision notes.

- [ ] **Step 4: Verify line-density outcome**

Confirm both chapters reduced physical lines more than words and that action/countdown sections retained visual spacing.

- [ ] **Step 5: Report final HEAD and deltas**

Report starting and ending HEAD, commits, file list, count changes, validation performed, and remaining risks.
