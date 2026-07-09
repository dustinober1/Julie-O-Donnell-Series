# /julie-publication-pass

## Purpose

Run chapter-level or full-book publication-readiness QA for the Julie O'Donnell series.

## Usage

```text
/julie-publication-pass <book-number>
```

Optional chapter-specific use:

```text
/julie-publication-pass <book-number> <chapter-number>
```

## Required Skills

- `julie-series-canon`
- `julie-publication-readiness`
- `julie-continuity-auditor`
- `julie-ai-tell-sweeper`

## Task

1. Verify repo scope.
2. Read book files, chapters, publication files, and prior QA reports.
3. Identify publication blockers.
4. Check metadata against actual manuscript promise.
5. Do not change prose unless explicitly requested.
6. Save a publication readiness report.

## Output Destination

Full-book report:

```text
books/book-XX/publication/publication-readiness-report.md
```

Chapter report:

```text
books/book-XX/revision-notes/ch-YYY-publication-pass.md
```

## Report

Use severity labels:

- Critical
- Recommended
- Optional

End with publication readiness rating and next command.
