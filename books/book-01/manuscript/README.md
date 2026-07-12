# Julie O’Donnell Book 1 — Accepted Manuscript

This directory contains **accepted prose only**.

The controlling inventory is [`../ACCEPTED_MANUSCRIPT.yaml`](../ACCEPTED_MANUSCRIPT.yaml). A prose file is canon only when it is both:

1. stored under this directory; and
2. listed in the accepted-manuscript inventory.

## Current accepted inventory

- Prologue
- Chapters 1–12
- Accepted length: **61,118 words**
- Accepted endpoint: approximately 07:18 EDT / 16:48 IST at the end of Chapter 12

## Directory layout

- `prologue.md`
- `chapters/chapter-01.md` through `chapters/chapter-12.md`
- `SOURCE.md` — manuscript authority and migration provenance
- `STATUS.md` — concise human-readable status pointer

No unaccepted chapter belongs in this directory.

Chapter 13, **The Carrier Stream**, is stored at [`../drafts/chapter-13.md`](../drafts/chapter-13.md). Its existence does not create canon.

## Authority

Accepted prose controls story truth. The control pack may explain, index, or plan around the prose, but it cannot overrule accepted events, dialogue, chronology, evidence, injuries, or character knowledge.

If a subordinate document conflicts with accepted prose, correct the subordinate document unless an explicit manuscript-revision commit changes the prose.

## Promotion rule

A draft becomes accepted only through one explicit production commit that:

- moves the reviewed prose into this directory;
- adds it to `../ACCEPTED_MANUSCRIPT.yaml`;
- updates the accepted word count and endpoint;
- updates `../../../PROJECT_STATE.yaml`;
- updates every affected timeline, character, relationship, evidence, knowledge, technology, public-narrative, and open-thread control; and
- records the acceptance verdict.

See [`../control/25-chapter-acceptance-gate.md`](../control/25-chapter-acceptance-gate.md).
