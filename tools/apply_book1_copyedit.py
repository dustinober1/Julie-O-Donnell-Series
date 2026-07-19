#!/usr/bin/env python3
"""Apply the approved Book 1 mechanical copyedit and regenerate manifest metadata.

This temporary script is assertion-based: every prose replacement must match exactly once.
It creates the required copyedit style sheet and query log, then updates accepted-file word
counts and SHA-256 values without changing manifest order or version.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"

REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "books/book-01/manuscript/chapters/chapter-02.md": [
        (
            "Apex did not need to falsify a denial. It needed only to enforce the accepted boundaries until the certification clock expired. He submitted an immediate request.",
            "Apex did not need to falsify a denial. It needed only to enforce the accepted boundaries until the certification clock expired. Marcus submitted an immediate request.",
        ),
        (
            "Elias muted the microphone. “Stop the transfer. Compliance flagged a corrupted validation object. They’re isolating the lab.”",
            "Elias muted the microphone. Keller said, “Stop the transfer. Compliance flagged a corrupted validation object. They’re isolating the lab.”",
        ),
    ],
    "books/book-01/manuscript/chapters/chapter-04.md": [
        (
            "No one had read him rights.",
            "No one had read him his rights.",
        ),
        (
            "“The matter is referred as a suspected attack on classified defense infrastructure.”",
            "“The matter is referred for investigation as a suspected attack on classified defense infrastructure.”",
        ),
    ],
    "books/book-01/manuscript/chapters/chapter-06.md": [
        (
            "“Recovery interface,” she said.\n\nElias looked at her. “You said the enclave keeps a local maintenance path for a contaminated feed.”",
            "“Recovery interface,” she said.\n\nElias looked at her. Julie continued, “You said the enclave keeps a local maintenance path for a contaminated feed.”",
        ),
    ],
    "books/book-01/manuscript/chapters/chapter-10.md": [
        (
            "Julie waited. “I opened the gate. I restored the labels. I pulled the recorder. No one made my hand do any of it.”",
            "Julie waited. Elias continued, “I opened the gate. I restored the labels. I pulled the recorder. No one made my hand do any of it.”",
        ),
    ],
    "books/book-01/manuscript/chapters/chapter-12.md": [
        (
            "Julie held the paper to the lens. “Closer.”\n\nShe moved it within a foot of the glass. “You’re not on the morning sheet.”",
            "Julie held the paper to the lens.\n\n“Closer.”\n\nShe moved it within a foot of the glass.\n\n“You’re not on the morning sheet.”",
        ),
        (
            "Bell stared at her. “WSS-four is about to receive a hardware-authenticated exchange tied to an active foreign operation. Your controller will record the same event we do.”",
            "Bell stared at her. Julie continued, “WSS-four is about to receive a hardware-authenticated exchange tied to an active foreign operation. Your controller will record the same event we do.”",
        ),
    ],
}

STYLE_SHEET = '''# Book 1 Copyedit Style Sheet

**Book:** *Veridrift*  
**Series:** Julie O’Donnell Series  
**Pass:** Full mechanical copyedit  
**English:** U.S. trade fiction  
**Status:** Completed against the accepted-manuscript inventory on the copyedit branch

## Source authority

- Canonical inventory: `../ACCEPTED_MANUSCRIPT.yaml`.
- Canonical prose: only the manifest-listed Prologue and Chapters 1–24, in manifest order.
- Generated compilations, archived drafts, historical Word files, and review exports are noncanonical.
- The accepted final line is **The bubble stayed centered.** Preserve it exactly.
- Plot, chronology, POV, clues, technical mechanisms, legal mechanisms, evidence, proof ceilings, chapter openings, chapter endings, and suspense structure are content locked.

## General style

- Use American English and conventional U.S. trade-fiction punctuation.
- Use the serial comma when three or more coordinate items appear in ordinary prose.
- Use smart double quotation marks and smart apostrophes in prose. Literal identifiers and code-like strings retain their source punctuation.
- Close em dashes against surrounding words—no spaces.
- Use an em dash for interrupted speech. Use a three-dot ellipsis only for genuine trailing speech or thought; do not introduce spaced-dot ellipses.
- Preserve intentional fragments, clipped internal thought, short paragraphs, one- or two-word sentences, countdown beats, and tactical dialogue.
- Close-POV internal thought remains roman and unquoted unless the accepted text establishes another treatment.
- Scene breaks use `---` on a line by itself where present. Do not add decorative breaks.
- Chapter headings use `# Chapter N — Title`. The Prologue retains its accepted heading.

## Capitalization

- Capitalize a formal rank immediately before a name: `Colonel Reed`, `Major Sharma`, `Captain Rao`.
- Lowercase generic rank references: `the colonel`, `the major`, `the captain`.
- Capitalize formal agency, office, facility, system, and unit names; lowercase generic descriptive uses.
- Preserve intentionally capitalized interface labels, warnings, status fields, code names, operational products, and evidence identifiers.
- Do not convert institutional responsibility into personal responsibility through capitalization or title treatment.

## Numbers, dates, and times

- Use numerals in timestamps, system displays, serials, identifiers, percentages, measurements, evidence counts, and technical logs.
- Spell out simple narrative numbers when natural to the established voice.
- In prose, use `94.1 percent`, `99.8 percent`, `8.4 percent`, and `0.07 percent`; displays may use `%` only when already established.
- Narrative form: `eleven-point-two seconds`; technical display form: `11.2`.
- Scene headings use 24-hour clock plus the full time-zone name unless the accepted heading uses compact `EDT` / `IST` notation.
- Preserve each source clock and its stated offset. Never silently normalize independent clocks into one master time.
- Main action dates: October 13–16. The final farm scene has no exact clock time.

## Dialogue

- Dialogue meaning, register, contractions, profanity, hesitation, operational shorthand, and professional voice are locked.
- Dialogue tags take commas; action beats remain separate sentences.
- Begin a new paragraph when the speaker changes.
- Do not attach another speaker’s dialogue to a character action beat.
- Do not make military, intelligence, technical, legal, or police professionals unnaturally formal to satisfy textbook grammar.
- Preserve Julie’s evidence-testing cadence without assigning it mechanically to every character.

## Internal and interface text

- System displays appear as plain uppercase lines, not Markdown code blocks or quotation marks.
- Preserve display field order when sequence carries evidentiary meaning.
- Leave blank lines around display blocks when needed for readability.
- Interface text may use literal hyphens, slashes, colons, and digits that are not typographically normalized.
- Acronyms are expanded on first natural use only when the manuscript requires it. Do not repeatedly re-expand established terms.

## Recurring characters and physical continuity

- **Julie M. O’Donnell** — Julie; she/her. Smart apostrophe and double `l` in prose. Former Army intelligence officer. Right wrist/forearm injured during the lower-tier escape; later braced and immobilized. Left hand becomes the functional hand for writing, steering, and evidence-adjacent actions.
- **Marcus L. Reed** — Marcus; he/him. Colonel / Army officer. Rib injury, right-thigh trauma, scalp wound above right ear, damaged boot/heel, intermittent oxygen need and concussion observation.
- **Elias M. Thorne** — Elias; he/him. Argus model developer. Left-hip injury, right-index-finger cut used for live biometric acts, cold exposure, dizziness. Administrator-token board remains tied to his identity and custody history.
- **Arthur R. Vance** — Vance; he/him. Apex executive. `APX-DIR-0019` is registered/bound executive authority; personal action is established only where live local authentication and corroborating source records place him.
- **Sarah Chen** — Sarah; she/her. Apex contractor integration/compliance. Preserve the distinction between her containment actions, force restrictions, source preservation, and later access suspension.
- **Daniel Mercer** — Mercer; he/him. Apex Protective Services. Taped wrist after the stairwell confrontation; later direct-observation declarations remain narrower than counsel’s narratives.
- **Senator Sterling** — Sterling; he/him. Do not invent a first name. Office/device responsibility does not by itself establish personal possession, knowledge, direction, intent, or command.
- **Major Ananya Sharma** — Sharma; she/her. Indian battery commander / local decision-maker. Her no-fire decision remains her command act.
- **Lieutenant Sameer Qureshi** — Qureshi; he/him.
- **Captain Arvind Rao** — Rao; he/him.
- **Naib Subedar Vikram Sethi** — Sethi; he/him. K-17 local custodian.
- **Lance Naik Suresh Pal** — Pal; he/him. Left-scalp injury; removed from questioning by medical authority.
- **Leland Price** — Price; he/him. DIA systems auditor. Authentic preservation/read-only request remains separate from the later borrowed continuity request.
- **General William Hackett** — Hackett; he/him.
- **Officer Gabriel Ortiz** — Ortiz; he/him. MPD scene/evidence officer.
- **Officer Hannah Park** — Park; she/her. MPD evidence witness/property handling.
- **Watch Commander Helena Brooks** — Brooks; she/her.
- **Special Agent Leila Grant** — Grant; she/her. DCIS examiner; findings remain source- and scope-limited.
- **Supervisory Special Agent Miriam Alvarez** — Alvarez; she/her. Named federal receiving authority.
- **Dana Webb** — Webb; she/her. Julie’s lawyer for immediate custody, charging, and access-to-counsel issues.
- **Dr. Rachel Nwosu** — Nwosu; she/her. Argus Program Integrity and Configuration Control authority.
- **Marisol Vega** — Vega; she/her. Legislative Secure Services deputy director.
- **Martin Vann** — Vann; he/him. LSS compromise-control custodian.
- **Samuel Drennan** — Drennan; he/him. Secure-communications courier; carrier is not authorizer.
- **Diane Kessler** — Kessler; she/her. Sterling-office deputy national-security director; continuity-exception authorizer, not yet instruction source.
- **Nora Bell** — Bell; she/her. Northbridge facilities/technical watch; controls the local WSS-4 record within her scope.
- **Tom Baines** — Baines; he/him. Sergeant in the Prologue.
- **Daniel Hargrove** — Hargrove; he/him. Lieutenant colonel in the Prologue; retain rank appropriate to scene date.

## Organizations and locations

- Apex Defense Systems.
- Argus / Argus Beta / Argus Enterprise 4.6 — use the version appropriate to the scene date.
- Department of Defense.
- Defense Intelligence Agency / DIA.
- Defense Criminal Investigative Service / DCIS.
- Metropolitan Police Department / MPD; `Metropolitan Police` is acceptable when context is clear.
- Legislative Secure Services / LSS.
- Northbridge Strategic Initiatives.
- Fenwick Annex / Fenwick Building — preserve the accepted context-specific form.
- Hartwell Executive Briefing Annex.
- Forward Post Arjun.
- Northern Command.
- Line of Control — no hyphens.
- Relay K-17 / K-17.
- Apex Building Three / Building Three.
- Reston, Virginia; Fairfax County, Virginia; Prince William County, Virginia; Culpeper County, Virginia; Washington, D.C.; Kashmir.

## Technology, systems, and operational identifiers

Preserve these exact forms according to context:

- Argus; Argus Beta; Argus Enterprise 4.6.
- Validation Package 88; Payload 88; `VAL-088`.
- `PAK_RELAY_17A`.
- `PAK_RELAY_17A_SOURCE_CORRECTION`.
- `SIGMA-NORMALIZE-4`.
- `APX-DIR-0019`.
- `B3-EXEC-01`.
- `WSS-4`.
- `SSO-NS-004`.
- `K17-PHASE-B`.
- `ARGUS-K17-RC-0751`.
- `APX-ICF-4`.
- `ARJ-K17-ACK-01`.
- Incident 187463.
- PCF-27.
- Masking Window Two.
- Phase B.
- Hartwell operational window: 07:46:00–07:48:30 EDT.
- Phase B authorization deadline: 07:49 EDT.
- Masking Window Two: 07:48–07:54 EDT.

Dialogue may speak serials in words, such as `APX-DIR-zero-zero-one-nine`; displays and narration retain the literal identifier.

## Evidence objects and exact custody terms

- Aluminum incident-capture / telemetry case.
- Primary evidence drive inside the aluminum case.
- Administrator-token circuit board / administrator board.
- Signed recovery-record cartridge / recovery cartridge.
- Dual-partition field module.
- Partition A: sealed derivative, read-only.
- Partition B: sealed WSS-4 incident capture.
- Bound paper custody log.
- Waterproof folder and itemization.
- Disconnected PCF-27 fleet telematics module / dead fleet transponder.
- Hartwell local-challenge and handoff record.
- K-17 original local incident cartridge and separate derivative.

Exact case counts:

- 136 sealed files.
- 47 incomplete files.
- 311 excluded during finalization.

Do not silently turn incomplete or excluded material into sealed evidence. Do not merge separate evidence objects, custodians, seals, clocks, or derivatives into one universal record.

## Preferred compounds and forms

- source-provenance review / provenance review, according to context.
- source-correction object.
- source-record reconstruction.
- correction-dependent side table.
- counter-battery.
- cross-border.
- line-of-sight.
- read-only.
- source-native.
- source-limited.
- no-use hold.
- live-finger confirmation.
- private-key operation.
- hardware-authenticated.
- time-sensitive.
- life-safety.
- clean-agent suppression.
- chain of custody as a noun; chain-of-custody only as a compound modifier when needed.

## Proof and authority ceilings

Keep these distinctions exact:

- Julie’s formal abort recommendation is not engagement authority or weapons release authority.
- Indian commanders retain engagement and firing authority.
- Identity binding, certificate mirroring, workstation mirroring, server assertion, and public-certificate presentation are not the same as a private-key action by the physical token.
- A later authenticated act does not prove who performed an earlier act.
- Device registration does not prove physical possession.
- A physical carrier is not the authorizer.
- An authorizer is not necessarily the instruction source.
- A hardware response does not prove human understanding, intent, or command.
- `not established` does not mean disproved.
- `preserved` does not mean produced, admitted, adopted, or proved true.
- A hash match establishes unchanged captured bytes, not source truth, completeness, or lawful acquisition.
- Release from custody or a decision not to charge today is not a judicial finding of innocence and does not bar later lawful process.
- Institutional responsibility does not automatically establish personal keystrokes.
- Vance’s live local authentication is established for the later 07:52 remote reconstruction only; original 02:14 construction remains unidentified.
- The Sterling-office device and continuity chain are established; Sterling’s personal possession, knowledge, direction, intent, and command remain unestablished.
- Tariq’s registered field authority is established; Tariq’s presence, possession, keystrokes, or personal command remain unestablished.

## Repetition and rhythm controls

Review but do not mechanically delete:

- `That wasn’t the question.`
- `That is not the same fact.`
- `The record did not prove...`
- `Not established.`
- repeated inventory and seal language when custody state changes or must be independently stated.
- camera, visible-hands, clock-source, and receipt details when they establish a new record.
- short countdown paragraphs and chapter-end hooks.

Do not reintroduce repeated `Not X. Not Y. Z.` templates. Do not conduct another line-edit or AI-voice pass under the copyedit label.

## Decisions recorded in this pass

- Preserved every accepted chapter opening, chapter ending, scene order, POV order, and suspense beat.
- Preserved intentional fragments, short paragraphs, interface blocks, and proof-limit repetition.
- Corrected only unambiguous grammar and speaker/action-beat attribution errors.
- No technical, legal, medical, military, intelligence, or continuity issue was silently rewritten.
- Final line remains **The bubble stayed centered.**
'''

QUERY_LOG = '''# Book 1 Copyedit Query Log

**Book:** *Veridrift*  
**Pass:** Full mechanical copyedit  
**Status:** No author-level copyedit queries identified

The sequential copyedit of the manifest-listed Prologue and Chapters 1–24 identified no uncertainty that required an author decision without first changing canon, technical meaning, legal meaning, evidentiary weight, chronology, POV, or suspense structure.

Routine grammar, punctuation, dialogue-mechanics, and speaker-attribution corrections are reflected directly in the manuscript diff and are not repeated here.

## Open queries

None.

## Deferred specialist-review boundary

The repository’s publication-readiness controls still show external specialist reviews as pending. Any later accepted correction from cyber/AI systems, military/artillery, legal/procedural, medical/physiology, physical-security, geopolitical/India–Pakistan, or political/institutional review may require a focused recopyedit and continuity check before final proofing. This is a workflow dependency, not an author-level copyedit query.
'''


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one match in {path}: found {count}\nOLD={old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def accepted_paths(manifest_text: str) -> list[str]:
    paths: list[str] = []
    in_accepted = False
    for line in manifest_text.splitlines():
        if line == "accepted_files:":
            in_accepted = True
            continue
        if in_accepted and line and not line.startswith(" "):
            break
        if in_accepted:
            match = re.match(r'^\s+- path: "([^"]+)"\s*$', line)
            if match:
                paths.append(match.group(1))
    if len(paths) != 25:
        raise SystemExit(f"expected 25 accepted files, found {len(paths)}")
    return paths


def update_manifest() -> tuple[int, dict[str, int]]:
    text = MANIFEST.read_text(encoding="utf-8")
    paths = accepted_paths(text)
    metadata: dict[str, tuple[int, str]] = {}
    for rel in paths:
        data = (ROOT / rel).read_bytes()
        words = len(data.decode("utf-8").split())
        metadata[rel] = (words, hashlib.sha256(data).hexdigest())

    lines = text.splitlines()
    current: str | None = None
    seen_words: set[str] = set()
    seen_hashes: set[str] = set()
    for index, line in enumerate(lines):
        path_match = re.match(r'^\s+- path: "([^"]+)"\s*$', line)
        if path_match:
            candidate = path_match.group(1)
            current = candidate if candidate in metadata else None
            continue
        if current and re.match(r'^\s+words:\s+\d+\s*$', line):
            indent = line[: len(line) - len(line.lstrip())]
            lines[index] = f"{indent}words: {metadata[current][0]}"
            seen_words.add(current)
            continue
        if current and re.match(r'^\s+sha256:\s+"[0-9a-f]+"\s*$', line):
            indent = line[: len(line) - len(line.lstrip())]
            lines[index] = f'{indent}sha256: "{metadata[current][1]}"'
            seen_hashes.add(current)
            current = None

    if seen_words != set(paths) or seen_hashes != set(paths):
        raise SystemExit("manifest entries were not all updated")

    total = sum(words for words, _ in metadata.values())
    total_matches = [i for i, line in enumerate(lines) if re.match(r'^total_accepted_words:\s+\d+\s*$', line)]
    if len(total_matches) != 1:
        raise SystemExit(f"expected one total_accepted_words field, found {len(total_matches)}")
    lines[total_matches[0]] = f"total_accepted_words: {total}"
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return total, {rel: metadata[rel][0] for rel in paths}


def main() -> None:
    for rel, replacements in REPLACEMENTS.items():
        path = ROOT / rel
        for old, new in replacements:
            replace_once(path, old, new)

    control = ROOT / "books/book-01/control"
    (control / "61-copyedit-style-sheet.md").write_text(STYLE_SHEET, encoding="utf-8")
    (control / "62-copyedit-query-log.md").write_text(QUERY_LOG, encoding="utf-8")

    total, counts = update_manifest()
    final_path = ROOT / "books/book-01/manuscript/chapters/chapter-24.md"
    if final_path.read_text(encoding="utf-8").rstrip().splitlines()[-1] != "The bubble stayed centered.":
        raise SystemExit("accepted final line changed")

    expected_changed = {
        "books/book-01/manuscript/chapters/chapter-02.md",
        "books/book-01/manuscript/chapters/chapter-04.md",
        "books/book-01/manuscript/chapters/chapter-06.md",
        "books/book-01/manuscript/chapters/chapter-10.md",
        "books/book-01/manuscript/chapters/chapter-12.md",
    }
    print(f"accepted total: {total}")
    for rel in sorted(expected_changed):
        print(f"{counts[rel]:>6}  {rel}")


if __name__ == "__main__":
    main()
