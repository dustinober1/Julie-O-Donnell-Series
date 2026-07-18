#!/usr/bin/env python3
"""Apply the three source-backed Book 1 desk-review corrections.

The replacements are intentionally exact and idempotent. The script updates the
accepted-manuscript word counts, SHA-256 values, total, and active control totals.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "books/book-01/ACCEPTED_MANUSCRIPT.yaml"

REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "books/book-01/manuscript/prologue.md": [
        (
            "Julie shoved past Hargrove, opened the emergency strike channel, and transmitted the order.",
            "Julie shoved past Hargrove, opened the emergency strike channel, and transmitted the formal abort recommendation.",
        )
    ],
    "books/book-01/manuscript/chapters/chapter-02.md": [
        (
            "The service had created a temporary mirror of his workstation, replayed his biometric token, and hidden the elevated act behind his identity. The mirror preserved the workstation serial, local clock, credential path, and expected biometric response. The audit trail did not look forged. It looked complete. Anyone reviewing it later would begin with Elias’s name, token, desk, and confirmed authentication. The administrative service sat one layer lower, available only to someone who already doubted the official event enough to look. The system had not fabricated an implausible alibi for itself. It had assembled the exact evidence an investigator had been trained to trust.",
            "The service had created a temporary mirror of his workstation, replayed his identity binding and public certificate, and hidden the elevated act behind his name. The mirror preserved the workstation serial, local clock, credential path, and a server-side assertion that biometric release had been confirmed. It did not reproduce a live finger or invoke the private key inside his physical token. The audit trail did not look forged. It looked complete. Anyone reviewing it later would begin with Elias’s name, token identity, desk, and confirmed-authentication status. The administrative service sat one layer lower, available only to someone who already doubted the official event enough to look. The system had not fabricated an implausible alibi for itself. It had assembled the exact evidence an investigator had been trained to trust.",
        )
    ],
    "books/book-01/manuscript/chapters/chapter-24.md": [
        (
            "Dana Webb, appointed for Julie’s immediate custody review, stood beside Ortiz with a court order held beneath the intake camera. Alvarez appeared on the federal channel. Grant sat at evidence control without an open source window. The common chest remained behind glass, closed and out of Julie’s reach. Webb began with the part no headline had decided.",
            "Dana Webb, appointed for Julie’s immediate custody review, stood beside Ortiz with a written MPD release authorization and counsel undertaking held beneath the intake camera. Alvarez appeared on the federal channel. Grant sat at evidence control without an open source window. The common chest remained behind glass, closed and out of Julie’s reach. Webb began with the part no headline had decided.",
        ),
        (
            "“DCIS has withdrawn its request for continued investigative detention. The United States Attorney’s Office is not seeking a present federal detainer. Neither decision is a charging disposition.”",
            "“DCIS has withdrawn its request for continued investigative detention. The United States Attorney’s Office is not seeking a present federal detainer. The D.C. prosecutor has declined to paper a local charge today. None of those decisions is a final charging disposition.”",
        ),
        (
            "“MPD, after the watch commander accepts the court order.”",
            "“MPD, after the watch commander accepts the release authorization.”",
        ),
        (
            "The order had been entered by a federal magistrate after a recorded conference involving Webb, the duty prosecutor, MPD counsel, Alvarez, and the receiving hospital. It authorized removal of the intake restraint and guarded transport for imaging, immobilization, observation, and treatment. If the attending physician later approved discharge, Julie would be released to transportation arranged through counsel.",
            "The authorization followed a recorded custody conference involving Webb, the duty federal and D.C. prosecutors, MPD counsel, Alvarez, and the receiving hospital. It directed MPD to remove the intake restraint and release Julie for counsel-arranged transport for imaging, immobilization, observation, and treatment. If the attending physician later approved discharge, she would remain outside custody unless a lawful arrest, warrant, summons, or detainer issued.",
        ),
        (
            "The order did not dismiss a charge that had not been filed. It did not decide admissibility, privilege, classification, employment, clearance, or the lawfulness of any act she had taken after leaving Apex. Its conditions were narrower than custody and wider than freedom.",
            "The authorization did not dismiss a charge that had not been filed. It did not decide admissibility, privilege, classification, employment, clearance, or the lawfulness of any act she had taken after leaving Apex. The accompanying counsel undertaking was narrower than custody and wider than an ordinary promise.",
        ),
        (
            "Julie had to remain available through Webb, appear on lawful notice, avoid contact with the seven MPD packages and every source original, enter no classified system, use no borrowed or suspended credential, and perform no investigative work on her own case. Any later evidence access required a new written authority naming the custodian, question, method, and scope.",
            "Julie agreed through Webb to remain available, appear on lawful notice, avoid contact with the seven MPD packages and every source original, enter no classified system, use no borrowed or suspended credential, and perform no investigative work on her own case. Any later evidence access required a new written authority naming the custodian, question, method, and scope.",
        ),
        (
            "MPD Watch Commander Helena Brooks entered the intake, identified herself to both cameras, and accepted the order.",
            "MPD Watch Commander Helena Brooks entered the intake, identified herself to both cameras, and accepted the release authorization and recorded undertaking.",
        ),
        (
            "Webb placed a sealed copy of the release conditions in Julie's property envelope and kept another.",
            "Webb placed a sealed copy of the release authorization and undertaking in Julie's property envelope and kept another.",
        ),
    ],
}


def apply_exact_replacements() -> None:
    for relative, pairs in REPLACEMENTS.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        changed = False
        for old, new in pairs:
            if new in text:
                continue
            count = text.count(old)
            if count != 1:
                raise RuntimeError(
                    f"expected exactly one source passage in {relative}; found {count}"
                )
            text = text.replace(old, new, 1)
            changed = True
        if changed:
            path.write_text(text, encoding="utf-8")


def accepted_paths(manifest_text: str) -> list[str]:
    accepted = manifest_text.split("\nexcluded_from_canon:", 1)[0]
    paths = re.findall(
        r'^\s+(?:-\s+)?path:\s*"([^"]+)"\s*$', accepted, re.MULTILINE
    )
    if len(paths) != 25:
        raise RuntimeError(f"expected 25 accepted prose paths; found {len(paths)}")
    return paths


def refresh_manifest_and_controls() -> int:
    manifest_text = MANIFEST.read_text(encoding="utf-8")
    paths = accepted_paths(manifest_text)
    total = 0

    for relative in paths:
        text = (ROOT / relative).read_text(encoding="utf-8")
        words = len(text.split())
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        total += words
        pattern = re.compile(
            rf'(  - path: "{re.escape(relative)}"\n'
            rf'    title: "[^"]+"\n'
            rf'    accepted_on: "[^"]+"\n'
            rf'    words: )\d+(\n'
            rf'    sha256: ")[0-9a-f]{{64}}(")'
        )
        manifest_text, count = pattern.subn(
            rf'\g<1>{words}\g<2>{digest}\g<3>', manifest_text, count=1
        )
        if count != 1:
            raise RuntimeError(f"could not refresh manifest entry for {relative}")

    manifest_text, count = re.subn(
        r"^total_accepted_words:\s*\d+\s*$",
        f"total_accepted_words: {total}",
        manifest_text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise RuntimeError("could not refresh manifest total")
    MANIFEST.write_text(manifest_text, encoding="utf-8")

    formatted = f"{total:,}"
    control_files = (
        ROOT / "README.md",
        ROOT / "books/book-01/control/README.md",
        ROOT / "books/book-01/control/51-publication-readiness-status.md",
    )
    for path in control_files:
        text = path.read_text(encoding="utf-8")
        text, count = re.subn(r"105,081", formatted, text)
        if count == 0 and formatted not in text:
            raise RuntimeError(f"accepted total not found in {path.relative_to(ROOT)}")
        path.write_text(text, encoding="utf-8")
    return total


def main() -> None:
    apply_exact_replacements()
    total = refresh_manifest_and_controls()
    print(f"Applied desk-review corrections; accepted words={total:,}")


if __name__ == "__main__":
    main()
