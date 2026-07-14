# 20. CONTROL-PACK MAINTENANCE RULES

## Authority and file placement

1. The accepted-manuscript inventory at `../ACCEPTED_MANUSCRIPT.yaml` controls which prose files are canon.
2. Accepted prose must live under `../manuscript/`.
3. Unaccepted prose must live under `../drafts/`.
4. No draft may be treated as canon because it is complete, titled, revised, mission-locked, or stored in Git.
5. `../../../PROJECT_STATE.yaml` is the sole authority for production status and navigation. Other status summaries are subordinate.
6. The series recurring-character ledger at `../../../series/recurring-character-ledger.md` controls cross-book continuity fields but cannot overrule accepted prose.
7. Archive files and external snapshots are never active sources of truth.

## Promotion and acceptance

8. Every chapter begins with a mission lock or approved chapter brief.
9. Every draft remains outside the accepted manuscript until the acceptance gate is complete.
10. Promotion requires one same-pass commit that:
    - moves the final reviewed prose into `../manuscript/`;
    - updates `../ACCEPTED_MANUSCRIPT.yaml`;
    - updates `../../../PROJECT_STATE.yaml`;
    - updates accepted word count and endpoint;
    - updates chapter status;
    - updates every affected timeline, character, relationship, evidence, knowledge, technology, location, public-narrative, antagonist, and thread record; and
    - records the acceptance verdict.
11. Later chapters may not use an unaccepted draft endpoint as canon.
12. A chapter title remains a draft title until promotion.
13. Rejected or superseded drafts remain available through Git history; do not create active filenames such as `final2`, `new-final`, or `latest`.

## Timeline and physical continuity

14. Update the master timeline whenever accepted prose uses an exact timestamp.
15. Record both EDT and IST when events materially affect the cross-border crisis.
16. Never hide a time conflict by changing only a table. Record the discrepancy until the manuscript itself is repaired.
17. Update injuries after every fall, fight, vehicle movement, treatment, rest period, worsening symptom, and meaningful elapsed-time change.
18. Do not record recovery without treatment and elapsed time.
19. Preserve the accepted Chapter 5-to-6 repair and L3-7 handoff unless an explicit manuscript-repair package supersedes it.

## Evidence and knowledge

20. Record every evidence transfer with time, location, transferor, recipient, seal condition, reason, and witnesses.
21. Keep the case, administrator board, recovery cartridge, Partition A, Partition B, WSS local audit, Chen records, and Sharma records as distinct objects.
22. Update both “what it proves” and “what it does not prove” whenever evidence changes.
23. Never promote registered authority into physical human custody without separate evidence.
24. Update the knowledge matrix whenever a character witnesses a screen, hears a record, decrypts content, receives evidence, learns a public claim, or appears in a private antagonist scene.
25. Never invent the contents of incomplete, excluded, encrypted, or unavailable records.

## Plot and series continuity

26. Update the thread-disposition matrix after every accepted chapter.
27. Resolve Book 1 obligations before using a series hook to defer them.
28. Move resolved threads into a payoff record rather than deleting them.
29. Update the recurring-character ledger whenever a returning character's status, knowledge, injury, relationship, legal exposure, location, or future function changes.
30. Do not assign a future-book role as canon until the character survives and reaches an accepted Book 1 end state.
31. High-level Act III architecture may guide word budget and sequence, but chapter functions become controlling only through individual chapter locks.
32. Plans for unwritten chapters remain non-canon.

## Word count and ending control

33. Recount accepted manuscript words whenever prose is promoted or revised.
34. Record only the accepted total in `PROJECT_STATE.yaml` and `../ACCEPTED_MANUSCRIPT.yaml`.
35. Draft word counts remain separate.
36. The Book 1 planning target is 112,500 words within an allowed range of 100,000–125,000 words.
37. Word count never justifies a scene that does not advance plot, character, evidence, or consequence.
38. The ending contract must be checked before accepting the climax, resolution, or epilogue.

## Revision and audit

39. Narrative House Style v2.2 controls craft but cannot create or change canon.
40. Run a discrepancy check before each new act or major phase.
41. Run an evidence-limits check before chapters involving investigation, arrest, testimony, publication, decryption, or institutional custody.
42. Run a full forward continuity audit before final revision.
43. Run a reverse-order payoff audit after the ending exists.
44. Before publication, audit exact times, EDT/IST conversion, titles, vehicles, security bypasses, certificate claims, evidence seals, injuries, knowledge, relationships, public narrative, and the official-record theme.

## Archive policy

45. The former Google Doc and uploaded Word snapshot are historical migration inputs only.
46. Do not edit external historical snapshots as active manuscripts.
47. Superseded status and planning states are preserved by Git history; do not keep duplicate active copies.
48. Archive records must say what is historical, why it is non-controlling, and where the active replacement lives.

## Historical application record — accepted Chapter 15

- `31-chapter-15-acceptance-review.md` records **ACCEPT** after one capitalization-only copyedit at 5,993 words.
- Accepted inventory is Prologue and Chapters 1–15 at **81,586** words.
- Accepted endpoint is **07:56:40 EDT / 17:26:40 IST**.
- The Chapter 15 draft has been removed; the corrected blob now lives only at `../manuscript/chapters/chapter-15.md`.
- Seven originals are separately sealed in MPD custody; no final federal/technical intake is established.
- Book 1 remains not publication-ready.

## Historical pre-acceptance application record — Chapter 16 first draft (superseded)

The entries below preserve the pre-acceptance audit state only. They are superseded by the Chapter 16 acceptance maintenance record that follows and do not describe current production status.

- `32-chapter-16-mission-lock.md` remains the controlling production plan for Chapter 16 — **The Hold Order**.
- One active first draft existed only at `../drafts/chapter-16.md`.
- Exact draft word count was **6,024**.
- Draft opening was **07:56:40 EDT / 17:26:40 IST**.
- Draft endpoint was **08:15:52 EDT / 17:45:52 IST**, inside the approved maximum.
- The draft used Julie primary, one bounded Marcus ambulance cutaway, one bounded Sharma cutaway, and a return to Julie.
- The draft kept all seven packages separate, sealed, offline, and in MPD custody; no accepted ledger was updated as though those drafted events occurred.
- Chapter 16 remained unaccepted and non-canon until the formal acceptance gate issued **ACCEPT** and a synchronized promotion commit was completed.

## Chapter 16 acceptance maintenance record — 2026-07-13

`33-chapter-16-acceptance-review.md` records **ACCEPT** after one surgical POV-firewall revision at 6,024 words. The reviewed blob `dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8` now lives only at `../manuscript/chapters/chapter-16.md`; the draft copy is removed. The revision removes narrator-level Washington, Hartwell, Payload 88, and MPD-specific knowledge from Sharma's bounded close-third movement without changing word count, events, or endpoint.

The accepted manifest, project state, status files, affected canon ledgers, series character ledger, and validation workflow are synchronized to 87,610 words and the 08:15:52 EDT / 17:45:52 IST endpoint. The validator protects Chapters 14, 15, and 16 and verifies the accepted total and endpoint.

## Historical Chapter 17 mission-lock maintenance record — 2026-07-13

- `34-chapter-17-mission-lock.md` approved **The First Examination** as planning only.
- Accepted inventory remained Prologue and Chapters 1–16 at **87,610 words**.
- Accepted endpoint remained **08:15:52 EDT / 17:45:52 IST**.
- No Chapter 17 prose existed at that gate.
- Special Agent Leila Grant was the named planned examiner without creating accepted character or event canon.
- `MPD-901446` was the sole package planned for opening; the other six remained sealed and unopened.
- MPD physical custody and the 09:12:52 EDT / 18:42:52 IST maximum endpoint were locked.

## Chapter 17 first-draft maintenance record — 2026-07-13

- One active first draft now exists only at `../drafts/chapter-17.md`.
- Exact draft word count is **5,888**.
- Draft opening is **08:15:52 EDT / 17:45:52 IST**.
- Draft endpoint is **09:12:52 EDT / 18:42:52 IST**.
- The draft uses Julie primary and one bounded Special Agent Leila Grant examination-room movement.
- The draft opens only `MPD-901446`; the other six packages remain sealed and unopened.
- The draft remains **unaccepted and non-canon**.
- Accepted inventory remains Prologue and Chapters 1–16 at **87,610 words**.
- Accepted endpoint remains **08:15:52 EDT / 17:45:52 IST**.
- `ACCEPTED_MANUSCRIPT.yaml` and all accepted story ledgers remain unchanged.
- Chapter 18 and later prose do not exist.

Next maintenance gate: conduct the formal Chapter 17 acceptance review. Do not draft Chapter 18 or create a complete remainder-of-Act-III outline.
