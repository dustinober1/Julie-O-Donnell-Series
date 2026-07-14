#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "fae5bbb8862f7275d802d7c0b76f1449a4979cf9"
BRANCH = "agent/chapter-17-acceptance-review"
DRAFT_BLOB = "1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1"
CH17_WORDS = 5888
OLD_TOTAL = 87610
NEW_TOTAL = 93498
OLD_ENDPOINT = "08:15:52 EDT / 17:45:52 IST"
NEW_ENDPOINT = "09:12:52 EDT / 18:42:52 IST"

def run(*args: str, capture: bool = False) -> str:
    cp = subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    return cp.stdout.strip() if capture else ""

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

def read(rel: str) -> str:
    path = ROOT / rel
    require(path.is_file(), f"missing required file: {rel}")
    return path.read_text(encoding="utf-8")

def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")

def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def append_block(rel: str, marker: str, block: str) -> None:
    text = read(rel)
    if marker not in text:
        write(rel, text.rstrip() + "\n\n" + block.strip() + "\n")

def normalize_active_status(rel: str) -> None:
    text = read(rel)
    replacements = [
        ("Prologue and Chapters 1–16", "Prologue and Chapters 1–17"),
        ("Prologue and Chapters 1-16", "Prologue and Chapters 1-17"),
        ("Chapters 13–16 accepted", "Chapters 13–17 accepted"),
        ("Chapters 13-16 accepted", "Chapters 13-17 accepted"),
        ("87,610", "93,498"),
        ("08:15:52 EDT / 17:45:52 IST", "09:12:52 EDT / 18:42:52 IST"),
        ("books/book-01/drafts/chapter-17.md", "books/book-01/manuscript/chapters/chapter-17.md"),
        ("../drafts/chapter-17.md", "../manuscript/chapters/chapter-17.md"),
        ("First draft exists; unaccepted; **non-canon**", "Accepted canon"),
        ("Draft path", "Accepted path"),
        ("Exact draft word count: **5,888 whitespace-delimited Markdown words**", "Exact words: **5,888**"),
        ("Draft opening", "Opening"),
        ("Draft endpoint", "Endpoint"),
        ("Acceptance-gate status:** Not yet conducted", "Verdict:** **ACCEPT**"),
        ("first draft exists; unaccepted; non-canon", "accepted and promoted; canon"),
        ("first draft exists but is not accepted", "is accepted and promoted"),
        ("unaccepted and non-canon", "accepted and canon"),
        ("acceptance gate not yet run", "formal acceptance gate passed with ACCEPT"),
        ("conduct the formal Chapter 17 acceptance review", "preserve the accepted Chapter 17 state; no Chapter 18 work was performed in this pass"),
        ("Conduct the formal Chapter 17 acceptance review", "Preserve the accepted Chapter 17 state; no Chapter 18 work was performed in this pass"),
        ("Formal Chapter 17 acceptance review", "Completed Chapter 17 formal acceptance review"),
        ("formal Chapter 17 acceptance review", "completed Chapter 17 formal acceptance review"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    text = re.sub(
        r"(?m)^.*Chapter 17.*(?:draft|unaccepted|non-canon).*$",
        lambda m: m.group(0)
            .replace("first draft", "accepted chapter")
            .replace("draft", "accepted manuscript")
            .replace("unaccepted", "accepted")
            .replace("non-canon", "canon"),
        text,
    )
    write(rel, text)

head = run("git", "rev-parse", "HEAD", capture=True)
run("git", "merge-base", "--is-ancestor", BASELINE, head)
current_branch = run("git", "branch", "--show-current", capture=True)
require(current_branch == BRANCH, f"wrong branch: {current_branch}")
require(True, "working tree prevalidated by workflow")

required_full_reads = [
    "books/book-01/manuscript/prologue.md",
    *[f"books/book-01/manuscript/chapters/chapter-{n:02d}.md" for n in range(1, 17)],
    "books/book-01/drafts/chapter-17.md",
    "books/book-01/control/34-chapter-17-mission-lock.md",
    "books/book-01/control/25-chapter-acceptance-gate.md",
    "books/book-01/control/33-chapter-16-acceptance-review.md",
    "PROJECT_STATE.yaml",
    "books/book-01/ACCEPTED_MANUSCRIPT.yaml",
    *[f"books/book-01/control/{n:02d}-" + name for n, name in [
        (4, "source-of-truth-canon-locks.md"),
        (5, "master-timeline.md"),
        (6, "character-state-ledger.md"),
        (7, "relationship-and-trust-matrix.md"),
        (8, "evidence-and-chain-of-custody-ledger.md"),
        (9, "knowledge-and-information-control-matrix.md"),
        (10, "technology-and-system-rules.md"),
        (11, "organizations-authorities-and-institutional-control.md"),
        (12, "location-and-security-architecture.md"),
        (13, "antagonist-objectives-and-conspiracy-model.md"),
        (14, "public-narrative-versus-actual-record.md"),
        (15, "open-plot-threads-and-payoff-matrix.md"),
        (16, "chapter-by-chapter-status-record.md"),
        (17, "style-tone-and-narrative-rules.md"),
        (18, "act-iii-entry-state.md"),
        (20, "control-pack-maintenance-rules.md"),
        (22, "book-1-ending-contract.md"),
        (23, "word-budget-and-act-iii-architecture.md"),
        (24, "thread-disposition-matrix.md"),
    ]],
    "series/recurring-character-ledger.md",
    "docs/Julie_ODonnell_Narrative_House_Style_v2.md",
    "docs/Julie_ODonnell_Narrative_House_Style_v2_1.md",
    "docs/Julie_ODonnell_Narrative_House_Style_v2_2.md",
    "books/book-01/control/README.md",
    "books/book-01/drafts/README.md",
    "books/book-01/manuscript/STATUS.md",
    ".github/workflows/book1-manuscript-validation.yml",
]
for rel in required_full_reads:
    read(rel)

draft = ROOT / "books/book-01/drafts/chapter-17.md"
require(blob_sha(draft) == DRAFT_BLOB, f"reviewed draft blob changed: {blob_sha(draft)}")
chapter17 = draft.read_text(encoding="utf-8")
require(len(chapter17.split()) == CH17_WORDS, "Chapter 17 count changed")
require(chapter17.startswith("# Chapter 17 - The First Examination\n"), "Chapter 17 title changed")
require("08:15:52 Eastern Daylight Time" in chapter17[:500], "Chapter 17 opening changed")
require("17:45:52 Indian Standard Time" in chapter17[:500], "Chapter 17 IST opening changed")
require("09:12:52 Eastern Daylight Time / 18:42:52 Indian Standard Time" in chapter17[-2200:], "Chapter 17 endpoint changed")
require(chapter17.count("# Chapter ") == 1, "unexpected extra chapter heading")
require("Chapter 18" not in chapter17, "Chapter 18 material appears in Chapter 17")
for bad in ("TODO", "DRAFTING NOTE", "ALTERNATE VERSION", "PLACEHOLDER"):
    require(bad not in chapter17, f"drafting artifact remains: {bad}")

protected = {
    "chapter-14.md": ("78f7fff02cd271fecbc94f7daf7151dbebbd5c6d", 5763),
    "chapter-15.md": ("b8e7e2ae573a6c25ea096121c75acee867f3fad2", 5993),
    "chapter-16.md": ("dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8", 6024),
}
for name, (sha, words) in protected.items():
    path = ROOT / "books/book-01/manuscript/chapters" / name
    require(blob_sha(path) == sha, f"protected blob changed: {name}")
    require(len(path.read_text(encoding="utf-8").split()) == words, f"protected count changed: {name}")

manifest_before = read("books/book-01/ACCEPTED_MANUSCRIPT.yaml")
require("accepted_words: 87610" in manifest_before, "accepted baseline total changed")
require("sequence: 17" not in manifest_before, "Chapter 17 already accepted")
require(not (ROOT / "books/book-01/manuscript/chapters/chapter-17.md").exists(), "Chapter 17 manuscript already exists")
require(not list((ROOT / "books/book-01").rglob("chapter-18.md")), "Chapter 18 prose exists")

accepted_ch17 = ROOT / "books/book-01/manuscript/chapters/chapter-17.md"
accepted_ch17.parent.mkdir(parents=True, exist_ok=True)
draft.rename(accepted_ch17)
require(blob_sha(accepted_ch17) == DRAFT_BLOB, "promotion changed Chapter 17 bytes")

manifest = """schema_version: 2
book: 1
title: null
status: "Controlling accepted-manuscript inventory"
last_verified: "2026-07-14"
accepted_words: 93498
word_count_method:
  name: "UTF-8 Markdown whitespace-delimited token count"
  implementation: "For each accepted file, len(Path(path).read_text(encoding='utf-8').split()); sum the accepted inventory"
  utility: "tools/count_book1_words.py"
  note: "All visible Markdown tokens are counted consistently, including headings, datelines, and screen-field text"
accepted_endpoint:
  chapter: 17
  eastern: "09:12:52 EDT"
  india: "18:42:52 IST"
  location: "Secure MPD evidence intake after the first independent single-package examination, with MPD-901446 resealed and all seven packages remaining in MPD custody"

accepted_files:
  - sequence: 0
    type: "prologue"
    title: "Six Years Ago"
    path: "books/book-01/manuscript/prologue.md"
  - sequence: 1
    type: "chapter"
    title: "The Official Version"
    path: "books/book-01/manuscript/chapters/chapter-01.md"
  - sequence: 2
    type: "chapter"
    title: "The Poisoned Feed"
    path: "books/book-01/manuscript/chapters/chapter-02.md"
  - sequence: 3
    type: "chapter"
    title: "The Exit Protocol"
    path: "books/book-01/manuscript/chapters/chapter-03.md"
  - sequence: 4
    type: "chapter"
    title: "Burn Notice"
    path: "books/book-01/manuscript/chapters/chapter-04.md"
  - sequence: 5
    type: "chapter"
    title: "The Second Clock"
    path: "books/book-01/manuscript/chapters/chapter-05.md"
  - sequence: 6
    type: "chapter"
    title: "The Descent"
    path: "books/book-01/manuscript/chapters/chapter-06.md"
  - sequence: 7
    type: "chapter"
    title: "The Human Key"
    path: "books/book-01/manuscript/chapters/chapter-07.md"
  - sequence: 8
    type: "chapter"
    title: "The 05:00 Abort"
    path: "books/book-01/manuscript/chapters/chapter-08.md"
  - sequence: 9
    type: "chapter"
    title: "The Life-Safety Override"
    path: "books/book-01/manuscript/chapters/chapter-09.md"
  - sequence: 10
    type: "chapter"
    title: "The Capital Connection"
    path: "books/book-01/manuscript/chapters/chapter-10.md"
  - sequence: 11
    type: "chapter"
    title: "Going Offensive"
    path: "books/book-01/manuscript/chapters/chapter-11.md"
  - sequence: 12
    type: "chapter"
    title: "The Sterling Trap"
    path: "books/book-01/manuscript/chapters/chapter-12.md"
  - sequence: 13
    type: "chapter"
    title: "The Carrier Stream"
    path: "books/book-01/manuscript/chapters/chapter-13.md"
  - sequence: 14
    type: "chapter"
    title: "The Witness Line"
    path: "books/book-01/manuscript/chapters/chapter-14.md"
  - sequence: 15
    type: "chapter"
    title: "The Split Record"
    path: "books/book-01/manuscript/chapters/chapter-15.md"
  - sequence: 16
    type: "chapter"
    title: "The Hold Order"
    path: "books/book-01/manuscript/chapters/chapter-16.md"
  - sequence: 17
    type: "chapter"
    title: "The First Examination"
    path: "books/book-01/manuscript/chapters/chapter-17.md"

excluded_from_canon:
  - path: "books/book-01/drafts/"
    reason: "Unaccepted prose only; no active Book 1 chapter draft after Chapter 17 promotion"
  - path: "archive/"
    reason: "Historical provenance only"
  - path: "docs/superpowers/"
    reason: "Design and implementation records, not story canon"

rules:
  - "Only files listed under accepted_files are accepted prose."
  - "The accepted total excludes all draft, archive, planning, repair-history, and design files."
  - "Adding a file to manuscript without updating this manifest does not accept it."
  - "Adding a file to this manifest without an explicit acceptance review and matching prose commit is invalid."
  - "Every promotion commit must update accepted_words, accepted_endpoint, PROJECT_STATE.yaml, chapter status, and all affected control ledgers."
"""
write("books/book-01/ACCEPTED_MANUSCRIPT.yaml", manifest)

project_state = """project: "Julie O'Donnell Series"
schema_version: 4
last_updated: "2026-07-14"

status_authority:
  file: "PROJECT_STATE.yaml"
  scope: "Production status and navigation only; not story canon"
  rule: "Any duplicated status summary must be corrected to match this file in the same production pass"

story_authority:
  accepted_manifest: "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
  accepted_prose_root: "books/book-01/manuscript/"
  control_pack_root: "books/book-01/control/"
  series_bible_root: "series/"
  draft_root: "books/book-01/drafts/"
  archive_root: "archive/"

active_book:
  number: 1
  title: null
  genre: "Contemporary geopolitical techno-thriller / military-intelligence thriller"

  word_budget:
    minimum: 100000
    planning_target: 112500
    maximum: 125000
    accepted_words: 93498
    words_to_planning_target: 19002
    minimum_words_remaining: 6502
    maximum_words_remaining: 31502
    accepted_words_before_chapter_13: 63655
    chapter_13_words: 6175
    accepted_words_before_chapter_14: 69830
    chapter_14_words: 5763
    accepted_words_before_chapter_15: 75593
    chapter_15_words: 5993
    accepted_words_before_chapter_16: 81586
    chapter_16_words: 6024
    accepted_words_before_chapter_17: 87610
    chapter_17_words: 5888
    accepted_act_iii_words: 29843
    count_method: "UTF-8 Markdown whitespace-delimited tokens; tools/count_book1_words.py"

  accepted_canon:
    manifest: "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
    prologue: true
    chapters: "1-17"
    acts:
      act_i: "complete"
      act_ii: "complete"
      act_iii: "Chapters 13-17 accepted; later prose not drafted"
    endpoint:
      chapter: 17
      eastern: "09:12:52 EDT"
      india: "18:42:52 IST"
      location: "Secure MPD evidence intake after the first independent single-package examination"
      status: "MPD-901446 resealed under MPD-SL-551821; former seal retained; all seven packages remain in MPD custody; Grant's bounded observation is signed; no final federal receiver"
    accepted_manuscript_words: 93498
    chapter_14:
      title: "The Witness Line"
      path: "books/book-01/manuscript/chapters/chapter-14.md"
      verdict: "ACCEPT"
      accepted_words: 5763
      reviewed_blob_sha: "78f7fff02cd271fecbc94f7daf7151dbebbd5c6d"
    chapter_15:
      title: "The Split Record"
      path: "books/book-01/manuscript/chapters/chapter-15.md"
      verdict: "ACCEPT"
      accepted_words: 5993
      reviewed_blob_sha: "b8e7e2ae573a6c25ea096121c75acee867f3fad2"
      opening: "07:49:32 EDT / 17:19:32 IST"
      endpoint: "07:56:40 EDT / 17:26:40 IST"
    chapter_16:
      title: "The Hold Order"
      path: "books/book-01/manuscript/chapters/chapter-16.md"
      verdict: "ACCEPT"
      accepted_words: 6024
      prose_changed_during_review: true
      reviewed_blob_sha: "dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8"
      opening: "07:56:40 EDT / 17:26:40 IST"
      endpoint: "08:15:52 EDT / 17:45:52 IST"
    chapter_17:
      title: "The First Examination"
      path: "books/book-01/manuscript/chapters/chapter-17.md"
      verdict: "ACCEPT"
      accepted_words: 5888
      prose_changed_during_review: false
      reviewed_blob_sha: "1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1"
      opening: "08:15:52 EDT / 17:45:52 IST"
      endpoint: "09:12:52 EDT / 18:42:52 IST"
      examiner: "Special Agent Leila Grant, Defense Criminal Investigative Service"
      custody_status: "all seven packages remain in MPD physical custody; MPD-901446 opened once, resealed under MPD-SL-551821, and returned to the common chest"
      federal_receiver_status: "none"

  drafts:
    active_chapter_drafts: []
    chapter_17: "accepted and promoted; no duplicate draft remains"

  future_prose:
    chapter_18_and_later: "not drafted"
    chapter_18_rule: "No Chapter 18 prose, mission lock, or remainder-of-Act-III outline was created during Chapter 17 acceptance"
    architecture_rule: "Do not create a complete chapter-by-chapter outline for the remainder of Act III"

  planning_controls:
    ending_contract: "books/book-01/control/22-book-1-ending-contract.md"
    word_budget_and_architecture: "books/book-01/control/23-word-budget-and-act-iii-architecture.md"
    thread_disposition: "books/book-01/control/24-thread-disposition-matrix.md"
    chapter_acceptance_gate: "books/book-01/control/25-chapter-acceptance-gate.md"
    chapter_16_review: "books/book-01/control/33-chapter-16-acceptance-review.md"
    chapter_17_mission_lock: "books/book-01/control/34-chapter-17-mission-lock.md"
    chapter_17_review: "books/book-01/control/35-chapter-17-acceptance-review.md"
    series_character_ledger: "series/recurring-character-ledger.md"

  chapter_17_record:
    title: "The First Examination"
    status: "accepted and promoted; canon"
    mission_lock: "books/book-01/control/34-chapter-17-mission-lock.md"
    review: "books/book-01/control/35-chapter-17-acceptance-review.md"
    accepted_path: "books/book-01/manuscript/chapters/chapter-17.md"
    draft_exists: false
    accepted: true
    acceptance_gate_passed: true
    accepted_manifest_changed: true
    accepted_words_changed: true
    accepted_words: 5888
    reviewed_blob_sha: "1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1"
    dominant_function: "Conduct the first independent, MPD-controlled technical examination of one evidence package and create a signed, reproducible finding without fragmenting the seven-package incident or overstating what the board proves"
    opening: "08:15:52 EDT / 17:45:52 IST"
    endpoint: "09:12:52 EDT / 18:42:52 IST"
    duration_minutes: 57
    pov: "Julie primary; one bounded Special Agent Leila Grant examination-room movement"
    examiner: "Special Agent Leila Grant, Defense Criminal Investigative Service"
    package_scope: "MPD-901446 only; other six packages remain sealed and unopened"
    result: "The physical board contains no original attributed physical signing event; later gate and reconciliation events remain authenticated; conclusion is signed and explicitly limited"
    next_gate: "No Chapter 18 work performed in this acceptance pass"

  narrative_house_style:
    version: "2.2"
    status: "locked for new chapter production and revision passes"
    guide: "docs/Julie_ODonnell_Narrative_House_Style_v2_2.md"
    v2_1_supplement: "docs/Julie_ODonnell_Narrative_House_Style_v2_1.md"
    v2_base: "docs/Julie_ODonnell_Narrative_House_Style_v2.md"
    authority: "Craft control only; accepted manuscript and Book 1 canon controls remain superior for facts and continuity"

source_of_truth:
  - rank: 1
    path: "books/book-01/manuscript/"
    role: "Controlling story facts for prose listed in the accepted-manuscript inventory"
  - rank: 2
    path: "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
    role: "Controlling inventory of accepted prose"
  - rank: 3
    path: "books/book-01/control/"
    role: "Canon controls and approved production planning"
  - rank: 4
    path: "series/"
    role: "Cross-book continuity and recurring-character controls"
  - rank: 5
    path: "books/book-01/drafts/"
    role: "Unaccepted prose only"
  - rank: 6
    path: "archive/"
    role: "Non-controlling legacy provenance"
  - rank: 7
    path: "README.md"
    role: "Human navigation summary only"

critical_status:
  chapter_14_acceptance:
    severity: "resolved"
    reviewed_blob_sha: "78f7fff02cd271fecbc94f7daf7151dbebbd5c6d"
  chapter_15_acceptance:
    severity: "resolved"
    reviewed_blob_sha: "b8e7e2ae573a6c25ea096121c75acee867f3fad2"
  chapter_16_acceptance:
    severity: "resolved"
    reviewed_blob_sha: "dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8"
  chapter_17_acceptance:
    severity: "resolved"
    status: "ACCEPT; promoted at 5,888 words with no prose revision"
    reviewed_blob_sha: "1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1"
  status_drift:
    severity: "resolved"
    status: "accepted inventory, count, endpoint, draft isolation, review record, ledgers, and validator synchronized through Chapter 17"
  next_gate:
    severity: "not started"
    status: "No Chapter 18 work was performed in this acceptance-review session"

archive:
  legacy_source_policy: "archive/legacy-sources/README.md"
  former_google_doc_active: false
  uploaded_word_snapshot_active: false
  superseded_status_snapshots: "Preserved in Git history; not duplicated as active files"

production_rules:
  - "Accepted manuscript prose outranks all summaries, plans, trackers, drafts, and external snapshots."
  - "No unaccepted chapter may live under books/book-01/manuscript/."
  - "Draft existence does not create canon."
  - "Promotion requires the same production pass to move prose, update the manifest and project state, and update every affected control ledger."
  - "Chapters 13 through 17 are accepted Act III canon."
  - "Registered authority never proves physical human custody without separate evidence."
  - "The physical-board mismatch does not identify the alternative identity path or human actor."
  - "The Hartwell presenter, WSS plaintext, K-17 result, and Phase B result remain unresolved."
  - "No final federal receiver exists at the accepted Chapter 17 endpoint."
  - "No draft or revision may imitate or closely emulate the recognizable prose of a living author."

next_recommended_action: "Preserve the accepted Chapter 17 state. No Chapter 18 prose, mission lock, or complete remainder-of-Act-III outline was created in this pass."
"""
write("PROJECT_STATE.yaml", project_state)

root_readme = """# Julie O'Donnell Series

Repository for the Julie O'Donnell contemporary geopolitical techno-thriller / military-intelligence thriller series.

## Current production state

The authoritative production status is [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml). Story canon is controlled by the accepted-manuscript inventory and accepted Markdown prose.

- Active book: Book 1 — title not yet locked
- Target length: **100,000–125,000 words**
- Planning target: **112,500 words**
- Accepted canon: Prologue and Chapters 1–17
- Accepted-manuscript length: **93,498 words**
- Accepted endpoint: **09:12:52 EDT / 18:42:52 IST**
- Chapter 17, **The First Examination**: accepted at **5,888 words**
- Chapter 17 reviewed blob: `1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1`
- Active chapter drafts: none
- Book 1: not publication-ready
- Chapter 18 work in this acceptance pass: none

## Accepted Chapter 17 endpoint

- Special Agent Leila Grant is the named independent DCIS examiner.
- Only `MPD-901446`, containing administrator-token board `EAT-0881147`, was opened.
- The physical board contains no corresponding physical signing event, monotonic transition, or local release record for the original attributed deployment.
- Later gate-access and provenance-reconciliation events contain internally consistent physical-board history.
- The preliminary observation is signed, reproducible, and expressly limited.
- Former seal `MPD-SL-551804` is retained; replacement seal `MPD-SL-551821` is applied.
- `MPD-901446` returned to the same common incident chest.
- All seven packages remain in MPD physical custody; no final federal receiver exists.
- Sterling's hostile public account remains dominant.
- Elias is neither exonerated nor reduced to a simple hostage or saboteur.
- Alternative identity path, human responsibility, Hartwell, WSS-4 plaintext, K-17, Phase B, field truth, guilt, immunity, admissibility, and public vindication remain unresolved.

## Source-of-truth hierarchy

1. [`books/book-01/ACCEPTED_MANUSCRIPT.yaml`](books/book-01/ACCEPTED_MANUSCRIPT.yaml) and the accepted files it lists
2. [`books/book-01/control/`](books/book-01/control/) for canon controls and approved production planning
3. [`series/`](series/) for cross-book continuity and recurring-character controls
4. [`books/book-01/drafts/`](books/book-01/drafts/) for unaccepted prose
5. [`PROJECT_STATE.yaml`](PROJECT_STATE.yaml) for production status and navigation
6. [`archive/`](archive/) and Git history for superseded or external-source provenance

Accepted prose outranks every summary, tracker, plan, and draft.

## Current production controls

- [Book 1 ending contract](books/book-01/control/22-book-1-ending-contract.md)
- [Word budget and provisional Act III architecture](books/book-01/control/23-word-budget-and-act-iii-architecture.md)
- [Thread disposition matrix](books/book-01/control/24-thread-disposition-matrix.md)
- [Chapter acceptance gate](books/book-01/control/25-chapter-acceptance-gate.md)
- [Chapter 16 acceptance review](books/book-01/control/33-chapter-16-acceptance-review.md)
- [Chapter 17 mission lock](books/book-01/control/34-chapter-17-mission-lock.md)
- [Chapter 17 acceptance review](books/book-01/control/35-chapter-17-acceptance-review.md)
- [Series recurring-character ledger](series/recurring-character-ledger.md)

## Permanent continuity repair

The Chapter 5-to-6 chronology, two-stage deadline, title, geography, and L3-7 handoff were repaired and integrated on July 12, 2026.

- Chapter 5: **The Second Clock**
- Chapter 7: **The Human Key**
- 16:30 EDT / 02:00 IST: allied source certification
- 05:00 EDT / 14:30 IST: executable counter-battery support commit and firing-decision point
- Integration commit: `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`
- Permanent record: `books/book-01/repairs/chapter-05-to-06-continuity-repair/`
"""
write("README.md", root_readme)

review = """# Chapter 17 Formal Acceptance Review

**Chapter:** 17 — *The First Examination*
**Review date:** 2026-07-14
**Repository:** `dustinober1/Julie-O-Donnell-Series`
**Review branch:** `agent/chapter-17-acceptance-review`
**Formal verdict:** **ACCEPT**

## 1. Repository baseline and drift

- Expected and verified starting `main`: `fae5bbb8862f7275d802d7c0b76f1449a4979cf9`.
- PR #39 was squash-merged at that commit.
- Drift: none.
- Reviewed draft path: `books/book-01/drafts/chapter-17.md`.
- Reviewed draft blob: `1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1`.
- Exact reviewed count: **5,888 whitespace-delimited Markdown words**.
- Prose changed during acceptance review: **No**.
- Protected Chapter 14, 15, and 16 blobs remained unchanged.
- Promotion commit reference: the synchronized commit that introduces this review and the accepted Chapter 17 path; Git history is authoritative.

## 2. Opening, endpoint, and timeline

- Opening: **08:15:52 EDT / 17:45:52 IST**.
- Endpoint: **09:12:52 EDT / 18:42:52 IST**.
- Live duration: **57 minutes**.
- The chapter begins directly from the accepted Chapter 16 intake state.
- Grant's 08:03 Alexandria dispatch, 08:11 written authorization, I-395 route, and 08:28:17 arrival are plausible.
- Intermediate custody, equipment, examination, reporting, reseal, and signature timestamps fit the locked clock.
- EDT and IST remain synchronized by nine hours thirty minutes.

**Assessment:** PASS.

## 3. Mission-lock authority and dominant mission

The controlling authority is `books/book-01/control/34-chapter-17-mission-lock.md`, subordinate to accepted prose through Chapter 16 and the active canon controls.

The chapter has one dominant mission: conduct the first independent, MPD-controlled technical examination of one evidence package and create a signed, reproducible finding without fragmenting the seven-package incident or overstating what the board proves.

Institutional disputes change custody, scope, tools, timing, independence, or report language. They do not become an equal second mission.

**Assessment:** PASS.

## 4. POV assessment

- Julie remains the primary close-third POV.
- Special Agent Leila Grant receives one bounded close-third examination-room movement.
- Grant observes, tests, and professionally infers only what is available in the room and on the board.
- Julie gains the technical result only when Grant communicates it or the shared record exposes it.
- No prohibited POV or omniscient institutional narrator appears.
- The Grant movement's reading of Julie's visible reaction is an observable professional inference, not a transfer of hidden knowledge.

**Assessment:** PASS.

## 5. Grant authority and independence

- Special Agent Leila Grant is a credible DCIS examiner.
- Supervisory Special Agent Miriam Alvarez's written authorization is separately identified.
- Hackett's assistance request, DCIS authority, and MPD consent remain distinct instruments.
- Grant is skeptical of Julie, Hackett, Apex, and incomplete evidence.
- She receives technical access only.
- She does not become custodian, adjudicator, immunity authority, final federal receiver, or Hackett's mouthpiece.

**Assessment:** PASS.

## 6. Evidence and custody assessment

- All seven packages begin and end in MPD incident `187463`.
- Only `MPD-901446` leaves the common chest.
- Only `MPD-901446` is opened.
- `EAT-0881147` is the examined board.
- Ortiz remains physical custodian.
- Park remains witness officer.
- Julie touches no package, board, tool, control, seal, or evidence surface.
- Existing seal `MPD-SL-551804` is photographed, removed under camera, and retained in a labeled sleeve.
- Replacement seal `MPD-SL-551821` is applied and cross-referenced.
- `MPD-901446` returns to the same common incident chest.
- The other six packages remain separate, sealed, offline, unopened, unconnected, and uncombined.
- Grant's generated log medium is derivative evidence and does not replace, merge, or fragment the original incident.

**Assessment:** PASS.

## 7. Examination method and technology

- The MPD room has no live network or uncontrolled wireless path.
- No Apex hardware, software, credential, observer, parser, validation network, or remote screen controls the result.
- Workstation, write blocker, certificate reader, camera, boot image, and log medium are separately identified.
- The boot-image digest is recorded and verified.
- A known reference card tests the tool for expected events and a deliberate absence.
- The signing path is physically unavailable.
- No biometric, private-key challenge, reset, counter increment, secure-element change, or production operation occurs.
- The board is disconnected and final tool state records zero writes, zero private-key operations, and zero new monotonic transitions.
- The post-restart repeated read establishes reproducibility rather than repeating exposition.

**Assessment:** PASS.

## 8. Technical finding, midpoint reversal, and limits

The signed preliminary observation establishes only that:

1. the examined board contains no physical private-key signing event, corresponding monotonic-counter transition, or local release record for the original deployment attribution preserved on the board;
2. later emergency gate-access and provenance-reconciliation events contain internally consistent physical-board history; and
3. the original attribution cannot be explained as ordinary physical use of this board in the same manner as the later events.

The same result weakens the claim that Elias's physical board performed the original deployment and strengthens the independent record that he voluntarily authenticated later acts with possible legal consequences. Julie expressly refuses omission, softening, or separation of the later events.

The chapter does not establish innocence, guilt, immunity, admissibility, an alternative identity path, a human operator, workstation use, Vance's keystrokes, Sterling's possession, Tariq's physical presence, complete Payload 88 history, all-seven-package authenticity, WSS-4 plaintext, K-17 outcome, Phase B outcome, field truth, or public vindication.

**Assessment:** PASS.

## 9. Success, failure, and hard-stop assessment

### Success

- Grant is named and authorized.
- One package is examined by a reproducible independent method.
- A bounded preliminary observation is signed.
- MPD custody remains intact.
- The former seal is retained.
- The replacement seal is applied.
- The package returns to the common chest.
- The report enters MPD and DCIS records without becoming public.

### Failure avoided

- No transfer away from MPD.
- No electronics-only case fragmentation.
- No Apex-controlled examination.
- No second package.
- No board alteration.
- No unsupported complete authentication or innocence finding.

### Hard stops

Grant states the stop conditions before opening, and no seal, serial, witness, camera, tool-state, read-only, counter, contamination, biometric, private-key, network, Apex-credential, second-package, or medical stop is triggered.

**Assessment:** PASS.

## 10. Medical and restraint continuity

- Julie's right forearm remains padded, braced, swollen, and materially unusable.
- The left-cuff transfer is deliberate, recorded, injury-compatible, and gives no tactical freedom.
- Julie leads verbally, analytically, and morally.
- Marcus remains in separate guarded care on four liters of oxygen at 92–93 percent and performs no new tactical, technical, or evidentiary action.
- Elias remains injured and separated, provides no biometric, handles no evidence, and performs no technical action.
- No trio reunion or direct communication occurs.
- No medical emergency is ignored for institutional convenience.

**Assessment:** PASS.

## 11. Institutional and public-pressure assessment

- The electronics-only federal request threatens incident unity.
- Apex's proprietary-tool and observer demands threaten independence.
- The second-package demand threatens scope.
- Hackett's stronger-conclusion request threatens limitation.
- Grant preserves the result by proving less than every interested party wants.
- MPD, DCIS, Hackett's office, and other ordinary officials remain reviewable professionals rather than presumed conspirators.
- Sterling's hostile account remains publicly dominant.
- No leak, press conference, correction, public fracture, or vindication occurs.

**Assessment:** PASS.

## 12. Style assessment

Under Narrative House Style v2.2:

- close-third past tense is maintained;
- procedural paragraphs are appropriately dense;
- short hard beats mark state changes;
- procedure changes choices;
- limitations operate as conflict;
- the opening begins with the contested question;
- the chapter contains no generic bureaucracy, lecture disguised as dialogue, repetitive evidence explanation, melodramatic speech, chase, breach, artificial countdown, or tactical dominance;
- injuries and restraint remain active;
- the ending lands on the first independent record rather than a later-chapter teaser; and
- no living author is imitated or closely emulated.

**Assessment:** PASS.

## 13. Word count and chapter integrity

- Exact count: **5,888 words**.
- Required range: **5,600–6,300 words**.
- Exactly one Chapter 17 heading appears.
- No TODO, drafting note, alternative, placeholder, Chapter 18 prose, Chapter 18 mission lock, or complete remainder-of-Act-III outline appears.

**Assessment:** PASS.

## 14. Revision record and post-review verification

### Blocking canon or mission failures

None.

### Blocking POV or knowledge failures

None.

### Blocking evidence, custody, medical, or technical failures

None.

### Nonblocking prose issues requiring change

None.

### Revisions made

None. The accepted prose preserves the exact reviewed blob `1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1`.

The complete chapter, mission lock, acceptance gate, accepted Chapter 16, and final promotion diff were reread. The exact count, opening, endpoint, package states, seals, tool states, injuries, restraints, limitations, and unresolved threads were reverified.

## 15. Threads advanced

- First named independent technical examination.
- First signed, independently reproducible contradiction to the physical-token deployment account.
- Independent counterrecord outside Apex's exclusive control.
- Julie's commitment to preserve inconvenient truth.
- Elias's voluntary-role distinction without exoneration.
- Hackett's bounded preservation sponsorship and willingness to accept an independent method.
- A stronger basis to preserve identity-mirroring, executive-authority, validation, and parser records.
- Staging for later public fracture without creating that fracture now.

## 16. Threads unresolved

- Final federal receiver.
- Broader multi-package examination.
- Alternative identity path and human responsibility.
- Hartwell presenter and exact challenged serial.
- Compact black case contents.
- WSS-4 plaintext.
- K-17 and Phase B outcomes.
- Reconstruction authorship, purpose, and truth.
- Sterling's physical possession, personal command, guilt, and legal fate.
- Vance's personal keystrokes and upstream direction.
- Tariq's physical presence.
- Bell, Chen, Mercer, and Price dispositions.
- Marcus's institutional consequences.
- Final legal, medical, geopolitical, relationship, and series aftermath.
- Public narrative fracture and vindication.

## 17. Accepted-manuscript effect

- Prose moved from `books/book-01/drafts/chapter-17.md` to `books/book-01/manuscript/chapters/chapter-17.md`.
- No duplicate draft remains.
- Reviewed blob remains unchanged.
- Accepted total changes from **87,610** to **93,498 words**.
- Accepted endpoint changes to **09:12:52 EDT / 18:42:52 IST**.
- The accepted endpoint is secure MPD evidence intake after the first independent single-package examination, with `MPD-901446` resealed and all seven packages remaining in MPD custody.
- The validator protects the final Chapter 17 blob and exact word count.

## 18. Formal verdict

**ACCEPT**

Chapter 17 satisfies the mission lock and every mandatory category in the Chapter acceptance gate without prose revision. It is ready for synchronized promotion and is promoted in the same review branch and pull request.

No Chapter 18 prose or mission lock was created. No complete chapter-by-chapter outline for the remainder of Act III was created.
"""
write("books/book-01/control/35-chapter-17-acceptance-review.md", review)

active_status_files = [
    "books/book-01/control/00-overview.md",
    "books/book-01/control/02-current-project-state.md",
    "books/book-01/control/16-chapter-by-chapter-status-record.md",
    "books/book-01/control/18-act-iii-entry-state.md",
    "books/book-01/control/20-control-pack-maintenance-rules.md",
    "books/book-01/control/23-word-budget-and-act-iii-architecture.md",
    "books/book-01/control/README.md",
    "books/book-01/drafts/README.md",
    "books/book-01/manuscript/STATUS.md",
]
for rel in active_status_files:
    normalize_active_status(rel)

status_block = """## Accepted Chapter 17 state — 2026-07-14

Chapter 17 — **The First Examination** — is accepted and promoted at **5,888 words** with reviewed blob `1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1`.

- Accepted manuscript: Prologue and Chapters 1–17.
- Accepted total: **93,498 words**.
- Accepted endpoint: **09:12:52 EDT / 18:42:52 IST**.
- Accepted path: `books/book-01/manuscript/chapters/chapter-17.md`.
- Active Chapter 17 draft: none.
- Review: `books/book-01/control/35-chapter-17-acceptance-review.md`.
- Custody: `MPD-901446` was opened once, examined read-only, resealed under `MPD-SL-551821`, and returned to the common chest; all seven packages remain in MPD custody.
- Technical result: no original attributed physical signing event appears on the examined board; later gate and reconciliation events remain authenticated.
- No final federal receiver exists.
- Sterling's public account remains dominant.
- Alternative identity path, human responsibility, Hartwell, WSS-4 plaintext, K-17, Phase B, field truth, guilt, immunity, and admissibility remain unresolved.
- No Chapter 18 prose, mission lock, or complete remainder-of-Act-III outline was created in this pass.
"""
for rel in active_status_files:
    append_block(rel, "## Accepted Chapter 17 state — 2026-07-14", status_block)

control_readme = read("books/book-01/control/README.md")
control_readme = re.sub(r"Canon Control Pack v\d+\.\d+", "Canon Control Pack v3.8", control_readme)
if "[35. Chapter 17 Acceptance Review](35-chapter-17-acceptance-review.md)" not in control_readme:
    control_readme = control_readme.rstrip() + "\n\n- [35. Chapter 17 Acceptance Review](35-chapter-17-acceptance-review.md)\n"
write("books/book-01/control/README.md", control_readme)

ledger_blocks = {
"books/book-01/control/04-source-of-truth-canon-locks.md": """## Accepted Chapter 17 canon lock — 2026-07-14

- Accepted prose now includes Chapter 17 — **The First Examination** — at `books/book-01/manuscript/chapters/chapter-17.md`.
- Reviewed blob: `1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1`; exact count: **5,888**.
- Accepted total: **93,498 words**.
- Accepted endpoint: **09:12:52 EDT / 18:42:52 IST**.
- Grant is the named independent DCIS examiner.
- One package, `MPD-901446`, was examined; all seven remain in MPD physical custody.
- The board lacks the original attributed physical signing event while later gate and reconciliation events remain authenticated.
- No alternative identity path, human operator, final receiver, innocence, guilt, immunity, admissibility, Hartwell result, WSS plaintext, K-17 result, Phase B result, field truth, or public vindication is established.
""",
"books/book-01/control/05-master-timeline.md": """## Accepted Chapter 17 timeline — 2026-07-14

- **08:15:52 EDT / 17:45:52 IST:** Chapter opens at secure MPD evidence intake with Julie restrained and seven packages in the common chest.
- **08:03 EDT:** Grant departs the DCIS Alexandria duty office under oral designation.
- **08:11 EDT:** Alvarez signs the written DCIS preliminary-inquiry and technical-assistance authorization.
- **08:28:17 EDT / 17:58:17 IST:** Grant arrives at MPD intake.
- **08:39:00 EDT / 18:09:00 IST:** `MPD-901446` enters the isolated examination room and its existing seal is recorded.
- **08:52:41 EDT / 18:22:41 IST:** the authorized read is complete; no counter or signing-state change has occurred.
- **09:01:14 EDT / 18:31:14 IST:** Grant reads the bounded preliminary observation aloud.
- **09:05:30 EDT / 18:35:30 IST:** reseal begins.
- **09:08:46 EDT / 18:38:46 IST:** Grant signs the preliminary observation.
- **09:12:52 EDT / 18:42:52 IST:** `MPD-901446` is resealed under `MPD-SL-551821`, returned to the common chest, and MPD retains all seven packages.
""",
"books/book-01/control/06-character-state-ledger.md": """## Accepted Chapter 17 character-state update — 2026-07-14

### Julie O'Donnell
- Remains detained at secure MPD evidence intake.
- Right forearm remains padded, braced, swollen, and materially unusable.
- Left restraint is deliberately transferred to a fixed front harness without tactical freedom.
- Performs no evidence handling or technical operation.
- Leads by narrowing the question, protecting custody, and accepting the part of the result that exposes Elias's later voluntary acts.

### Marcus Reed
- Remains in separate guarded medical care on four liters of oxygen at 92–93 percent.
- Performs no new tactical, technical, evidentiary, or communication act in Chapter 17.
- Institutional consequences of his correction remain unresolved.

### Elias Thorne
- Remains injured and in separate guarded medical custody.
- Provides no biometric and performs no technical or evidentiary act.
- The independent board examination weakens the physical-token deployment attribution while authenticating later gate and reconciliation acts.
- He is neither exonerated nor reduced to a simple hostage or saboteur.

### Special Agent Leila Grant
- Introduced as a named DCIS examiner under Alvarez's authorization.
- Skeptical, independent, method-driven, and limited to one package and one question.
- Recurring-series status is not assumed.
""",
"books/book-01/control/07-relationship-and-trust-matrix.md": """## Accepted Chapter 17 relationship update — 2026-07-14

- **Julie ↔ Grant:** bounded professional respect begins. Grant trusts the reproducible method, not Julie's preferred theory; Julie accepts Grant's complete limited result.
- **Julie ↔ Elias:** Julie protects Elias from a false original physical-token attribution without erasing his later voluntary choices or legal exposure.
- **Julie ↔ Hackett:** Hackett's preservation sponsorship produces a bounded institutional result, but he remains neither receiver, adjudicator, immunity authority, nor uncomplicated ally.
- **Julie ↔ MPD / Ortiz / Park:** procedural trust grows through custody discipline rather than personal allegiance.
- **Grant ↔ Apex:** no trust relationship; Apex claims are logged but receive no equipment, observer, custody, or veto role.
""",
"books/book-01/control/08-evidence-and-chain-of-custody-ledger.md": """## Accepted Chapter 17 evidence and custody update — 2026-07-14

- Common incident: MPD `187463`.
- Sole opened package: `MPD-901446`.
- Examined original: administrator-token board `EAT-0881147`.
- Physical custodian: Officer Gabriel Ortiz, badge 4172.
- Witness officer: Officer Hannah Park, badge 5831.
- Former seal: `MPD-SL-551804`, photographed and retained in a labeled evidence sleeve.
- Replacement seal: `MPD-SL-551821`, applied under camera and cross-referenced.
- Grant receives technical access only; physical custody remains MPD.
- The other six packages remain separate, sealed, offline, unopened, unconnected, and uncombined.
- `MPD-901446` returns to the same recorded position in the common chest.
- DCIS log medium `DCIS-LM-3106` contains examiner-generated logs/screenshots only and is a derivative attachment, not a replacement original or separate case.
- No package ownership transfer or final federal receiving act occurs.
""",
"books/book-01/control/09-knowledge-and-information-control-matrix.md": """## Accepted Chapter 17 knowledge update — 2026-07-14

- Grant knows only the independently exposed physical-board history and the written scope/authority around the examination.
- Ortiz and Park know the witnessed package, seal, tool-state, finding, and reseal record.
- Julie learns Grant's bounded conclusion through the on-record explanation and signed observation.
- Hackett receives the signed observation through the DCIS/MPD preservation channel.
- Marcus and Elias do not receive the result directly in Chapter 17.
- The public does not learn the finding.
- No character gains the alternative identity path, human operator, Vance keystrokes, Sterling possession, Tariq presence, complete Payload 88 history, WSS plaintext, K-17 result, Phase B result, or field truth.
""",
"books/book-01/control/10-technology-and-system-rules.md": """## Accepted Chapter 17 technology update — 2026-07-14

- A physical secure-element board records this board's signing history, not every use of a mirrored or replayed identity.
- `EAT-0881147` exposes no physical private-key signing event, matching monotonic transition, or local release record for the original attributed deployment.
- Later emergency gate and provenance-reconciliation events do expose internally consistent physical-board history.
- The examination uses an isolated DCIS workstation, verified boot image, serialized write blocker and reader, passive evidence interface, and reference-card false-positive control.
- No live network, Apex tool, Apex credential, biometric, private-key challenge, reset, counter increment, secure-element change, or production operation occurs.
- Pre- and post-examination counter values match; final state records zero writes, zero private-key operations, and zero new monotonic transitions.
- The result contradicts ordinary physical use of this board at the original attribution time but does not identify an alternative identity path or human actor.
""",
"books/book-01/control/11-organizations-authorities-and-institutional-control.md": """## Accepted Chapter 17 institutional update — 2026-07-14

- DCIS opens a preliminary inquiry limited to preservation and independent technical assistance.
- Supervisory Special Agent Miriam Alvarez authorizes Special Agent Leila Grant in writing.
- Hackett's assistance request, DCIS authority, and MPD consent remain separate instruments.
- MPD retains the package and controls room access, movement, opening, witness record, and reseal.
- Grant controls technical method and report language.
- Apex receives no observer, equipment, parser, credential, custody, or veto role.
- No final federal receiver exists at the endpoint.
- A later preservation request for identity-mirroring, executive-authority, tool-validation, and parser records is permitted; no responsive record arrives in Chapter 17.
""",
"books/book-01/control/12-location-and-security-architecture.md": """## Accepted Chapter 17 location update — 2026-07-14

### Secure MPD evidence intake and digital-evidence room
- Caged vehicle/intake lane, locked common incident chest, recorded package movement, and camera-covered examination corridor.
- Isolated examination room with fixed steel evidence surface, continuous MPD camera, independent wall clock, antistatic mat, and logged access.
- Network wall jack is physically disconnected and tagged; ordinary radios/wireless devices remain outside.
- Observation alcove allows Julie to see custody movement while restrained without entering the technical work area.
- The architecture separates physical custody, technical access, witness continuity, and public intake operations.
""",
"books/book-01/control/14-public-narrative-versus-actual-record.md": """## Accepted Chapter 17 public-versus-actual update — 2026-07-14

### Public account
Sterling's armed-insider account remains dominant. Public reporting treats detention and recovered classified material as support for the hostile story. No public correction, leak, press conference, or vindication occurs.

### Actual nonpublic record
Grant's signed preliminary observation independently establishes that the examined physical board lacks the original attributed physical signing event while later gate and reconciliation events remain authenticated. The record is bounded, nonpublic, and does not establish innocence, guilt, human responsibility, or the wider conspiracy.
""",
"books/book-01/control/15-open-plot-threads-and-payoff-matrix.md": """## Accepted Chapter 17 thread update — 2026-07-14

### Advanced
- Independent technical examination: first named, reproducible single-package examination completed.
- Independent counterrecord: Grant's signed observation now exists outside Apex's exclusive control.
- Elias original-deployment attribution: physical-board claim materially weakened.
- Elias later voluntary acts: independently authenticated and preserved with legal ambiguity.
- Hackett: preservation sponsorship produces a bounded result without final custody or adjudication.
- Public fracture: technically staged, not publicly triggered.

### Still open
Final receiver; alternative identity path; human operator; broader package authentication; Hartwell presenter and exact serial; compact black case; WSS plaintext; K-17; Phase B; reconstruction; Sterling/Vance/Tariq personal acts; Chen/Mercer/Bell/Price outcomes; Marcus consequences; legal/medical aftermath; public vindication.
""",
"books/book-01/control/24-thread-disposition-matrix.md": """## Accepted Chapter 17 disposition update — 2026-07-14

| Thread | Chapter 17 disposition | Remaining obligation |
|---|---|---|
| First independent examination | Completed for `MPD-901446` only | Broader examination remains optional and bounded by later evidence needs |
| Physical-token deployment attribution | Materially contradicted | Identify alternative identity path and human responsibility |
| Elias later voluntary acts | Independently authenticated | Resolve legal meaning without hostage/saboteur simplification |
| Independent counterrecord | Signed and preserved | Determine institutional/public use |
| Hackett preservation role | Advanced | Final receiver and broader institutional choice unresolved |
| Sterling public account | Unchanged publicly | Authenticated public fracture remains required |
| Hartwell / WSS-4 / K-17 / Phase B | Not advanced beyond limitations | All remain active Book 1 obligations |
""",
"series/recurring-character-ledger.md": """## Accepted Book 1 Chapter 17 update — 2026-07-14

### Julie O'Donnell
Accepted end state advances to 09:12:52 EDT at secure MPD evidence intake. She remains detained, right-hand impaired, separated from Marcus and Elias, and committed to bounded truth over exonerating simplification.

### Marcus Reed
Remains in guarded medical care on four liters of oxygen; his prior correction and its institutional consequences remain active. No Chapter 17 action or recovery is added.

### Elias Thorne
Remains injured and separated. The physical board no longer supports ordinary original physical-token use but independently supports his later voluntary gate and reconciliation acts. Legal status and future series role remain unresolved.

### Special Agent Leila Grant
First accepted appearance. DCIS examiner who signs the first independent, reproducible board finding. No future-book or recurring role is assumed by Book 1 Chapter 17.
""",
}
for rel, block in ledger_blocks.items():
    append_block(rel, "## Accepted Chapter 17" if rel != "series/recurring-character-ledger.md" else "## Accepted Book 1 Chapter 17", block)

append_block(
    "books/book-01/control/13-antagonist-objectives-and-conspiracy-model.md",
    "## Chapter 17 non-expansion note — 2026-07-14",
    """## Chapter 17 non-expansion note — 2026-07-14

Chapter 17 adds no accepted antagonist act, motive, command, physical possession, or personal keystroke. The independent board mismatch strengthens preservation need but does not identify the alternative actor or expand the conspiracy model.
""",
)

workflow = r"""name: Book 1 manuscript validation

on:
  pull_request:
    paths:
      - "README.md"
      - "PROJECT_STATE.yaml"
      - "books/book-01/**"
      - "series/recurring-character-ledger.md"
      - "tools/count_book1_words.py"
      - ".github/workflows/book1-manuscript-validation.yml"
  push:
    branches: [main]
    paths:
      - "README.md"
      - "PROJECT_STATE.yaml"
      - "books/book-01/**"
      - "series/recurring-character-ledger.md"
      - "tools/count_book1_words.py"
      - ".github/workflows/book1-manuscript-validation.yml"

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          show-progress: false

      - name: Count accepted manuscript
        run: python tools/count_book1_words.py --expect 93498

      - name: Validate accepted Chapter 17 promotion
        shell: bash
        run: |
          python - <<'PY'
          from pathlib import Path
          import hashlib

          root = Path('.')
          manifest = (root / 'books/book-01/ACCEPTED_MANUSCRIPT.yaml').read_text(encoding='utf-8')
          project = (root / 'PROJECT_STATE.yaml').read_text(encoding='utf-8')
          review = (root / 'books/book-01/control/35-chapter-17-acceptance-review.md').read_text(encoding='utf-8')

          def require(condition, message):
              if not condition:
                  raise SystemExit(message)

          def blob(path):
              data = path.read_bytes()
              return hashlib.sha1(f"blob {len(data)}\0".encode('ascii') + data).hexdigest()

          require('accepted_words: 93498' in manifest, 'accepted total is not 93498')
          require('sequence: 17' in manifest, 'Chapter 17 missing from manifest')
          require('chapter: 17' in manifest, 'accepted endpoint chapter is not 17')
          require('09:12:52 EDT' in manifest and '18:42:52 IST' in manifest, 'accepted endpoint changed')
          require('chapters: "1-17"' in project, 'PROJECT_STATE accepted range wrong')
          require('accepted_words: 93498' in project, 'PROJECT_STATE count wrong')
          require('acceptance_gate_passed: true' in project, 'Chapter 17 acceptance gate not locked true')
          require('**ACCEPT**' in review, 'review verdict missing')
          require('1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1' in review, 'reviewed blob missing')

          ch17 = root / 'books/book-01/manuscript/chapters/chapter-17.md'
          require(ch17.is_file(), 'accepted Chapter 17 missing')
          require(not (root / 'books/book-01/drafts/chapter-17.md').exists(), 'duplicate Chapter 17 draft remains')
          require(not list((root / 'books/book-01').rglob('chapter-18.md')), 'Chapter 18 prose exists')
          require(blob(ch17) == '1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1', 'Chapter 17 blob changed')
          require(len(ch17.read_text(encoding='utf-8').split()) == 5888, 'Chapter 17 count changed')

          protected = [
              ('chapter-14.md', '78f7fff02cd271fecbc94f7daf7151dbebbd5c6d', 5763),
              ('chapter-15.md', 'b8e7e2ae573a6c25ea096121c75acee867f3fad2', 5993),
              ('chapter-16.md', 'dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8', 6024),
              ('chapter-17.md', '1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1', 5888),
          ]
          chapter_root = root / 'books/book-01/manuscript/chapters'
          for name, expected_blob, expected_words in protected:
              path = chapter_root / name
              require(path.is_file(), f'missing protected prose: {name}')
              require(blob(path) == expected_blob, f'protected blob changed: {name}')
              require(len(path.read_text(encoding='utf-8').split()) == expected_words, f'protected word count changed: {name}')

          required_status = [
              root / 'README.md',
              root / 'PROJECT_STATE.yaml',
              root / 'books/book-01/control/00-overview.md',
              root / 'books/book-01/control/02-current-project-state.md',
              root / 'books/book-01/control/16-chapter-by-chapter-status-record.md',
              root / 'books/book-01/control/18-act-iii-entry-state.md',
              root / 'books/book-01/control/20-control-pack-maintenance-rules.md',
              root / 'books/book-01/control/23-word-budget-and-act-iii-architecture.md',
              root / 'books/book-01/control/README.md',
              root / 'books/book-01/drafts/README.md',
              root / 'books/book-01/manuscript/STATUS.md',
          ]
          for path in required_status:
              text = path.read_text(encoding='utf-8')
              for phrase in ['93,498', '09:12:52 EDT / 18:42:52 IST', 'Accepted Chapter 17 state']:
                  require(phrase in text, f'{phrase} missing from {path}')

          control_readme = (root / 'books/book-01/control/README.md').read_text(encoding='utf-8')
          require('Canon Control Pack v3.8' in control_readme, 'control pack version wrong')
          require('[35. Chapter 17 Acceptance Review](35-chapter-17-acceptance-review.md)' in control_readme, 'review link missing')

          for temp in [
              root / 'tools/promote_chapter17_acceptance.py',
              root / '.github/workflows/chapter17-acceptance-promotion.yml',
          ]:
              require(not temp.exists(), f'temporary promotion file remains: {temp}')

          print('accepted Chapter 17 promotion validated')
          PY

      - name: Check whitespace
        if: github.event_name == 'pull_request'
        run: git diff --check "origin/${{ github.base_ref }}...HEAD"
"""
pass  # connector updates validator

(ROOT / "tools/promote_chapter17_acceptance.py").unlink()
pass  # connector removes temporary workflow

require(blob_sha(accepted_ch17) == DRAFT_BLOB, "final Chapter 17 blob changed")
require(len(accepted_ch17.read_text(encoding="utf-8").split()) == CH17_WORDS, "final Chapter 17 count changed")
require(not draft.exists(), "draft still exists")
require(not list((ROOT / "books/book-01").rglob("chapter-18.md")), "Chapter 18 prose exists")
require("accepted_words: 93498" in read("books/book-01/ACCEPTED_MANUSCRIPT.yaml"), "manifest total wrong")
require("sequence: 17" in read("books/book-01/ACCEPTED_MANUSCRIPT.yaml"), "manifest Chapter 17 missing")
require("**ACCEPT**" in read("books/book-01/control/35-chapter-17-acceptance-review.md"), "verdict missing")
run("python", "tools/count_book1_words.py", "--expect", "93498")
run("git", "diff", "--check")

status = run("git", "status", "--short", capture=True)
require(status, "promotion produced no changes")
print(status)

run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
run("git", "commit", "-m", "Accept and promote Chapter 17 — The First Examination")
run("git", "push", "origin", f"HEAD:{BRANCH}")
