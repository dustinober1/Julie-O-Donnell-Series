# Julie O’Donnell Series

Repository for the Julie O’Donnell contemporary geopolitical techno-thriller / military-intelligence thriller series.

## Current production state

- Active book: Book 1 — title not yet locked
- Accepted manuscript: Prologue and Chapters 1–12
- Acts I and II: complete
- Act III: not drafted
- Canon endpoint: approximately 07:18 EDT / 16:48 IST at the end of Chapter 12
- Next planned chapter: Chapter 13; title and dominant objective not yet locked
- Controlling manuscript: GitHub Markdown files in `books/book-01/manuscript/`

## Source-of-truth hierarchy

1. `books/book-01/manuscript/` — accepted manuscript prose and controlling story truth.
2. `books/book-01/control/` — continuity, evidence, technology, character, timeline, and production controls through Chapter 12.
3. `PROJECT_STATE.yaml` and this README — navigation and status only.

If any repository document conflicts with the accepted manuscript prose, the accepted manuscript controls and the subordinate document must be corrected.

## Critical continuity warning

The accepted manuscript contains an unresolved chronology and geography break between Chapters 5 and 6. Chapter 5 ends around 16:14 EDT at the production-vault entrance, while Chapter 6 opens at 04:52 EDT behind a descending hydraulic shutter as an immediate continuation.

The proposed repair package is stored at:

`books/book-01/repairs/chapter-05-to-06-continuity-repair/`

It has not yet been integrated into the controlling manuscript.

## Repository layout

```text
.
├── README.md
├── PROJECT_STATE.yaml
└── books/
    └── book-01/
        ├── manuscript/    # Controlling Prologue and Chapters 1–12 in Markdown
        ├── control/       # Canon Control Pack v1.0, split by section
        └── repairs/       # Proposed and accepted manuscript-repair records
```

## Immediate next decisions

- Review and integrate or reject the proposed Chapter 5-to-6 continuity repair.
- Lock Chapter 13’s dominant mission and abort condition after the repair is resolved.
- Decide whether Chapter 13 includes a K-17 or Sharma cutaway.
- Keep the physical custodian of SSO-NS-004 unresolved until established by evidence in accepted prose.
