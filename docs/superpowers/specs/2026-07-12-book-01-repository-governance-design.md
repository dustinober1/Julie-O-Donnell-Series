# Book 1 Repository Governance Design

## Status

Approved by the author on July 12, 2026 through the instruction to implement the repository-organization work session.

## Problem

Book 1 has a strong manuscript and control pack, but repository status drift makes production unsafe:

- Chapter 13 exists as a complete unaccepted draft inside the accepted-manuscript directory.
- Some files say Chapter 13 does not exist.
- Some files say Act III is undrafted while others record a Chapter 13 draft.
- Word-count summaries conflict.
- Book 1 obligations and series carryovers are mixed together.
- Current character controls do not provide cross-book recurrence fields.
- Draft promotion is not protected by a formal gate.
- External Word and Google Doc sources remain available without a dedicated archive policy.

The design must preserve all accepted prose while making accidental canon drift difficult.

## Goals

1. Keep accepted prose and unaccepted prose physically separate.
2. Establish one production-status authority.
3. Establish one accepted-manuscript inventory.
4. Preserve the 100,000–125,000-word target with a usable planning budget.
5. Define the Book 1 ending before later Act III prose.
6. Classify every open thread as Book 1 payoff, partial/series, series, merged, or optional.
7. Track recurring characters across books without inventing future canon.
8. Formalize chapter review and promotion.
9. Archive external and superseded sources without maintaining duplicate active manuscripts.
10. Preserve Chapter 13 prose byte-for-byte while moving it out of the accepted directory.

## Non-goals

- No accepted prose revision.
- No Chapter 13 acceptance.
- No Chapter 14 drafting.
- No identification of SSO-NS-004’s physical custodian.
- No new canon fact.
- No publication of private Google Doc links or redundant binary manuscripts.

## Authority architecture

### Story canon

`books/book-01/ACCEPTED_MANUSCRIPT.yaml` inventories accepted prose. The listed manuscript files are the highest story authority.

### Production status

`PROJECT_STATE.yaml` is the sole authority for acceptance status, word budget, current production gate, and navigation.

### Book controls

`books/book-01/control/` stores continuity, evidence, knowledge, ending, architecture, thread, and acceptance controls.

### Series controls

`series/` stores cross-book continuity and recurring-character planning. It cannot overrule accepted prose.

### Drafts

`books/book-01/drafts/` stores all unaccepted prose.

### Archive

`archive/` records non-controlling external-source provenance and archive policy. Git history preserves superseded repository files.

## Directory design

```text
books/book-01/
├── ACCEPTED_MANUSCRIPT.yaml
├── manuscript/
│   ├── prologue.md
│   └── chapters/chapter-01.md ... chapter-12.md
├── drafts/
│   └── chapter-13.md
├── control/
└── repairs/
```

Chapter 13 moves by reusing the existing Git blob at the draft path and deleting the manuscript-path tree entry. No prose bytes change.

## Status data flow

1. Accepted prose changes.
2. `ACCEPTED_MANUSCRIPT.yaml` records accepted files, count, and endpoint.
3. `PROJECT_STATE.yaml` records the production consequence.
4. Human-readable README and STATUS files summarize and link back.
5. Control ledgers record story-state consequences.
6. Series ledger records cross-book consequences.

A summary may repeat a value for readability, but it is never authoritative.

## Book completion controls

### Ending contract

Separates required Book 1 resolutions from deliberate series carryovers and imposes an anti-cliffhanger test.

### Word budget

Uses 112,500 words as the midpoint planning target, with 61,118 accepted words and 51,382 words remaining to target.

### Provisional Act III architecture

Provides sequence and word ranges without creating story canon. Each chapter still requires its own mission lock.

### Thread disposition

Consolidates duplicate threads and assigns every existing thread a Book 1 or series obligation.

## Chapter acceptance flow

1. Lock mission.
2. Draft in `drafts/`.
3. Review continuity, evidence, character, craft, and series impact.
4. Record one explicit verdict.
5. Promote in one same-pass commit.
6. Update manifest, project state, all control ledgers, word count, endpoint, and series ledger.
7. Draft the next chapter only after promotion.

## Recurring-character design

Each candidate receives:

- identity and aliases;
- accepted appearance range;
- age status;
- physical and voice continuity;
- competencies and limitations;
- legal, employment, and public status;
- accepted location;
- knowledge and false beliefs;
- evidence or leverage;
- Julie relationship;
- Book 1 end-state requirement;
- series tier;
- future-book function;
- return trigger;
- no-retcon locks; and
- last update.

Unknown information remains not established.

## Archive design

The former Google Doc and uploaded Word snapshot are registered as historical inputs. The public repository stores only descriptive metadata and a Word-file hash, not the binary or private URL.

Superseded status files are preserved by Git history rather than duplicated into an active archive.

## Verification

The implementation is acceptable only if:

- `manuscript/chapters/chapter-13.md` is deleted;
- `drafts/chapter-13.md` points to the same blob;
- accepted prose files are otherwise unchanged;
- the accepted manifest lists only Prologue and Chapters 1–12;
- all active status files agree on 61,118 accepted words and Chapter 13 draft status;
- control index links resolve;
- no new file claims Chapter 13 is canon;
- no new file identifies the physical custodian;
- Chapter 14 is blocked pending Chapter 13 acceptance; and
- the final Git comparison shows only governance, status, planning, archive, and path changes.
