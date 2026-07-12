# Julie O’Donnell Series

Repository for the Julie O’Donnell contemporary geopolitical techno-thriller / military-intelligence thriller series.

## Current production state

- Active book: Book 1 — title not yet locked
- Accepted manuscript: Prologue and Chapters 1–12
- Acts I and II: complete
- Act III: not drafted
- Canon endpoint: approximately 07:18 EDT / 16:48 IST at the end of Chapter 12
- Next planned chapter: Chapter 13; title not locked; dominant mission, abort condition, POV structure, and Act III launch state locked in `books/book-01/control/21-chapter-13-mission-lock.md`
- Controlling manuscript: GitHub Markdown files in `books/book-01/manuscript/`

## Source-of-truth hierarchy

1. `books/book-01/manuscript/` — accepted manuscript prose and controlling story truth.
2. `books/book-01/control/` — continuity, evidence, technology, character, timeline, production controls, and locked planning records through the Chapter 13 mission lock.
3. `PROJECT_STATE.yaml` and this README — navigation and status only.

If any repository document conflicts with the accepted manuscript prose, the accepted manuscript controls and the subordinate document must be corrected.

## Chapter 5-to-6 continuity repair

The chronology, deadline, geography, and immediate physical handoff between Chapters 5 and 6 were repaired and integrated on July 12, 2026.

- Chapter 5 is now **The Second Clock**.
- Chapter 7 remains **The Human Key**.
- 16:30 EDT / 02:00 IST is the allied source-certification stage.
- 05:00 EDT / 14:30 IST is the executable counter-battery support commit and firing-decision point.
- Chapter 5 now ends at hydraulic shutter L3-7 in the seconds immediately preceding Chapter 6.
- Chapter 6 remains unchanged.

Permanent repair history:

`books/book-01/repairs/chapter-05-to-06-continuity-repair/`

Integration commit: `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`

## Repository layout

```text
.
├── README.md
├── PROJECT_STATE.yaml
└── books/
    └── book-01/
        ├── manuscript/    # Controlling Prologue and Chapters 1–12 in Markdown
        ├── control/       # Canon Control Pack and Chapter 13 mission lock
        └── repairs/       # Permanent accepted manuscript-repair records
```

## Immediate next action

- Draft Chapter 13 in a fresh context using the locked mission document and the accepted GitHub manuscript as the sole source of truth.
- Do not create or treat any full Act III chapter-by-chapter outline as controlling canon.
- Keep the physical custodian of SSO-NS-004 unresolved until established by evidence in accepted prose.
- Keep Act III undrafted until Chapter 13 prose is drafted and accepted.
