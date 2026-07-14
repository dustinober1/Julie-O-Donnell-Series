# 20. CONTROL-PACK MAINTENANCE RULES

## Purpose

These rules keep accepted prose, the manifest, production status, control files, drafts, and validation aligned without allowing planning to become accidental canon.

## Authority order

1. Accepted manuscript prose listed in `../ACCEPTED_MANUSCRIPT.yaml`.
2. The accepted-manuscript inventory.
3. Current canon and continuity controls.
4. Approved chapter-specific mission locks.
5. Series controls.
6. Drafts.
7. Archive and Git history.
8. Navigation summaries.

A lower source never overrides a higher source.

## Acceptance and drafting rules

- A mission lock is approved planning, not story canon.
- A draft remains non-canon until a formal review issues **ACCEPT**.
- Promotion must move prose to `../manuscript/chapters/`, update the manifest, recount accepted words, update the endpoint, and synchronize all materially affected controls in one production pass.
- No unaccepted chapter may live under `../manuscript/`.
- Only one active draft path per chapter is allowed.
- Accepted chapter files must not be silently edited outside an explicit review or repair process.

## Word-count rules

- Count UTF-8 Markdown using whitespace-delimited tokens through `tools/count_book1_words.py`.
- Planning and drafting do not change accepted totals.
- Accepted totals change only when prose is promoted.
- The current accepted total is **87,610 words** through Chapter 16.

## Evidence and knowledge maintenance

Every accepted-chapter promotion must update, where materially affected:

- master timeline;
- character and injury state;
- relationship and trust state;
- evidence and custody ledger;
- knowledge matrix;
- technology rules;
- organizations and authorities;
- location/security architecture;
- antagonist model;
- public narrative;
- open threads;
- chapter status;
- Act III state;
- word budget;
- thread disposition; and
- recurring-character ledger.

A plan may identify a future evidence source, examiner, or endpoint without treating that future event as accepted fact.

## Current accepted locks

- Accepted inventory: Prologue and Chapters 1–16.
- Accepted total: 87,610 words.
- Accepted endpoint: 08:15:52 EDT / 17:45:52 IST.
- Chapter 14 protected blob: `78f7fff02cd271fecbc94f7daf7151dbebbd5c6d`.
- Chapter 15 protected blob: `b8e7e2ae573a6c25ea096121c75acee867f3fad2`.
- Chapter 16 protected blob: `dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8`.
- Chapter 17 prose does not exist.

## Chapter 17 mission-lock maintenance record

`34-chapter-17-mission-lock.md` approves **The First Examination** as planning only.

The lock must remain consistent with these constraints:

- opening from the exact accepted Chapter 16 endpoint;
- Julie primary POV;
- one bounded Special Agent Leila Grant examination-room POV;
- `MPD-901446` as the sole package planned for opening;
- MPD physical custody throughout;
- the other six packages sealed and unopened;
- read-only physical-token examination;
- no biometric, private-key signing act, live network, Apex credential, or second package;
- planned maximum endpoint 09:12:52 EDT / 18:42:52 IST;
- planning range 5,600–6,300 words;
- no public vindication, final federal receiver, K-17 result, Phase B definition, WSS plaintext, or human-operator finding.

## Validator requirements for the planning gate

The repository validator must require:

- accepted total 87,610;
- accepted manifest ending at Chapter 16;
- unchanged accepted endpoint;
- protected Chapter 14, 15, and 16 blobs and counts;
- presence of `34-chapter-17-mission-lock.md`;
- absence of Chapter 17 prose under drafts and manuscript during this planning-lock PR;
- Chapter 17 as the next drafting gate only after the lock is approved; and
- absence of temporary repair workflows or duplicate controls.

## Current next gate

Draft exactly one complete first version at `../drafts/chapter-17.md` from `34-chapter-17-mission-lock.md`. Do not draft Chapter 18 or create a complete chapter-by-chapter outline for the remainder of Act III.
