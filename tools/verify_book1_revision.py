#!/usr/bin/env python3
"""Independent final verification for the Book 1 developmental revision."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-01"
MANIFEST = BOOK / "ACCEPTED_MANUSCRIPT.yaml"
COMPILED = BOOK / "compiled/current/Julie_O_Donnell_Book_1_REVISED.md"
REPORT = ROOT / "artifacts/book1-final-verification.md"
TARGET_MIN = 105_000
TARGET_MAX = 110_000
EXPECTED_TOTAL = 105_081
PROTECTED_HASHES = {
    "books/book-01/manuscript/prologue.md": "e1cd0d3c1d01539130fda08dd9068405a2e67b4a3527297431131afbd13a9ce7",
    "books/book-01/manuscript/chapters/chapter-01.md": "99219cdc18b6e21c353e06f21c97740d9375045f9515ca40d920d87cc51cc75a",
}
FORBIDDEN = (
    "the answer matched Chapter 11",
    "the scene card begun in Chapter 14",
    "the end of Chapter 21",
    "the Chapter 21 comparison",
    "during Chapter 21",
    "the same restraint geometry in which Chapter 22 had ended",
    "On July thirteenth",
    "At exactly 08:14:44 EDT / 17:44:44 IST",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    raise AssertionError(message)


def manifest_entries() -> tuple[list[dict[str, str]], int]:
    text = MANIFEST.read_text(encoding="utf-8")
    total_match = re.search(r"^total_accepted_words:\s*(\d+)\s*$", text, re.MULTILINE)
    if not total_match:
        fail("manifest total word count missing")
    block = text.split("\nexcluded_from_canon:", 1)[0]
    pattern = re.compile(
        r'^\s+- path:\s+"([^"]+)"\s*\n'
        r'\s+title:\s+"([^"]+)"\s*\n'
        r'\s+accepted_on:\s+"([^"]+)"\s*\n'
        r'\s+words:\s+(\d+)\s*\n'
        r'\s+sha256:\s+"([a-f0-9]{64})"\s*$',
        re.MULTILINE,
    )
    entries = [
        {"path": p, "title": t, "accepted_on": a, "words": w, "sha": s}
        for p, t, a, w, s in pattern.findall(block)
    ]
    if len(entries) != 25:
        fail(f"expected 25 manifest entries, found {len(entries)}")
    return entries, int(total_match.group(1))


def paragraph_metrics(text: str) -> tuple[int, int]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    prose = [part for part in paragraphs if not part.startswith("#")]
    one_sentence = 0
    for part in prose:
        marks = len(re.findall(r"[.!?](?:[”\"])?(?:\s|$)", part))
        if marks <= 1:
            one_sentence += 1
    return len(prose), one_sentence


def main() -> None:
    checks: list[str] = []
    entries, manifest_total = manifest_entries()
    paths: list[Path] = []
    actual_total = 0

    for index, entry in enumerate(entries):
        path = ROOT / entry["path"]
        if not path.is_file():
            fail(f"missing accepted file: {entry['path']}")
        paths.append(path)
        words = len(path.read_text(encoding="utf-8").split())
        actual_total += words
        if words != int(entry["words"]):
            fail(f"word mismatch {entry['path']}: manifest={entry['words']} actual={words}")
        actual_sha = digest(path)
        if actual_sha != entry["sha"]:
            fail(f"hash mismatch {entry['path']}")
        if index == 0 and path.name != "prologue.md":
            fail("first accepted file is not prologue")
        if index > 0:
            expected_number = index
            expected_name = f"chapter-{expected_number:02d}.md"
            if path.name != expected_name:
                fail(f"accepted order mismatch: expected {expected_name}, found {path.name}")
            first_line = path.read_text(encoding="utf-8").splitlines()[0]
            if not re.fullmatch(rf"# Chapter {expected_number} — .+", first_line):
                fail(f"chapter heading mismatch: {entry['path']} -> {first_line!r}")

    if actual_total != manifest_total:
        fail(f"manifest total {manifest_total} != actual total {actual_total}")
    if actual_total != EXPECTED_TOTAL:
        fail(f"expected final total {EXPECTED_TOTAL}, found {actual_total}")
    if not TARGET_MIN <= actual_total <= TARGET_MAX:
        fail(f"word count outside target: {actual_total}")
    checks.append(f"Accepted inventory: 25 files, {actual_total:,} words, all hashes match.")

    for relative, expected in PROTECTED_HASHES.items():
        actual = digest(ROOT / relative)
        if actual != expected:
            fail(f"protected opening file changed: {relative}")
    checks.append("Protected prologue and Chapter 1 hashes are unchanged.")

    accepted_text = "\n\n".join(path.read_text(encoding="utf-8") for path in paths)
    for phrase in FORBIDDEN:
        if phrase in accepted_text:
            fail(f"forbidden drafting/continuity artifact remains: {phrase}")
    if re.search(r"[^\n]# Chapter \d+", accepted_text):
        fail("chapter heading attached to prose")
    if "`" in accepted_text:
        fail("backtick display artifacts remain")
    checks.append("Publication blockers and drafting artifacts are absent.")

    detailed_thermostat = sum(
        phrase in accepted_text
        for phrase in ("He generated a compressor fault.", "He bridged the contacts eight times.")
    )
    if detailed_thermostat != 1:
        fail(f"expected one detailed thermostat transmission, found {detailed_thermostat}")
    checks.append("Thermostat transmission appears once in detailed form.")

    required = {
        "bilateral pilot": "classified bilateral pilot",
        "Apex delegated authority": "The contract divided sovereignty from control.",
        "SIGMA transformation": "REVISION 8 VARIATION MAP: INPUT",
        "Julie K-17 error": "INITIAL RELEASE SUSPENSION ACHIEVED USING OVERBROAD DEPENDENCY BOUNDARY.",
        "K-17 delay": "ADDITIONAL DELAY ATTRIBUTABLE TO ANALYTIC SCOPE: 43 SECONDS.",
        "Grant blind replication": "Alvarez required a blind replication.",
        "Vance later release": "VANCE LIVE AUTHENTICATION OF 07:52 REMOTE RECONSTRUCTION: ESTABLISHED.",
        "Sterling proof limit": "STERLING PERSONAL COMMAND: NOT ESTABLISHED",
        "series thread": "ORIGINAL 02:14 DEPLOYMENT CONSTRUCTOR: NOT IDENTIFIED.",
    }
    for label, phrase in required.items():
        if phrase not in accepted_text:
            fail(f"required revision missing: {label}")
    checks.append("Technical causality, Julie's analytical error, independent replication, and antagonist proof limits are present.")

    chronology = {
        15: "October 13",
        17: "October 14",
        20: "October 15",
        24: "October 16",
    }
    for number, date in chronology.items():
        text = (BOOK / f"manuscript/chapters/chapter-{number:02d}.md").read_text(encoding="utf-8")
        if date not in text[:250]:
            fail(f"final-act chronology missing in Chapter {number}: {date}")
    checks.append("Final investigation chronology spans October 13–16.")

    chapter_24 = (BOOK / "manuscript/chapters/chapter-24.md").read_text(encoding="utf-8")
    if not chapter_24.rstrip().endswith("The bubble stayed centered."):
        fail("final line changed")
    final_farm = chapter_24.rsplit("\n\n---\n\n", 1)[-1]
    if re.search(r"\b\d{2}:\d{2}(?::\d{2})?\s+(?:EDT|EST|IST)\b", final_farm):
        fail("exact timestamp remains in final farm section")
    checks.append("Final image is untimestamped and final line is preserved.")

    compiled_expected = "\n\n".join(path.read_text(encoding="utf-8").rstrip() for path in paths) + "\n"
    if not COMPILED.is_file():
        fail("compiled revised manuscript missing")
    compiled_actual = COMPILED.read_text(encoding="utf-8")
    if compiled_actual != compiled_expected:
        fail("compiled revised manuscript does not equal accepted inventory")
    if len(compiled_actual.split()) != actual_total:
        fail("compiled word count mismatch")
    checks.append("Compiled revised manuscript exactly matches accepted inventory.")

    specialist = (BOOK / "control/50-specialist-review-brief.md").read_text(encoding="utf-8")
    if specialist.count("UNREVIEWED") < 6:
        fail("specialist brief does not mark all required areas UNREVIEWED")
    for term in ("SIGINT", "Military Targeting", "Classified-Facility", "PKI", "Federal Investigation", "Indian Army"):
        if term not in specialist:
            fail(f"specialist area missing: {term}")
    checks.append("Six required specialist reviews are explicitly marked UNREVIEWED.")

    for control in (
        ROOT / "README.md",
        ROOT / "PROJECT_STATE.yaml",
        BOOK / "manuscript/STATUS.md",
        BOOK / "control/00-overview.md",
    ):
        if f"{actual_total:,}" not in control.read_text(encoding="utf-8") and str(actual_total) not in control.read_text(encoding="utf-8"):
            fail(f"control file missing current word count: {control.relative_to(ROOT)}")
    checks.append("Primary control files report the current accepted word count.")

    prose_paragraphs, one_sentence = paragraph_metrics(accepted_text)
    ratio = one_sentence / prose_paragraphs if prose_paragraphs else 0
    if ratio > 0.70:
        fail(f"one-sentence paragraph ratio remains too high: {ratio:.1%}")
    checks.append(f"Paragraph rhythm gate passes: {one_sentence:,}/{prose_paragraphs:,} one-sentence paragraphs ({ratio:.1%}).")

    report_lines = [
        "# Book 1 Final Verification",
        "",
        "**Result:** PASS",
        "",
        f"**Accepted words:** {actual_total:,}",
        f"**Compiled SHA-256:** `{digest(COMPILED)}`",
        "",
        "## Checks",
        "",
    ]
    report_lines.extend(f"- PASS — {check}" for check in checks)
    report_lines.extend(
        [
            "",
            "## Publication gate",
            "",
            "Developmental revision and repository verification are complete. External specialist review, approved technical corrections, line/copyedit, and proofread remain required before publication.",
            "",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"PASS: Book 1 final verification ({actual_total:,} words)")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
