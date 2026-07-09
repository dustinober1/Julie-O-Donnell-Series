# Julie O'Donnell Series

Working repository for the Julie O'Donnell thriller series.

This repo is designed to hold the story bible, Book 1 relaunch documents, chapter-production prompts, canon locks, OpenCode skills, slash commands, and manuscript files needed to write a long-running commercial thriller series consistently with AI/coding-agent assistance.

## Current status

- **Project:** Julie O'Donnell Series
- **Genre lane:** contemporary military / intelligence / political techno-thriller
- **Core engine:** a former Army intelligence officer who once saw an AI-enabled targeting system lie is pulled back toward systems that can misclassify, escalate, and kill at national-security scale.
- **Primary protagonist:** former Captain Julie O'Donnell
- **Book 1 status:** outline expanded / ready for chapter blueprinting
- **Repository status:** OpenCode production-system scaffold in progress

## Start here

Read these files in order before drafting or editing:

1. `docs/00_START_HERE_Project_Dashboard.md`
2. `PROJECT_STATE.yaml`
3. `docs/01_Series_Premise_and_Commercial_Hook.md`
4. `docs/02_Book_1_Relaunch_Reset_Diagnostic.md`
5. `docs/03_Book_1_Story_Bible.md`
6. `docs/04_Character_Bible.md`
7. `docs/05_Technology_and_Threat_Model.md`
8. `docs/06_Continuity_Canon_Locks.md`
9. `docs/07_Prose_Style_and_Voice_DNA.md`
10. `docs/08_Chapter_Production_Pipeline.md`
11. `docs/09_Agent_Prompt_Library.md`
12. `.opencode/skills/julie-series-canon.md`
13. `series-bible/00-series-dashboard.md`
14. `production/workflow-guide.md`

## OpenCode workflow

The repo now includes a Julie-specific OpenCode workflow layer:

```text
.opencode/
  skills/
  commands/
```

Use the slash commands in this order for chapter production:

```text
/julie-repo-verify
/julie-chapter-context <book-number> <chapter-number>
/julie-plan-chapter <book-number> <chapter-number>
/julie-draft-chapter <book-number> <chapter-number>
/julie-revise-chapter <book-number> <chapter-number>
/julie-continuity-pass <book-number> <chapter-number>
/julie-canon-update <book-number> <chapter-number>
/julie-next-chapter-prompt <book-number> <next-chapter-number>
```

## Working principle

Chapter commands may discover canon. Only canon-maintenance commands may promote canon.

## Primary repository areas

- `docs/` — recovered and early project foundation docs.
- `.opencode/skills/` — reusable expert behavior for OpenCode agents.
- `.opencode/commands/` — slash-command workflows for planning, drafting, revising, auditing, and canon maintenance.
- `series-bible/` — durable series truth and long-term continuity.
- `references/` — grounded technical, procedural, and market references.
- `templates/` — reusable document templates for books, chapters, metadata, and QA.
- `books/` — per-book planning, manuscript, revision, continuity, and publication assets.
- `production/` — workflow, status, quality gates, and release support.
- `marketing/` — positioning, launch, ads, newsletter, and sell-through assets.
- `archive/` — deprecated canon, old drafts, retired prompts, and unused concepts.

## Source note

The repo was initialized from the Julie O'Donnell material recoverable in the current ChatGPT project context. A Gemini share link was provided earlier, but the shared page could not be fetched automatically in this environment. Future pasted/exported chat content should be merged into `docs/99_Source_Reconstruction_Log.md` and then promoted into canon only after review.
