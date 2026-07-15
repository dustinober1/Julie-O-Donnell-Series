#!/usr/bin/env python3
"""Validate the accepted Julie O'Donnell Book 1 state through Chapter 20."""

from pathlib import Path
import re
import subprocess

ROOT = Path(".")
BOOK = ROOT / "books/book-01"
CHAPTERS = BOOK / "manuscript/chapters"
DRAFTS = BOOK / "drafts"
CONTROL = BOOK / "control"


def require(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(message)


def blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path)], text=True
    ).strip()


def validate_protected_prose() -> None:
    protected = {
        "chapter-13.md": ("e7d04921431e571aab434f2f4b808655e363d30c", 6175),
        "chapter-14.md": ("78f7fff02cd271fecbc94f7daf7151dbebbd5c6d", 5763),
        "chapter-15.md": ("b8e7e2ae573a6c25ea096121c75acee867f3fad2", 5993),
        "chapter-16.md": ("dd5249f4b510a9da9ad19ab2902a95ce1e62a1d8", 6024),
        "chapter-17.md": ("1c4022ebb8d27d8d448f98bcf74fbf09e6e560c1", 5888),
        "chapter-18.md": ("6f5873d6e975ec74646af152aad22ea84545fc01", 4478),
        "chapter-19.md": ("1c7cc22fc7c480cb247efa1f6a2c0d0b1e1b1baf", 5393),
        "chapter-20.md": ("0bd12f43beeef48d5e897ee1fa78a333bd23099b", 4307),
    }

    for name, (expected_blob, expected_words) in protected.items():
        path = CHAPTERS / name
        require(path.is_file(), f"missing protected chapter: {name}")
        actual_blob = blob(path)
        require(
            actual_blob == expected_blob,
            f"protected blob changed: {name} = {actual_blob}",
        )
        words = len(path.read_text(encoding="utf-8").split())
        require(
            words == expected_words,
            f"protected count changed: {name} = {words}",
        )
    print("protected prose: OK")


def validate_review_and_inventory() -> None:
    mission20 = CONTROL / "40-chapter-20-mission-lock.md"
    review20 = CONTROL / "41-chapter-20-acceptance-review.md"
    chapter20 = CHAPTERS / "chapter-20.md"

    mission_blob = blob(mission20)
    require(
        mission_blob == "c074e4f6f9ec9cddcbc701e2923f34b3082ede5a",
        f"Chapter 20 mission lock changed: {mission_blob}",
    )
    require(review20.is_file(), "Chapter 20 acceptance review missing")
    review_text = review20.read_text(encoding="utf-8")
    for sentinel in [
        "# ACCEPT",
        "## Promotion authorization",
        "Reviewed/promoted prose blob:** `0bd12f43beeef48d5e897ee1fa78a333bd23099b`",
        "Exact final word count:** **4,307**",
        "New accepted-manuscript total:** **107,676**",
        "No Chapter 21 prose, Chapter 21 mission lock",
    ]:
        require(sentinel in review_text, f"acceptance review missing: {sentinel}")

    chapter20_paths = sorted(BOOK.rglob("chapter-20.md"))
    require(
        chapter20_paths == [chapter20],
        f"unexpected Chapter 20 prose paths: {chapter20_paths}",
    )
    require(not (DRAFTS / "chapter-20.md").exists(), "Chapter 20 draft remains")
    require(
        sorted(CONTROL.glob("*chapter-20-mission-lock*.md")) == [mission20],
        "alternate Chapter 20 mission lock exists",
    )
    require(
        sorted(CONTROL.glob("*chapter-20-acceptance-review*.md")) == [review20],
        "alternate Chapter 20 acceptance review exists",
    )

    manifest = (BOOK / "ACCEPTED_MANUSCRIPT.yaml").read_text(encoding="utf-8")
    require("accepted_words: 107676" in manifest, "accepted total changed")
    require(
        "accepted_endpoint:\n  chapter: 20" in manifest,
        "accepted endpoint is not Chapter 20",
    )
    require('eastern: "11:26:32 EDT"' in manifest, "accepted eastern endpoint changed")
    require('india: "20:56:32 IST"' in manifest, "accepted India endpoint changed")
    listed = [int(n) for n in re.findall(r"chapter-(\d+)\.md", manifest)]
    require(
        listed.count(20) == 1 and max(listed) == 20,
        f"Chapter 20 manifest state invalid: {listed}",
    )
    print("review and inventory: OK")


def validate_chapter20_content() -> None:
    text20 = (CHAPTERS / "chapter-20.md").read_text(encoding="utf-8")
    require(
        text20.startswith(
            "10:44:12 EDT / 20:14:12 IST\n\n"
            "# Chapter 20 - The Custody Exception\n\n"
            "Secure MPD Evidence Intake\nWashington, D.C.\n"
        ),
        "Chapter 20 opening changed",
    )
    require(
        "At 11:26:32 EDT / 20:56:32 IST" in text20[-2400:],
        "Chapter 20 endpoint missing",
    )
    require(
        text20.count("Legislative Secure Services Compromise-Control Intake") == 1,
        "Grant cutaway architecture changed",
    )
    require(
        text20.count("Secure MPD Evidence Intake") == 2,
        "Julie location architecture changed",
    )

    required = [
        "Legislative Secure Services no-use hold begins now",
        "Custodian Martin Vann",
        "Deputy authority Marisol Vega",
        "LSS-SL-90418",
        "LSS-CD-187463-01",
        "WSS4-CD-187463-01",
        "Samuel Drennan",
        "Diane Kessler",
        "06:54:00–10:57:18 EDT",
        "The carrier is not the authorizer.",
        "the authorizer is not yet the instruction source",
        "No transfer to DCIS or MPD.",
        "It did not identify Samuel Drennan as the WSS carrier.",
        "Hartwell retained `HWA-LCA-1187`",
        "WSS-4 retained its local audit and sponsor original",
        "Forward Post Arjun retained `ARJ-K17-001`, `ARJ-K17-002`, and `ARJ-K17-003`",
        "MPD retained `MPD-901441` through `MPD-901447`",
        "seven sealed packages in the same locked chest",
        "ORIGINALS: RETAINED BY SOURCE CUSTODIANS",
        "STERLING PERSONAL POSSESSION / OPERATION / COMMAND: NOT ESTABLISHED",
        "Who instructed Kessler to create and use the continuity exception",
    ]
    missing = [item for item in required if item not in text20]
    require(not missing, f"Chapter 20 required element missing: {missing}")

    prohibited = [
        "Sterling instructed Kessler",
        "Drennan was a conspirator",
        "Bell was a conspirator",
        "Northbridge knowingly joined",
        "Vance personally typed",
        "WSS plaintext was decrypted",
        "Sterling was guilty",
        "Julie was exonerated",
        "Samuel Drennan’s credential appeared at both WSS-4 and Hartwell",
        "carrier credential belonging to Samuel Drennan",
    ]
    present = [item for item in prohibited if item in text20]
    require(not present, f"Chapter 20 prohibited conclusion present: {present}")
    print("Chapter 20 content sentinels: OK")


def validate_synchronized_controls() -> None:
    for path in [
        ROOT / "PROJECT_STATE.yaml",
        ROOT / "README.md",
        BOOK / "manuscript/STATUS.md",
        CONTROL / "16-chapter-by-chapter-status-record.md",
        CONTROL / "18-act-iii-entry-state.md",
        CONTROL / "20-control-pack-maintenance-rules.md",
        CONTROL / "23-word-budget-and-act-iii-architecture.md",
        CONTROL / "24-thread-disposition-matrix.md",
        CONTROL / "README.md",
    ]:
        text = path.read_text(encoding="utf-8")
        require(
            "107,676" in text or "107676" in text,
            f"accepted total missing in {path}",
        )
        require("11:26:32 EDT" in text, f"Chapter 20 endpoint missing in {path}")

    require(
        "No active Book 1 chapter draft exists."
        in (DRAFTS / "README.md").read_text(encoding="utf-8"),
        "draft status not synchronized",
    )

    for path in [
        CONTROL / "00-overview.md",
        CONTROL / "02-current-project-state.md",
        CONTROL / "04-source-of-truth-canon-locks.md",
        CONTROL / "05-master-timeline.md",
        CONTROL / "06-character-state-ledger.md",
        CONTROL / "07-relationship-and-trust-matrix.md",
        CONTROL / "08-evidence-and-chain-of-custody-ledger.md",
        CONTROL / "09-knowledge-and-information-control-matrix.md",
        CONTROL / "10-technology-and-system-rules.md",
        CONTROL / "11-organizations-authorities-and-institutional-control.md",
        CONTROL / "12-location-and-security-architecture.md",
        CONTROL / "13-antagonist-objectives-and-conspiracy-model.md",
        CONTROL / "14-public-narrative-versus-actual-record.md",
        CONTROL / "15-open-plot-threads-and-payoff-matrix.md",
    ]:
        require(
            "<!-- CH20_ACCEPTED_STATE_START -->"
            in path.read_text(encoding="utf-8"),
            f"Chapter 20 control delta missing in {path}",
        )
    print("synchronized controls: OK")


def validate_absence_and_hygiene() -> None:
    require(not list(BOOK.rglob("chapter-21.md")), "Chapter 21 prose exists")
    require(
        not list(CONTROL.glob("*chapter-21-mission-lock*.md")),
        "Chapter 21 mission lock exists",
    )
    require(
        not (ROOT / ".github/workflows/chapter20-acceptance-apply.yml").exists(),
        "temporary acceptance workflow remains",
    )
    require(
        not (ROOT / ".github/workflows/chapter20-acceptance-pr.yml").exists(),
        "temporary pull-request runner remains",
    )
    require(
        not (ROOT / "chapter20-validator-final.yml").exists(),
        "temporary validator handoff remains",
    )
    require(
        not (ROOT / ".chapter20-acceptance-py").exists(),
        "temporary Chapter 20 script directory remains",
    )
    require(
        not (ROOT / ".chapter20-acceptance").exists(),
        "temporary Chapter 20 payload directory remains",
    )

    text20 = (CHAPTERS / "chapter-20.md").read_text(encoding="utf-8")
    for artifact in ["TODO", "DRAFTING NOTE", "ALTERNATE VERSION", "PLACEHOLDER"]:
        require(artifact not in text20, f"Chapter 20 drafting artifact remains: {artifact}")
    print("absence and hygiene sentinels: OK")


def main() -> None:
    validate_protected_prose()
    validate_review_and_inventory()
    validate_chapter20_content()
    validate_synchronized_controls()
    validate_absence_and_hygiene()
    print("Book 1 accepted Chapter 20 state: VALID")


if __name__ == "__main__":
    main()
