# Skill: Julie Canon Update Governance

## Purpose

Control how canon is proposed, reviewed, promoted, and logged for the Julie O'Donnell series.

Use this skill only during canon-maintenance commands.

## Core Rule

Chapter commands may discover canon. Only canon-maintenance commands may promote canon.

## Canon Destinations

Use the narrowest durable destination:

- Global series fact: `.opencode/skills/julie-series-canon.md`
- Series overview: `series-bible/00-series-dashboard.md`
- Character-specific canon: `series-bible/02-julie-character-canon.md`
- Recurring cast: `series-bible/03-recurring-cast.md`
- Timeline fact: `series-bible/04-series-timeline.md`
- AI/system rule: `series-bible/05-ai-threat-taxonomy.md` or `series-bible/12-technology-rules.md`
- Institution rule: `series-bible/06-institutional-canon.md`
- Book-specific fact: `books/book-XX/chapter-facts.md` or `books/book-XX/continuity-log.md`
- Possible future item: `series-bible/unresolved-series-threads.md`
- Proposed but not promoted: `series-bible/proposed-canon-updates.md`

## Canon Classification

Classify each candidate as:

- Character Lock
- Backstory Lock
- Relationship Lock
- Technical Rule
- Institutional Rule
- Timeline Lock
- Series Arc Lock
- Book-Specific Lock
- Marketing/Positioning Lock
- Reject as Trivia

## Promotion Test

Promote only if all are true:

1. The fact is supported by manuscript, book plan, or user instruction.
2. The fact affects future chapters or future books.
3. The fact is not already captured elsewhere.
4. The fact is not scene trivia.
5. The fact does not conflict with a higher-priority lock.
6. The promotion destination is clear.

## Required Log Entry

Every promoted item must produce an entry in `series-bible/canon-change-log.md` with:

- date;
- source;
- classification;
- exact canon statement;
- destination file;
- reason it matters;
- any replaced or superseded canon.

## Rejection Standard

When rejecting a candidate, explain why:

- transient scene detail;
- duplicate;
- too speculative;
- contradicted by current canon;
- belongs in book-level notes;
- unsupported by actual text.

## Safety Rule

Do not rewrite large portions of canon files unless performing an explicit canon repair pass. Most canon updates should be small, additive, and logged.
