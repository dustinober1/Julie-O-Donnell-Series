# /julie-chapter-context

## Purpose

Create a concise context packet for a specific chapter so drafting or revision can happen without canon drift.

## Usage

```text
/julie-chapter-context <book-number> <chapter-number>
```

## Required Skills

- `julie-series-canon`
- `julie-series-memory`
- `julie-continuity-auditor`

## Read First

- `PROJECT_STATE.yaml`
- `.opencode/skills/julie-series-canon.md`
- `series-bible/09-continuity-locks.md`
- requested book's `book-bible.md`
- requested book's `chapter-outline.md`
- requested book's `clue-map.md`
- requested book's `continuity-log.md`
- previous chapter if available
- current blueprint if available

## Task

Produce a context packet containing:

- chapter purpose;
- current plot position;
- required clue movement;
- Julie emotional state;
- technical state of the investigation;
- institutional pressure;
- continuity locks;
- forbidden reveals;
- open questions.

## Output Destination

Save to:

```text
books/book-XX/chapter-context/ch-YYY-context.md
```

If that folder does not exist, create it.
