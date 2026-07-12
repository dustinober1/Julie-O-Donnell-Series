# Book 1 Repository Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove repository ambiguity while preserving accepted prose and preparing Book 1 for a controlled 100,000–125,000-word completion.

**Architecture:** Separate accepted prose, drafts, book controls, series controls, and archive provenance. Use `PROJECT_STATE.yaml` for production status and `ACCEPTED_MANUSCRIPT.yaml` for accepted inventory. Move Chapter 13 by reusing its existing Git blob so its prose is unchanged.

**Tech Stack:** GitHub Markdown, YAML, Git tree/blob/commit APIs, repository history.

## Global Constraints

- Accepted prose must not change.
- Chapter 13 must remain unaccepted.
- Chapter 13 prose must move byte-for-byte from manuscript to drafts.
- Accepted word count remains 61,118.
- Book target remains 100,000–125,000 words with a 112,500-word planning target.
- The physical custodian of SSO-NS-004 remains unresolved.
- Chapter 14 prose must not begin before the Chapter 13 acceptance decision.
- Private external-document URLs and the Word binary must not enter the public repository.

---

### Task 1: Establish authority files

**Files:**
- Create: `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
- Modify: `PROJECT_STATE.yaml`
- Modify: `README.md`

**Produces:** One accepted inventory and one production-status authority.

- [x] **Step 1:** Define the accepted Prologue and Chapters 1–12 in the manifest.
- [x] **Step 2:** Record 61,118 accepted words and the Chapter 12 endpoint.
- [x] **Step 3:** Record Chapter 13 as a complete unaccepted draft.
- [x] **Step 4:** Point the root README to the authoritative files.

### Task 2: Separate draft prose from accepted prose

**Files:**
- Create: `books/book-01/drafts/README.md`
- Move unchanged blob: `books/book-01/manuscript/chapters/chapter-13.md` → `books/book-01/drafts/chapter-13.md`
- Modify: `books/book-01/manuscript/README.md`
- Modify: `books/book-01/manuscript/STATUS.md`
- Modify: `books/book-01/manuscript/SOURCE.md`

**Produces:** A manuscript directory containing accepted prose only.

- [x] **Step 1:** Reuse the existing Chapter 13 blob at the draft path.
- [x] **Step 2:** Delete the manuscript-path tree entry.
- [x] **Step 3:** Document promotion rules and draft non-canonicity.
- [x] **Step 4:** Confirm no prose bytes changed.

### Task 3: Upgrade Book 1 control pack

**Files:**
- Modify: `books/book-01/control/README.md`
- Modify: `books/book-01/control/00-overview.md`
- Modify: `books/book-01/control/02-current-project-state.md`
- Modify: `books/book-01/control/16-chapter-by-chapter-status-record.md`
- Modify: `books/book-01/control/18-act-iii-entry-state.md`
- Modify: `books/book-01/control/20-control-pack-maintenance-rules.md`
- Modify: `books/book-01/control/21-chapter-13-mission-lock.md`

**Produces:** Control Pack v3.0 with no stale Chapter 13 status.

- [x] **Step 1:** Replace repeated status with references to authority files.
- [x] **Step 2:** Preserve the accepted Chapter 12 endpoint.
- [x] **Step 3:** Record Chapter 13 as draft-only.
- [x] **Step 4:** Preserve mission, abort, evidence, POV, and custodian limits.
- [x] **Step 5:** Block Chapter 14 pending acceptance.

### Task 4: Add completion controls

**Files:**
- Create: `books/book-01/control/22-book-1-ending-contract.md`
- Create: `books/book-01/control/23-word-budget-and-act-iii-architecture.md`
- Create: `books/book-01/control/24-thread-disposition-matrix.md`
- Create: `books/book-01/control/25-chapter-acceptance-gate.md`
- Create: `books/book-01/control/27-chapter-13-acceptance-review.md`

**Produces:** Ending, budget, thread, acceptance, and current review controls.

- [x] **Step 1:** Define required Book 1 payoffs and bounded series carryovers.
- [x] **Step 2:** Allocate 44,500–56,000 remaining words across provisional units.
- [x] **Step 3:** Classify every existing open thread.
- [x] **Step 4:** Define exact ACCEPT/REVISE/HOLD/REJECT verdicts.
- [x] **Step 5:** Record Chapter 13 as HOLD pending full audit.

### Task 5: Add series character control

**Files:**
- Create: `series/README.md`
- Create: `series/recurring-character-ledger.md`

**Produces:** Cross-book continuity for core, recurring, network, and conditional characters.

- [x] **Step 1:** Define required recurring-character fields.
- [x] **Step 2:** Populate current accepted states without inventing ages or future facts.
- [x] **Step 3:** Add return triggers and no-retcon locks.

### Task 6: Register archive provenance

**Files:**
- Create: `archive/README.md`
- Create: `archive/legacy-sources/README.md`
- Create: `books/book-01/control/26-repository-governance-repair-record.md`

**Produces:** Historical-source clarity without duplicate active manuscripts.

- [x] **Step 1:** Register the former Google Doc as inactive migration input.
- [x] **Step 2:** Register the uploaded Word snapshot by filename, size, format, and SHA-256.
- [x] **Step 3:** Keep private URLs and binary content out of the public repo.
- [x] **Step 4:** State that Git history is the archive for superseded status files.

### Task 7: Verify and publish

**Files:**
- Create: `docs/superpowers/specs/2026-07-12-book-01-repository-governance-design.md`
- Create: `docs/superpowers/plans/2026-07-12-book-01-repository-governance-implementation.md`

**Produces:** One reviewable branch and draft pull request.

- [x] **Step 1:** Parse the new YAML files.
- [x] **Step 2:** Scan active files for stale phrases and status contradictions.
- [x] **Step 3:** Verify Chapter 13’s source and destination blob SHA are identical.
- [x] **Step 4:** Compare branch against `main`.
- [x] **Step 5:** Open a draft pull request with the governance summary and validation evidence.
