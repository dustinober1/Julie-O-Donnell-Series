#!/usr/bin/env python3
"""Complete the Book 1 target-length revision with substantive consequences and corroboration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"


def add_before(text: str, anchor: str, addition: str, marker: str) -> str:
    if marker in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing anchor: {marker}")
    return text.replace(anchor, addition + anchor, 1)


def add_after(text: str, anchor: str, addition: str, marker: str) -> str:
    if marker in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing anchor: {marker}")
    return text.replace(anchor, anchor + addition, 1)


def revise_02(text: str) -> str:
    anchor = """The route belonged to a classified bilateral pilot established after three warning failures along the Line of Control. Argus did not command Indian artillery, and the United States did not hold the firing key. The pilot delivered a machine-readable American threat assessment, supporting coordinates, confidence state, and counter-battery product into Northern Command's planning network. Indian commanders retained weapons authority. In practice, a validated American packet could place ammunition at the guns and firing data one human decision from execution before contradictory collection crossed the same bureaucracy.

Elias pushed away hard enough"""
    replacement = """The route belonged to a classified bilateral pilot established after three warning failures along the Line of Control. Argus did not command Indian artillery, and the United States did not hold the firing key. The pilot delivered a machine-readable American threat assessment, supporting coordinates, confidence state, and counter-battery product into Northern Command's planning network. Indian commanders retained weapons authority. In practice, a validated American packet could place ammunition at the guns and firing data one human decision from execution before contradictory collection crossed the same bureaucracy.

The policy behind the pilot was public even if its implementation was not. A Northbridge Strategic Initiatives paper had argued that automated warning was useless unless it entered allied planning systems before human uncertainty consumed the response window. Senator Sterling had championed similar authorization language in committee. Nothing about the paper or the provision established an operational role. It meant the political and professional network supporting Argus existed long before the present warning.

Elias pushed away hard enough"""
    return text.replace(anchor, replacement, 1) if "The policy behind the pilot was public" not in text else text


def revise_15(text: str) -> str:
    anchor = """Brooks had never seen the feed. She did not know whether Julie was right. She did not need to know before making the garage survivable.

Ortiz began with Marcus."""
    addition = """Brooks had never seen the feed. She did not know whether Julie was right. She did not need to know before making the garage survivable.

She approached Julie only after the force line and civilian lane were established.

“You are being detained in connection with unauthorized access, removal of classified material, assault allegations, and the current security alert. I am not asking you for a technical statement in this garage.”

Julie had spent the morning fighting to make someone listen. The offer not to listen yet felt almost hostile.

Brooks continued. “I need immediate safety facts. Are there weapons, explosive devices, hazardous materials, active transmitters, or commands still running in the van or on any object?”

“No weapons or explosives. The telematics module is disconnected. The evidence case and field module are offline. The local recovery action completed. I do not know whether Apex has another remote action pending.”

“Any person still in immediate danger because of something you started?”

“The fire and suppression systems at Building Three require independent inspection. Hartwell and Northbridge hold records that may be at risk of deletion or overwrite. K-seventeen is an unresolved foreign field issue. I cannot direct any of them from here.”

Brooks recorded the answer as a safety statement, not a confession or expert finding.

“Do you want to make a substantive statement before counsel?”

Julie looked at the seven objects still held by people who could barely stand. Six years earlier, she had believed accuracy required speaking before anyone framed the question. Today, the record already existed outside her mouth.

“No.”

Brooks nodded. “Good decision or bad, it is yours.”

Ortiz began with Marcus."""
    return text.replace(anchor, addition, 1) if "You are being detained in connection with unauthorized access" not in text else text


def revise_16(text: str) -> str:
    anchor = """The investigation had finally acquired something the crisis never had.

A night in which no one was allowed to turn urgency into permission."""
    addition = """The investigation had finally acquired something the crisis never had.

---

Guarded Hospital Room
Washington, D.C.
22:18 Eastern Daylight Time

Julie lay awake beneath a monitor that turned each heartbeat into a green point moving left to right.

Her left wrist was secured to a padded rail. The right forearm rested above her chest inside the temporary immobilizer. Outside the room, an MPD officer sat beneath a television cycling through the sabotage alert, the Building Three fire, and Sterling's statements.

Dana Webb arrived after ten with an appointment order, two legal pads, and no request for Julie to explain the case.

“I am your lawyer for detention, immediate charging, and access to counsel. I am not your investigator, publicist, or conduit to the evidence.”

Julie looked at the blank pads. “Then why bring paper?”

“So you can write questions you are not going to act on.”

Webb placed one within reach of Julie's left hand.

Julie wrote HARTWELL, PRICE, K17, SARAH, APX-DIR-0019, STERLING DEVICE. The letters leaned backward. Under them she began listing the calls she would make if the restraint opened.

Webb read none of it. “Every one of those sources has a preservation demand or a named custodian in progress. You are not permitted to contact them. You are not permitted to direct Grant or Alvarez. You are not permitted to use someone else to do either.”

“What if the first examination chooses the wrong question?”

“Then your lawyer objects after learning what the authority permits. You do not solve it from a hospital bed.”

Julie stared at the monitor. The four-second gateway wheel had taught her that delay killed. The last day had taught her that speed could also make the first incomplete account impossible to dislodge.

She crossed out the call list and left the questions.

Webb took the second pad for herself. “Now tell me only what I need for the detention review: injuries, medications, whether anyone questioned you after the physician stopped contact, and whether an officer threatened or promised anything.”

Julie answered the narrower questions.

When Webb left, the television outside showed her photograph again. Julie did not ask the guard to turn it off. She did not ask for a phone.

She listened to the hospital systems carry their own weight and waited for morning.

A night in which no one was allowed to turn urgency into permission."""
    return text.replace(anchor, addition, 1) if "Dana Webb arrived after ten" not in text else text


def revise_17(text: str) -> str:
    anchor = """The examination record sealed at 10:06.

BOARD EAT-0881147"""
    addition = """Before the record sealed, Alvarez required a blind replication.

A second DCIS examiner who had not watched Grant's queries received the written scope, the reader's verified starting state, and the board package under the same camera. Grant left the examination surface and could not direct the sequence. The second examiner selected the deployment range, emergency range, lifetime counter, and event-class query from the scope card.

The result matched Grant's: no physical board event at 02:14, distinct live-released events at the gate and recovery console, continuous lifetime counter, and zero source writes from either examination.

Apex counsel preserved the same mirror-service objection. The second examiner preserved the same limit without copying Grant's language: the board excluded its own physical participation and did not identify the system that presented its identity elsewhere.

Grant compared the two method logs. Different operators had reached the same direct observation from the same object without using Apex software or Julie's instructions.

Only then did she allow the finding to seal.

The examination record sealed at 10:06.

BOARD EAT-0881147"""
    return text.replace(anchor, addition, 1) if "Alvarez required a blind replication" not in text else text


def revise_18(text: str) -> str:
    anchor = """Sharma signed beneath Qureshi.

K-17 had not been taken."""
    addition = """Sharma signed beneath Qureshi.

She went to the aid room before returning to operations.

Pal lay propped beneath a thermal blanket with three staples closing the cut along his scalp. The medical officer allowed one question from him and none from Sharma.

“Did we fire?”

“No.”

His eyes closed for a moment. “Was the relay empty?”

“The outer compound was empty when you reached it. The record shows an accepted challenge and a failed commit. The inner boundary remains uncleared.”

He opened his eyes again. “So we don't know.”

“We know what the patrol observed. We know what the cartridge recorded. We know what neither can tell us.”

Pal nodded once. The answer was not reassuring. It was the one he could carry without later discovering his injury had been used to support a cleaner story.

The medical officer ended the visit.

K-17 had not been taken."""
    return text.replace(anchor, addition, 1) if "She went to the aid room before returning to operations" not in text else text


def revise_19(text: str) -> str:
    anchor = """The result did not identify Sterling.

It converted the signer from a certificate into a moving physical object that an institution now had to find.

---

Alvarez’s receiving instrument"""
    addition = """The result did not identify Sterling.

It converted the signer from a certificate into a moving physical object that an institution now had to find.

Hackett asked Grant to authorize an immediate public statement confirming that a Sterling-office device had participated in the operational chain.

“No,” Grant said from Hartwell's controlled phone. “We have a device serial, office authority class, challenge result, and institutional custody path. We do not have the current custodian, assignment exception, instruction source, or personal operator.”

“The office is already accusing O'Donnell in public.”

“That does not expand Hartwell's source.”

Alvarez backed Grant. The named federal receiver now owned not only the duty to act, but the duty to prevent a partial result from becoming the next official overclaim. She ordered the Hartwell derivative held inside incident 187463 until LSS answered the locator request or documented its refusal.

The delay gave Sterling's office more time to speak. It also kept a hardware-authenticated office link from being published as proof that Sterling personally held or commanded the device.

---

Alvarez’s receiving instrument"""
    return text.replace(anchor, addition, 1) if "Hackett asked Grant to authorize an immediate public statement" not in text else text


def revise_20(text: str) -> str:
    anchor = """Vann placed the pouch inside a rigid secondary container, closed it, and applied the LSS hold seal. Two-person custody followed it through the rear control door. Grant never saw the signer itself. She saw the institution that had accepted responsibility for not using it.

Vega authorized a certified derivative"""
    addition = """Vann placed the pouch inside a rigid secondary container, closed it, and applied the LSS hold seal. Two-person custody followed it through the rear control door. Grant never saw the signer itself. She saw the institution that had accepted responsibility for not using it.

Drennan remained at the transfer table after the device left.

“Am I in custody?” he asked.

“No,” Vega said. “You are directed to remain available under the office and LSS preservation notices. You may leave with counsel after your credential and route records are preserved.”

Drennan looked at Grant. “My name will be the one on every camera carrying the case.”

“Yes.”

“I did not choose the route.”

“The assignment record says Kessler authorized your custody. It does not yet identify the instruction source or your knowledge.”

“My job was to keep the case closed and get it through the security paths.”

“Then preserve that statement with your lawyer and the records that can test it.”

He glanced toward the door through which the signer had disappeared. “If I had refused, someone else would have carried it.”

Grant did not tell him whether refusal would have changed anything. “That is not a physical observation. Decide with counsel whether it belongs in your statement.”

Drennan nodded. The carrier would not be protected by turning him into a hero. He would be protected, if the records allowed it, by keeping movement, authorization, knowledge, and command separate.

Vega authorized a certified derivative"""
    return text.replace(anchor, addition, 1) if "Drennan remained at the transfer table after the device left" not in text else text


def revise_21(text: str) -> str:
    anchor = """Grant sealed the finding.

PRICE AUTHENTICATED DIA-SAR-PRICE-01."""
    addition = """Before Grant sealed the finding, Price asked what the result changed for him.

Alvarez answered from the incident channel. “It changes the federal incident's attribution of the later continuity request. It does not decide your DIA employment review, the propriety of the expedited flag, the rejected access attempt, or whether another authority brings charges.”

“So the record can say my name was borrowed and DIA can still fire me for the thing I actually did.”

“Yes.”

Price let out a short breath that almost became a laugh. “That may be the first answer today I believe completely.”

Shah asked whether the federal finding would be sent to DIA's deciding official.

“It will be available through the authenticated incident route with your client's statement and the source limits,” Alvarez said. “DCIS will not recommend an employment outcome.”

Price looked at the original request still open on the standalone terminal. “Then leave the expedited flag where it is.”

“It is already there,” Grant said.

“I know. I am telling myself.”

Grant sealed the finding.

PRICE AUTHENTICATED DIA-SAR-PRICE-01."""
    return text.replace(anchor, addition, 1) if "Price asked what the result changed for him" not in text else text


def revise_22(text: str) -> str:
    anchor = """The two tracks met on Grant’s display.

The construction sources showed"""
    addition = """The two tracks met on Grant’s display.

Before comparing them, Grant requested the government Argus registry receipt for the later reconstruction. The registry remained outside Apex and recorded what product arrived, when it arrived, which certificate chain accompanied it, and what prior product it superseded.

The government source matched the Apex release event without relying on Apex's description.

PRODUCT RECEIVED: ARGUS-K17-RC-0751
RECEIPT: 07:52:12.117 EDT / OCTOBER 13
AUTHORITY CHAIN: APX-DIR-0019
SUPERSEDES: K17 CHALLENGED STATE
LOCAL COMMIT SUCCESS FIELD: NO

The registry did not identify Vance's palm or show what his console displayed. The Apex source did. The government registry independently established that the product his source recorded leaving Building Three was the product that entered the official chain one fraction of a second later.

Grant attached the sources without merging them. If Apex later challenged the camera, the government still held the received product and certificate. If the government registry were challenged, Apex still held the local release event. Neither institution could erase the other by revising its own record.

The construction sources showed"""
    return text.replace(anchor, addition, 1) if "Grant requested the government Argus registry receipt" not in text else text


def revise_23(text: str) -> str:
    anchor = """The office had surrendered the causal claim without surrendering the political fight.

It could still accuse Julie of unlawful conduct."""
    addition = """The office had surrendered the causal claim without surrendering the political fight.

The law-enforcement systems changed more slowly than the news banners. Alvarez sent the DCIS correction to MPD, the Army lookout desk, District police, and the federal coordination center that had inherited Apex's armed-insider alert. Each authority had to amend its own record.

The new bulletin did not cancel custody or declare the subjects harmless. It removed the unsupported claim that Julie had created the Argus corruption, removed Elias's hostage classification, and replaced the armed-architect language with the actual unresolved allegations: unauthorized access, removal of classified material, interference with security operations, and evidence preservation under incident 187463.

Mercer read the amended alert from an Apex administrative room after surrendering team command. The document no longer instructed officers to recover telemetry at the expense of subject preservation. Sarah's force standard had become the controlling regional note.

The correction did not make the next officer trust Julie. It changed what the officer was officially permitted to assume before meeting her.

It could still accuse Julie of unlawful conduct."""
    return text.replace(anchor, addition, 1) if "The law-enforcement systems changed more slowly than the news banners" not in text else text


def revise_24(text: str) -> str:
    anchor = """The common chest did not accompany her. Neither did a public statement masquerading as a release credential.

A hospital transport chair entered the alcove."""
    addition = """The common chest did not accompany her. Neither did a public statement masquerading as a release credential.

Webb placed a sealed copy of the release conditions in Julie's property envelope and kept another.

“If a reporter, agency, contractor, congressional office, or former colleague contacts you about the facts, you refer them to me. If someone offers access, a clearance workaround, or a private copy of evidence, you refuse and tell me. If you discover something from public reporting, you do not test it against anyone connected to the case.”

“You included former colleague for Marcus.”

“I included it because you know people who will call an instruction a conversation.”

Julie looked through the glass at the chest. The temptation did not require a credential. It required only a question someone else was willing to answer off the record.

“I understand.”

Webb waited.

Julie corrected herself. “I agree.”

A hospital transport chair entered the alcove."""
    return text.replace(anchor, addition, 1) if "Webb placed a sealed copy of the release conditions" not in text else text


def main() -> None:
    revisions = {
        "chapter-02.md": revise_02,
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
