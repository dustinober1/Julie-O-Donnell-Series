# Chapter 1 Narrative-Density Revision Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Revise Chapter 1 — *The Official Version* under Narrative House Style v2.1 so it reaches Marcus and the telemetry sooner, uses denser narrative outside pressure beats, and preserves every accepted canon fact and the Chapter 2 handoff.

**Architecture:** Keep the chapter’s existing two-location structure: Julie’s farm and Apex Building Three. Compress routine dialogue, travel recap, repeated access challenges, and low-pressure one-line paragraphs while preserving the farm’s honest-causality opening, Marcus’s moral admission, the access restrictions, Julie’s trauma response, and the final telemetry recognition.

**Tech Stack:** GitHub Markdown manuscript, GitHub connector, Narrative House Style v2.1, manual continuity and page-density validation.

## Global Constraints

- Repository: `dustinober1/Julie-O-Donnell-Series`.
- Branch: `main`.
- GitHub Markdown manuscript is the sole source of truth.
- Narrative House Style v2.1 controls dialogue function, narrative compression, isolated paragraphs, fragments, and page density.
- Do not imitate or closely emulate the recognizable prose of any living author.
- Preserve all accepted plot, chronology, evidence, knowledge, injury, technology, and chapter-ending facts.
- Chapter 1 remains one chapter; do not split the farm and Apex sections.
- Preserve the exact final line: `Six years later, the machine was lying in exactly the same voice.`
- Chapter 2 must still open with Julie trying to prove herself wrong inside Room 402B.

---

### Task 1: Establish the Chapter 1 revision baseline

**Files:**
- Read: `docs/Julie_ODonnell_Narrative_House_Style_v2_1.md`
- Read: `docs/Julie_ODonnell_Narrative_House_Style_v2.md`
- Read: `artifacts/book-01-chapter-revision-map.md`
- Read: `books/book-01/manuscript/prologue.md`
- Read: `books/book-01/manuscript/chapters/chapter-01.md`
- Read: `books/book-01/manuscript/chapters/chapter-02.md`

**Produces:** A locked checklist of facts and handoff conditions that the revised chapter must preserve.

- [ ] **Step 1:** Confirm repository and branch are exactly `dustinober1/Julie-O-Donnell-Series` and `main`.
- [ ] **Step 2:** Record the starting HEAD before manuscript edits.
- [ ] **Step 3:** Confirm Chapter 1’s controlling dramatic mission: Marcus persuades Julie to inspect the new Pakistan feed; Julie decides whether the same physical impossibility is recurring.
- [ ] **Step 4:** Lock the following facts: Marcus arrives alone; telemetry is sanitized; 11.2-second cadence; severe weather; Price suspended after requesting raw access; 99.8% confidence and brief 100% display; 16:30 source certification; 05:00 support-product commit; Apex-managed environment; plate-triggered access change; Room 402B supervised sandbox; export disabled; query mirroring enabled; continuous recording; phone and digital truck key surrendered; mechanical key retained.
- [ ] **Step 5:** Confirm Chapter 2 opens in Room 402B with the same feed, Marcus present, and Julie trying to prove herself wrong.

### Task 2: Revise Chapter 1 prose

**Files:**
- Modify: `books/book-01/manuscript/chapters/chapter-01.md`

**Consumes:** Task 1 canon and handoff checklist.

**Produces:** A complete revised Chapter 1 under House Style v2.1.

- [ ] **Step 1:** Compress the opening property inventory while preserving the failed fence, cause/effect/evidence motif, Julie’s preference for physical work, and the repeated calls.
- [ ] **Step 2:** Bring Marcus’s Suburban onto the page sooner while preserving Julie’s threat response, shotgun, and his solitary arrival.
- [ ] **Step 3:** Preserve the strongest Marcus–Julie conflict lines, including the six-year accusation, defensible-truth admission, and the lack of reconciliation.
- [ ] **Step 4:** Convert routine telemetry, review-cell, access-request, vehicle-security, and tracking questions into specific narrative where dialogue adds no resistance or character.
- [ ] **Step 5:** Keep Price’s suspension, the seven-minute Apex response, Marcus’s admission, the brief 100% display, and Julie’s decision to go as distinct pressure turns.
- [ ] **Step 6:** Compress the drive while preserving Julie’s four-second trauma response and the old Ford’s low-connectivity value.
- [ ] **Step 7:** Preserve the plate reader, access modification at 11:39, Sarah Chen’s institutional role, surrendered electronics, retained mechanical key, and Room 402B restrictions.
- [ ] **Step 8:** Compress repeated Apex-first/government-second observations after the controlling ownership fact is clear.
- [ ] **Step 9:** Preserve the official-version exchange only to the level needed to establish 99.8% confidence, degraded collection, contradictory ground reporting, and the validated-assessment clock.
- [ ] **Step 10:** End on the unchanged final telemetry recognition with no explanation afterward.
- [ ] **Step 11:** Commit the revised manuscript with message `Revise Chapter 1 for narrative density`.

### Task 3: Validate canon, continuity, and page density

**Files:**
- Read: revised `books/book-01/manuscript/chapters/chapter-01.md`
- Read: `books/book-01/manuscript/prologue.md`
- Read: `books/book-01/manuscript/chapters/chapter-02.md`

**Produces:** A verified revision record and count basis.

- [ ] **Step 1:** Confirm the Prologue references remain coherent: Fort Belvoir rain, Marcus’s `confusion` wording, Julie’s resignation, six-year separation, nightmares, and `analyst delay`.
- [ ] **Step 2:** Confirm Chapter 2 still begins with the same feed, room, camera, Marcus position, and 11.2-second pattern.
- [ ] **Step 3:** Confirm no reconciliation has been added between Julie and Marcus.
- [ ] **Step 4:** Confirm Price remains under suspended access review rather than detention or proven conspiracy.
- [ ] **Step 5:** Confirm the 100% display remains an anomaly, not proof of manipulation.
- [ ] **Step 6:** Confirm all access restrictions and electronic-custody facts remain unchanged.
- [ ] **Step 7:** Count revised words, physical Markdown lines, dialogue-start paragraphs, and isolated one-sentence paragraphs using the same practical basis used for the Prologue revision note.
- [ ] **Step 8:** Compare the revised chapter against the approximate 4,800-word planning baseline and record the limitations of that comparison.

### Task 4: Document the Chapter 1 revision

**Files:**
- Create: `artifacts/book-01-chapter-01-house-style-v2-1-revision-note.md`

**Consumes:** Task 3 verification and counts.

**Produces:** A permanent revision note.

- [ ] **Step 1:** Record starting HEAD, manuscript-revision commit, revision date, branch, and controlling style guide.
- [ ] **Step 2:** Record original approximate count, revised count, physical-line change, dialogue-start count, and isolated-paragraph count.
- [ ] **Step 3:** List major dialogue converted to narrative and major dialogue deliberately preserved.
- [ ] **Step 4:** List every protected technical, continuity, access, and custody fact.
- [ ] **Step 5:** Document Chapter 2 handoff validation and remaining risks.
- [ ] **Step 6:** Commit with message `Document Chapter 1 narrative-density revision`.

### Task 5: Update project tracking

**Files:**
- Modify: `PROJECT_STATE.yaml`
- Modify: `books/book-01/manuscript/STATUS.md`

**Consumes:** Accepted revised Chapter 1 and its revision note.

**Produces:** Current repository navigation and revision status.

- [ ] **Step 1:** Add Chapter 1 to the House Style v2.1 revised-chapters list.
- [ ] **Step 2:** Add the Chapter 1 revision-note path and mark Chapter 1 as revised in manuscript status.
- [ ] **Step 3:** Update approximate accepted-manuscript length using the documented Chapter 1 delta.
- [ ] **Step 4:** Set the next recommended revision to Chapter 2 — *The Poisoned Feed*.
- [ ] **Step 5:** Preserve Chapter 13’s drafted-but-unaccepted status and all unrelated project-state facts.
- [ ] **Step 6:** Commit tracking changes in independently reviewable commits.

### Task 6: Final verification

**Files:**
- Verify all files changed since the implementation baseline.

**Produces:** Final completion report.

- [ ] **Step 1:** Compare starting implementation HEAD to final HEAD and confirm only the intended manuscript, note, plan, and tracking files changed.
- [ ] **Step 2:** Re-fetch the revised Chapter 1 and verify the exact final line.
- [ ] **Step 3:** Re-fetch the revision note and confirm count and continuity claims match the committed manuscript.
- [ ] **Step 4:** Re-fetch `PROJECT_STATE.yaml` and `STATUS.md` to confirm v2.1 and revised-section tracking are correct.
- [ ] **Step 5:** Report starting and ending HEAD, commits, files changed, count deltas, validation performed, and remaining risks.