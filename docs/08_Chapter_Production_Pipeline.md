# 08 — Chapter Production Pipeline

## Purpose

This pipeline is for producing high-quality thriller chapters with AI/coding-agent assistance while preserving canon, continuity, and a non-AI feel.

Do not skip directly from a thin outline to final prose. Each chapter should move through planning, drafting, review, revision, and canon update.

## Standard folder structure

```text
books/book-01/
  outline.md
  chapter-blueprint-template.md
  manuscript/
    ch-001.md
    ch-002.md
    ...
```

Optional later folders:

```text
books/book-01/
  blueprints/
  revision-notes/
  continuity-reports/
```

## Phase 0 — Canon load

Before working on any chapter, read:

1. `PROJECT_STATE.yaml`
2. `docs/00_START_HERE_Project_Dashboard.md`
3. `docs/03_Book_1_Story_Bible.md`
4. `docs/04_Character_Bible.md`
5. `docs/05_Technology_and_Threat_Model.md`
6. `docs/06_Continuity_Canon_Locks.md`
7. `docs/07_Prose_Style_and_Voice_DNA.md`
8. `books/book-01/outline.md`

## Phase 1 — Chapter blueprint

For each chapter, create or confirm:

- chapter number;
- chapter title;
- POV;
- timeline/date position;
- location;
- scene objective;
- external conflict;
- internal conflict;
- clue/reveal/escalation;
- technology/system detail introduced;
- continuity dependencies;
- chapter-ending hook;
- target word count.

Use `books/book-01/chapter-blueprint-template.md`.

## Phase 2 — Draft pass

Draft the chapter from the approved blueprint.

Requirements:

- Start in scene, not summary.
- Maintain thriller pressure.
- Show Julie's competence through specific observations and choices.
- Keep technology legible and consequential.
- Avoid generic AI prose markers.
- End with propulsion.

## Phase 3 — Structural review

Review the chapter for story function:

- Does it advance the main plot?
- Does it increase pressure?
- Does it reveal or complicate character?
- Does it earn its place in the book?
- Does it avoid repeating an earlier beat?
- Does it create a reason to read the next chapter?

## Phase 4 — Canon and continuity review

Check against:

- Julie's military/intelligence background;
- Argus/Apex naming rules;
- prologue wound;
- present-day system threat;
- timeline;
- supporting character roles;
- unresolved vs locked canon.

Flag any contradiction instead of silently changing canon.

## Phase 5 — Thriller pressure pass

Strengthen:

- scene objectives;
- reversals;
- deadlines;
- access restrictions;
- institutional pressure;
- stakes clarity;
- chapter hooks.

Cut or compress:

- static explanation;
- repeated emotional beats;
- long room descriptions;
- generic dread;
- dialogue that restates known facts.

## Phase 6 — Line-level anti-AI pass

Search for and revise:

- repetitive sentence openings;
- overused body reactions;
- vague intensifiers;
- generic thriller phrases;
- exposition-heavy dialogue;
- too-clean thematic statements;
- unnatural over-explanation;
- repeated words within paragraphs.

## Phase 7 — Update control docs

After a chapter is accepted, update as needed:

- `books/book-01/outline.md` if the outline changed;
- `docs/06_Continuity_Canon_Locks.md` if canon is newly locked;
- `PROJECT_STATE.yaml` if major status changes;
- a future chapter-specific continuity report if added.

## Chapter quality gates

A chapter is not ready if:

- Julie does not make an active choice;
- the scene could be removed without changing the plot;
- the system threat is abstract;
- a character explains instead of acts;
- the chapter ends flat;
- the prose sounds like a generic AI thriller;
- canon is changed without updating control docs.

## Recommended chapter lengths

- Prologue: 1,500–2,500 words.
- Early chapters: 2,000–3,000 words.
- Mid-book pressure chapters: 1,800–2,800 words.
- Final-act chapters: 1,500–2,500 words with faster cuts.

## Recommended POV strategy

Primary POV should be Julie unless the outline deliberately uses cutaways.

Possible cutaway types:

- contractor containment;
- political pressure;
- command center escalation;
- antagonist manipulation;
- old witness or ally.

Cutaways must add pressure or dramatic irony. Do not use them just to explain plot.

## Commit message conventions

Use clear commit messages:

- `add Book 1 chapter 1 blueprint`
- `draft Book 1 prologue`
- `revise chapter 3 for canon and pressure`
- `update ARGUS naming canon`
- `add character bible entries`

## Definition of done for a drafted chapter

A drafted chapter is done when it has:

1. Approved blueprint.
2. Complete prose.
3. Continuity check.
4. Thriller pressure pass.
5. Anti-AI line pass.
6. Updated outline/control docs if needed.
7. Clear next-chapter handoff.
