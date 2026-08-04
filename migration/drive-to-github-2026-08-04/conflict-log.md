# Book 2 Drive-to-GitHub Migration — Conflict Log

Conflicts found while migrating Book 2 out of Google Drive on 2026-08-04. Each records what disagreed, which side controls, and what was done. Nothing was resolved silently.

---

## BC-01 — The Drive control documents forbid GitHub authority

**Type:** Governance conflict, resolved in GitHub's favor by author instruction.

`00 - README - Book 2 Control Center` stated, verbatim:

> **Source of Truth**
>
> All Book 2 work lives inside the Google Drive folder 02_BOOK 2 within the Julie O'Donnell Series folder.
>
> GitHub is not a Book 2 source, backup, staging area, review system, or publication authority. Do not create or rely on Book 2 branches, commits, pull requests, issues, repository control files, or commit hashes. A GitHub artifact cannot establish or change Book 2 canon.

Its authority order likewise placed Drive folders at every level.

`10 - Book 2 Chapter 2 Drafting Authorization and Manuscript Drafting` opened its authority section with:

> Google Drive remained the sole working, canon, and production environment.

**Conflict:** these statements contradict `PROJECT_STATE.yaml`, which has recorded since 2026-07-25 that "GitHub is the sole active source of truth" with Drive limited to "archived snapshots, review copies generated from GitHub, large production binaries, and nontechnical collaborator distribution only." Book 1 and Book 2 were operating under opposite governance.

**Resolution:** the author directed on 2026-08-04 that Book 2 move to the repository. The control center's source-of-truth and authority-order sections were rewritten on import to record GitHub as authoritative and to place repository paths in the authority order. The superseded Drive text is preserved above.

The Chapter 2 drafting record was **not** rewritten. It is a closed historical record of a workstream that genuinely did run under Drive authority, and rewriting it would falsify that history. A note was added to its provenance header pointing here.

**Follow-up for the author:** the Drive documents still say what is quoted above. Anyone opening Drive will read that GitHub cannot establish canon. Consider adding a redirect notice at the top of the Drive control center so the two do not drift apart again.

---

## BC-02 — Two different prologues were both live

**Type:** Canon conflict between two Drive documents, resolved by date and specificity.

`01 - Prologue Situation & Scene Lock - Duffield Data Center Fire` (modified 2026-07-20) locks the prologue as:

- Cumberland Ridge Data Services, a fictional data center outside Duffield, Scott County, Virginia
- POV: Joel Stidham, 42, senior overnight facilities engineer
- Second character: Derek Sluss, 29, his mentee
- Eight locked scenes, an electrical surge and fire, and a two-part evidence design

`06 - Book 2 Chapter Architecture` (modified 2026-07-25) locks the prologue as:

- Title: "The Warning That Cannot Have Happened"
- POV: veteran duty manager
- Location: dam control room
- 1,800–2,200 words, four movements, ending with the emergency release withheld and the warning withdrawn

These are different openings with different POV characters, locations, casts, and inciting events. Neither document referenced the other. Both were marked LOCKED.

**Resolution:** confirmed by the controlling document itself. `04 - Book 2 Premise & Story Architecture Lock`, imported after this conflict was first recorded, states the supersession explicitly:

> This decision supersedes the earlier Cumberland Ridge Data Services / Duffield, Virginia data-center opening and its associated Joel Stidham, Derek Sluss, and anti-automation development direction. Those earlier decisions remain preserved in the Decision Log as historical development records only. They do not control the active Book 2 outline or manuscript.

The chapter architecture is therefore correct, and the reasoning that pointed to it independently also holds: it is five days later, it is cited as governing by the Chapter 1 drafting authorization, and its prologue is the one the accepted Chapter 1 continues from — Chapter 1 opens in the Canadian joint response center dealing with the withdrawn spillway warning, which is the dam prologue's ending state, not a data-center fire.

The Duffield lock was imported and marked SUPERSEDED rather than dropped. Its two-part evidence design, its rule against portraying displaced workers as inherently violent, and its Joel/Derek character work may still be reusable elsewhere.

**Follow-up for the author:** none required for correctness — the supersession is explicit and recorded. Worth noting only that the Duffield lock contains the only worked-out treatment of the automation-and-employment theme in the Book 2 material, and the Drive copy carries no marking to warn a reader that it is retired.

---

## BC-03 — A different project's control documents sit in a Book 2 folder

**Type:** Filing conflict. No content was imported.

The Drive folder `1Hc9qwOCu2yCitjHQbraXL5cmdUfyK1lq` contains documents titled as Book 2 material:

- `00 - README - Book 2 Control Center`
- `01 - Book 2 Editorial Audit and Repair Plan`
- `CURRENT - Book 2 Drive Production Bible`
- `02 - Chapter POV Timeline and Word Count Ledger`
- `04 - Book 2 Prose Texture and Voice Watchlist`
- `05 - Book 2 Packaging Metadata and Production Status`
- `06 - Book 2 Authoritative Calendar and Elapsed-Time Map`
- `07 - Book 2 Injury, Body-State, Clothing, and Equipment Map`

These belong to a **different series**. The voice watchlist tracks characters named Caden, Seraith, Vashara, and Inquisitor Arven; motifs including jasmine, sea, lyre, and minor third; "monster embodiment" and "gothic diction"; and a 41-chapter manuscript of roughly 79,110 words at Entry 46 of its own audit program.

None of it concerns Julie O'Donnell.

**Resolution:** excluded from this migration. Nothing from that folder was imported.

**Follow-up for the author:** this is a live hazard, not a filing curiosity. Both projects have a "Book 2 Control Center," a "Book 2 Chapter POV Timeline and Word Count Ledger," and numbered control documents in overlapping ranges. Voice guidance written for a gothic fantasy is one folder away from the Julie drafting workflow. Renaming that folder to name its own series would remove the risk.

---

## BC-04 — A governing document that does not exist

**Type:** Missing authority. Recorded, not resolved.

Six Book 2 documents cite `05 - Book 2 Act Architecture` as governing authority:

- `outline/06-chapter-architecture.md` §1 lists it among "Governing documents."
- `control/08-chapter-01-drafting-authorization.md` lists it under "Governing Documents Verified."
- `control/09-chapter-01-formal-acceptance.md` lists it under "Documents Verified," described as "verified as readable and reviewed."
- `control/10-chapter-02-drafting-authorization.md` places it third in its control hierarchy.
- `control/03-decision-log-and-canon-ledger.md` and `outline/07-scene-architecture-and-chapter-mission-locks.md` also reference it.

**No such document exists in Drive.** Searches by exact title and by title-plus-content returned nothing, and it was not present in any of the three Book 2 folders enumerated for this migration.

Two of the citing documents assert that it was verified as readable during their own production gates. That assertion cannot have been accurate.

**Practical effect:** limited. The act-level content those documents needed is present in `outline/06-chapter-architecture.md` §4, which allocates all five acts to chapters with word budgets, and in the premise lock's escalation material. Nothing in the drafted chapters depends on the missing file.

**One discrepancy worth the author's eye:** the premise lock's planning checklist anticipates a **four-part** act architecture, while the implemented chapter architecture uses **five** acts (I–V). The premise lock does refer to Act V elsewhere, so this looks like an early planning value that was superseded rather than a live contradiction — but it was never reconciled in writing, and the document that would have reconciled it is the one that does not exist.

**Follow-up for the author:** decide whether `05` was ever written. If it was and lives outside the three Book 2 folders, it should be imported. If it never existed, the six citing documents overstate their own verification, and the cleanest fix is to point them at `06-chapter-architecture.md` §4 instead.

---

## Summary

| ID | Conflict | Disposition |
|---|---|---|
| BC-01 | Drive documents forbid GitHub authority | Resolved for GitHub; control center rewritten, historical record preserved |
| BC-02 | Two live prologue designs | Chapter architecture controls; Duffield lock marked superseded |
| BC-03 | Another series' documents filed as Book 2 | Excluded; flagged to the author |
| BC-04 | Six documents cite an act architecture that does not exist | Recorded; content is covered elsewhere, no drafting impact |
