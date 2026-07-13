# Julie O’Donnell Book 1 — Accepted Manuscript

This directory contains **accepted prose only**.

The controlling inventory is [`../ACCEPTED_MANUSCRIPT.yaml`](../ACCEPTED_MANUSCRIPT.yaml). A prose file is canon only when it is both stored under this directory and listed in the accepted-manuscript inventory.

## Current accepted inventory

- Prologue
- Chapters 1–14
- Accepted length: **75,593 words**
- Accepted endpoint: **07:49:32 EDT / 17:19:32 IST**, public parking garage level six beside powered-down PCF-27 under Metropolitan Police scene control

## Directory layout

- `prologue.md`
- `chapters/chapter-01.md` through `chapters/chapter-14.md`
- `SOURCE.md` — manuscript authority and migration provenance
- `STATUS.md` — concise human-readable status pointer

No unaccepted chapter belongs in this directory. No active chapter draft currently exists under `../drafts/`.

Chapter 15 has an approved mission lock at `../control/30-chapter-15-mission-lock.md`, but no Chapter 15 prose exists and no Chapter 15 file belongs here until formal acceptance.

## Authority

Accepted prose controls story truth. The control pack may explain, index, or plan around the prose, but it cannot overrule accepted events, dialogue, chronology, evidence, injuries, or character knowledge.

If a subordinate document conflicts with accepted prose, correct the subordinate document unless an explicit manuscript-revision commit changes the prose.

## Promotion rule

A draft becomes accepted only through one explicit production commit that moves the reviewed prose here, adds it to the manifest, updates the accepted word count and endpoint, updates `PROJECT_STATE.yaml`, updates every affected control, and records the verdict.

See [`../control/25-chapter-acceptance-gate.md`](../control/25-chapter-acceptance-gate.md).
