# Julie O'Donnell Series

Repository for the Julie O'Donnell contemporary geopolitical techno-thriller / military-intelligence thriller series.

## Current production state

The authoritative production status is [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml). Story canon is controlled by the accepted-manuscript inventory and accepted Markdown prose.

- Active book: Book 1 — title not yet locked
- Target length: **100,000–125,000 words**
- Planning target: **112,500 words**
- Accepted canon: Prologue and Chapters 1–16
- Accepted-manuscript length: **87,610 words**
- Accepted endpoint: **08:15:52 EDT / 17:45:52 IST**
- Chapter 13, **The Carrier Stream**: accepted
- Chapter 14, **The Witness Line**: accepted
- Chapter 15, **The Split Record**: accepted after one capitalization-only copyedit at **5,993 words**
- Chapter 16, **The Hold Order**: accepted unchanged at **6,024 words**
- Immediate production action: Chapter 17 mission planning and mission locking only
- Book 1: not publication-ready

## Accepted Chapter 16 endpoint

- Hackett is the named federal preservation sponsor for MPD incident `187463`; he is not the physical receiver or technical examiner.
- MPD retains physical custody of all seven packages, `MPD-901441` through `MPD-901447`.
- Every package remains separate, sealed, offline, unopened, unconnected, and uncombined.
- Marcus has placed his complete six-years-ago correction on an attributable record while under EMS authority; EMS ended the call at the medical boundary.
- Sharma has acknowledged preservation of the bounded challenged allied incident set without deciding either product true or false.
- Julie knows only that a restricted allied preservation acknowledgment exists; she does not know Sharma's identity or the no-fire outcome.
- No final federal receiver, technical examiner, public vindication, Hartwell presenter, exact challenged serial, WSS plaintext, K-17 result, or Phase B result exists.

## Chapter 16 acceptance

Chapter 16 — **The Hold Order** — is accepted at [`books/book-01/manuscript/chapters/chapter-16.md`](books/book-01/manuscript/chapters/chapter-16.md).

- Words: **6,024**
- Opening: **07:56:40 EDT / 17:26:40 IST**
- Endpoint: **08:15:52 EDT / 17:45:52 IST**
- POV: Julie, Marcus, Sharma, Julie
- Verdict: **ACCEPT**
- Prose changed during review: **No**
- Reviewed blob: `ff6fbaa66170a03502589309b3d1c2d74b50a289`
- Mission lock: [`books/book-01/control/32-chapter-16-mission-lock.md`](books/book-01/control/32-chapter-16-mission-lock.md)
- Acceptance review: [`books/book-01/control/33-chapter-16-acceptance-review.md`](books/book-01/control/33-chapter-16-acceptance-review.md)

No active Chapter 16 draft remains. Chapter 17 and later prose do not exist.

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
- [Chapter 15 acceptance review](books/book-01/control/31-chapter-15-acceptance-review.md)
- [Chapter 16 mission lock](books/book-01/control/32-chapter-16-mission-lock.md)
- [Chapter 16 acceptance review](books/book-01/control/33-chapter-16-acceptance-review.md)
- [Series recurring-character ledger](series/recurring-character-ledger.md)

## Chapter 17 rule

The next session is for **Chapter 17 mission planning and mission locking only** from the accepted Chapter 16 endpoint. Do not draft Chapter 17. Do not create a complete chapter-by-chapter outline for the remainder of Act III.

## Permanent continuity repair

The Chapter 5-to-6 chronology, two-stage deadline, title, geography, and L3-7 handoff were repaired and integrated on July 12, 2026.

- Chapter 5: **The Second Clock**
- Chapter 7: **The Human Key**
- 16:30 EDT / 02:00 IST: allied source certification
- 05:00 EDT / 14:30 IST: executable counter-battery support commit and firing-decision point
- Integration commit: `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`
- Permanent record: `books/book-01/repairs/chapter-05-to-06-continuity-repair/`
