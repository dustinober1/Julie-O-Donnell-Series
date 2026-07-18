#!/usr/bin/env python3
"""Add the final thousand words of substantive technical and emotional consequence."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"


def patch(path: Path, anchor: str, replacement: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    if anchor not in text:
        raise RuntimeError(f"missing anchor for {marker}")
    path.write_text(text.replace(anchor, replacement, 1), encoding="utf-8")
    print(path.relative_to(ROOT))


def main() -> None:
    patch(
        CHAPTER_DIR / "chapter-02.md",
        """The sandbox restriction had been disabled, the synthetic-source label removed, and the export prohibition replaced by an executive waiver without a visible government approver. Each safeguard had failed differently: switched off, deleted, overruled. The pattern looked less like a broken deployment than one designed to survive three kinds of audit.

Payload 88 was no longer pretending to be intelligence inside a test environment.""",
        """The sandbox restriction had been disabled, the synthetic-source label removed, and the export prohibition replaced by an executive waiver without a visible government approver. Each safeguard had failed differently: switched off, deleted, overruled. The pattern looked less like a broken deployment than one designed to survive three kinds of audit.

A transformation manifest sat beneath the waiver. Elias opened it expecting a list of copied files. Instead it described how the post-archive object consumed Revision Eight.

REVISION 8 VARIATION MAP: INPUT
ENVIRONMENTAL IRREGULARITY CLASS: COLLECTION DAMAGE
TIMING VARIANCE: RECONSTRUCT TO REFERENCE
DEVICE-AGING DRIFT: RECONSTRUCT TO REFERENCE
CONFLICTING CARRIER EVENTS: CORRECTION-DEPENDENT
REFERENCE ENVELOPE: PACKET 0001

He read the fields twice. The mess he had added to make the test believable had not been deleted from the archived package. It had been reclassified. SIGMA would receive every deliberate irregularity as evidence that the collected signal needed repair. The first packet became the reference envelope. Later packets inherited its carrier structure while timing and equipment drift were pulled toward the same model state.

The process explained the live feed Julie was seeing without requiring Revision Eight itself to have been clean. Human reaction differences became correction targets. Independent radio aging became damage. Weather response became something to compensate away. Observations that contradicted the reconstructed formation but shared its carrier family moved into a dependent side table instead of reaching the threat model.

The object did not merely add synthetic artillery. It used the believable version as raw material and then removed the very disorder that had taught Argus to distrust it.

Elias copied the manifest path to the maintenance drive. The field that identified who approved the transformation was not visible at his level.

Payload 88 was no longer pretending to be intelligence inside a test environment.""",
        "A transformation manifest sat beneath the waiver",
    )

    patch(
        CHAPTER_DIR / "chapter-08.md",
        """Julie compared the source time with the enclave clock. “Almost four minutes. Forty-three seconds of that belongs to my first boundary.”

“And distance?” Marcus asked.""",
        """Julie compared the source time with the enclave clock. “Almost four minutes. Forty-three seconds of that belongs to my first boundary.”

Elias looked at her rather than the map. “The original recovery record already shows why you chose it.”

“It also shows what I deferred.”

“We can describe the delay as a consequence of the poisoned dependency structure.”

“It was. I still selected the structure.”

Julie opened the supplemental notice field and wrote the operational warning herself.

INITIAL RELEASE SUSPENSION ACHIEVED USING OVERBROAD DEPENDENCY BOUNDARY.
FOURTEEN CORRECTION-DEPENDENT OBSERVATION REFERENCES DEFERRED.
SUPPLEMENTAL REVIEW RESTORED LOW-LEVEL MOVEMENT TOWARD K-17.
ADDITIONAL DELAY ATTRIBUTABLE TO ANALYTIC SCOPE: 43 SECONDS.
FIELD PRESENCE, IDENTITY, AND OBJECTIVE: UNCONFIRMED.

She signed the scope statement. Elias authenticated only that the restored references came from his package's correction-dependent table and that the source blocks remained unchanged. Marcus attached no command conclusion.

The warning that left the enclave would not present Julie as the analyst who had found every distinction in time. It would present the sequence in which she had stopped the larger lie, missed a smaller truth inside its machinery, and corrected the miss before anyone could make her first result final.

“And distance?” Marcus asked.""",
        "INITIAL RELEASE SUSPENSION ACHIEVED USING OVERBROAD DEPENDENCY BOUNDARY",
    )

    patch(
        CHAPTER_DIR / "chapter-23.md",
        """The correction did not make the next officer trust Julie. It changed what the officer was officially permitted to assume before meeting her.

It could still accuse Julie of unlawful conduct.""",
        """The correction did not make the next officer trust Julie. It changed what the officer was officially permitted to assume before meeting her.

The original Apex bulletin remained preserved beside every amendment. The coordination center would not overwrite it with a cleaner final alert. Investigators could later see when the armed-architect language entered, which authority supplied it, when Elias changed from possible hostage to voluntary subject, and how long each unsupported premise remained active after the underlying evidence contradicted it.

Ortiz received the amended bulletin in the same intake room where the seven packages had arrived. He compared the new language with his scene report and added no personal conclusion. Brooks reviewed the force note and released the extra tactical team that had remained outside the hospital solely because the original alert treated evidence loss as an imminent deadly threat.

The officers did not become witnesses for Julie. They became people no longer ordered to meet her through Vance's description.

It could still accuse Julie of unlawful conduct.""",
        "The original Apex bulletin remained preserved beside every amendment",
    )

    patch(
        CHAPTER_DIR / "chapter-24.md",
        """The yellow legal pad rested inside a clear sleeve on the fence rail. It held no client, assignment, or promise that any institution would accept her terms. It held the conditions under which she would return and the conditions under which she would refuse.

The neighbor packed the ground again.""",
        """The yellow legal pad rested inside a clear sleeve on the fence rail. It held no client, assignment, or promise that any institution would accept her terms. It held the conditions under which she would return and the conditions under which she would refuse.

Webb had written one note beneath Julie's four rules before placing the page in the sleeve.

A TERM THAT CANNOT BE ENFORCED IS A PREFERENCE.

Julie had disliked the sentence because it turned principle into future work. Mandates would need withdrawal clauses. Custody agreements would need remedies when a source holder changed scope. Participants would need someone other than Julie to receive a stop decision when she was the person most convinced the work had to continue.

The practice did not exist yet. Its first unfinished task was building rules capable of restraining its founder.

The neighbor packed the ground again.""",
        "A TERM THAT CANNOT BE ENFORCED IS A PREFERENCE",
    )


if __name__ == "__main__":
    main()
