---
entry_id: postmortem
axis: format
topic_slug: remote-work-policy
topic_label: Arguing a public position on return-to-office
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Anchor-Day Policy Launch - Room Booking Contradiction (July 7)

## Severity

SEV-3

## Summary

On July 3, the all-staff email announcing the anchor-day hybrid policy went out before decision authority between HR and Facilities had been formally confirmed. Facilities was operating a room-booking system premised on voluntary distributed attendance across the full week, not the mandatory two-day concentration the new policy required. On the first official anchor Tuesday (July 7), three teams arrived without adequate room reservations and had to conduct their planned collaboration sessions in a split-room, split-remote configuration, negating the purpose of the anchor day for those teams.

## Timeline

- 2026-06-20 - Status report for the week ending June 20 flags unresolved decision authority between HR and Facilities as a critical blocker; escalation to executive sponsor targeted for June 28.
- 2026-06-27 - Manager FAQ draft not completed; deadline slips one week. Leadership brief review conducted with no new objections surfaced.
- 2026-06-28 - Executive sponsor briefing held. Decision authority question raised. Sponsor acknowledged the gap and committed to resolve it "before any communication goes wide." No written confirmation issued. Facilities was not party to the briefing.
- 2026-07-03 09:00 - Communications team sends the all-staff email announcing the anchor-day hybrid policy. Email names Tuesday and Thursday as anchor days effective immediately, with July 7 as the first anchor Tuesday.
- 2026-07-03 09:50 - Employees begin booking conference rooms for July 7. Room-booking system starts rejecting reservations for groups larger than six in the main collaboration spaces.
- 2026-07-03 10:30 - First escalation reaches Facilities. They confirm their booking quotas were modeled on 40-60% weekly occupancy distributed across all five days, not on concentrated mandatory turnout on two specific days.
- 2026-07-03 14:00 - Priya Ahluwalia (Policy Working Group Lead) escalates to the executive sponsor and Facilities Director. Emergency room-reassignment triage begins for July 7.
- 2026-07-07 08:00 - First anchor Tuesday begins. Triage resolved two of the five team conflicts; three teams cannot be accommodated and run sessions with part of the team remote, part in-office.
- 2026-07-07 17:30 - Priya collects incident reports from affected team leads.
- 2026-07-08 10:00 - Postmortem initiated.

## Root Cause

The policy and its operational infrastructure were treated as a single system when they were actually two separate systems with independent owners and incompatible assumptions. The policy working group owned the policy language; Facilities owned the room-booking infrastructure. No mechanism required these two to align before the announcement. The June 28 executive sponsor briefing produced a verbal commitment to resolve decision authority before the communication "went wide," but the commitment was not documented and was not passed to the Communications team. Communications, operating on their own launch calendar, sent the announcement five days later without a hold signal. The systemic condition that allowed this was the absence of a formal cross-functional launch gate: a checkpoint with defined owners and a documented sign-off requirement before any all-staff policy communication is released.

## Impact

- Employees affected: all staff with office access on July 7; approximately 40% of the company
- Duration: July 3 (announcement) through July 10 (interim booking quotas updated by Facilities)
- Functions affected: room-booking system (Facilities), work location policy (HR and Policy Working Group), manager communications pipeline
- Trust cost: managers received operationally contradictory signals within the same 24-hour window - a policy email promising predictable anchor-day collaboration and a booking system that prevented that collaboration from being scheduled

## Contributing Factors

- Decision authority over the policy was never formally assigned in writing before the launch
- The executive sponsor's verbal commitment on June 28 was not documented and did not propagate to the Communications team
- Communications and the Policy Working Group operated on separate planning tracks without a shared gate
- Facilities room-booking quotas were modeled against historical voluntary occupancy patterns, not the mandatory two-day concentration the anchor-day model requires; the model was never updated after the policy direction was set
- The Manager FAQ, flagged in the June 20 status report as a pre-launch dependency, was not completed before the announcement

## Action Items

- [ ] Assign a single named decision owner (role level: Chief People Officer or designee) for all work location policy communications, documented in writing, before any further all-staff policy announcements - Owner: Chief People Officer - Due: July 15
- [ ] Update Facilities room-booking quotas to reflect 80-90% occupancy on Tuesdays and Thursdays for the remainder of July; recalibrate after observing the first four anchor days and set permanent baselines - Owner: Facilities Director - Due: July 10
- [ ] Add a formal cross-functional launch gate to the policy communications checklist requiring written sign-off from HR, Facilities, and Communications before any policy announcement is released - Owner: Priya Ahluwalia - Due: July 18
- [ ] Send an all-staff follow-up acknowledging the room-booking gap, apologizing for the disruption on July 7, and describing the interim process for the July 14 anchor day - Owner: Communications team - Due: July 9
- [ ] Complete the Manager FAQ covering anchor-day room protocols, accommodation requests, and onboarding - Owner: Priya Ahluwalia - Due: July 18

## Lessons Learned

The June 20 status report named the exact condition that caused this incident: unresolved decision authority between HR and Facilities. The working group saw it, documented it, and set a resolution target. The gap was not in diagnosis - it was in enforcement. There was no mechanism to hold the launch until the blocker cleared. A verbal commitment in a briefing is not a launch gate; it is a good-faith intention that does not propagate downstream unless someone is explicitly responsible for confirming that it did.

A second lesson: the policy is not the implementation. The anchor-day model is coherent as a decision. The room-booking system was not updated to match it. These two things needed to be aligned before day one, and the only way to ensure that alignment is a sign-off process that requires Facilities to confirm readiness, not just HR and Communications. The working group's scope did not include Facilities; that was the gap the launch gate would have closed.
