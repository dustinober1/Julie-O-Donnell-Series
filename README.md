# Julie O'Donnell Series

Repository for the Julie O'Donnell contemporary geopolitical techno-thriller / military-intelligence thriller series.

## Current production state

The authoritative production status is [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml). Story canon is controlled by the accepted-manuscript inventory and accepted Markdown prose.

- Active book: Book 1 — title not yet locked
- Target length: **100,000–125,000 words**
- Planning target: **112,500 words**
- Accepted canon: Prologue and Chapters 1–15
- Accepted-manuscript length: **81,586 words**
- Accepted endpoint: **07:56:40 EDT / 17:26:40 IST**
- Chapter 13, **The Carrier Stream**: accepted
- Chapter 14, **The Witness Line**: accepted
- Chapter 15, **The Split Record**: accepted after one capitalization-only copyedit at **5,993 words**
- Chapter 16, **The Hold Order**: mission locked; prose not drafted
- Immediate production action: draft Chapter 16 only under `books/book-01/drafts/chapter-16.md` from the approved mission lock
- Book 1: not publication-ready

## Accepted Chapter 15 endpoint

- Julie is in marked MPD transport under an injury-compatible restraint.
- Marcus is in guarded ambulance care; his hard abort did not trigger.
- Elias is in separate guarded medical transport.
- MPD retains seven separately sealed evidence packages under incident `187463`.
- The superseding allied product became controlling at 07:54 EDT / 17:24 IST, while Sharma preserved prior, superseding, local anomaly, abort, and no-fire records as one challenged incident set.
- Hartwell presenter/exact serial, WSS plaintext, K-17 access, Phase B, final federal custody, and public fracture remain unresolved.

## Approved Chapter 16 mission

Chapter 16 — **The Hold Order** — is controlled by [`books/book-01/control/32-chapter-16-mission-lock.md`](books/book-01/control/32-chapter-16-mission-lock.md).

Its dominant function is to force a named federal preservation authority behind the interim MPD chain while keeping all seven packages separate, sealed, offline, and in MPD custody. The lock uses Julie as primary POV with one bounded Marcus ambulance cutaway and one bounded Sharma cutaway. It plans a 5,800–6,500-word chapter opening at 07:56:40 EDT / 17:26:40 IST and ending no later than 08:16:40 EDT / 17:46:40 IST.

The mission lock is planning only. It does not change accepted prose, count, endpoint, evidence custody, character state, or canon.

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
├── books/
│   └── book-01/
│       ├── ACCEPTED_MANUSCRIPT.yaml
│       ├── manuscript/        # Accepted prose only
│       ├── drafts/            # Unaccepted prose only
│       ├── control/           # Canon and production controls
│       └── repairs/           # Permanent accepted repair records
├── docs/
├── tools/
└── series/
```

## Current production controls

- [Book 1 ending contract](books/book-01/control/22-book-1-ending-contract.md)
- [Word budget and provisional Act III architecture](books/book-01/control/23-word-budget-and-act-iii-architecture.md)
- [Thread disposition matrix](books/book-01/control/24-thread-disposition-matrix.md)
- [Chapter acceptance gate](books/book-01/control/25-chapter-acceptance-gate.md)
- [Chapter 14 acceptance review](books/book-01/control/29-chapter-14-acceptance-review.md)
- [Chapter 15 mission lock](books/book-01/control/30-chapter-15-mission-lock.md)
- [Chapter 15 acceptance review](books/book-01/control/31-chapter-15-acceptance-review.md)
- [Chapter 16 mission lock](books/book-01/control/32-chapter-16-mission-lock.md)
- [Series recurring-character ledger](series/recurring-character-ledger.md)

## Chapter 16 rule

Draft Chapter 16 only at `books/book-01/drafts/chapter-16.md` from the approved mission lock. Do not place it in the accepted manuscript, update the accepted inventory, change the 81,586-word accepted total or 07:56:40 EDT / 17:26:40 IST accepted endpoint, draft Chapter 17, or create a complete remainder-of-Act-III outline during that session.

## Permanent continuity repair

The Chapter 5-to-6 chronology, two-stage deadline, title, geography, and L3-7 handoff were repaired and integrated on July 12, 2026.

- Chapter 5: **The Second Clock**
- Chapter 7: **The Human Key**
- 16:30 EDT / 02:00 IST: allied source certification
- 05:00 EDT / 14:30 IST: executable counter-battery support commit and firing-decision point
- Integration commit: `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`
- Permanent record: `books/book-01/repairs/chapter-05-to-06-continuity-repair/`
