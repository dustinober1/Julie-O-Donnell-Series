#!/usr/bin/env python3
"""Add substantive scene depth to the compressed final act without restoring repetition."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"


def insert_before(text: str, anchor: str, addition: str, marker: str) -> str:
    if marker in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing insertion anchor for {marker}")
    return text.replace(anchor, addition + anchor, 1)


def insert_after(text: str, anchor: str, addition: str, marker: str) -> str:
    if marker in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing insertion anchor for {marker}")
    return text.replace(anchor, anchor + addition, 1)


def revise_15(text: str) -> str:
    anchor = """That was not allegiance to Julie. It was a professional refusing to create an unreceipted disappearance in front of public cameras.

Ortiz began with Marcus."""
    addition = """That was not allegiance to Julie. It was a professional refusing to create an unreceipted disappearance in front of public cameras.

MPD Watch Commander Helena Brooks arrived before the first package moved. She wore no tactical armor, only a uniform shirt beneath a rain shell and the expression of a person who had been briefed by four agencies that each believed it owned the scene.

Brooks ordered the garage ramps held for emergency vehicles and ordinary civilian exit rather than sealed as a tactical box. Office workers trapped on the upper level were allowed to leave through a screened lane after officers photographed the route and warned them not to approach the van. Several carried phones already showing Julie’s Apex photograph. One man stopped long enough to stare at her before Park moved him on.

“Public safety first,” Brooks told Mercer. “No private team establishes a crossfire in a commercial garage. Your people remain behind my line unless Officer Ortiz asks for technical assistance.”

Mercer looked toward the east ramp, where an Apex vehicle waited beyond the police barrier. “If they move the media, I am responsible for failing to recover it.”

“You are responsible for the orders you follow here,” Brooks said. “MPD is responsible for movement.”

She reviewed the two force directives Sarah had preserved. Vance’s executive addendum treated imminent loss of material as a national-security emergency. Sarah’s instruction restricted firearms to an identified deadly threat with a clear background. Brooks signed the scene log accepting Sarah’s narrower standard for every person inside the police perimeter.

Julie watched Mercer read the signature. His face did not show gratitude. It showed the release of one impossible choice: he no longer had to decide whether a man in Reston could turn evidence loss into permission to shoot across civilians in Washington.

Brooks had never seen the feed. She did not know whether Julie was right. She did not need to know before making the garage survivable.

Ortiz began with Marcus."""
    return text.replace(anchor, addition, 1) if "MPD Watch Commander Helena Brooks arrived" not in text else text


def revise_16(text: str) -> str:
    anchor = """Julie had assumed Sarah’s compliance vocabulary existed only to protect Apex. Some of it did. The same habit had preserved the moment Vance changed an evidence-recovery problem into a force problem and then an occupied-room suppression act.

“I misread her,” Julie said."""
    addition = """Julie had assumed Sarah’s compliance vocabulary existed only to protect Apex. Some of it did. The same habit had preserved the moment Vance changed an evidence-recovery problem into a force problem and then an occupied-room suppression act.

---

Apex Building Three
Reston, Virginia
09:03 Eastern Daylight Time

Sarah stood at the incident desk while the building generated the first consolidated account.

The draft described Julie as the architect of a deliberate source corruption, Marcus as an armed accomplice, and Elias as a coerced employee whose administrator credential had been exploited during the attack. It listed the fire alarm, production-gate entry, suppression discharge, and stolen telemetry case. Every event had happened. The document placed them in the order most useful to Apex.

The source-contamination discovery appeared after the unauthorized export. Vance’s material-loss force addendum appeared under continuing containment. The occupied-room suppression override appeared as an automated equipment-protection response. Sarah’s refusal to authorize lethal force did not appear at all.

Vance entered the incident room with counsel and told her to certify the summary for government coordination.

“It is a narrative,” Sarah said. “The source index is not complete.”

“The source index contains privileged command traffic and technical details irrelevant to apprehension.”

“It contains the order of the force directives and the suppression override.”

“The executive addendum restated the capture priority.”

“It changed the force condition from threat to life to loss of material.”

Counsel said, “That is your interpretation.”

Sarah turned the two directives on the display. “Then preserve both and let someone else interpret them.”

Vance looked at the draft. “The occupied-room interlock had been defeated by the intruders’ fire action.”

“The room still reported three occupants when APX-DIR-0019 armed suppression.”

“They had compromised the life-safety controller.”

“The hardened status channel is the source saying otherwise.”

Vance’s voice lowered. “You are permitting procedural ambiguity to become their defense.”

“No. I am refusing to make our first report cleaner than the system record.”

Mercer joined from a second station. Sarah asked him to state only what he had directly observed: Julie and Marcus inside the review room, the case in Marcus’s custody, the evacuation, the attempted administrative hold, the lower-tier pursuit, the gate standoff, Vance’s force addendum, and the later order to recover media after the occupied-room override.

Mercer refused one sentence counsel had drafted for him: that Julie had intentionally used fire to damage a strategic system. He had seen her use the life-safety network. He had not seen her intent.

Sarah sealed the source-category index before Vance could replace it with the narrative. She preserved the company’s objections beside it and accepted the internal review notice that followed under her name.

She did not warn Julie. She did not withdraw the alert. She preserved the record in which those acts would later be judged.

---

Secure MPD Evidence Intake
Washington, D.C.

“I misread her,” Julie said."""
    return text.replace(anchor, addition, 1) if "Sarah stood at the incident desk" not in text else text


def revise_17(text: str) -> str:
    anchor = """No event appeared.

She widened the range by twelve hours in each direction.

Still none.

Apex counsel said, “That does not exclude a mirrored-signature service presenting the board certificate without advancing the local counter.”"""
    addition = """No event appeared.

She widened the range by twelve hours in each direction.

Still none.

Grant asked the reader for the board’s lifetime counter, manufacturing initialization, last verified maintenance event, and every increment between them. The total was continuous. No rollover, reset, skipped number, or counter-repair event appeared. The deployment interval sat between two ordinary development signatures without room for the missing act.

Apex counsel argued that the secure element could have entered an emergency shadow mode not exposed to an untrusted reader. Grant requested the public certificate policy stored on the board. The policy listed every event class capable of using the private key. Emergency administrator access remained counter-bound. Backup signing remained counter-bound. Recovery signing remained counter-bound. No uncounted shadow mode appeared.

“That policy could be incomplete,” counsel said.

“It could,” Grant replied. “Produce the signed manufacturer extension or Apex modification that adds the claimed mode. Until then, the physical object exposes one continuous counter.”

Julie watched Grant refuse the temptation to call the missing event impossible. She made Apex carry the mechanism it proposed instead of using confidence in the board as a substitute.

Apex counsel said, “That does not exclude a mirrored-signature service presenting the board certificate without advancing the local counter.”"""
    return text.replace(anchor, addition, 1) if "Grant asked the reader for the board’s lifetime counter" not in text else text


def revise_18(text: str) -> str:
    anchor = """From Kestrel, they observed K-17 through thermal optics and glass for nine minutes. The mast stood. External power appeared normal. The weather cover over the service enclosure remained closed. No person occupied the visible outer compound.

At the outer security wicket, frozen mud held six partial approach marks"""
    addition = """From Kestrel, they observed K-17 through thermal optics and glass for nine minutes. The mast stood. External power appeared normal. The weather cover over the service enclosure remained closed. No person occupied the visible outer compound.

The final approach had cost Pal his footing. A sheet of ice had broken beneath the third man while the patrol crossed a narrow shelf below the relay. Pal caught the man’s harness, struck his own head against the anchor rock, and remained on the line until Rao transferred the weight. The patrol could have turned back under its casualty rule. Pal had passed the field orientation check and insisted that the relay remained visible from the next protected fold.

Rao accepted one more bound, then stopped the patrol at Kestrel long enough to observe before allowing any approach. The delay gave the unseen occupants time to withdraw if they were still outside. It also prevented five exhausted soldiers from walking directly into a compound because a machine in another country had declared what should be there.

When they moved, they did so in pairs with the relay mast between them and the ridgeline. One soldier covered the western escape terrain. One watched the closed inner boundary. Sethi approached only after Rao photographed the wicket from outside its sensor line. The patrol never formed the single cluster the earlier American model had projected onto enemy units. Mountain procedure already knew that real people moved around exposure, injury, weather, and fear.

At the outer security wicket, frozen mud held six partial approach marks"""
    return text.replace(anchor, addition, 1) if "The final approach had cost Pal his footing" not in text else text


def revise_19(text: str) -> str:
    anchor = """Grant left for Hartwell.

Alvarez’s receiving instrument remained on the wall beside Sarah’s source index and Arjun’s bounded acknowledgment."""
    addition = """Grant left for Hartwell.

---

Hartwell Executive Briefing Annex
Washington, D.C.
11:07 Eastern Daylight Time

Hartwell’s production room had no place for the MPD chest and no authority to ask for it.

Grant entered with the DCIS receiving instrument, a clean encrypted receiver, and a paper scope card. Hartwell duty security officer Renee Collins read the card beneath the local camera and compared every requested field with the administrative hold created the previous morning.

The held record covered the local challenge window, controlled doors, device serial, access classes, challenge result, and institutional custody path immediately before and after. It excluded briefing content, attendees not physically connected to the device, and every camera outside the challenge corridor.

Collins identified the Hartwell clock source and its offset from the government product registry. Grant kept both. A perfect common time would have been easier to read and harder to defend.

The local challenge began at 07:46:58 on October 13.

DEVICE SERIAL: SSO-NS-004
OFFICE AUTHORITY: STERLING OFFICE NATIONAL SECURITY
LOCAL PERIMETER CHALLENGE: ACCEPTED
CHALLENGE RESPONSE: VALID

A compact signer case entered the challenge corridor through a credentialed legislative-support path. The camera showed a closed case, a gloved Hartwell security officer, and an office support courier whose identity remained masked in the first production because LSS controlled the personnel link. The courier never opened the case. The device answered while the case remained inside the marked challenge cradle.

The challenge event did not show Sterling, his hand, or any command from him. It showed an office-registered device arriving under an authorized support path and satisfying the perimeter condition required by the WSS routing message.

At 07:48:21, Hartwell security removed the closed case from the cradle and returned it to the same credentialed office custody class. The event log identified the receiving role, not the person. Less than a minute later, the next authentication window opened elsewhere in the operational chain.

Grant asked Collins whether Hartwell could identify the individual courier.

“LSS owns the identity binding,” Collins said. “Hartwell can certify the credential class, challenge corridor, case serial, and handoff. We cannot unmask the office assignment through this record.”

“Current location?”

“Not Hartwell. The case left through the authorized legislative-support path before the preservation demand reached us.”

That absence became the most urgent fact in the room.

Grant generated a source-limited derivative and verified its first event, last event, count, clock basis, device serial, challenge state, and withheld categories. Collins retained the original. Grant carried only the derivative and an authenticated Hartwell request that Legislative Secure Services locate SSO-NS-004 and place it under no-use control without powering or challenging it.

The signer had entered Hartwell lawfully enough to satisfy the local system and left before anyone asked who held it.

Grant returned to the DCIS channel from Hartwell’s controlled phone.

“The device is confirmed. The physical courier remains an LSS identity. SSO-NS-zero-zero-four is no longer at Hartwell. Locator and no-use request transmitted.”

The result did not identify Sterling.

It converted the signer from a certificate into a moving physical object that an institution now had to find.

---

Alvarez’s receiving instrument remained on the wall beside Sarah’s source index and Arjun’s bounded acknowledgment."""
    return text.replace(anchor, addition, 1) if "Hartwell’s production room had no place for the MPD chest" not in text else text


def revise_20(text: str) -> str:
    anchor = """The certificate withheld route details, internal requestor, substantive purpose, and office deliberations pending privilege and classification review.

“Who initiated the exception?” Grant asked."""
    addition = """The certificate withheld route details, internal requestor, substantive purpose, and office deliberations pending privilege and classification review.

Diane Kessler appeared through a separate office records channel. She was not in the compromise-control room and had no access to the signer. Office counsel limited her participation to the continuity authorization she had signed.

Grant asked whether Kessler recognized the derivative.

“Yes. I authorized the custody exception at 06:54 on October thirteenth.”

“Why?”

“The office continuity system presented an accepted NSB-emergency request requiring a registered portable signer to support two secure facilities during an active regional warning.”

“Did you speak with Leland Price?”

“No.”

“Receive a direct credential challenge from him?”

“No. The request entered as an inherited, accepted source-audit action.”

“Did you create the operational fields naming WSS-four, Hartwell, K-seventeen, or source reconstruction?”

“Not manually.”

“Did you know those fields were present when you authorized custody?”

Kessler looked toward counsel.

“I knew the request required WSS-four and Hartwell continuity. I am not answering substantive task content beyond the produced authorization.”

Grant left the refusal intact.

“Why Drennan?”

“He was the on-duty courier enrolled for both facilities and had no technical role in the message process. The carrier was selected to move a closed device, not to interpret or operate it.”

Drennan's visible position became narrower. Kessler had chosen him because he was ordinary within the custody system, not because the record showed he belonged to the operation behind it.

“Did Senator Sterling direct you to authorize the exception?”

Office counsel objected before Kessler answered. “Deliberative and outside the agreed production.”

Grant recorded the unanswered question rather than turning the objection into an answer.

“Who initiated the exception?” Grant asked."""
    return text.replace(anchor, addition, 1) if "Diane Kessler appeared through a separate office records channel" not in text else text


def revise_21(text: str) -> str:
    anchor = """Price stared at his name attached to a record class he had never used. Shah touched the edge of his sleeve, not to stop him, but to keep the silence from answering for him.

“Did you create that record?” Grant asked."""
    addition = """Price stared at his name attached to a record class he had never used. Shah touched the edge of his sleeve, not to stop him, but to keep the silence from answering for him.

The later request preserved phrases from his original: transient source state, integrity review, time-sensitive preservation. Around them sat fields he had never written. The continuity object used the caution in his request as the reason to bypass ordinary delay. It had taken the part of him that distrusted a disappearing display and converted it into an apparent demand for operational action.

Price asked to see the inherited-reference field beside his original receipt. Grant allowed the comparison without exposing the route beyond the categories already produced.

The request number matched exactly. The requestor name matched. The source subject line matched. His original signature did not appear. Instead, the office object identified the inherited reference as sufficient authentication for continuity processing.

“They used the receipt as authority,” Price said.

Grant corrected the scope. “The office workflow treated it as inherited authority. We have not yet shown who caused that workflow to run.”

Price looked at the administrative attorney across from him. “Your report says I tried to persist unauthorized data. This system turned the persistence request into permission to act.”

The attorney did not argue. “The administrative review concerns what you did. The later construction is under separate inquiry.”

For the first time, Price understood why keeping both records separate protected him better than a statement calling him vindicated. His real act would remain visible. The borrowed act would no longer be able to hide inside it.

“Did you create that record?” Grant asked."""
    return text.replace(anchor, addition, 1) if "The later request preserved phrases from his original" not in text else text


def revise_22(text: str) -> str:
    anchor = """Sarah transferred source control and lost access.

---

The two tracks met on Grant’s display."""
    addition = """Sarah transferred source control and lost access.

The preserved-room door unlocked behind her. Two internal-security officers waited with an Apex attorney. Neither touched her or asked for the derivative. The source had already crossed into the federal hold.

“You are placed on paid administrative leave pending review of unauthorized disclosure and failure to follow executive incident direction,” the attorney said.

Sarah removed her badge without being asked and placed it in the envelope he held open.

“Preserve the access-suspension event with the release source,” she said.

“That is an employment record.”

“It is also the event that ended my ability to certify the source after production.”

The attorney did not promise. Sarah looked through the fixed camera instead.

“For the incident record: my source access ended after the complete release range sealed. I did not open, alter, or remove the original. Mercer’s declaration remains separate from mine.”

She left Building Three under escort through the same controlled corridor where she had once told Julie certification was an answer to people who knew what they were looking at.

Mercer stayed behind long enough to surrender command of the Apex recovery team. His officers returned weapons and body-camera media under the joint incident hold. He did not claim that his later restraint erased the pursuit or the force orders he had followed.

Vance issued no confession. Through counsel, he stated that the later reconstruction was an authorized continuity product released during an active foreign threat, that the local K-17 failure did not establish the absence of enemy activity, and that his live authentication showed responsible executive action rather than concealment.

The statement fit the source well enough to require a real answer. It did not dispute that he saw the failed local state before release.

The government Argus Configuration Control Office suspended APX-DIR-0019 from new operational release while preserving the certificate for examination. Vance retained legal and corporate rights. He lost the ability to make another product controlling before the argument began.

---

The two tracks met on Grant’s display."""
    return text.replace(anchor, addition, 1) if "Two internal-security officers waited with an Apex attorney" not in text else text


def revise_23(text: str) -> str:
    anchor = """The three receipts resolved through separate systems. None required the MPD chest to open. None required the signer to answer another challenge.

News alerts simplified the result within minutes."""
    addition = """The three receipts resolved through separate systems. None required the MPD chest to open. None required the signer to answer another challenge.

At Forward Post Arjun, Qureshi printed the public Argus notice beside India’s still-classified local acknowledgment. The American document did not claim that Washington had saved the mountain. It stated that the poisoned support product had been withdrawn and that the later reconstruction omitted a failed local event. The decision not to fire remained Sharma’s and Northern Command’s matter.

Northern Command authorized a separate operational statement: no rounds had been fired in Mission Zebra-Nine, the local commander had held execution after the source state failed, and K-17 remained under technical review. It named no American subject, no field authority, and no location beyond the already public sector.

Sharma read the last line twice.

NO ROUNDS FIRED.

The sentence was smaller than everything the night had contained. It was also the result the soldiers at the guns could verify without trusting Argus, Apex, Julie, or the politics in Washington.

News alerts simplified the result within minutes."""
    return text.replace(anchor, addition, 1) if "At Forward Post Arjun, Qureshi printed the public Argus notice" not in text else text


def revise_24(text: str) -> str:
    anchor = """The farm appeared beyond the trees in late light.

The sight produced relief first and suspicion behind it."""
    addition = """The farm appeared beyond the trees in late light.

Webb's driver stopped at the top of the gravel lane. Julie sat for a moment with her left hand on the door handle and listened to the engine idle. No radio reported her location. No secure line waited for acknowledgment. The ordinary absence of a system felt less like peace than a sense she had forgotten to check one.

Webb had arranged for the neighbor to hold Julie's personal phone until counsel reviewed the messages and for someone else to drive the Ford home from the police lot. Julie had protested both arrangements and lost to the physician's order before the argument became serious.

The Ford stood beside the barn with the mechanical key on the kitchen table. Her phone remained powered down inside a paper evidence-style bag that was not evidence at all, only a boundary Webb knew Julie would understand.

Inside the farmhouse, the refrigerator had begun its uneven hum. A stack of unopened mail waited beneath a feed-store calendar. On the counter sat a note from her neighbor listing the horses' meals, the mare's minor scrape, and the mornings the well pump had complained. Nothing on the page required classification, authority, or a proof ceiling. It required Julie to decide when she could safely climb the barn steps again.

She left the mail unopened and walked toward the pasture.

The sight produced relief first and suspicion behind it."""
    return text.replace(anchor, addition, 1) if "Webb's driver stopped at the top of the gravel lane" not in text else text


def main() -> None:
    revisions = {
        "chapter-15.md": revise_15,
        "chapter-16.md": revise_16,
        "chapter-17.md": revise_17,
        "chapter-18.md": revise_18,
        "chapter-19.md": revise_19,
        "chapter-20.md": revise_20,
        "chapter-21.md": revise_21,
        "chapter-22.md": revise_22,
        "chapter-23.md": revise_23,
        "chapter-24.md": revise_24,
    }
    for name, revise in revisions.items():
        path = CHAPTER_DIR / name
        original = path.read_text(encoding="utf-8")
        updated = revise(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
