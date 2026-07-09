# /julie-repo-verify

## Purpose

Verify repository scope before any read/write work.

## Usage

```text
/julie-repo-verify
```

## Required Checks

1. Confirm repository full name is exactly:

```text
dustinober1/Julie-O-Donnell-Series
```

2. Confirm default branch is `main`.
3. Confirm write permission if visible.
4. Confirm current HEAD if the connector/tool exposes it.
5. Search for major project files:
   - `PROJECT_STATE.yaml`
   - `.opencode/skills/julie-series-canon.md`
   - `series-bible/00-series-dashboard.md`
   - `books/book-01/`
6. If the repository resolves to any other repo, stop immediately and do not edit.

## Output

Report:

- repository full name;
- default branch;
- write permission status;
- current HEAD if available;
- whether the repo is safe to edit;
- next recommended command.
