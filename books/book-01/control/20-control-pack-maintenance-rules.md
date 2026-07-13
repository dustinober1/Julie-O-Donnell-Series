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

## Current application record — accepted Chapter 15

- `31-chapter-15-acceptance-review.md` records **ACCEPT** after one capitalization-only copyedit at 5,993 words.
- Accepted inventory is Prologue and Chapters 1–15 at **81,586** words.
- Accepted endpoint is **07:56:40 EDT / 17:26:40 IST**.
- The Chapter 15 draft has been removed; the corrected blob lives only at `../manuscript/chapters/chapter-15.md`.
- Seven originals are separately sealed in MPD custody; no final federal/technical intake is established.
- Book 1 remains not publication-ready.

## Current application record — approved Chapter 16 mission lock

- `32-chapter-16-mission-lock.md` is the approved pre-draft control for Chapter 16 — **The Hold Order**.
- The lock opens exactly at the accepted Chapter 15 endpoint: **07:56:40 EDT / 17:26:40 IST**.
- The accepted manuscript remains Prologue and Chapters 1–15 at **81,586** words.
- `../ACCEPTED_MANUSCRIPT.yaml`, accepted prose, accepted count, and accepted endpoint are unchanged.
- The lock’s dominant function is to force a named federal preservation authority behind the interim MPD chain while all seven packages remain separate, sealed, offline, and in MPD custody.
- The planned POV is Julie primary, one bounded Marcus ambulance cutaway, one bounded Sharma cutaway, and a return to Julie.
- The target range is **5,800–6,500 words**.
- The maximum planned endpoint is **08:16:40 EDT / 17:46:40 IST**.
- The lock requires Marcus’s attributable six-years-ago correction, Hackett’s named preservation choice, and a bounded allied preservation acknowledgment.
- The lock prohibits resolution of Hartwell presenter/serial, WSS plaintext, K-17 access, Phase B, reconstruction truth/authorship/purpose, final federal custody, technical merits, and public vindication.
- The mission lock is planning only and does not update timeline, character, relationship, evidence, knowledge, technology, organization, location, antagonist, public-narrative, or recurring-character canon.
- Chapter 16 may be drafted only at `../drafts/chapter-16.md`.
- Do not draft Chapter 17 or create a complete remainder-of-Act-III outline during Chapter 16 drafting.
