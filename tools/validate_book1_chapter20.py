#!/usr/bin/env python3
"""Validate accepted Book 1 through Chapter 20 and the authorized Chapter 21 non-canon draft."""

from pathlib import Path
import os
import re
import subprocess

ROOT = Path(".")
BOOK = ROOT / "books/book-01"
CHAPTERS = BOOK / "manuscript/chapters"
DRAFTS = BOOK / "drafts"
CONTROL = BOOK / "control"
MANIFEST = BOOK / "ACCEPTED_MANUSCRIPT.yaml"

EXPECTED_MANIFEST_BLOB = "93cc38d2927cbfd99d8a622a93b11f53a2df8ee2"
EXPECTED_CHAPTER21_LOCK_BLOB = "6c92a5764e5c74d88a8325511ae2b0a86b30b356"
EXPECTED_CHAPTER21_DRAFT_BLOB = "866d4210b7fc808aef48144a91a58280f38fc99c"
EXPECTED_CHAPTER21_DRAFT_WORDS = 4415
CHAPTER21_HARD_CEILING = 5400
AUTHORIZED_DRAFT = DRAFTS / "chapter-21.md"


def require(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(message)


def blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path)], text=True
    ).strip()


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


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
        words = word_count(path)
        require(
            words == expected_words,
            f"protected count changed: {name} = {words}",
        )
    print("protected accepted prose: OK")


def validate_review_and_inventory() -> None:
    mission20 = CONTROL / "40-chapter-20-mission-lock.md"
    review20 = CONTROL / "41-chapter-20-acceptance-review.md"
    chapter20 = CHAPTERS / "chapter-20.md"

    require(
        blob(mission20) == "c074e4f6f9ec9cddcbc701e2923f34b3082ede5a",
        "Chapter 20 mission lock changed",
    )
    require(review20.is_file(), "Chapter 20 acceptance review missing")
    review_text = review20.read_text(encoding="utf-8")
    for sentinel in [
        "# ACCEPT",
        "## Promotion authorization",
        "Reviewed/promoted prose blob:** `0bd12f43beeef48d5e897ee1fa78a333bd23099b`",
        "Exact final word count:** **4,307**",
        "New accepted-manuscript total:** **107,676**",
    ]:
        require(sentinel in review_text, f"Chapter 20 review missing: {sentinel}")

    require(
        sorted(BOOK.rglob("chapter-20.md")) == [chapter20],
        "unexpected Chapter 20 prose path",
    )
    require(not (DRAFTS / "chapter-20.md").exists(), "Chapter 20 draft remains")

    require(MANIFEST.is_file(), "accepted manifest missing")
    actual_manifest_blob = blob(MANIFEST)
    require(
        actual_manifest_blob == EXPECTED_MANIFEST_BLOB,
        f"accepted manifest changed: {actual_manifest_blob}",
    )
    manifest = MANIFEST.read_text(encoding="utf-8")
    require("accepted_words: 107676" in manifest, "accepted total changed")
    require(
        "accepted_endpoint:\n  chapter: 20" in manifest,
        "accepted endpoint is not Chapter 20",
    )
    require('eastern: "11:26:32 EDT"' in manifest, "accepted EDT endpoint changed")
    require('india: "20:56:32 IST"' in manifest, "accepted IST endpoint changed")
    listed = [int(n) for n in re.findall(r"chapter-(\d+)\.md", manifest)]
    require(listed.count(20) == 1 and max(listed) == 20, "manifest chapter range changed")
    require(21 not in listed, "Chapter 21 entered accepted manifest")
    print("review and accepted inventory: OK")


def validate_chapter20_content() -> None:
    text = (CHAPTERS / "chapter-20.md").read_text(encoding="utf-8")
    require(
        text.startswith(
            "10:44:12 EDT / 20:14:12 IST\n\n"
            "# Chapter 20 - The Custody Exception\n\n"
            "Secure MPD Evidence Intake\nWashington, D.C.\n"
        ),
        "Chapter 20 opening changed",
    )
    require(
        "At 11:26:32 EDT / 20:56:32 IST" in text[-2400:],
        "Chapter 20 endpoint missing",
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
        "MPD retained `MPD-901441` through `MPD-901447`",
        "Who instructed Kessler to create and use the continuity exception",
    ]
    missing = [item for item in required if item not in text]
    require(not missing, f"Chapter 20 required element missing: {missing}")
    print("Chapter 20 content sentinels: OK")


def validate_chapter21_mission_lock() -> None:
    mission = CONTROL / "42-chapter-21-mission-lock.md"
    require(mission.is_file(), "Chapter 21 mission lock missing")
    actual = blob(mission)
    require(
        actual == EXPECTED_CHAPTER21_LOCK_BLOB,
        f"Chapter 21 mission lock changed: {actual}",
    )
    require(
        sorted(CONTROL.glob("*chapter-21-mission-lock*.md")) == [mission],
        "Chapter 21 mission lock missing or duplicated",
    )
    text = mission.read_text(encoding="utf-8")
    for sentinel in [
        "# 42. CHAPTER 21 MISSION LOCK — THE BORROWED NAME",
        "11:26:32 EDT / 20:56:32 IST",
        "12:18:04 EDT / 21:48:04 IST",
        "Leland Price",
        "The initiating instruction therefore contains a borrowed or constructed identity path.",
        "Who constructed and submitted the `NSB-EMERGENCY` continuity request",
    ]:
        require(sentinel in text, f"Chapter 21 mission lock missing: {sentinel}")
    print("Chapter 21 mission lock: OK")


def validate_chapter21_draft() -> None:
    require(AUTHORIZED_DRAFT.is_file(), "authorized Chapter 21 draft missing")
    chapter21_paths = sorted(BOOK.rglob("chapter-21.md"))
    require(
        chapter21_paths == [AUTHORIZED_DRAFT],
        f"unexpected Chapter 21 prose paths: {chapter21_paths}",
    )
    require(
        not (CHAPTERS / "chapter-21.md").exists(),
        "Chapter 21 prose entered accepted manuscript",
    )

    actual_blob = blob(AUTHORIZED_DRAFT)
    actual_words = word_count(AUTHORIZED_DRAFT)
    require(
        actual_blob == EXPECTED_CHAPTER21_DRAFT_BLOB,
        f"Chapter 21 draft blob changed: {actual_blob}",
    )
    require(
        actual_words == EXPECTED_CHAPTER21_DRAFT_WORDS,
        f"Chapter 21 draft count changed: {actual_words}",
    )
    require(
        actual_words <= CHAPTER21_HARD_CEILING,
        f"Chapter 21 draft exceeds hard ceiling: {actual_words}",
    )

    text = AUTHORIZED_DRAFT.read_text(encoding="utf-8")
    require(
        text.startswith(
            "11:26:32 EDT / 20:56:32 IST\n\n"
            "# Chapter 21 - The Borrowed Name\n\n"
            "Secure MPD Evidence Intake\nWashington, D.C.\n"
        ),
        "Chapter 21 draft opening changed",
    )
    require(
        "At 12:18:04 EDT / 21:48:04 IST" in text[-2600:],
        "Chapter 21 draft endpoint missing",
    )
    require(text.count("DIA Administrative Review Unit") == 1, "Price cutaway count changed")
    require(text.count("Secure MPD Evidence Intake") == 2, "Julie location architecture changed")

    required = [
        "SO-NS-REQ-6540",
        "SO-CD-187463-02",
        "DIA-SAR-PRICE-01",
        "DIA-AR-PRICE-01",
        "DCIS-CD-187463-PRICE-01",
        "Price’s active authority ended more than twelve hours before",
        "SSO-NS-004",
        "WSS-4",
        "K17-PHASE-B",
        "The named requestor is not the instruction source",
        "Kessler remained the authorizer",
        "Drennan remained the carrier",
        "REQUEST CONSTRUCTOR: UNPROVED",
        "MPD-901441 through MPD-901447",
        "LSS-SL-90418",
        "four liters of oxygen",
        "ninety-two to ninety-three percent saturation",
        "successful remote Argus reconstruction",
        "who constructed and submitted the `NSB-EMERGENCY` continuity request after Price’s authority ended",
    ]
    missing = [item for item in required if item not in text]
    require(not missing, f"Chapter 21 required element missing: {missing}")

    prohibited = [
        "Sterling instructed Kessler",
        "Sterling personally operated",
        "Price authored the later request",
        "Price was innocent",
        "Kessler was a conspirator",
        "Drennan was a conspirator",
        "Vance personally typed",
        "Vance built the borrowed Price identity",
        "Tariq was physically present",
        "WSS plaintext was decrypted",
        "Julie was exonerated",
        "Sterling was guilty",
        "same person built both",
        "same actor created every",
    ]
    present = [item for item in prohibited if item in text]
    require(not present, f"Chapter 21 prohibited conclusion present: {present}")

    for artifact in ["TODO", "DRAFTING NOTE", "ALTERNATE VERSION", "PLACEHOLDER"]:
        require(artifact not in text, f"Chapter 21 drafting artifact remains: {artifact}")
    print("Chapter 21 non-canon draft: OK")


def validate_synchronized_controls() -> None:
    synchronized = [
        ROOT / "PROJECT_STATE.yaml",
        ROOT / "README.md",
        BOOK / "manuscript/STATUS.md",
        DRAFTS / "README.md",
        CONTROL / "16-chapter-by-chapter-status-record.md",
        CONTROL / "18-act-iii-entry-state.md",
        CONTROL / "20-control-pack-maintenance-rules.md",
        CONTROL / "23-word-budget-and-act-iii-architecture.md",
        CONTROL / "24-thread-disposition-matrix.md",
        CONTROL / "README.md",
    ]

    for path in synchronized:
        text = path.read_text(encoding="utf-8")
        require("107,676" in text or "107676" in text, f"accepted total missing in {path}")
        require("11:26:32 EDT" in text, f"accepted endpoint missing in {path}")
        require("The Borrowed Name" in text, f"Chapter 21 title missing in {path}")
        require(EXPECTED_CHAPTER21_LOCK_BLOB in text, f"mission-lock blob missing in {path}")
        require(EXPECTED_CHAPTER21_DRAFT_BLOB in text, f"draft blob missing in {path}")
        require(str(EXPECTED_CHAPTER21_DRAFT_WORDS) in text.replace(",", ""), f"draft count missing in {path}")
        require("non-canon" in text.lower(), f"non-canon state missing in {path}")
        require("acceptance review" in text.lower(), f"review gate missing in {path}")

    project = (ROOT / "PROJECT_STATE.yaml").read_text(encoding="utf-8")
    require("accepted_words: 107676" in project, "PROJECT_STATE accepted words changed")
    require(
        "accepted_manuscript_effect: none" in project,
        "PROJECT_STATE draft effect missing",
    )
    print("synchronized planning/navigation state: OK")


def validate_absence_and_hygiene() -> None:
    require(
        not list(CONTROL.glob("*chapter-21-acceptance-review*.md")),
        "Chapter 21 acceptance review exists",
    )

    chapter22_artifacts = [
        path
        for path in BOOK.rglob("*")
        if path.is_file()
        and ("chapter-22" in path.name.lower() or "chapter_22" in path.name.lower())
    ]
    require(not chapter22_artifacts, f"Chapter 22 artifact exists: {chapter22_artifacts}")

    remainder_outlines = [
        path
        for path in BOOK.rglob("*")
        if path.is_file()
        and (
            "remainder-outline" in path.name.lower()
            or "remainder_outline" in path.name.lower()
            or "remainder-of-act-iii-outline" in path.name.lower()
            or "remainder_of_act_iii_outline" in path.name.lower()
        )
    ]
    require(
        not remainder_outlines,
        f"complete remainder outline artifact exists: {remainder_outlines}",
    )

    allowed_ch21 = {
        AUTHORIZED_DRAFT,
        CONTROL / "42-chapter-21-mission-lock.md",
    }
    suspicious = []
    bad_fragments = (
        "alternate",
        "backup",
        "latest",
        "final",
        "helper",
        "debug",
        "payload",
        "runner",
        "apply",
        "trigger",
        "copy",
    )
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        name = path.name.lower()
        if "chapter21" in name or "chapter-21" in name or "chapter_21" in name:
            if path not in allowed_ch21 and any(fragment in name for fragment in bad_fragments):
                suspicious.append(path)
    require(not suspicious, f"temporary/alternate Chapter 21 artifact exists: {suspicious}")

    forbidden_paths = [
        ROOT / ".github/workflows/chapter20-acceptance-apply.yml",
        ROOT / ".github/workflows/chapter20-acceptance-pr.yml",
        ROOT / "chapter20-validator-final.yml",
        ROOT / ".chapter20-acceptance-py",
        ROOT / ".chapter20-acceptance",
        ROOT / ".github/workflows/chapter21-mission-lock-apply.yml",
        ROOT / ".github/workflows/chapter21-mission-lock-pr.yml",
        ROOT / "chapter21-validator-final.yml",
        ROOT / ".chapter21-mission-lock-py",
        ROOT / ".chapter21-mission-lock",
        ROOT / ".github/workflows/chapter21-draft-apply.yml",
        ROOT / ".github/workflows/chapter21-draft-pr.yml",
        ROOT / ".chapter21-draft-py",
        ROOT / ".chapter21-draft",
    ]
    remaining = [path for path in forbidden_paths if path.exists()]
    require(not remaining, f"temporary helper artifact remains: {remaining}")
    print("absence and hygiene sentinels: OK")


def validate_diff_hygiene() -> None:
    base = os.environ.get("BOOK1_DIFF_BASE", "HEAD^")
    result = subprocess.run(
        ["git", "diff", "--check", base, "--"],
        text=True,
        capture_output=True,
    )
    require(
        result.returncode == 0,
        f"git diff --check failed against {base}:\n{result.stdout}{result.stderr}",
    )
    print(f"git diff --check against {base}: OK")


def main() -> None:
    validate_protected_prose()
    validate_review_and_inventory()
    validate_chapter20_content()
    validate_chapter21_mission_lock()
    validate_chapter21_draft()
    validate_synchronized_controls()
    validate_absence_and_hygiene()
    validate_diff_hygiene()
    print("Book 1 accepted Chapter 20 and Chapter 21 non-canon draft state: VALID")


if __name__ == "__main__":
    main()
