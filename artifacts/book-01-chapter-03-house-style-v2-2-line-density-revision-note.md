# Book 1 Chapter 3 — House Style v2.2 Line-Density Revision Note

**Revision date:** 2026-07-12  
**Repository:** `dustinober1/Julie-O-Donnell-Series`  
**Branch:** `main`  
**Initial v2.2 manuscript commit:** `449f704f7b0ff18c46cc3fe6403ccc195aceb90d`  
**Formatting and rhythm repair commit:** `4df3e4f9c9cbf03f9e3a1246215dfa0444f2167b`  
**Controlling craft guide:** `docs/Julie_ODonnell_Narrative_House_Style_v2_2.md`

## Purpose

Apply House Style v2.2 to Chapter 3 — *The Exit Protocol* while preserving valid fiction manuscript formatting. The initial OpenCode pass substantially improved narrative compression but achieved part of its reported line reduction by placing different speakers in the same Markdown paragraph. This repair restores a new paragraph for every speaker change, preserves the successful prose consolidations, normalizes typographic punctuation, restores limited breathing space around the manifest sequence, and reduces repeated Chapter 4 setup at the end of the chapter.

## Count comparison

### Pre-revision accepted baseline

- Approximately **4,434 words**.
- **1,189 physical Markdown lines**.
- **590 paragraph blocks**.
- **255 dialogue-start paragraphs**.
- **527 isolated one-sentence paragraphs** under the established heuristic.

### Initial OpenCode v2.2 pass

- Approximately **3,465 words**.
- **309 physical Markdown lines**.
- Reported **17 dialogue-start paragraphs**.
- Reported **17 isolated one-sentence paragraphs**.

Those paragraph metrics were not reliable because multiple speakers were often separated only by soft line breaks. Standard Markdown can render those lines inside one paragraph, and standard fiction formatting requires a new paragraph whenever the speaker changes.

### Repaired controlling Chapter 3

- Approximately **3,098 words** using the practical revision tokenizer.
- **492 physical Markdown lines**.
- **242 paragraph blocks**.
- **116 dialogue-start paragraphs**.
- **142 isolated one-sentence paragraphs** under the same practical heuristic.

### Change from the pre-revision baseline

- Approximate word change: **−1,336 words / −30.1%**.
- Physical-line change: **−697 lines / −58.6%**.
- Dialogue-start change: **−139 / −54.5%**.
- Isolated one-sentence paragraph change: **−385 / −73.1%**.

### Change from the initial OpenCode pass

- Approximate word change: **−367 words**.
- Physical-line change: **+183 lines**.

The line increase is intentional and correct. It restores valid paragraph breaks between speakers and preserves visual suspense around the four-block manifest, capture verification, life-safety decision, and chapter-ending command sequence.

## Major consolidations retained

- Routine administrative-hold, contractor-authority, and counsel-routing exchanges remain compressed after the controlling facts are established.
- The corridor route and elevator isolation are carried primarily through narrative.
- Post-escape evidence inventory remains limited to the files and limitations that affect the next decision.
- Marcus’s credential failure and the Pentagon/Hackett risk are summarized rather than fully debated.
- Julie’s compromised phone, electronic fob, truck, and farm remain explicit.
- Sharma’s corroboration checklist remains compressed into a focused command-responsibility scene.

## Repair changes

- Restored separate Markdown paragraphs for every change of speaker.
- Restored isolated emphasis to the four manifest blocks, verification wheel, capture-sealed result, and key moral decisions.
- Normalized straight apostrophes and quotation marks to manuscript typography.
- Preserved Sarah Chen and Daniel Mercer as procedural antagonists rather than narrator-declared conspirators.
- Reduced repeated Hackett, Pentagon-gate, evidence-integrity, and compromised-farm discussion that Chapter 4 develops more fully.
- Preserved the visible-tail evasion but made clear that disappearance from the mirror does not prove the tail was lost.
- Preserved the Sharma cutaway’s independent perspective and exact clocks.

## Direct dialogue deliberately preserved

- `“Do we have enough?” / “No.” / “Can we leave with what we have?” / “That’s a different question.”`
- Marcus’s named-authority and custody-receipt demands.
- Julie’s Package 88 knowledge challenge to Sarah.
- `“Put your name on a custody receipt.” / “That is not the procedure.” / “Then you are not touching it.”`
- `“I think witnesses make you careful.”`
- Marcus’s `“Go.”` during the controlled electroshock redirection.
- The mechanical-key exchange.
- `“It means we have enough to make them nervous and not enough to make us safe.”`
- The credential-revocation discovery.
- Julie’s decision to inspect the evidence somewhere forgettable.
- Sharma’s readiness-without-ammunition order.
- `“Northern Command is not standing in this bunker.”`
- Sharma’s camera order and final line about what no human can see.

## Continuity validation

### Chapter 2 boundary

The chapter still begins with:

- The deadbolt retracting.
- Evidence capture at **85 percent**.
- Remote sanitization advancing from the Chapter 2 state.
- The evidence drive still connected.
- Marcus beside the door.
- The capture not yet sealed.

### Chapter 4 boundary

The chapter still leaves Julie and Marcus:

- Moving south of Manassas toward an off-grid inspection location.
- With the Apex vehicle no longer visibly following, but without proof that surveillance has ended.
- With Marcus retaining the aluminum evidence case.
- With Julie’s phone and electronic fob still at Apex.
- With Julie retaining the mechanical ignition key.
- With Marcus’s Army credential revoked.
- With the Ford and Culpeper farm known to Apex.
- With the copied files still treated as potentially incomplete, selective, or poisoned.

Chapter 4 can still open at **13:07 EDT** with the Apex vehicle absent for twelve miles, the case between Marcus’s boots, and the fuller Hackett/evidence debate unresolved.

### India-side clocks

- Cutaway begins at **22:18 IST**.
- American source certification remains **02:00 IST / 16:30 EDT**.
- Counter-battery support release remains **14:30 IST / 05:00 EDT**.
- The displayed countdown remains `03:41:22 UNTIL ALLIED SOURCE CERTIFICATION.`

## Canon and force validation

The repair preserves:

- Partial capture rather than decisive evidence.
- Integrity as proof of post-capture preservation, not original truth.
- No identification of the Payload 88 deployer.
- No firearm drawn or discharged.
- Mercer’s electroshock weapon held and used as a controlled less-lethal tool.
- Marcus redirecting the weapon rather than striking Mercer.
- Julie refusing to drive into the officer blocking the Ford.
- A real air-handling fault supporting the alarm.
- Outside fire response creating witnesses.
- Sarah and Mercer remaining competent and professionally motivated.
- Sharma remaining independent and unaware of Julie, Marcus, Elias, Payload 88, or Apex’s internal events.

## Remaining risks

- Chapter 3 is materially shorter than the original accepted version. Future passes should not remove additional custody pressure or escape geometry without a new design review.
- Markdown physical-line count is only a proxy for final typeset pages; valid speaker paragraphing must never be removed to improve the metric.
- Chapter 4 intentionally revisits the official-version problem, evidence integrity, Hackett, and the compromised farm. The repaired Chapter 3 limits setup but does not eliminate all thematic overlap.
- The approximate accepted-manuscript total uses tracker arithmetic rather than a full repository-wide recount.

## Acceptance recommendation

Accept the repaired Chapter 3 as the controlling manuscript. It retains the successful narrative compression while restoring valid fiction paragraphing, honest metrics, crisis rhythm, punctuation consistency, and a cleaner Chapter 4 handoff.
