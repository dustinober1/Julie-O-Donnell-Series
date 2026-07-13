# Julie O'Donnell Series

Repository for the Julie O'Donnell contemporary geopolitical techno-thriller / military-intelligence thriller series.

## Current production state

The authoritative production status is [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml). Story canon is controlled by the accepted-manuscript inventory and the accepted Markdown prose.

Current snapshot:

- Active book: Book 1 — title not yet locked
- Target length: **100,000–125,000 words**
- Planning target: **112,500 words**
- Accepted canon: Prologue and Chapters 1–14
- Accepted-manuscript length: **75,593 words**
- Accepted endpoint: **07:49:32 EDT / 17:19:32 IST**, public parking garage level six beside powered-down PCF-27 under Metropolitan Police scene control
- Chapter 13, **The Carrier Stream**: accepted
- Chapter 14, **The Witness Line**: accepted unchanged after formal review
- Chapter 15 and later prose: not drafted
- Immediate production action: a dedicated Chapter 15 mission-planning and mission-lock session; do not draft Chapter 15 in that session

## Source-of-truth hierarchy

1. [`books/book-01/ACCEPTED_MANUSCRIPT.yaml`](books/book-01/ACCEPTED_MANUSCRIPT.yaml) and the accepted files it lists
2. [`books/book-01/control/`](books/book-01/control/) for canon controls and approved production planning
3. [`series/`](series/) for cross-book continuity and recurring-character controls
4. [`books/book-01/drafts/`](books/book-01/drafts/) for unaccepted prose
5. [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml) for production status and navigation
6. [`archive/`](archive/) and Git history for superseded or external-source provenance

Accepted prose outranks every summary, tracker, plan, and draft. Draft prose cannot create canon until explicitly promoted through the acceptance gate.

## Repository layout

```text
.
├── README.md
├── PROJECT_STATE.yaml
├── archive/
│   └── legacy-sources/
├── books/
│   └── book-01/
│       ├── ACCEPTED_MANUSCRIPT.yaml
│       ├── manuscript/        # Accepted prose only
│       ├── drafts/            # Unaccepted prose only
│       ├── control/           # Canon and production controls
│       └── repairs/           # Permanent accepted repair records
├── docs/
│   └── superpowers/           # Approved designs and implementation plans
├── tools/
│   └── count_book1_words.py
└── series/
    └── recurring-character-ledger.md
```

## Current production controls

- [Book 1 ending contract](books/book-01/control/22-book-1-ending-contract.md)
- [Word budget and provisional Act III architecture](books/book-01/control/23-word-budget-and-act-iii-architecture.md)
- [Thread disposition matrix](books/book-01/control/24-thread-disposition-matrix.md)
- [Chapter acceptance gate](books/book-01/control/25-chapter-acceptance-gate.md)
- [Repository governance repair record](books/book-01/control/26-repository-governance-repair-record.md)
- [Chapter 13 acceptance review](books/book-01/control/27-chapter-13-acceptance-review.md)
- [Chapter 14 mission lock](books/book-01/control/28-chapter-14-mission-lock.md)
- [Chapter 14 acceptance review](books/book-01/control/29-chapter-14-acceptance-review.md)
- [Series recurring-character ledger](series/recurring-character-ledger.md)

## Chapter 15 production rule

Chapter 15 has no accepted mission lock and no prose. The next session may lock its dramatic function, evidence/custody problem, clocks, POV, abort condition, and endpoint. It must not draft Chapter 15 until that planning gate is complete.

## Permanent continuity repair

The Chapter 5-to-6 chronology, two-stage deadline, title, geography, and L3-7 handoff were repaired and integrated on July 12, 2026.

- Chapter 5: **The Second Clock**
- Chapter 7: **The Human Key**
- 16:30 EDT / 02:00 IST: allied source certification
- 05:00 EDT / 14:30 IST: executable counter-battery support commit and firing-decision point
- Integration commit: `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`
- Permanent record: `books/book-01/repairs/chapter-05-to-06-continuity-repair/`
