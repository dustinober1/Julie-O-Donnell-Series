# Book 1 One-Sentence Paragraph Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reduce the remaining mechanical one-sentence narrative paragraphs in the accepted Book 1 manuscript while preserving every story fact and the 105,081-word content lock.

**Architecture:** Generate a full context export for all strict audit candidates, convert the reviewed decisions into an explicit paragraph-integration map, apply only those integrations, then regenerate accepted hashes, compiled output, and before/after audit artifacts. The repair changes paragraph boundaries and minimal punctuation only; lexical word sequence is verified before commit.

**Tech Stack:** Python 3 standard library, Markdown accepted manuscript, YAML-style manifest parsing, GitHub Actions validation.

## Global Constraints

- Accepted source inventory is `books/book-01/ACCEPTED_MANUSCRIPT.yaml`.
- Accepted words must remain exactly 105,081.
- Plot, pacing, scene order, POV, chronology, evidence, technology, dialogue meaning, character decisions, knowledge, worldbuilding, suspense structure, reveals, and ending are locked.
- System displays, scene metadata, separators, and chapter endings are protected.
- Final line remains `The bubble stayed centered.`

---

### Task 1: Export full candidate context

**Files:**
- Create: `tools/export_book1_one_sentence_context.py`
- Create temporarily: `.github/workflows/book1-one-sentence-context.yml`
- Output artifact: `artifacts/book1-one-sentence-context.json`

- [ ] Generate every strict candidate with file, paragraph number, previous paragraph, candidate paragraph, next paragraph, paragraph kinds, word count, and reasons.
- [ ] Run the exporter on the accepted inventory.
- [ ] Upload the JSON as a workflow artifact.
- [ ] Confirm accepted word count and existing manuscript validation remain green.

### Task 2: Build the explicit repair map

**Files:**
- Create: `books/book-01/control/52-one-sentence-repair-map.json`

- [ ] Review every candidate in context.
- [ ] Assign one action: `keep`, `merge_previous`, `merge_next`, `attach_next_dialogue`, or `attach_previous_dialogue`.
- [ ] Record a short reason for every kept isolated line.
- [ ] Prefer leaving ambiguous dialogue attribution unchanged.
- [ ] Confirm countdowns, discoveries, motifs, and scene boundaries remain protected.

### Task 3: Apply content-locked paragraph integrations

**Files:**
- Create: `tools/apply_book1_one_sentence_repair.py`
- Modify: accepted prose files listed by the repair map

- [ ] Load the explicit repair map and accepted files.
- [ ] Apply only mapped paragraph-boundary changes.
- [ ] Reject stale paragraph text or mismatched context.
- [ ] Verify lexical signatures and repository word counts remain unchanged per file.
- [ ] Verify protected non-narrative blocks, scene separators, and final paragraphs remain unchanged.

### Task 4: Synchronize canon controls and compiled output

**Files:**
- Modify: `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
- Modify: `books/book-01/compiled/current/Julie_O_Donnell_Book_1_REVISED.md`
- Modify: `tools/verify_book1_revision.py` only if protected opening hashes change
- Create: `artifacts/book1-one-sentence-repair.md`
- Create: `books/book-01/control/53-one-sentence-repair.md`

- [ ] Recompute accepted-file hashes without changing word counts.
- [ ] Recompile the accepted manuscript strictly from the manifest.
- [ ] Generate before/after narrative-only audit metrics.
- [ ] Record the changed files and protected decisions.

### Task 5: Final validation and pull request

**Files:**
- Create temporarily: `.github/workflows/book1-one-sentence-repair.yml`

- [ ] Run `python3 tools/count_book1_words.py --expect 105081`.
- [ ] Run `python3 tools/validate_book1_publication_readiness.py`.
- [ ] Run `python3 tools/verify_book1_revision.py`.
- [ ] Compile the repair and audit tools.
- [ ] Parse synchronized YAML controls.
- [ ] Run `git diff --check`.
- [ ] Confirm strict review candidates fall below 75 or document every remaining exception.
- [ ] Remove temporary workflows.
- [ ] Open a draft pull request with measured before/after results.
