# 09 — Agent Prompt Library

## Purpose

Use these prompts with AI/coding agents to continue the Julie O'Donnell Series without losing the premise, canon, or style target.

Replace bracketed fields before running.

---

## Prompt 1 — Repo orientation and canon load

```text
We are working in the GitHub repository:

Repository: dustinober1/Julie-O-Donnell-Series
Default branch: main
Project: Julie O'Donnell Series
Genre: contemporary intelligence / military techno-thriller

Before editing, verify the repository full name is exactly dustinober1/Julie-O-Donnell-Series. If the connector resolves to any other repo, stop.

Read these files first:

- README.md
- PROJECT_STATE.yaml
- docs/00_START_HERE_Project_Dashboard.md
- docs/01_Series_Premise_and_Commercial_Hook.md
- docs/02_Book_1_Relaunch_Reset_Diagnostic.md
- docs/03_Book_1_Story_Bible.md
- docs/04_Character_Bible.md
- docs/05_Technology_and_Threat_Model.md
- docs/06_Continuity_Canon_Locks.md
- docs/07_Prose_Style_and_Voice_DNA.md
- docs/08_Chapter_Production_Pipeline.md
- books/book-01/outline.md

Then summarize:

1. locked canon;
2. provisional canon;
3. unresolved decisions;
4. next best writing task.

Do not draft prose yet.
```

---

## Prompt 2 — Expand Book 1 outline

```text
We are working in dustinober1/Julie-O-Donnell-Series on Book 1 of the Julie O'Donnell Series.

First verify repo scope. Then read all control docs listed in README.md.

Task:

Expand books/book-01/outline.md into a complete commercial thriller outline of 45–60 chapters targeting 100,000–125,000 words.

Requirements:

- Preserve the prologue: six years ago, FOB near Pakistan border, Julie as Captain, Argus Beta, engineered SIGINT/timestamp pattern, Hargrove command pressure.
- Preserve the Act I hearing/cover-story wound: officials, oversight figures, and contractor-aligned voices attempt to reframe the disaster as Julie's officer hesitation instead of ARGUS failure.
- Preserve present-day Julie in Culpeper, Virginia with farmhouse/horse/fence-work life.
- Build the present-day crisis around ARGUS-ENT-4.6 / Apex Defense / RoboWarning and a potential Pakistan/India escalation risk.
- Keep Julie competent, guarded, and active.
- Make the AI/system threat grounded: bad data, incentives, confidence laundering, contractor pressure, political/command timelines.
- Do not make the AI sentient.

For each chapter include:

- chapter number;
- working title;
- POV;
- location;
- story function;
- conflict;
- clue/reveal;
- Julie internal beat;
- ARGUS/Apex/system element if any;
- chapter-ending hook.

Update books/book-01/outline.md only unless a clear canon change requires updating PROJECT_STATE.yaml or docs/06_Continuity_Canon_Locks.md.
```

---

## Prompt 3 — Create a chapter blueprint

```text
We are working in dustinober1/Julie-O-Donnell-Series.

Verify repo scope and read the control docs listed in README.md.

Task:

Create a detailed blueprint for Book 1 Chapter [Prologue], working title "[TITLE]", using books/book-01/chapter-blueprint-template.md.

Use the current Book 1 outline and preserve all canon.

The blueprint must include:

- POV;
- timeline;
- location;
- scene goal;
- conflict;
- opening image;
- beat-by-beat sequence;
- clue/reveal/escalation;
- Julie competence moment;
- internal/emotional beat;
- tech/system detail;
- continuity risks;
- ending hook;
- target word count.

Do not draft prose yet unless explicitly asked.
```

---

## Prompt 4 — Draft a chapter from blueprint

```text
We are working in dustinober1/Julie-O-Donnell-Series.

Verify repo scope and read:

- PROJECT_STATE.yaml
- docs/03_Book_1_Story_Bible.md
- docs/04_Character_Bible.md
- docs/05_Technology_and_Threat_Model.md
- docs/06_Continuity_Canon_Locks.md
- docs/07_Prose_Style_and_Voice_DNA.md
- docs/08_Chapter_Production_Pipeline.md
- books/book-01/outline.md
- [BLUEPRINT_FILE]

Task:

Draft Book 1 Chapter [NUMBER] in books/book-01/manuscript/ch-[###].md.

Requirements:

- Follow the approved blueprint.
- Start in scene.
- Maintain thriller pressure.
- Show Julie's competence through action and observation.
- Keep technical explanations brief and consequential.
- Avoid generic AI-writing markers.
- End with a strong hook.
- Do not change canon silently.

After drafting, provide a short report with:

1. word count estimate;
2. canon used;
3. unresolved issues;
4. next-chapter handoff.
```

---

## Prompt 5 — Chapter revision pass

```text
We are working in dustinober1/Julie-O-Donnell-Series.

Verify repo scope and read the relevant control docs plus books/book-01/manuscript/ch-[###].md.

Task:

Perform a revision pass on Chapter [NUMBER] for:

1. thriller pressure;
2. Julie competence;
3. ARGUS/Apex continuity;
4. institutional realism;
5. anti-AI prose cleanup;
6. chapter-ending hook.

Do not change major plot or canon unless there is a clear contradiction. If you find a contradiction, report it before revising.

Update the chapter file and provide a concise change report.
```

---

## Prompt 6 — Whole-outline continuity audit

```text
We are working in dustinober1/Julie-O-Donnell-Series.

Verify repo scope and read all control docs plus books/book-01/outline.md.

Task:

Audit the Book 1 outline for continuity, escalation, character agency, technology plausibility, and commercial thriller pacing.

Output sections:

1. Critical issues that must be fixed before drafting.
2. Recommended improvements.
3. Optional enhancements.
4. Chapter-by-chapter notes.
5. Canon updates required.

Do not edit files unless explicitly instructed after the audit.
```

---

## Prompt 7 — Recover pasted chat into canon

```text
We are working in dustinober1/Julie-O-Donnell-Series.

I am pasting prior chat/source material below. Your job is to reverse-engineer it into the existing repo docs.

First read:

- PROJECT_STATE.yaml
- docs/06_Continuity_Canon_Locks.md
- docs/99_Source_Reconstruction_Log.md

Then analyze the pasted source and classify each detail as:

- locked canon;
- provisional canon;
- contradiction with current repo;
- useful style/tone guidance;
- discarded or non-canon.

Update docs/99_Source_Reconstruction_Log.md first. Then update PROJECT_STATE.yaml and any relevant docs only for details that should become canon.

Do not draft prose.

PASTED SOURCE:
[PASTE HERE]
```
