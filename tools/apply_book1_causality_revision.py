#!/usr/bin/env python3
"""Apply idempotent causality, authority, and analytic-agency revisions to Book 1."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"missing anchor for {label}")
    return text.replace(old, new, 1)


def revise_chapter_02(text: str) -> str:
    routing_old = """INDIAN NORTHERN COMMAND
SOURCE CERTIFICATION: 16:30 EDT
COUNTER-BATTERY SUPPORT COMMIT: 05:00 EDT

Elias pushed away hard enough for his chair to strike the workstation behind him."""
    routing_new = """INDIAN NORTHERN COMMAND
SOURCE CERTIFICATION: 16:30 EDT
COUNTER-BATTERY SUPPORT COMMIT: 05:00 EDT

The route belonged to a classified bilateral pilot established after three warning failures along the Line of Control. Argus did not command Indian artillery, and the United States did not hold the firing key. The pilot delivered a machine-readable American threat assessment, supporting coordinates, confidence state, and counter-battery product into Northern Command's planning network. Indian commanders retained weapons authority. In practice, a validated American packet could place ammunition at the guns and firing data one human decision from execution before contradictory collection crossed the same bureaucracy.

Elias pushed away hard enough for his chair to strike the workstation behind him."""
    text = replace_once(text, routing_old, routing_new, "bilateral pilot")

    authority_old = """The live warning belonged to the government. The test material that might explain it belonged to the contractor. Even Marcus’s program-oversight credential showed temporary authority only over government operational data. The boundary was legally clean and operationally absurd: the government could act on the warning, but the officer responsible for the warning could not inspect the contractor material most likely to explain why it was wrong. Apex did not need to falsify a denial. It needed only to enforce ownership until the certification clock expired.

He submitted an immediate request."""
    authority_new = """The live warning belonged to the government. The test material that might explain it belonged to the contractor. Even Marcus’s program-oversight credential showed temporary authority only over government operational data. The boundary was legally clean and operationally absurd: the government could act on the warning, but the officer responsible for the warning could not inspect the contractor material most likely to explain why it was wrong.

The contract divided sovereignty from control. The government owned the program requirement, classification authority, and operational decision. Apex operated Building Three, the ingestion architecture, validation archive, production release workflow, facility security, credential administration, and first-line incident response under delegated authorities distributed across several agreements. No single Apex role was sovereign. Together they let the company control the room, the data path, the access log, and the first account of a failure before a government officer could invoke a separate channel. The alternate government routes still entered through infrastructure Apex maintained.

Apex did not need to falsify a denial. It needed only to enforce the accepted boundaries until the certification clock expired.

He submitted an immediate request."""
    text = replace_once(text, authority_old, authority_new, "Apex delegated authority")

    sarah_old = """“Technical boundaries do not disappear because you dislike them.”

The intercom went silent."""
    sarah_new = """“Technical boundaries do not disappear because you dislike them.”

Marcus said, “Put this on the record: Director Vance changed the consultant scope after the vehicle entered the campus, and his office is the approval authority now withholding the comparison set.”

Sarah paused long enough for the compliance recorder to remain audible. “The access modification and approval chain are already in the session record. I will add your stated operational basis. I will not characterize the anomaly as sabotage, employee action, or source contamination until an authorized comparison supports one of those terms.”

The answer protected Apex’s scope and refused a conclusion Vance could later place in her mouth.

The intercom went silent."""
    text = replace_once(text, sarah_old, sarah_new, "Sarah early integrity")

    sigma_old = """One surviving report from the Anwar investigation had referenced SIGMA-NORMALIZE-2. Reconstruction was not malicious by itself. Every sensor system estimated missing or damaged information; without that work, weather and hardware failure could make real collection unusable. The danger came from sequence. Applied after authentic collection, normalization repaired damage. Applied to synthetic telemetry before provenance was settled, it could supply physical mess the source had never experienced or remove inconsistencies that might expose it. The same tool could preserve truth or make a lie look weathered, depending on what entered first.

Six years earlier, training-archive noise had been wrapped inside a live signal."""
    sigma_new = """One surviving report from the Anwar investigation had referenced SIGMA-NORMALIZE-2. Reconstruction was not malicious by itself. Every sensor system estimated missing or damaged information; without that work, weather and hardware failure could make real collection unusable. The danger came from sequence. Applied after authentic collection, normalization repaired damage. Applied to synthetic telemetry before provenance was settled, it could supply physical mess the source had never experienced or remove inconsistencies that might expose it. The same tool could preserve truth or make a lie look weathered, depending on what entered first.

Revision Eight complicated the hypothesis. Elias’s archived index described a package built to include weather response, equipment aging, terrain masking, and human timing error. The live feed displayed the opposite: exact intervals, repeated carrier structure, and a path through granite. If the deployed object was truly derived from Revision Eight, something after archival had reclassified the package’s deliberate irregularities as collection damage. A reconstruction routine could then smooth the human timing, flatten the equipment drift, and rebuild multiple packets from one reference envelope. That would make the deployed derivative cleaner than the test Elias authored and explain why the carrier scar repeated across changing weather. Julie did not yet have the ninth object or SIGMA change history to prove the transformation.

Six years earlier, training-archive noise had been wrapped inside a live signal."""
    text = replace_once(text, sigma_old, sigma_new, "SIGMA hypothesis")
    return text


def revise_chapter_08(text: str) -> str:
    lineage_old = """The first three objects contained thousands of packet blocks. The console highlighted several possible ranges and asked her to select the disputed source boundary.

Elias reached for the largest one.

Julie stopped his hand.

“That suspends the whole relay.”

“It’s the fastest defensible range.”

“It discards everything collected through it, including anything real.”

“We have forty seconds.”

“Then don’t waste one asking me to erase evidence.”

She expanded the raw layer.

The familiar emissions appeared as a repeating series of peaks spaced eleven-point-two seconds apart. Weather variation moved through the surrounding traffic in ragged bands. The target signal held its shape with the same impossible smoothness she had seen in Room 402B.

Julie isolated the carrier structure.

Seven small fluctuations repeated near the beginning of each synthetic packet. The same seven returned seventeen milliseconds later. Identical, every time.

She dragged the comparison against the sealed blocks in the case.

MATCHING STRUCTURE: VAL-088

The console drew a boundary around the first packet carrying the repeated structure. It extended through the source-correction object and into the model-derived track set.

Julie shortened the far edge.

Elias looked at her. “Why?”

“The correction object kept running after the synthetic bursts began. I want the observed packets beyond the last match preserved.”

“That leaves contaminated reconstruction in the workspace.”

“It leaves it available for comparison. We invalidate what cannot survive the comparison. We do not make the rest disappear because it is inconvenient.”

The clock reached 00:27.

Behind them, the gate bolts gave a deep answering knock.

Marcus said, “Stage two.”

The console accepted Julie’s narrowed boundary.

DISPUTED RANGE SELECTED
RAW OBSERVATIONS: PRESERVED
RECONSTRUCTED SIGNAL: CHALLENGED
VALIDATION-DERIVED ARTIFACTS: CHALLENGED
DOWNSTREAM CACHED CONCLUSIONS: INCLUDED"""
    lineage_new = """The first three objects contained thousands of packet blocks. Elias opened the Revision Eight irregularity map beside the deployed source-correction object.

His approved package carried different timing distributions for command roles, weather-dependent loss, unequal equipment drift, terrain-shadow failures, and maintenance histories that changed the radios independently. The post-archive derivative had passed those variations into SIGMA-NORMALIZE-4 as correctable collection damage. SIGMA rebuilt the target bursts against one reference envelope, tightened the acknowledgments toward eleven-point-two seconds, flattened the device drift, and propagated the same reconstructed carrier structure across packets captured under different physical conditions.

The clean feed was not Revision Eight. It was Revision Eight after the parts that made it believable had been processed as errors.

A second rule sat beneath the transformation.

CONFLICTING OBSERVATIONS SHARING RECONSTRUCTED CARRIER: ROUTE TO CORRECTION-DEPENDENT SIDE TABLE

“That is the mask,” Elias said. “Anything that disturbed the false formation but touched its carrier family was diverted before the model saw it.”

The console offered three disputed boundaries: the complete relay, the source-correction lineage and every dependent table, or only packet blocks directly matching VAL-088.

Elias reached for the complete relay.

Julie stopped his hand.

“That discards everything collected through it.”

“It is the fastest boundary the recovery rule already understands.”

“We are not erasing a mountain because someone poisoned one path.”

She expanded the raw layer. The familiar emissions appeared every eleven-point-two seconds while weather variation moved through surrounding traffic in ragged bands. The target remained impossibly smooth.

Julie isolated the carrier structure and compared it with the sealed VAL-088 blocks.

MATCHING STRUCTURE: VAL-088

A packet-only boundary was precise but left some cached products connected through the source-correction object's internal dependency tables. Walking every dependency by hand would take longer than the release clock allowed.

Julie selected the middle option: source-correction lineage and dependent tables. It would suspend every product built through the poisoned correction while leaving the relay’s primary raw stream intact.

Elias read the scope. “The dependent side table includes observations the correction process already classified as self-noise.”

“The primary raw source stays preserved.”

“The table may be the only index telling us which raw blocks were diverted.”

The clock reached 00:27. Behind them, the gate bolts gave a deep answering knock.

Marcus said, “Stage two.”

Julie looked at the release queue and confirmed the lineage boundary.

DISPUTED RANGE SELECTED
PRIMARY RAW OBSERVATIONS: PRESERVED
CORRECTION-DEPENDENT OBSERVATIONS: DEFERRED WITH CHALLENGED LINEAGE
RECONSTRUCTED SIGNAL: CHALLENGED
VALIDATION-DERIVED ARTIFACTS: CHALLENGED
DOWNSTREAM CACHED CONCLUSIONS: INCLUDED

She saw deferred and treated it as preserved for later review. Under the clock, the distinction looked smaller than allowing the firing product to leave."""
    text = replace_once(text, lineage_old, lineage_new, "Chapter 8 boundary selection")

    final_old = """The selected boundary began with the first physically impossible carrier structure. It preserved the raw packets before and after it. It restored the labels Elias’s team had placed on Payload 88. It included every model assumption and cached targeting conclusion derived from the poisoned layer.

It did not certify that no enemy movement existed.

That was the point."""
    final_new = """The selected boundary began with the source-correction object built from the physically impossible carrier structure. It preserved the primary relay stream, restored the labels Elias’s team had placed on Payload 88, and included every model assumption and cached targeting conclusion derived through the poisoned correction. It also deferred the correction-dependent observation table Julie had decided could wait.

The action did not certify that no enemy movement existed.

It suspended a weapon product built from a source whose provenance had already failed. That was enough for the immediate decision and less complete than Julie wanted to admit."""
    text = replace_once(text, final_old, final_new, "Chapter 8 final scope")

    review_old = """The system began the post-reconciliation review automatically. A new pane opened beneath the withdrawn assessment.

GENUINE SOURCE ACTIVITY WILL BE REEVALUATED
RETAINED RAW OBSERVATIONS: PRESENT

Julie moved back to the console.

Elias looked up. “The synthetic layer is gone.”

“The poisoned layer is excluded,” she said. “That is not the same as nothing being there.”

She opened the retained observations.

The primary artillery sector was almost empty. Weather noise returned in irregular bands. Civilian communications drifted with the storm. A few heavy-engine signatures appeared on known roads, none arranged into the offensive formation Argus had projected.

At the edge of the map, a group of low-confidence events blinked into view.

They were nowhere near Sector Zebra-Nine.

Julie expanded them.

Short thermal signatures appeared one at a time beneath a ridge line. They lasted between two and four seconds, then vanished behind terrain. A vibration sensor farther east recorded brief weight transfers too light for vehicles and too regular for loose rock. Three narrow communications bursts sat almost entirely beneath Payload 88’s carrier structure.

Before reconciliation, each had been marked as duplicate contamination and removed by the source-correction object.

Now they aligned.

Not artillery.

People.

Five, perhaps six, moving in intervals that kept them from occupying the same sensor field at once.

Elias leaned closer. “That should not have been filtered.”

“It destabilized the false movement model,” Julie said.

“The correction routine treated anything sharing its carrier structure as self-noise.” He touched the lineage map. “Payload Eighty-Eight did not only add the artillery pattern. The production object used the pattern as a mask.”

Julie brought up the timestamps."""
    review_new = """The system began the post-reconciliation review automatically. A new pane opened beneath the withdrawn assessment.

GENUINE SOURCE ACTIVITY WILL BE REEVALUATED
RETAINED PRIMARY RAW OBSERVATIONS: PRESENT
CORRECTION-DEPENDENT OBSERVATIONS: DEFERRED / 14 EVENT REFERENCES

Julie moved back to the console.

Elias looked up. “Why are fourteen references deferred?”

“The lineage boundary.”

“You said the raw source would remain.”

“It did.”

“The raw blocks did. The index telling us which blocks the correction object diverted is inside the challenged side table.” Elias pulled the boundary record onto the second screen. “The system is reevaluating only the primary stream. Your scope temporarily carried genuine observations out with the poisoned dependencies.”

Julie looked at the words she had accepted under the clock.

CORRECTION-DEPENDENT OBSERVATIONS: DEFERRED WITH CHALLENGED LINEAGE.

She had preserved the raw material and suppressed the map required to find part of it. The method had been defensible for stopping release. The first result was still incomplete because of her choice.

“I made the boundary too broad.”

Marcus looked at the sealed gate. “Can you fix it without restarting the release?”

Elias opened the sealed recovery record. “We cannot change the original action. We can append a supplemental raw-observation review against the preserved event references. It will carry the first limitation and whoever authorizes the correction.”

“Do it,” Julie said.

“Your name goes on the analytic scope.”

“It should.”

She selected:

SUPPLEMENTAL REVIEW — DEFERRED CORRECTION-DEPENDENT OBSERVATIONS
INITIAL RANGE LIMITATION: OVERBROAD LINEAGE BOUNDARY
ANALYTIC AUTHORITY: O'DONNELL, JULIE M.
AUTHOR VALIDATION: THORNE, ELIAS M.
EXTERNAL RELEASE STATE: REMAINS SUSPENDED

Elias authenticated the author side. The console walked the fourteen references back to the preserved primary blocks. Forty-three seconds passed while the gate override advanced and any movement on the mountain continued without them seeing it.

The primary artillery sector remained almost empty. Weather noise returned in irregular bands. Civilian communications drifted with the storm. A few heavy-engine signatures appeared on known roads, none arranged into the offensive formation Argus had projected.

Then the deferred references aligned at the edge of the map, nowhere near Sector Zebra-Nine.

Short thermal signatures appeared one at a time beneath a ridge line. They lasted between two and four seconds, then vanished behind terrain. A vibration sensor farther east recorded brief weight transfers too light for vehicles and too regular for loose rock. Three narrow communications bursts sat almost entirely beneath Payload 88’s carrier structure.

Before reconciliation, each had been marked as duplicate contamination and removed by the source-correction object. Julie’s first boundary had left them deferred for another forty-three seconds.

Now they aligned.

Not artillery.

People.

Five, perhaps six, moving in intervals that kept them from occupying the same sensor field at once.

Elias leaned closer. “That should never have been classified as self-noise.”

“It destabilized the false movement model,” Julie said.

“The correction routine treated anything sharing its carrier structure as contamination. Payload Eighty-Eight did not only add the artillery pattern. The production object used the pattern as a mask.”

The supplemental review sealed beside the original recovery record without changing it. Julie's overbroad boundary and Elias's correction would travel together.

Julie brought up the timestamps."""
    text = replace_once(text, review_old, review_new, "Chapter 8 K17 correction")

    age_old = """“How old is the last contact?” Marcus asked.

“Less than three minutes.”"""
    age_new = """“How old is the last contact?” Marcus asked.

Julie compared the source time with the enclave clock. “Almost four minutes. Forty-three seconds of that belongs to my first boundary.”"""
    text = replace_once(text, age_old, age_new, "K17 delay consequence")
    return text


def main() -> None:
    changes = {
        "chapter-02.md": revise_chapter_02,
        "chapter-08.md": revise_chapter_08,
    }
    for name, revise in changes.items():
        path = CHAPTER_DIR / name
        original = path.read_text(encoding="utf-8")
        updated = revise(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
