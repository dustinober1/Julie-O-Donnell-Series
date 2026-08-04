# 71. Book 1 Detail Continuity Findings — Phase 0 and Mechanical Phase 1

**Plan:** `70-detail-continuity-audit-plan.md`
**Phases executed:** Phase 0 (baseline), Phase 1 mechanical half (D1, D2, D3, D8), Phase 2 rules R1–R8, Phase 3 adjudication of everything those rules surfaced
**Also executed:** targeted R9/R10/R11 judgment checks over Chapters 5–14 (§6a)
**Not yet executed:** the full scene-card pass (D4, D5, D6, D7, D9), rules R12–R14, and any judgment check over Chapters 15–24
**Audit head commit:** `08e1b7df53624a8bbea1bbfd7c18062c6f0f84bb`
**Manuscript state:** frozen; no accepted prose file was modified by this pass
**Date:** 2026-08-04

---

## 1. Phase 0 baseline

| Check | Result |
|---|---|
| `tools/count_book1_words.py` | 105,157 words, matches manifest |
| `tools/validate_book1_publication_readiness.py` | PASS |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 17 tests, OK (1 skipped) |
| Per-file SHA-256 vs. `ACCEPTED_MANUSCRIPT.yaml` | 25 of 25 match, 0 mismatches |

The manuscript is exactly what the manifest says it is. Everything below concerns story fact, not integrity.

## 2. Extraction

`tools/extract_book1_detail_index.py` produced **10,983 detail records** from the 25 accepted files into `artifacts/book1-detail-index.json`:

| Class | Records |
|---|---|
| D1 clock and calendar | 535 |
| D2 named entities | 7,757 |
| D3 designators and codes | 520 |
| D8 quantities | 2,171 |

## 3. Rule results

`tools/check_book1_detail_rules.py`:

| Rule | Checked | Result |
|---|---|---|
| R1 EDT/IST offset | 6 pairs | **clean** |
| R2 scene chronology | 68 scene headers | 1 item, adjudicated NO ISSUE |
| R3 countdown monotonicity | 29 values across 5 clocks | **clean** |
| R4 sub-second restatement | 12 values | **clean** |
| R5 designator canonical form | 76 designators | **clean** |
| R6 entity near-miss names | 149 recurring names | 4 items, all adjudicated NO ISSUE |
| R7 anchored quantities | 4 facts | **clean** |
| R8 first-mention index | 1,179 entries | recorded for the R11 knowledge review |

**No hard rule failed.** Every one of the eleven items the review rules raised was adjudicated and resolved without a prose change.

This is a genuinely good result and worth stating plainly: across 285 timestamp occurrences, 76 distinct designators, and 12 sub-second forensic timestamps that later chapters re-cite, the drafting holds. The `07:08:09.442` challenge response restated in Chapters 12, 13, 14, 19, and 22 matches its origin every time. `APX-DIR-0019`, `SSO-NS-004`, `PCF-27`, `K-17`, `L3-7`, and `VAL-088` never drift in form. All five concurrent Act II countdown clocks decrease correctly, and the external commit clock's arithmetic lands exactly on the 05:00 anchor.

## 4. Finding DC-01 — control documents place the crisis on the wrong calendar days

**Classification:** LEDGER-STALE
**Severity:** structural; affects every control that dates Book 1, and the series handoff
**Accepted prose:** correct and internally consistent. **No prose change is recommended.**

### The defect

Book 1's control documents file the entire crisis under **October 13**. The prose does not support that. It places the opening on **October 12**, crosses midnight inside Chapter 5, and puts the facility climax and MPD intake on **October 13**.

### Evidence

Three independent chains agree.

**1. Chapter 5 narrates a continuous midnight crossing.**

The chapter opens at 15:41 EDT and runs without a break through 18:06, 21:40, **00:18**, 03:57, 04:27, and 04:50. Scene headers at 04:27 and 04:50 are in Eastern Daylight Time, in narrative present. Chapters 6 through 14 continue that morning to 07:49.

**2. The stated dates from Chapter 15 onward fix which side of midnight is which.**

Chapter 15 states **October 13** at 07:49 — the same moment Chapter 14 ends. Chapter 16 states October 13 and closes at 22:18 with Julie waiting for morning. Chapter 17 states **October 14** and opens on overnight imaging. That sequence is coherent and leaves no room to read the predawn run as anything but October 13, which places Chapters 1 through Chapter 5's opening on **October 12**.

**3. Chapter 21 anchors the same reading from outside the main thread.**

> Price's last active audit session ended at 17:58 on **October 12**. His classified authority was suspended five minutes later. […] The office request had been created **the next morning at 06:41**.

17:58 on October 12 falls inside Chapter 5's evening. "The next morning at 06:41" falls inside the Chapter 11 window, which the derived chronology independently assigns to October 13. Both land exactly where the midnight crossing puts them.

The full scene-by-scene derivation is in `artifacts/book1-derived-chronology.md`, regenerable with `--chronology`.

### What the controls say instead

| Control | Current statement | Prose-derived |
|---|---|---|
| `continuity/01-master-timeline.md:17` | `## October 13 — immediate crisis`, spanning 10:43 through 22:18 | Two calendar days: 10:43–21:40 is October 12; 00:18–22:18 is October 13 |
| `PROJECT_STATE.yaml:31` | `crisis_day: "October 13"` | Crisis opens October 12 and climaxes October 13 |
| `PROJECT_STATE.yaml:32` | `investigation_and_release: "October 14-16"` | Investigation opens October 13 (MPD intake 08:18, Sarah 09:03, counsel 22:18) |

The master timeline's October 13 heading covers 10:43 through 22:18 — thirty-six hours of story under a twenty-four-hour label.

### How it happened

`continuity/01-master-timeline.md:35` records the mechanism:

> The accepted developmental revision resets the final lower-tier run to the predawn release window below. Earlier 16:xx drafting timestamps are historical and noncanonical in accepted prose.

Moving the climax from 16:xx to 04:xx pushed it across midnight. The prose absorbed the change correctly. The date headings above it were never revisited, because no control in the repository compares a stated date against the number of midnights the prose actually crosses. `59-post-research-continuity-audit.md` §4.4 checked EDT/IST conversions and event ordering and found no mismatch — correctly, because there is none. It did not check day assignment.

### Why it matters despite the prose being correct

1. The master timeline is marked **LOCKED** and is the reference a future correction would consult. A correction that trusted the October 13 heading would introduce a real prose defect.
2. `series/book-01-timeline-and-clock-handoff.md` and the recurring-character ledger carry Book 1's chronology into Books 2–5. An off-by-one day propagates.
3. Chapters 1 through 14 never state a date. Nothing in the prose contradicts the wrong reading, so it can persist indefinitely.

### Corroboration from the series layer

`series/book-01-timeline-and-clock-handoff.md` — an active, series-level control — **already carries the correct two-day structure**. It has a `# October 12` section holding Price's SAR and his 17:58 suspension, and a `# October 13 — Initial Operation` section holding 04:59:50, 05:14:36, 06:41:18, 07:08, and the 07:51–07:54 release sequence. (Its 02:14 entry was on the wrong side of that boundary — see DC-03 below.)

That is the same reading the prose gives, and it directly contradicts the book-level master timeline. Two active controls disagreed about what day the climax falls on, and the series-level one was right. The book-level timeline was repaired to match.

### Repair applied 2026-08-04

Applied under author authorization. **No accepted prose file was touched; all 25 manifest hashes still match.**

| File | Change |
|---|---|
| `continuity/01-master-timeline.md` | Split `## October 13 — immediate crisis` into `## October 12 — first review day` and `## October 13 — facility re-entry and release window`. Added the derivation note and the previously missing overnight bridge (16:30 certification, 18:06, 21:40, 00:18, 03:57) that carries the story across midnight, plus the 04:27–04:51 re-entry sequence. |
| `continuity/07-public-narrative-ledger.md` | Retitled the Apex/fugitive narrative section to October 12–13 and noted which stages fall on which day. |
| `PROJECT_STATE.yaml` | `crisis_day: "October 13"` → `crisis_days: "October 12-13"`; `investigation_and_release: "October 14-16"` → `"October 13-16"`; added a `calendar_note` pointing at the derivation. |
| `61-copyedit-style-sheet.md` | Main action dates October 13–16 → October 12–16. |

Verified already correct and left unchanged: `continuity/02-evidence-custody-ledger.md` (06:39:16 on October 13), `continuity/01-master-timeline.md` line for the 07:51:38–07:52:12 October 13 source range, and the entire series handoff.

Historical records that state the superseded reading — `59-post-research-continuity-audit.md`, `51-developmental-revision-summary.md`, `56-copyedit-style-sheet.md` — were deliberately left alone. They document the state that existed when they were written.

## 4a. Finding DC-02 — a superseded re-entry row survived in the master timeline

**Classification:** CONTRADICTION between two active controls
**Severity:** material; the row described an architecture the repository had already replaced
**Repair:** applied 2026-08-04

`continuity/01-master-timeline.md` carried:

> `| 15:41–16:14 | Elias is held; Julie and Marcus re-enter; the three reach the core approach. | LOCKED |`

That row describes the **pre-repair** 16:xx architecture. Three lines below it, the same file states that "earlier 16:xx drafting timestamps are historical and noncanonical in accepted prose." The row contradicted the note directly beneath it, and both were marked LOCKED.

The accepted architecture in `repairs/chapter-05-to-06-continuity-repair/README.md` is explicit: the first stormwater approach happens *before* 16:30 and is **abandoned**; re-entry happens *before 05:00*. The prose agrees — Julie and Marcus clear the culvert mouth at 15:57, wait out the night, and re-enter at 04:27.

Replaced with four rows verified line by line against Chapter 5:

| Time | Event | Prose |
|---|---|---|
| 15:41–15:43 | Elias held; Vance interviews him | ch05:7 |
| 15:49–15:57 | First stormwater approach and withdrawal | ch05:215, 217, 243 |
| 16:21–16:30 | 05:00 support object identified from the Ford; culvert re-entry planned | ch05:268, 276, 325 |
| 04:27–04:51 | Re-entry, Compliance Four reunion, core access lift | ch05:393, 455, 682, 1090 |

This finding is a direct consequence of DC-01: forcing the two-day split required examining the split point, and the stale row was sitting on it.

## 4b. Finding DC-03 — the 02:14 attribution was dated to the wrong day

**Classification:** CONTRADICTION between prose and an active series control
**Severity:** material; 02:14 is the book's central unresolved thread and carries into Books 2–5
**Repair:** applied 2026-08-04

`series/book-01-timeline-and-clock-handoff.md` filed the 02:14 identity construction under `# October 13 — Initial Operation`. The prose puts it a day earlier.

Chapter 2 is explicit. Elias, at his desk during the Apex review day, finds the deployment authorization:

> His employee cryptographic token had approved the bridge at **02:14 that morning**. At 02:14, Elias had been asleep in his townhouse.

"That morning" is the morning of the day he is working — the Apex review day, which is **October 12**. The construction precedes Julie's 11:52 arrival by roughly nine and a half hours, and precedes the facility climax by about twenty-six hours, not two and a half.

This defect was invisible under the old single-day reading. When every scene was filed under October 13, "02:14 that morning" and the 04:50 climax sat on the same day and nothing contradicted anything. Correcting DC-01 is what exposed it — and it is the clearest demonstration of why DC-01 mattered even though the prose was right.

Note that the series handoff had the harder half correct: it already separated Price's October 12 record from the October 13 operation. Only the 02:14 line was on the wrong side.

**Repair:**

| File | Change |
|---|---|
| `series/book-01-timeline-and-clock-handoff.md` | Moved the 02:14 entry from the October 13 section to October 12, with the Chapter 2 basis stated. Left a pointer in the October 13 section so the dependency stays visible. |
| `continuity/01-master-timeline.md` | Added 02:14 to the October 12 table. The book-level timeline had never carried it as a dated event at all. |

The undated references to "the original 02:14 deployment" in the evidence, knowledge, and technology ledgers were checked and are correct as written; they assert no day.

## 5. Items adjudicated as NO ISSUE

| Item | Rule | Adjudication |
|---|---|---|
| Chapter 8 header `04:58` follows Chapter 7's `04:58:11` | R2 | Deliberate scene-boundary restatement of the same minute. Chapter 8 opens eleven seconds before Chapter 7's last stamp, which reads as continuous. NO ISSUE. |
| `Ford` / `Fort` | R6 | Julie's truck and Fort Belvoir. Distinct. |
| `India` / `Indian` | R6 | Country and adjective. Distinct. |
| `Pakistan` / `Pakistani` | R6 | Country and adjective. Distinct. |
| `Service` / `Services` | R6 | Defense Criminal Investigative *Service*; Apex Protective *Services*. Both correct throughout. |

## 6. Corrections made to the rules themselves

Recorded because each was a false positive the accepted manuscript exposed, and each is now locked by a test in `tools/test_book1_detail_rules.py`:

| Symptom | Cause | Fix |
|---|---|---|
| 5 false countdown failures in Chapter 8 | Act II runs five concurrent clocks; the rule treated them as one sequence | Reads are attributed to the clock their own line names |
| `discharge` matched Chapter 5 | "the stormwater **discharge** rose" is weather | Labels must name the instrument (`DISCHARGE IN`, `suppression clock`) |
| 73 chronology findings | Compared screen text and countdowns against narrative time | Only standalone scene headers count as narrative present |
| 23 entity variants including `Clean`/`Clear`, `Make`/`Take` | Counted sentence-initial capitals as names | Only mid-sentence capitals count |
| 37 quantity findings | Reported recurrence rather than checking facts | Curated single-valued anchored facts, tightly patterned |

The lesson generalizes: a rule that cannot distinguish a stormwater discharge from a suppression countdown will produce confident nonsense at volume. Every rule here was tightened until its output was small enough to adjudicate by hand.

## 6a. Targeted judgment checks on B2 and B3

Not the full scene-card pass. These were focused checks on the three
judgment rules most likely to hold a defect, run over Chapters 5–14 — the
batches carrying the midnight crossing, the repaired 5-to-6 seam, the
concurrent countdowns, and the densest custody load. Recorded so a later
full pass knows what has and has not been looked at.

**R9 possession chain — clean.**

The Chapter 5 to Chapter 6 shutter handoff matches the accepted repair
architecture exactly. Chapter 5 ends with Marcus holding the case handle and
the tool bag (ch05:1225); Chapter 6 has him throw the case through ahead of
the others, fling the bag through on Julie's shout, and dive after it
(ch06:23–29). The bag splits open and scatters a flashlight, tape, and the
pry bar — all three of which were established as its contents in Chapter 5
(ch05:481, 535, 1004).

The Chapter 10 custody formation is meticulous. Julie records the case seal
indicator, serial, integrity-manifest identifier, and display state verbatim,
then names every person who handled it since Building Three and notes
explicitly that Elias did not (ch10:305–313). The cartridge, board, and dead
transponder are separated, bagged, and logged individually (ch10:327, 598).
The board stays with Elias throughout (ch10:321, 598; ch11:11, 212, 232).

**R10 capability ceilings — clean.**

Julie's wrist injury is acquired on the page: she takes Marcus's weight
through the shutter (ch06:27) and immediately after, "Julie flexed the hand
that had taken his weight. Pain ran from her thumb into her wrist"
(ch06:37). Every subsequent action respects it — left forearm to shove the
case through (ch07:473), injured right *forearm* rather than grip to catch a
weapon hand (ch07:445), and an explicit re-check in the cutout where she
tries to flex the wrist and the pain has deepened (ch10:219).

Elias's bandaged index finger and Marcus's ribs are tracked with the same
consistency (ch11:11, 212; ch07:443).

**R11 knowledge ordering — clean at the index level.**

The R8 first-mention index was checked against the order in which each
entity becomes usable. Nothing is used before it is introduced. PCF-27 is
named when the van is acquired (ch09), Fenwick before the intake (ch11 into
ch12), Hartwell before the garage (ch12 into ch13), SSO-NS-004 at the WSS-4
session (ch12), and the investigative cast — Grant, Alvarez, Webb, Kessler —
only once the investigation reaches them (ch16, ch20). The 07:08
synchronization is discussed in Chapter 10 as a scheduled future event, not
as knowledge held early.

This is index-level, not scene-level. It confirms nothing is referenced
before introduction; it does not confirm that every character's private
knowledge state is correct at every moment. That remains open.

## 7. What this pass does not cover

R1–R8 reach only what pattern matching can see. The classes most likely to hold undetected defects are untouched:

- **D5 / R9 possession chain** — who physically holds the seven packages in every scene
- **D6 / R10 capability ceilings** — Julie's right hand, Marcus's ribs, Elias's hip and finger
- **D7 / R11 knowledge ordering** — characters acting on information before they receive it
- **D4 / R12 physical transit**, **D9 / R13 surface continuity**, **R14 proof-ceiling discipline**

Per §10 of the plan, the registries coming back clean was treated as evidence that drafting was tighter than remembered, so the judgment effort was aimed at B2 and B3 rather than spread across all 25 files. Those targeted checks (§6a) also came back clean.

What remains is the scene-level work over **Chapters 15–24** — the custody, examination, and public-correction chapters where R14 proof-ceiling discipline carries the most weight — plus R12 physical transit and R13 surface continuity across the whole book. On the evidence so far, the expected yield from the prose is low and the expected yield from the control layer is higher, since all three defects found to date were control defects.

## 8. Verdict

# PASS WITH THREE CONTROL DEFECTS, ALL REPAIRED

The accepted prose passed every mechanical rule and required no change. Three defects were found in the control layer, all repaired, none requiring a prose change:

- **DC-01** — Book 1's date headings compressed two calendar days into one.
- **DC-02** — a superseded 16:xx re-entry row survived in the master timeline, contradicting a note three lines beneath it.
- **DC-03** — the 02:14 identity construction, the book's central unresolved thread, was dated to the wrong day in the series handoff.

DC-02 and DC-03 were both found *because* DC-01 was repaired. Neither was reachable while the calendar collapsed two days into one: DC-02 sat exactly on the split point, and DC-03 was self-consistent under the wrong reading. That is the argument for the bottom-up direction in one line — the top-down passes had examined all three of these files and found nothing, because they were checking the facts someone had already thought to record.
