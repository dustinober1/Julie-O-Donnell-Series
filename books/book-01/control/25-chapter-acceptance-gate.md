# 25. CHAPTER ACCEPTANCE GATE

## Purpose

This gate prevents drafts, plans, and status summaries from becoming accidental canon.

A chapter is not accepted until every required review is complete and one explicit promotion commit updates prose and controls together.

## Stage 1 — Pre-draft lock

Before drafting, record:

- chapter number and working title;
- controlling accepted opening time and location;
- POV structure;
- dominant chapter mission;
- immediate objective;
- failure consequence;
- abort condition or decision boundary;
- required evidence gain, loss, or limitation;
- required character and relationship change;
- injury, clothing, equipment, vehicle, and custody state;
- required payoff and setup;
- intended endpoint; and
- prohibited overclaims.

## Stage 2 — Draft placement

- Store prose in `../drafts/`.
- Keep one active draft path.
- Do not place the file under `../manuscript/`.
- Do not add it to `../ACCEPTED_MANUSCRIPT.yaml`.
- Record the draft in `../../../PROJECT_STATE.yaml`.
- Record its review file in this control pack.

## Stage 3 — Acceptance review

### Continuity

- [ ] Opens from the exact accepted prior endpoint.
- [ ] Exact times are compatible with the master timeline.
- [ ] EDT/IST conversions are correct where applicable.
- [ ] Locations and travel time are plausible.
- [ ] Injuries, treatment, fatigue, clothing, and mobility are continuous.
- [ ] Vehicles, credentials, phones, weapons, and equipment are continuous.
- [ ] Evidence objects remain distinct and correctly held.

### Evidence and knowledge

- [ ] Every new fact has an on-page source.
- [ ] “What it proves” and “what it does not prove” are both preserved.
- [ ] No character knows information they have not received.
- [ ] No registered certificate is turned into physical identity without evidence.
- [ ] Encrypted, incomplete, excluded, or destroyed material is not reconstructed by convenience.
- [ ] Public claims are separated from technical findings.

### Character and ethics

- [ ] Each POV remains within established knowledge and voice.
- [ ] The protagonist does not become physically or technically superhuman.
- [ ] Supporting characters retain agency.
- [ ] Relationship changes are earned on page.
- [ ] Civilian and institutional actors are not treated as conspirators without evidence.
- [ ] Moral boundaries are tested rather than ignored.

### Structure and craft

- [ ] The chapter has one dominant mission.
- [ ] Secondary functions support rather than compete with it.
- [ ] Scene sequence escalates cause and consequence.
- [ ] Technical explanation changes a decision.
- [ ] The ending changes the story state.
- [ ] Narrative House Style v2.2 is satisfied without altering canon.
- [ ] Working title matches the accepted chapter function.
- [ ] Draft word count supports the book budget.

### Series continuity

- [ ] Returning-character fields are updated.
- [ ] No future-book role is assumed before the character’s accepted end state.
- [ ] Series seeds do not replace Book 1 payoff.
- [ ] No-retcon locks are preserved.

## Stage 4 — Verdict

Use exactly one verdict:

- **ACCEPT:** Ready for promotion.
- **REVISE:** Specific changes required; draft remains active.
- **HOLD:** Structurally viable but blocked by unresolved canon, research, or ending architecture.
- **REJECT:** Draft is not the controlling path and must not be used.

Record reasons and required actions. Never use “basically accepted,” “provisionally canon,” or similar ambiguous status.

## Stage 5 — Promotion commit

A promotion commit must perform all of the following together:

1. Move the reviewed prose from `../drafts/` to `../manuscript/chapters/`.
2. Add the file to `../ACCEPTED_MANUSCRIPT.yaml`.
3. Recount accepted words.
4. Update the accepted endpoint.
5. Update `../../../PROJECT_STATE.yaml`.
6. Update chapter status.
7. Update timeline.
8. Update character state and injuries.
9. Update relationships and trust.
10. Update evidence custody.
11. Update knowledge boundaries.
12. Update technology and system state.
13. Update organizations, locations, antagonist state, and public narrative.
14. Update open-thread disposition.
15. Update the recurring-character ledger.
16. Record the acceptance verdict and commit reference.

If any required update is absent, the chapter remains unaccepted even if the prose was moved.

## Stage 6 — Post-promotion check

Before drafting the next chapter:

- verify no duplicate draft remains active;
- verify all links point to the accepted path;
- verify the next mission lock starts from the new accepted endpoint;
- verify word budget and ending contract remain viable; and
- verify `PROJECT_STATE.yaml` contains no stale status.
