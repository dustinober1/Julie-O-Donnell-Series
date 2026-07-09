# Julie O'Donnell Series Drift Audit — 2026-07-09

## Scope

- Audit target: whole series, with Book 1 as the active book.
- Repository verified: `Julie-O-Donnell-Series`, project `Julie O'Donnell Series`.
- Manuscript rewrite performed: no.
- Output path: `series-bible/series-drift-audits/2026-07-09-drift-audit.md`.

## Files Read

- `PROJECT_STATE.yaml`
- `progress.yaml`
- `.opencode/skills/julie-series-canon.md`
- `.opencode/skills/julie-series-memory.md`
- `.opencode/skills/julie-continuity-auditor.md`
- `.opencode/skills/julie-ai-plausibility.md`
- `.opencode/skills/julie-publication-readiness.md`
- `.opencode/commands/julie-series-drift-audit.md`
- `series-bible/01-series-premise-and-promise.md`
- `series-bible/02-julie-character-canon.md`
- `series-bible/03-recurring-cast.md`
- `series-bible/04-series-timeline.md`
- `series-bible/05-ai-threat-taxonomy.md`
- `series-bible/09-continuity-locks.md`
- `series-bible/10-book-by-book-series-arc.md`
- `series-bible/11-relationship-map.md`
- `series-bible/12-technology-rules.md`
- `series-bible/13-villain-and-antagonist-rules.md`
- `series-bible/14-mystery-and-clue-rules.md`
- `series-bible/canon-change-log.md`
- `series-bible/proposed-canon-updates.md`
- `series-bible/unresolved-series-threads.md`
- `books/book-01/book-dashboard.md`
- `books/book-01/book-bible.md`
- `books/book-01/ai-threat-design.md`
- `books/book-01/character-arcs.md`
- `books/book-01/timeline.md`
- `books/book-01/chapter-outline.md`
- `books/book-01/clue-map.md`
- `books/book-01/red-herring-map.md`
- `books/book-01/suspect-map.md`
- `books/book-01/chapter-facts.md`
- `books/book-01/continuity-log.md`
- `books/book-01/revision-watchlist.md`
- `books/book-01/publication-checklist.md`
- `books/book-01/publication/publication-readiness-report.md`
- `books/book-01/chapter-blueprints/prologue.md`
- `books/book-01/chapter-blueprints/ch-001.md`
- `books/book-01/chapter-blueprints/ch-002.md`
- `books/book-01/chapter-blueprints/ch-003.md`
- `books/book-01/chapters/prologue.md`
- `books/book-01/chapters/ch-001.md`
- `books/book-01/chapters/ch-002.md`
- `books/book-01/chapters/ch-003.md`
- `books/book-01/exports/manuscript.md`
- `books/book-02/book-dashboard.md`
- `books/book-02/book-bible.md`
- `books/book-02/ai-threat-design.md`
- `books/book-03/book-dashboard.md`
- `books/book-03/ai-threat-design.md`
- `books/book-04/book-dashboard.md`
- `books/book-04/ai-threat-design.md`

## Executive Status

Book 1 is pre-draft, not partially drafted. The apparent production drift comes from placeholder chapter, export, revision, continuity, canon-update, and publication files existing before their passes have run. The chapter files for the prologue and Chapters 1-3 explicitly say `Draft not started`, and the export file is also a placeholder.

The series canon itself is currently stable. The strongest risk is not manuscript inconsistency yet; it is scaffold-state ambiguity plus unresolved institutional roles being left open too long before chapter planning.

## Critical Findings

### Critical — Repository State Can Be Misread as Production Progress

- Evidence: `books/book-01/chapters/prologue.md`, `ch-001.md`, `ch-002.md`, and `ch-003.md` exist but all say `Draft not started`.
- Evidence: `books/book-01/exports/manuscript.md` exists but says it is a placeholder.
- Evidence: revision reports, continuity passes, and canon-update files exist but are marked `Not started`.
- Risk: future agents or workflows may treat file existence as pass completion or manuscript progress.
- Recommended repair: add a clear `stage` or `status` convention to dashboards and trackers that distinguishes `placeholder created`, `planned`, `drafted`, `revised`, `continuity-passed`, and `exported`.

### Critical — Production Hold Remains Active and Should Not Be Bypassed

- Evidence: `PROJECT_STATE.yaml`, `progress.yaml`, `series-bible/00-series-dashboard.md`, `books/book-01/book-dashboard.md`, and `books/book-01/publication-checklist.md` all preserve the production hold.
- Risk: chapter placeholders and export placeholders could tempt drafting or export assembly before scaffold review and role resolution.
- Recommended repair: leave production hold active until the Book 1 dashboard, chapter tracker, and unresolved role list are reconciled.

## Recommended Findings

### Recommended — Unresolved Institutional Roles Are Now Blocking Architecture

- Open items: Vance's exact government title, Mara Keene's agency placement, Evan Rusk's prologue-era role, Selene Cho's Apex title, Reed Calder's old/current titles, and the present-day agency chain.
- Drift risk: if these remain unresolved into chapter planning, the book may accumulate vague crisis rooms, overbroad authority, or implausible access.
- Recommended repair: resolve these before `/julie-plan-chapter 1 prologue` or `/julie-plan-chapter 1 1` produces final chapter blueprints.

### Recommended — Book 1 Threat Mechanism Is Stable but Narrow

- Current lock: provenance laundering, confidence inflation, dependent corroboration, whitelisted endpoint abuse, vendor relay/log purge, confidence collapse after contaminated packets are isolated.
- Positive finding: ARGUS/Argus naming is consistent across the files read.
- Drift risk: the planned mechanism is subtle and could become too abstract without concrete packet/source/log moments in the chapter plans.
- Recommended repair: each Act I and Act II blueprint should specify one reader-visible symptom of the mechanism, not just a conceptual label.

### Recommended — Julie's Arc Is Correctly Protected but Needs Scene-Level Guardrails

- Current arc: exile/avoidance to reluctant reentry to shareable proof, with only partial official-record correction.
- Positive finding: no current file makes Julie too healed or too eager to rejoin the system.
- Drift risk: because the actual prose has not started, the danger is still prospective: Julie could become either too passive from trauma or too instantly validated by old colleagues.
- Recommended repair: the first four chapter plans should each identify whether the scene emphasizes competence, wound pressure, constrained access, or proof-building.

### Recommended — Supporting Cast Is Functionally Designed but Not Yet Evolving

- Positive finding: Mara, Evan, Cho, Hargrove, Vance, and Reed each have a clear planned function.
- Drift risk: they are still role-functions more than relationship arcs because exact titles and relationship histories are unresolved.
- Recommended repair: resolve at least Mara's agency placement and prior relationship with Julie before drafting Chapter 1, because that relationship controls the reentry path and trust-under-constraint engine.

### Recommended — Future-Book Threat Differentiation Is Good but Unevenly Scaffolded

- Positive finding: Books 2-4 explicitly avoid repeating Book 1's provenance-laundering mechanism.
- Positive finding: Book 2 points toward medical triage/proxy variables/objective mismatch; Book 3 toward feedback loops/automation bias; Book 4 toward audit suppression/proxy exclusion/synthetic risk profiles.
- Drift risk: `series-bible/10-book-by-book-series-arc.md` sketches Books 5-8, but only Books 1-4 have visible book scaffolds.
- Recommended repair: no need to scaffold Books 5-8 yet, but future audits should track that the long arc extends beyond the current physical book folders.

### Recommended — Publication Assets Are Premature but Safely Marked

- Evidence: Book 1 publication files exist, but `publication-readiness-report.md` says `Not started` and the checklist says manuscript is not drafted.
- Risk: metadata and export files may be mistaken for readiness if status is not checked.
- Recommended repair: keep publication files, but do not run `/julie-publication-pass 1` until manuscript drafting, revision, continuity pass, AI-tell sweep, and metadata drafting are complete.

## Optional Findings

### Optional — Canon Bloat Is Currently Under Control

- `series-bible/proposed-canon-updates.md` has no pending queue.
- `series-bible/canon-change-log.md` contains only the initial scaffold entry.
- `books/book-01/chapter-facts.md` has no drafted-chapter facts yet.
- Recommendation: maintain the current restraint. Do not promote placeholder planning details unless they affect future chapters or books.

### Optional — Commercial Series Fatigue Risk Is Low at This Stage

- The series promise is clear: grounded AI/institutional thriller pressure with human accountability.
- The planned future domains are sufficiently varied.
- Main fatigue risk will appear later if every book resolves by the same proof pattern: Julie spots anomalous confidence, finds provenance trouble, exposes a protected vendor. Future books should vary not only the AI mechanism but also the investigation texture and personal stakes.

## Drift Checklist

| Check | Status | Notes |
|---|---|---|
| Julie is not becoming too healed too quickly | Pass | Current files preserve partial healing and incomplete vindication. |
| AI threats are not repeating too closely | Pass with watchpoint | Books 2-4 are differentiated; Books 5-8 remain high-level placeholders. |
| ARGUS/Argus canon is stable | Pass | Naming is consistent across canon, technology, and Book 1 files. |
| Institutional consequences do not disappear | Watch | Consequences are planned but not yet generated by a completed Book 1. |
| Supporting cast relationships evolve | Watch | Relationship engines exist, but exact roles/history remain unresolved. |
| Villains remain human and plausible | Pass with watchpoint | Reed, Vance, Cho, and Hargrove are grounded, but motives/titles need specificity. |
| The series arc advances | Pass for plan | Book 1 begins the corrected-record arc without overresolving it. |
| Technical realism remains grounded | Pass with watchpoint | Mechanism is plausible; chapter plans need concrete evidence beats. |
| Reader promise stays clear | Pass | Grounded intelligence/AI governance thriller lane is coherent. |

## Canon Repair Recommendations

Do not change locked canon yet. No manuscript fact currently requires promotion because the manuscript has not been drafted.

Recommended canon-adjacent repairs:

- Add or update a status note clarifying that placeholder chapter files, revision reports, continuity passes, canon-update reports, exports, and publication files do not mean those passes are complete.
- Resolve the six Book 1 role questions in `series-bible/unresolved-series-threads.md` before final chapter planning.
- After roles are resolved, record durable role decisions in the proper canon files and add a `series-bible/canon-change-log.md` entry.

## Book-Level Adjustment Recommendations

- Update `books/book-01/chapter-outline.md` so the Chapter Tracker reflects existing placeholder files and their real status.
- Keep `books/book-01/book-dashboard.md` aligned with the actual workflow stage: scaffolded/pre-draft/chapter planning pending.
- Before drafting, run context and planning for the prologue first unless deliberately skipping the prologue.
- Ensure early blueprints include concrete visible signs of the ARGUS mechanism: confidence rising without independence, too-clean synchronization, provenance ambiguity, and institutional resistance to uncertainty.

## Next Safe Step

Run:

```text
/julie-chapter-context 1 prologue
```

Then run:

```text
/julie-plan-chapter 1 prologue
```

Do not draft prose until the prologue context packet and blueprint are complete and reviewed.
