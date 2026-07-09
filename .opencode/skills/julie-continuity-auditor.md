# Skill: Julie Continuity Auditor

## Purpose

Audit Julie O'Donnell chapters, book plans, and series documents for canon conflicts, timeline problems, clue drift, technical inconsistency, relationship drift, and long-series continuity risks.

## Required Inputs

Before auditing, read:

- `PROJECT_STATE.yaml`
- `.opencode/skills/julie-series-canon.md`
- `series-bible/09-continuity-locks.md`
- `series-bible/04-series-timeline.md`
- active book `book-bible.md`
- active book `timeline.md`
- active book `clue-map.md`
- active book `chapter-facts.md`
- active chapter or plan
- nearby chapters when available

## Audit Categories

Check for:

- character continuity;
- backstory continuity;
- technology continuity;
- institutional continuity;
- clue timing;
- red-herring logic;
- timeline sequence;
- geography and travel plausibility;
- emotional arc progression;
- recurring-cast consistency;
- unresolved-thread tracking;
- publication-facing contradictions.

## Severity Levels

Use these labels:

- **Critical** — breaks canon, mystery logic, timeline, or reader trust.
- **Recommended** — improves clarity, consistency, or long-series durability.
- **Optional** — polish, preference, or minor note.

## Output Requirements

Produce a continuity pass report with:

- chapter/book audited;
- files read;
- no-edit summary;
- critical findings;
- recommended fixes;
- optional improvements;
- canon candidates;
- items that should not be promoted to canon;
- recommended next command.

## Canon Candidate Handling

If a new durable fact appears, do not update the canon skill directly unless the command is explicitly `/julie-canon-update`.

Instead, list it under `Canon Candidates` with:

- proposed statement;
- source chapter;
- classification;
- reason it matters;
- recommended destination file.
