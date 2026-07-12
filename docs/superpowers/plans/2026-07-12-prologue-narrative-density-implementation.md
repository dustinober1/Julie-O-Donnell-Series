# Prologue Narrative-Density Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the Julie O’Donnell house style to v2.1 and revise the Prologue with moderate narrative compression while preserving every canon, timing, casualty, and emotional lock.

**Architecture:** The work is divided into four independently reviewable units: style-control update, Prologue revision, revision documentation/status tracking, and final continuity validation. The style guide defines the dialogue and paragraph-density rules first; the Prologue then applies those rules without changing plot or canon.

**Tech Stack:** GitHub Markdown manuscript and control documents; GitHub connector for file reads/writes and commit verification; manual continuity audit plus deterministic text counts.

## Global Constraints

- GitHub `dustinober1/Julie-O-Donnell-Series` on `main` is the sole source of truth.
- Do not access or reference the former Google Doc.
- Preserve exact timestamps: 09:41:16 abort initiation, 09:41:19 weapon release, 09:41:20 gateway authentication.
- Preserve 11 civilian deaths, including five children.
- Preserve Imran Khalid’s misidentification as Farid Anwar and Anwar’s escape.
- Preserve the overwritten local cache and the absence of surviving proof beyond Julie’s observation.
- Preserve Marcus’s late support, “There was confusion in the room,” and the Fort Belvoir confrontation.
- Preserve the final institutional judgment and Chapter 1 continuity.
- Do not identify the current conspiracy as responsible for the old strike.
- Do not imitate a living author.
- Target 10–15% fewer words, but dramatic completeness controls.
- Improve page density by reducing low-value dialogue turns and isolated one-sentence paragraphs outside crisis beats.

---

### Task 1: Update Narrative House Style to v2.1

**Files:**
- Modify: `docs/Julie_ODonnell_Narrative_House_Style_v2.md`

**Interfaces:**
- Consumes: approved design in `docs/superpowers/specs/2026-07-12-prologue-narrative-density-design.md`
- Produces: controlling v2.1 rules for dialogue function, narrative compression, isolated-paragraph use, and page-density auditing

- [ ] **Step 1: Read the complete current style guide and identify insertion points**

Read the version header, dialogue rules, sentence-and-paragraph rules, production checks, and lock statement.

Expected finding: v2.0 already controls exposition compression but does not explicitly define when dialogue should become narrative or require page-density metrics.

- [ ] **Step 2: Update the version and production state**

Change the header to:

```markdown
**Version:** 2.1  
**Status:** Locked for new chapter production and revision passes  
**Repository baseline reviewed:** `<CURRENT_HEAD_BEFORE_STYLE_UPDATE>`  
**Accepted manuscript scope reviewed:** Prologue and current accepted chapters  
**Current production state:** Chapter 12 and Chapter 13 prose exist; Chapter 12 has received a House Style revision; Prologue narrative-density revision authorized
```

- [ ] **Step 3: Add the Narrative Density and Dialogue Function section**

Insert a dedicated section after the existing institutional-dialogue diagnosis and before detailed paragraph rules:

```markdown
## Narrative density and dialogue function

Dialogue remains a signature tool when it creates conflict, asserts or challenges authority, forces a decision, reveals deception or divided loyalty, changes custody or force, or lands an emotional wound.

Convert an exchange to narrative when it only transfers routine information, repeats an established technical distinction, lists unchanged status, qualifies the same fact for a third time, or creates question-and-answer rhythm without resistance or consequence.

For each exchange, ask:

1. Does the answer create conflict, surprise, cost, or a changed decision?
2. Does the wording reveal character or institutional position?
3. Would narrative summary preserve the information with less page space?
4. Has the distinction already been dramatized once?

If the exchange fails the first two tests and passes the third or fourth, compress it into narrative.
```

- [ ] **Step 4: Add the isolated-paragraph and page-density rules**

Add:

```markdown
### Isolated-paragraph rule

Reserve isolated one-sentence paragraphs for discoveries, reversals, system transitions, physical failures, moral refusals, irreversible actions, chapter turns, or lines whose silence creates necessary pressure.

Group low-pressure observations, minor reactions, routine movement, and supporting qualifications into fuller paragraphs.

### Page-density audit

Every revision must review:

- dialogue-turn count;
- isolated one-sentence paragraph count;
- fragment frequency;
- repeated screen-text translation;
- repeated evidentiary qualification;
- paragraph density outside action sequences.

No fixed dialogue percentage controls the book. Dramatic function controls.
```

- [ ] **Step 5: Update the production checklist and lock statement**

Add dialogue-function and page-density checks to the final production checklist. Revise the lock statement so v2.1 explicitly accelerates both word flow and printed-page flow without flattening action rhythm.

- [ ] **Step 6: Verify the style guide contains no conflict with existing rules**

Check that:
- dialogue remains the preferred vehicle for institutional conflict;
- short paragraphs remain permitted under pressure;
- no fixed dialogue ratio is introduced;
- canon authority remains above style control.

- [ ] **Step 7: Commit the style guide update**

Commit message:

```text
Update Julie O'Donnell house style to v2.1
```

---

### Task 2: Revise the Prologue with moderate narrative compression

**Files:**
- Modify: `books/book-01/manuscript/prologue.md`
- Read for continuity: `books/book-01/manuscript/chapters/chapter-01.md`

**Interfaces:**
- Consumes: House Style v2.1 and the approved design
- Produces: revised accepted Prologue with unchanged canon and a denser page shape

- [ ] **Step 1: Record the current Prologue baseline**

Capture:
- exact current blob SHA;
- word count;
- dialogue-turn count;
- isolated one-sentence paragraph count;
- exact required timestamps and casualty facts.

- [ ] **Step 2: Revise the anomaly setup**

Keep:
- ozone/hot-canvas opening;
- Argus Beta feed;
- 94.1 percent confidence;
- exact 11.2-second cadence;
- weather degradation;
- smooth target line.

Compress:
- Baines’s repeated-run exchange;
- isolated repetition that does not yet increase pressure;
- routine commands that can live inside narrative action.

- [ ] **Step 3: Revise the Hargrove confrontation**

Preserve the strongest conflict:
- “What the fuck is the holdup?”
- feed compromised;
- too clean/too perfect;
- hidden uncertainty;
- Hargrove’s command pressure;
- Julie demanding sixty seconds.

Convert repeated encryption, movement, and thermal rebuttal pairs into one narrative-supported confrontation after the physical contradiction is established.

- [ ] **Step 4: Preserve and sharpen the Exercise 7C discovery**

Keep:
- carrier noise as hardest element to fake;
- identical repeated sequence;
- Exercise 7C match;
- Fort Belvoir synthetic origin;
- Marcus supporting abort only in the final seconds.

Use short paragraphs only as the countdown changes choices.

- [ ] **Step 5: Preserve the four-second abort sequence exactly**

Retain:

```text
ABORT REQUEST INITIATED: 09:41:16
WEAPON RELEASE: 09:41:19
GATEWAY AUTHENTICATION COMPLETE: 09:41:20
```

The visual sequence must still make clear:
- Julie initiated before release;
- Argus held the message;
- authentication completed after release;
- the weapon was already away.

- [ ] **Step 6: Compress casualty and convoy aftermath without reducing consequence**

Preserve:
- two children visible before impact;
- compound destruction;
- real convoy leaving under cover;
- eleven civilian deaths;
- five children;
- Imran Khalid identity;
- Anwar escape.

Remove redundant fragments only where the same consequence has already landed.

- [ ] **Step 7: Compress the investigation summary**

Summarize the first three panels in narrative. Preserve the final hearing as a live scene because the missing four seconds and certified-parameter defense create the institutional wound.

Do not invent new evidence or a surviving cache.

- [ ] **Step 8: Preserve Marcus’s testimony and resignation confrontation**

Retain:
- “There was confusion in the room.”
- the fact that Marcus shapes truth to survive review;
- Julie cleared;
- Hargrove’s nonpermanent letter;
- Argus Beta remaining operational;
- resignation three months later;
- “You did what you could defend.”
- medal discarded;
- final three-line judgment.

- [ ] **Step 9: Compare the revised ending against Chapter 1**

Verify Chapter 1 can still accurately refer to:
- six years of separation;
- Marcus’s defensible testimony;
- analyst delay;
- Julie’s resignation;
- nightmares and distrust;
- the same physical pattern returning.

- [ ] **Step 10: Commit the Prologue revision**

Commit message:

```text
Revise Prologue for narrative density
```

---

### Task 3: Add revision documentation and update project state

**Files:**
- Create: `artifacts/book-01-prologue-house-style-v2-1-revision-note.md`
- Modify: `PROJECT_STATE.yaml`
- Modify only if needed: `books/book-01/manuscript/STATUS.md`

**Interfaces:**
- Consumes: final revised Prologue and style-guide commit
- Produces: auditable counts, documented canon preservation, and current revision status

- [ ] **Step 1: Create the revision note**

Include:
- starting and ending commit SHAs;
- original and revised word counts;
- word-count delta and percentage;
- original and revised dialogue-turn counts;
- original and revised isolated-paragraph counts;
- major cuts;
- preserved dialogue;
- technical facts preserved;
- Chapter 1 handoff result;
- remaining risks.

- [ ] **Step 2: Update `PROJECT_STATE.yaml`**

Set:
- `narrative_house_style.version` to `2.1`;
- `manuscript_revisions_applied` to true;
- revision list/status to include Prologue and Chapter 12;
- next recommended action to the next selected chapter revision rather than drafting an already existing Chapter 13.

Do not alter accepted canon endpoint or Chapter 13 status beyond what the repository currently proves.

- [ ] **Step 3: Update manuscript status only if stale**

If `books/book-01/manuscript/STATUS.md` still says the Prologue is unrevised or Chapter 13 is undrafted, correct only those stale fields supported by current files.

- [ ] **Step 4: Commit documentation and status**

Commit message:

```text
Document Prologue narrative-density revision
```

---

### Task 4: Final continuity and page-density validation

**Files:**
- Read: `books/book-01/manuscript/prologue.md`
- Read: `books/book-01/manuscript/chapters/chapter-01.md`
- Read: `docs/Julie_ODonnell_Narrative_House_Style_v2.md`
- Read: `PROJECT_STATE.yaml`
- Read: `artifacts/book-01-prologue-house-style-v2-1-revision-note.md`

**Interfaces:**
- Consumes: all final files
- Produces: verified final HEAD and completion report

- [ ] **Step 1: Run exact-fact checks**

Verify the revised Prologue contains:
- `94.1 percent`;
- `11.2 seconds`;
- `09:41:16`;
- `09:41:19`;
- `09:41:20`;
- eleven civilians;
- five children;
- Imran Khalid;
- Farid Anwar;
- overwritten local cache;
- “There was confusion in the room”;
- “You did what you could defend.”

- [ ] **Step 2: Run knowledge and canon checks**

Verify:
- no current-conspiracy attribution;
- no sentient Argus language;
- no surviving old cache;
- Marcus still supports Julie late;
- Julie is cleared rather than convicted;
- Hargrove is not secretly tied to the current plot.

- [ ] **Step 3: Run page-density checks**

Confirm:
- word reduction is within the intended range or documented if outside;
- dialogue turns are lower;
- isolated one-sentence paragraphs are lower outside the four-second crisis;
- the four-second sequence retains sharp visual spacing;
- final ending remains isolated and strong.

- [ ] **Step 4: Verify GitHub HEAD and file state**

Confirm the latest commits are present on `main`, fetch the committed files, and ensure no stale metadata remains.

- [ ] **Step 5: Report completion**

Report:
- starting and ending HEAD;
- commits;
- files changed;
- all count deltas;
- major stylistic improvement;
- continuity validation;
- remaining risks;
- recommended next chapter for the same moderate narrative-density pass.
