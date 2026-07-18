#!/usr/bin/env python3
"""Synchronize Book 1 control files with the accepted revised manuscript."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-01"
MANIFEST = BOOK / "ACCEPTED_MANUSCRIPT.yaml"
DATE = "2026-07-18"
TARGET_MIN = 105_000
TARGET_MAX = 110_000


def prose_paths() -> list[Path]:
    return [BOOK / "manuscript/prologue.md"] + [
        BOOK / f"manuscript/chapters/chapter-{number:02d}.md" for number in range(1, 25)
    ]


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_manifest(paths: list[Path]) -> None:
    text = MANIFEST.read_text(encoding="utf-8")
    total = sum(word_count(path) for path in paths)

    text = re.sub(r"^version:\s*\d+\s*$", "version: 2", text, count=1, flags=re.MULTILINE)
    text = re.sub(
        r'^status:\s*"[^"]+"\s*$',
        'status: "developmentally_revised"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r'^generated_on:\s*"[^"]+"\s*$',
        f'generated_on: "{DATE}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r'^total_accepted_words:\s*\d+\s*$',
        f"total_accepted_words: {total}",
        text,
        count=1,
        flags=re.MULTILINE,
    )

    insert_marker = f'generated_on: "{DATE}"\n'
    metadata = (
        f'developmental_revision_completed: "{DATE}"\n'
        f'publication_readiness: "specialist_review_and_copyedit_required"\n'
        f'target_words_min: {TARGET_MIN}\n'
        f'target_words_max: {TARGET_MAX}\n'
    )
    if "developmental_revision_completed:" not in text:
        text = text.replace(insert_marker, insert_marker + metadata, 1)
    else:
        text = re.sub(
            r'^developmental_revision_completed:\s*"[^"]+"\s*$',
            f'developmental_revision_completed: "{DATE}"',
            text,
            flags=re.MULTILINE,
        )
        text = re.sub(
            r'^publication_readiness:\s*"[^"]+"\s*$',
            'publication_readiness: "specialist_review_and_copyedit_required"',
            text,
            flags=re.MULTILINE,
        )
        text = re.sub(r"^target_words_min:\s*\d+\s*$", f"target_words_min: {TARGET_MIN}", text, flags=re.MULTILINE)
        text = re.sub(r"^target_words_max:\s*\d+\s*$", f"target_words_max: {TARGET_MAX}", text, flags=re.MULTILINE)

    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        words = word_count(path)
        digest = sha256(path)
        pattern = re.compile(
            rf'(\n\s+- path:\s+"{re.escape(relative)}".*?\n\s+words:)\s*\d+(\n\s+sha256:)\s*"[a-f0-9]+"',
            re.DOTALL,
        )
        replacement = rf'\g<1> {words}\g<2> "{digest}"'
        text, count = pattern.subn(replacement, text, count=1)
        if count != 1:
            raise RuntimeError(f"manifest entry not updated: {relative}")

    MANIFEST.write_text(text, encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def update_readme(total: int) -> None:
    write(
        ROOT / "README.md",
        f"""# Julie O'Donnell Series

Canonical repository for the contemporary geopolitical techno-thriller series centered on Julie O'Donnell.

## Current release candidate

**Book 1: _Veridrift_**

- Prologue plus 24 chapters.
- Accepted revised manuscript: **{total:,} words**.
- Developmental revision completed **July 18, 2026**.
- Final act now unfolds across October 13–16 rather than a single implausibly compressed morning.
- Publication blockers, drafting metatext, duplicated thermostat transmission, date conflicts, heading inconsistencies, and system-display artifacts have been removed.
- The causal chain from Validation Package 88 through `SIGMA-NORMALIZE-4` and the live poisoned feed is explicit.
- Julie's overbroad K-17 provenance boundary and signed supplemental correction are canon.
- Original 02:14 constructor and Senator Sterling's personal knowledge or command remain deliberately unresolved series threads.

## Publication state

The developmental revision is complete, but the novel is **not yet approved for publication**. Required next stages:

1. Complete the six external specialist reviews in `books/book-01/control/50-specialist-review-brief.md`.
2. Apply any approved technical corrections with a new continuity pass.
3. Perform a dedicated line/copyedit and proofread.
4. Regenerate print and ebook production files from the accepted-manuscript inventory.

## Source of truth

`books/book-01/ACCEPTED_MANUSCRIPT.yaml` is the canonical prose inventory. Only the listed prologue and chapter files are accepted manuscript sources.

Core paths:

- `books/book-01/manuscript/`
- `books/book-01/control/`
- `books/book-01/ACCEPTED_MANUSCRIPT.yaml`
- `series/`
- `tools/`

Generated or historical compiled files are not authoritative unless explicitly produced from the accepted inventory and validated against its hashes.
""",
    )


def update_project_state(total: int) -> None:
    write(
        ROOT / "PROJECT_STATE.yaml",
        f"""series:
  title: "Julie O'Donnell Series"
  genre: "contemporary geopolitical techno-thriller / military-intelligence thriller"
  protagonist: "Julie O'Donnell"
  planned_books: 5
  planning_horizon: "5-book series with expandable later cases"
  status: "active"

repository:
  branch_policy: "main remains protected; developmental revision is reviewed through PR"
  book_1_source_of_truth: "books/book-01/ACCEPTED_MANUSCRIPT.yaml"
  updated: "{DATE}"

book_1:
  title: "Veridrift"
  status: "developmentally_revised"
  publication_readiness: "specialist_review_and_copyedit_required"
  accepted_words: {total}
  target_words_min: {TARGET_MIN}
  target_words_max: {TARGET_MAX}
  structure:
    prologue: "accepted; unchanged in developmental revision"
    chapters: 24
    crisis_day: "October 13"
    investigation_and_release: "October 14-16"
  revision_completed: "{DATE}"
  preserved_ending: "The bubble stayed centered."
  open_series_threads:
    - "human or upstream instruction behind the original 02:14 construction"
    - "Senator Sterling's personal knowledge, direction, intent, or command"
  required_next_steps:
    - "six external specialist reviews"
    - "continuity review after technical corrections"
    - "line and copyedit"
    - "proofread and production export"

quality_controls:
  publication_readiness_validator: "tools/validate_book1_publication_readiness.py"
  developmental_metrics: "tools/analyze_book1_revision.py"
  specialist_review_brief: "books/book-01/control/50-specialist-review-brief.md"
  current_validation: "passing at {total} accepted words"
""",
    )


def update_status(total: int) -> None:
    write(
        BOOK / "manuscript/STATUS.md",
        f"""# Book 1 Manuscript Status

## Current state

**_Veridrift_ is developmentally revised, not publication-final.**

- Canonical accepted manuscript: prologue plus Chapters 1–24.
- Current accepted word count: **{total:,}**.
- Target range: **{TARGET_MIN:,}–{TARGET_MAX:,}**.
- Developmental revision completed: **July 18, 2026**.
- Prologue and Chapter 1 were preserved from the accepted pre-revision text.

## Revision outcomes

- Final act compressed and rebuilt as one accumulating proof sequence.
- Post-apprehension investigation moved across October 13–16.
- Julie now makes and records a consequential analytical scope error involving K-17.
- Grant, Alvarez, Ortiz, Sharma, Sarah, Vega, and other professionals originate correct process independently.
- Elias has a concrete family stake and retains control of future contact.
- Sarah's earlier institutional restraint is seeded before her source-preservation actions.
- Vance's later live-authenticated release is proved; his original deployment authorship remains unproved.
- Sterling-office responsibility is established without inventing Sterling's personal command.
- Final exact farm timestamp removed; final line preserved.

## Publication blockers removed

- in-world chapter-number drafting references;
- chapter heading attached to prose;
- duplicate thermostat transmission;
- July/October contradiction;
- heading and scene-spacing inconsistencies;
- backticked display artifacts;
- overexplicit Vance confession;
- unrealistic same-morning federal resolution.

## Required before publication

The manuscript still requires the external reviews listed in `../control/50-specialist-review-brief.md`, followed by approved technical revisions, a continuity check, line/copyedit, and proofreading.
""",
    )


def update_overview(total: int) -> None:
    write(
        BOOK / "control/00-overview.md",
        f"""# Book 1 Control Overview — _Veridrift_

## Locked premise

A disgraced Army intelligence analyst discovers that synthetic telemetry is being used to manufacture an India–Pakistan crisis—but stopping the strike means nothing unless she can preserve a chain of evidence powerful institutions are already rewriting.

## Canonical state

- Prologue plus 24 chapters.
- Accepted manuscript inventory: `books/book-01/ACCEPTED_MANUSCRIPT.yaml`.
- Accepted words: **{total:,}**.
- Developmental revision completed: **2026-07-18**.
- Series-opener resolution retained.

## Structural engines

1. Detect and stop the poisoned military warning.
2. Preserve evidence while escaping Apex control.
3. Place separate records under named lawful authority and correct the public causal account.

The third engine now operates as one accumulating proof sequence across October 13–16 rather than repeated same-day custody demonstrations.

## Central proof chain

- Revision Eight remains a deliberately messy validation package.
- A post-archive derivative reclassifies its irregularities as collection damage.
- `SIGMA-NORMALIZE-4` rebuilds the live source toward a common reference, creating the impossibly clean 11.2-second signal and diverting conflicting observations.
- Julie's first provenance boundary stops the counter-battery release but temporarily defers fourteen K-17 observation references.
- Elias identifies the scope problem; Julie signs a supplemental correction recording the forty-three-second delay.
- Sharma independently holds fire and preserves the K-17 local record.
- Vance's live-authenticated later reconstruction release is proved from Apex and government sources.

## Character outcome locks

- Julie refuses a permanent government return and cannot work on her own unresolved case.
- Marcus files the complete correction; possible personal contact does not equal forgiveness or romance.
- Elias retains ownership of his voluntary acts and controls all future contact.
- Sharma remains an independent parallel custodian, not Julie's subordinate.
- Sarah remains institutional, preserves direct records, loses source access, and is not converted into a secret ally.
- Grant and Alvarez originate their own defensible methods.
- Vance's later act is established; original construction and upstream direction remain open.
- Sterling's office device and authority chain are established; Sterling's personal command remains unproved.

## Publication state

Developmental edit complete. External specialist review, technical continuity review, line/copyedit, and proofread remain mandatory.
""",
    )


def update_chapter_status() -> None:
    rows = [
        ("Prologue", "Six Years Ago", "Accepted / unchanged", "Synthetic carrier discovered; four-second abort delay; official timeline rewritten."),
        ("1", "The Official Version", "Accepted / unchanged", "Fence motif; Marcus brings the impossible Pakistan signal; Julie enters Apex."),
        ("2", "The Poisoned Feed", "Revised", "Payload 88, bilateral pilot, Apex authority structure, post-archive derivative, SIGMA transformation, Elias framed."),
        ("3", "The Exit Protocol", "Revised / blocker pass", "Partial evidence capture, administrative detention, life-safety escape, official account begins."),
        ("4", "Burn Notice", "Revised / reflowed", "Fugitives inspect the partial capture; Vance pressures Elias; return-to-Apex mission forms."),
        ("5", "The Human Key", "Revised / reflowed", "Duplicate thermostat scene removed; Elias family stake added; Vance made less confessional."),
        ("6", "The Descent", "Accepted with formatting pass", "Cooling-route descent and lower-tier pursuit."),
        ("7", "The Human Key", "Accepted with formatting pass", "Elias voluntarily opens the gate; immutable emergency act recorded."),
        ("8", "The 05:00 Abort", "Revised", "Provenance reset stops release; Julie's overbroad boundary delays K-17 discovery; supplemental correction sealed."),
        ("9", "The Life-Safety Override", "Accepted with formatting pass", "Occupied-room suppression override, independent fire relay, escape with originals."),
        ("10", "The Capital Connection", "Accepted with continuity pass", "Evidence sources separated; Vance authority chain, Northbridge endpoint, K-17 Phase B."),
        ("11", "Going Offensive", "Accepted with continuity pass", "Northbridge objective, consent and abort rules, module preparation."),
        ("12", "The Sterling Trap", "Revised / reflowed", "WSS-4 capture, Sterling-office signer, Hartwell next challenge, K-17 status remains bounded."),
        ("13", "The Carrier Stream", "Revised / reflowed", "Hartwell physical-custody operation and police contact."),
        ("14", "The Named Officer", "Revised / reflowed", "Ortiz establishes public scene authority and preserves the seven-object chain."),
        ("15", "The Split Record", "Rebuilt", "Apprehension, medical limits, Brooks/Ortiz scene control, seven packages remain separate."),
        ("16", "The Hold Order", "Rebuilt", "Named federal authority, overnight preservation, Sarah's internal source fight, no same-day examination."),
        ("17", "The First Examination", "Rebuilt", "Grant independently and blindly replicates the physical-board finding; Price located."),
        ("18", "The Local Record", "Rebuilt", "Sharma preserves K-17 cartridge; local commit failed; zero writes; patrol and casualty boundaries."),
        ("19", "The Name on the Record", "Rebuilt", "Alvarez accepts federal responsibility; no-fire result; Hartwell limited production."),
        ("20", "The Custody Exception", "Rebuilt", "LSS no-use hold; Drennan carrier, Kessler authorizer, instruction source unresolved."),
        ("21", "The Borrowed Name", "Rebuilt", "Price's authentic request separated from inherited identity and continuity construction."),
        ("22", "The Release Record", "Rebuilt", "Construction mechanism identified; Vance's later live release proved; original constructor unproved."),
        ("23", "The Official Correction", "Rebuilt", "Failed overclaim preserved; three bounded public releases; alerts corrected."),
        ("24", "The Terms of Return", "Rebuilt", "Lawful release, Marcus and Elias boundaries, independent practice terms, centered bubble."),
    ]
    lines = [
        "# Chapter-by-Chapter Status Record — Book 1",
        "",
        "**Revision date:** 2026-07-18  ",
        "**Status:** Developmental revision complete; specialist review and copyedit required.",
        "",
        "| Unit | Title | State | Controlling function / result |",
        "|---|---|---|---|",
    ]
    for unit, title, state, result in rows:
        lines.append(f"| {unit} | {title} | {state} | {result} |")
    lines.extend(
        [
            "",
            "## Global locks",
            "",
            "- Final line: **The bubble stayed centered.**",
            "- Accepted length remains within 105,000–110,000 words.",
            "- Original 02:14 human/upstream constructor remains unresolved.",
            "- Sterling personal knowledge, direction, intent, and command remain unresolved.",
            "- No chapter is publication-final until specialist review, technical continuity review, line/copyedit, and proofread are complete.",
        ]
    )
    write(BOOK / "control/16-chapter-by-chapter-status-record.md", "\n".join(lines))


def update_threads() -> None:
    write(
        BOOK / "control/24-thread-disposition-matrix.md",
        """# Thread Disposition Matrix — End of Book 1

## Resolved in Book 1

| Thread | Disposition |
|---|---|
| False artillery certainty / immediate war risk | Provenance reset suspends the U.S. counter-battery product; Sharma holds fire; no Indian rounds are fired. |
| Payload 88 relation to live feed | Post-archive derivative and `SIGMA-NORMALIZE-4` transform messy Revision Eight into the unnaturally clean operational source. |
| Elias as original deployer | Physical board did not sign at 02:14; identity was mirrored/constructed. His later voluntary acts remain his. |
| Price as operational requestor | Price authenticated only his source-review request; the office workflow inherited his identity and reference after his authority ended. |
| K-17 local commit | Field authority reaches the controller; local authentication fails; zero writes occur; later product omits the events. |
| Julie's analytical infallibility | Her first lineage boundary defers fourteen genuine observation references for forty-three seconds; she signs the supplemental correction. |
| Vance's later operational act | Apex source, camera/access evidence, live palm event, and government registry establish his later remote reconstruction release. |
| False public authorship accusation | Three bounded releases withdraw the claim that Julie, Marcus, Elias, or Price originated the poison or constructed the route. |
| Marcus's six-year testimony | He files a complete sworn correction without obtaining automatic forgiveness. |
| Evidence custody | Seven objects enter common MPD custody, then named federal receiving authority, without being merged. |

## Deliberately unresolved series threads

| Thread | End-of-book boundary |
|---|---|
| Original 02:14 constructor | APX-ICF-4 and `APX-DIR-0019` mechanism/authority binding established; human or upstream initiating instruction not recorded in produced sources. |
| Sterling personal command | Sterling-office device and continuity chain established; personal possession, knowledge, direction, intent, and command not proved. |

## Continuing legal and professional consequences

| Character / institution | Open consequence |
|---|---|
| Julie | Charging, admissibility, and unauthorized-conduct review unresolved; prohibited from working on her own case. |
| Marcus | Medical and Army administrative review; testimony consequences unresolved. |
| Elias | Legal, clearance, and employment consequences for voluntary emergency acts unresolved; future contact controlled by him. |
| Price | DIA administrative decision unresolved; later borrowed identity cannot be treated as his authenticated act. |
| Sarah | Apex access suspended; preserved source record remains under federal hold. |
| Vance | Operational authority suspended; charging and original-deployment attribution unresolved. |
| Sterling office | Device remains under LSS no-use hold; continuity instruction source and personal responsibility unresolved. |
| K-17 | Physical inner boundary and field-team identity remain unresolved; original local media retained by Arjun. |

## Book 2 handoff rule

A later book may investigate the two deliberate series threads through a new lawful mandate. Julie may not use Book 1 evidence or access to investigate her own unresolved case without separate authority and safeguards.
""",
    )


def update_ledger() -> None:
    write(
        ROOT / "series/recurring-character-ledger.md",
        """# Recurring Character Ledger

## Julie O'Donnell

- **Book 1 end state:** conditionally released, right wrist immobilized, no restored clearance, no permanent government role.
- **Character movement:** accepts that responsible custody can require other people to carry weight; records her own K-17 scope error.
- **Future-work lock:** written mandate, originals remain with custodians, proof limits travel with findings, participants retain counsel/consent/right to stop, and Julie cannot work on her own unresolved case.
- **Open exposure:** unauthorized access and evidence-removal consequences remain unresolved.

## Marcus Reed

- **Book 1 end state:** hospitalized; operational access gone; Army medical and administrative review pending.
- **Completed arc:** files the complete six-year correction after knowing it may cost his institution and career.
- **Relationship lock:** may later request personal contact; no work partnership, romance promise, or automatic forgiveness.

## Elias Thorne

- **Book 1 end state:** represented, injured, and facing legal/clearance/employment review.
- **Identity lock:** physical board did not sign original deployment; later gate, recovery, recorder-removal, Northbridge, and abort-overrun acts are voluntary and remain his.
- **Personal stake:** father/retirement dinner and public hero-or-criminal framing.
- **Future-contact lock:** no direct or indirect approach unless Elias authorizes it through counsel; no permanent-team assumption.

## Major Ananya Sharma

- **Book 1 end state:** independent custodian of the no-fire and K-17 local record.
- **Operational lock:** local commit failed, zero writes, inner boundary unresolved, original cartridge retained at Arjun.
- **Series function:** parallel protagonist whose method does not depend on Julie or U.S. institutions.

## Sarah Chen

- **Book 1 end state:** Apex source access suspended; on administrative leave after sealing the source-native release range.
- **Character lock:** remains institutional and supported lawful capture; refused lethal-force expansion and preserved direct records.
- **Do not convert:** not a secret ally or automatic member of Julie's future practice.

## Daniel Mercer

- **Book 1 end state:** surrendered Apex recovery-team command; direct-observation declaration preserved separately.
- **Character lock:** professional security actor who follows defensible procedure once Vance stops supplying one.

## Leila Grant

- **Book 1 end state:** independent DCIS examiner and method authority.
- **Character lock:** originates the board examination and blind replication; corrects Julie's overreach when necessary.
- **Series potential:** recurring institutional counterpart, not subordinate.

## Miriam Alvarez

- **Book 1 end state:** named federal receiving authority for incident 187463.
- **Character lock:** owns jurisdictional and disclosure decisions without claiming every source or person.

## Gabriel Ortiz / Helena Brooks

- **Book 1 end state:** MPD officers who preserve public safety, named custody, and the seven-package chain.
- **Character lock:** neither needs to understand Argus before refusing unreceipted seizure or unsafe force.

## Leland Price

- **Book 1 end state:** represented, under DIA administrative review, later continuity act excluded from his authenticated conduct.
- **Character lock:** real expedited-retention and rejected-access decisions remain visible.

## Arthur Vance

- **Book 1 end state:** later live-authenticated reconstruction release proved; operational authority suspended; represented.
- **Proof lock:** original 02:14 construction, upstream instruction, and personal authorship of Payload 88 deployment remain unproved.
- **Voice lock:** speaks through defensible authority and risk language, not broad confession.

## Senator Sterling / Sterling Office

- **Book 1 end state:** office device and continuity chain established; public causal accusation withdrawn.
- **Proof lock:** Sterling's personal possession, knowledge, direction, intent, and command remain unproved.
- **Supporting roles:** Samuel Drennan is the carrier; Diane Kessler authorized the custody exception; initiating instruction source remains unresolved.

## Nora Bell / Northbridge

- **Book 1 end state:** Northbridge local audit preserves the WSS session; Bell's direct actions remain bounded to facility responsibility.
- **Proof lock:** Northbridge endpoint participation does not by itself establish message authorship or Sterling command.
""",
    )


def main() -> None:
    paths = prose_paths()
    total = sum(word_count(path) for path in paths)
    if not TARGET_MIN <= total <= TARGET_MAX:
        raise RuntimeError(f"accepted words {total} outside target")
    update_manifest(paths)
    update_readme(total)
    update_project_state(total)
    update_status(total)
    update_overview(total)
    update_chapter_status()
    update_threads()
    update_ledger()
    print(f"finalized controls for {total} words")


if __name__ == "__main__":
    main()
