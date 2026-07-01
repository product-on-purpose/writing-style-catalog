---
entry_id: user-manual
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Project Halyard Close-Out Celebration - User Manual

## Table of Contents

- [Getting Started](#getting-started)
- [Attending the Celebration](#attending-the-celebration)
  - [RSVP and Logistics](#rsvp-and-logistics)
  - [Joining Remotely](#joining-remotely)
- [Giving and Receiving Recognition](#giving-and-receiving-recognition)
  - [The Recognition Wall](#the-recognition-wall)
  - [Giving a Shoutout](#giving-a-shoutout)
  - [Receiving a Shoutout](#receiving-a-shoutout)
- [The Retrospective Session](#the-retrospective-session)
  - [Reading the Timeline Packet](#reading-the-timeline-packet)
  - [Participating in the Extended-Scope Retro](#participating-in-the-extended-scope-retro)
- [Swag and Artifacts](#swag-and-artifacts)
  - [Claiming Your Halyard Swag](#claiming-your-halyard-swag)
  - [The Commemorative Phase Chart](#the-commemorative-phase-chart)
- [Troubleshooting](#troubleshooting)
- [Reference](#reference)

## Getting Started

This manual covers the Project Halyard close-out celebration on June 30, 2026, and the extended-scope retrospective that runs as part of it. It is for anyone who had time against the checkout-reflow rebuild at any point across the fourteen-month run - engineering, infra, QA, analytics, or anyone who rotated off before the June 13 cutover.

It is a reference, not a script. Look up the section you need rather than reading the whole thing in order.

Before the event:
- Read the June 2 - June 20, 2026 status report circulated by Priya Vasquez, the program lead. It is the fastest way to reconstruct the timeline if your memory of specific weeks has already compressed.
- Read or skim the timeline packet (see Reading the Timeline Packet). It goes out to all invitees three days before the session.
- RSVP by June 26 (see RSVP and Logistics). Catering and the recognition-wall printing both run off the RSVP count.

You do not need to prepare a formal presentation. The retrospective is structured; the celebration portion is not.

## Attending the Celebration

### RSVP and Logistics

The celebration and retrospective run back to back on June 30, starting at 3:00 PM, in the fourth-floor common area. Budget roughly two hours: ninety minutes for the retrospective, the remainder for recognition and the informal celebration.

Steps:
1. Open the calendar invite titled "Project Halyard Close-Out."
2. Select an RSVP response by June 26. This date is firm - it is the cutoff Dani Rowe uses to finalize catering and swag counts.
3. If you have a dietary restriction, add it as a note on the RSVP rather than mentioning it the day of.
4. If you rotated off the project before the June 13 cutover, RSVP anyway. You are invited regardless of when you left.

Options / Parameters:
- Attendance mode: in-person (fourth-floor common area) or remote (video link in the invite)
- Dietary note: free-text field on the RSVP form
- Plus-ones: not applicable. This is a working-hours internal event for people who were on the project.

Notes:
- If you are not sure whether you counted as "on the project," you did. Anyone with commits, incident-response time, review time, or planning time against Halyard at any phase qualifies.

### Joining Remotely

The retrospective portion runs for in-person and remote attendees at the same time. The celebration portion afterward is lighter for remote attendees, but recognition-wall contributions and shoutouts are fully accessible remotely.

Steps:
1. Use the video link in the calendar invite, not a personal meeting link.
2. Join at 3:00 PM sharp for the retrospective. The recognition segment that follows is less time-sensitive.
3. To submit a written shoutout remotely, use the form linked in the invite rather than waiting for the in-person card station (see Giving a Shoutout).

Notes:
- The retrospective is recorded for anyone who cannot attend either way. The recording is not a substitute for the written retrospective summary that follows - see The Retrospective Session.

## Giving and Receiving Recognition

### The Recognition Wall

The recognition wall is a physical board, mirrored on the remote form, where anyone can post a named, specific piece of recognition: who did something, what it was, and what it cost or prevented. It stays up for a week after the event for anyone who missed it.

Steps:
1. Take an index card from the station near the entrance, or open the remote form.
2. Write one entry per card: name, the specific decision or action, and what would have happened without it.
3. Pin the card to the wall under the relevant phase heading - Foundation, Canary, Ramp, Slip, or Cutover - or select the matching phase in the remote form.

Options / Parameters:
- Format: index card (in person) or remote form (same fields, submitted online)

Notes:
- Generic praise does not work well on the wall. "Great work this year" is not a wall entry. "Marcus Teel filed the February cart-state bug when he could have marked it low severity and moved on" is a wall entry. If you are stuck on wording, see Giving a Shoutout for the same method spoken aloud.

### Giving a Shoutout

A shoutout is the spoken version of a recognition-wall entry, given at the microphone during the recognition segment. The method is the same either way: name the person, name the specific thing they did, name what it cost or prevented.

Steps:
1. Signal Priya Vasquez before the segment starts if you want a slot. Slots are also open to walk-ups if time allows.
2. State the person's name and what they specifically did. A role title is not a substitute for the action - "she was a great lead" names a title; "she recommended the parallel-run option knowing it would cost fourteen months of double operating overhead" names the action.
3. State what would have happened on the easier path, if you know it.
4. Keep it under a minute. Two or three sentences is usually enough once the specifics are there.

Options / Parameters:
- Delivery: spoken at the mic, or written on a wall card if you would rather not speak
- Length: no hard limit, but the segment is time-boxed, so specific and short beats long and general

Notes:
- Examples from the record, if you want a model to work from: Dani Rowe calling the March hold when the February near-miss was not fully resolved; Marcus Teel filing the February bug on his own initiative; Jordan Osei rewriting the payment callback handler over a weekend instead of patching around it; Sam Wickfield holding the regression bar on June 9 when every hour of delay felt enormous. None of that shows up in a commit count. That is what the shoutout segment is for.

### Receiving a Shoutout

Steps:
1. Let the recognition land. Do not deflect it onto the whole team in the moment - there is a separate closing note for team-wide thanks.
2. If a detail is wrong (wrong date, wrong attribution), correct it briefly and warmly, then let the recognition stand.
3. A short "thank you" is a complete response. Nothing further is required.

Notes:
- People routinely undercount their own contribution on a fourteen-month project, because the work stopped feeling unusual to them somewhere around month six. The wall and the shoutouts exist partly to correct for that.

## The Retrospective Session

### Reading the Timeline Packet

The timeline packet goes out three days before the event. It contains the dated sequence of incidents, slips, and decisions across the full run: the February and April near-misses, both launch-date slips, and the June 13 cutover.

Steps:
1. Read the packet before June 30. The ninety-minute retrospective slot is not long enough to reconstruct the timeline from memory in the room.
2. Note anything you remember differently from the packet and raise it during the session, not after.

Notes:
- The packet draws directly on the ADR, the status report, and the incident tickets. It is not a summary written from memory.

### Participating in the Extended-Scope Retro

This retro is structured by project phase, not by sprint. A standard sprint-retro format does not fit a fourteen-month run, so this session runs longer and covers more ground than a normal retrospective.

Steps:
1. The facilitator opens with what was supposed to happen at each phase boundary, then moves to what actually happened.
2. Participants add what a given divergence cost or prevented, phase by phase: foundation and shadow mode, canary ramp, the February slip, the April slip, cutover.
3. Before the session closes, confirm who is writing the summary and when it circulates. This session produces its own written record, separate from this manual.

Options / Parameters:
- Format: structured discussion by phase, not free-form
- Duration: ninety minutes, held to the clock so the recognition segment is not squeezed

Notes:
- This manual covers how to attend and participate in the day's events. It is not the retrospective's written output; that summary is a separate document, expected the week after June 30.

## Swag and Artifacts

### Claiming Your Halyard Swag

Steps:
1. Check the swag table near the entrance on your way in or out.
2. Take one item per person. The run was sized to the RSVP count, not to walk-ins.
3. If you RSVP as remote and want an item, note it on the RSVP form. Remote swag ships the following week.

Notes:
- Swag is optional and unrelated to whether you give or receive recognition. Skipping the table has no bearing on anything else in this manual.

### The Commemorative Phase Chart

A printed copy of the five-phase rollout chart from the checkout-reflow README is posted at the event and mailed to remote attendees who request it.

Steps:
1. Take a copy from the station next to the recognition wall, or request one on the RSVP form if attending remotely.
2. If you want a specific phase annotated with your own note before it is archived, add it during the week the wall stays up.

Notes:
- The chart is decorative, not a substitute for the record. The ADR, the status report, and the incident tickets remain the authoritative documents.

## Troubleshooting

**I can't attend in person on June 30.**
Join remotely using the video link in the calendar invite. The retrospective runs for both audiences at once; use the remote form for recognition-wall entries and shoutouts.

**I rotated off the project before the June 13 cutover and I'm not sure I still count as invited.**
You count. RSVP anyway. Anyone with time against Halyard at any phase is invited, regardless of when they left.

**I don't know what to say for a shoutout.**
Use the method in Giving a Shoutout: name the person, name the specific thing they did, name what would have happened on the easier path. If you cannot get that specific, pull an example from the timeline packet instead of defaulting to general praise.

**I missed the RSVP deadline.**
Contact Dani Rowe directly. Catering and the swag count are locked after June 26, but a late RSVP can usually still be added to the attendee list and the remote link.

**A recognition-wall entry I wrote has a detail wrong.**
Corrections are welcome. Cross out the incorrect detail and write the correction beside it rather than removing the card; the wall stays up for a week specifically so entries can be refined.

**I was on the project but I'm not named anywhere in the status report or the ADR.**
Most of the fourteen months of work does not appear in either document by design - both name the decisions that changed the outcome, not the full roster. The complete contributor list is in CONTRIBUTORS.md, and the recognition wall is open to any name, named document or not.

## Reference

### Glossary

- **Parallel run**: Operating the old and new checkout systems at the same time, routing live traffic to only one, so the new system can be validated under real load without a single-shot cutover risk.
- **Near-miss**: An issue found and fixed before it reached a customer. Halyard had two, in February and April 2026.
- **Cutover**: The point at which all live traffic moves to the new system and the old system stops carrying production load. Halyard's cutover was June 13, 2026.
- **Archive window**: The 30-day period after cutover during which the legacy system stays available in read-only mode before decommission.
- **Close-out**: The set of activities - status report, retrospective, recognition, decommission - that formally end a project after launch.

### Key dates

| Date | Event |
|------|-------|
| 2025-02-14 | ADR-0017 accepted; parallel-run approach chosen |
| 2026-02 | First near-miss found (cart-state mismatch, Marcus Teel) |
| 2026-04 | Second near-miss found (payment-callback race condition, Jordan Osei) |
| 2026-06-13 | Full cutover to the rebuilt checkout |
| 2026-06-13 to 2026-06-14 | First peak-load weekend held without incident |
| 2026-06-25 | Milestone closure recorded (ADR-0017) |
| 2026-06-26 | RSVP deadline for the close-out celebration |
| 2026-06-27 | Operational runbook handoff target (Dani Rowe) |
| 2026-06-30 | Close-out celebration and extended-scope retrospective |
| 2026-07-07 | Cart-abandonment baseline report target (Mia Chen) |
| 2026-07-14 | Legacy checkout decommission target |

### Where to find the full record

- ADR-0017 - the architectural decision and its recorded consequences
- The June 2 - June 20, 2026 status report - the final close-out status, near-miss detail, and the asks
- checkout-reflow README - the phase-by-phase rollout chart and the people who held the migration together
- CONTRIBUTORS.md - the complete project roster
- Legacy Checkout Decommission Runbook - the procedure that closes the archive window on July 14
