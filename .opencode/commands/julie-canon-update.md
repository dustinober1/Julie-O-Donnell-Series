# /julie-canon-update

## Purpose

Review new chapter/book facts and promote only durable canon into the appropriate series or book file.

## Usage

```text
/julie-canon-update <book-number> <chapter-number-or-final>
```

## Required Skills

- `julie-series-canon`
- `julie-canon-update-governance`
- `julie-continuity-auditor`
- `julie-series-memory`

## Task

1. Verify repo scope.
2. Read the relevant chapter, continuity pass, chapter facts, continuity log, and proposed canon updates.
3. Identify candidate facts.
4. Classify each candidate.
5. Reject trivia.
6. Promote only durable canon to the narrowest correct file.
7. Update `series-bible/canon-change-log.md` for promoted canon.
8. Save a chapter-level canon update report.

## Output Destination

```text
books/book-XX/canon-updates/ch-YYY-canon-update.md
```

For final book-level update:

```text
books/book-XX/canon-updates/final-canon-update.md
```

## Canon Promotion Destinations

- `.opencode/skills/julie-series-canon.md`
- `series-bible/02-julie-character-canon.md`
- `series-bible/03-recurring-cast.md`
- `series-bible/04-series-timeline.md`
- `series-bible/05-ai-threat-taxonomy.md`
- `series-bible/06-institutional-canon.md`
- `series-bible/09-continuity-locks.md`
- active book `continuity-log.md`
- active book `chapter-facts.md`

## Report

Include promoted facts, rejected facts, files changed, and next recommended command.
