# /julie-next-chapter-prompt

## Purpose

Generate a complete copy-paste prompt for continuing the Julie O'Donnell workflow in a new context window.

## Usage

```text
/julie-next-chapter-prompt <book-number> <next-chapter-number>
```

## Required Skills

- `julie-series-canon`
- `julie-series-memory`
- `julie-chapter-architect`
- `julie-continuity-auditor`

## Task

1. Verify repo scope.
2. Read current project state and active book files.
3. Review latest completed chapter, latest continuity pass, and latest canon update.
4. Identify the next logical chapter task.
5. Generate a full prompt that can be pasted into a fresh ChatGPT/OpenCode context.
6. Include repository guardrails, allowed files, required reads, locked canon, chapter objective, and output requirements.

## Output Destination

```text
books/book-XX/prompts/ch-YYY-next-context-prompt.md
```

If that folder does not exist, create it.

## Prompt Must Include

- repository full name;
- default branch;
- scope verification step;
- files to read first;
- current book and chapter status;
- locked canon reminders;
- task instructions;
- forbidden changes;
- expected output/report.

## Report

Include the generated prompt and the path where it was saved.
