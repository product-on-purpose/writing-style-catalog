---
diff_pair_id: format-adr-vs-meeting-notes-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: adr
entry_b: meeting-notes
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `adr` vs `meeting-notes`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `adr` - A short structured document that captures a significant architectural decision, its context, and its consequences.
**B:** `meeting-notes` - A structured capture of what was decided and what was assigned - not a transcript. Organized by outcome so someone who missed the meeting can act without asking follow-up questions.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `adr`

# ADR-0014: Adopt Async-First Standup Format

## Status

Accepted

## Context

The engineering team has grown from 6 to 11 engineers over 18 months. The team now spans four timezones: US Pacific (3 engineers), US Eastern (3 engineers), UK (2 engineers), India (3 engineers). The current synchronous standup is scheduled at 9am Pacific, which is 9:30pm India Standard Time.

Three forces pushed this decision:

**Timezone asymmetry.** The India-based engineers are disproportionately burdened by the meeting schedule. Attendance data from Q1 shows the three India engineers averaged 3.2 standup appearances per week out of 5, compared to 4.6 for US-based engineers. The shortfall is not disengagement - it is 9:30pm.

**Information loss.** Status shared verbally in the meeting does not persist. We have documented three incidents in the past quarter where an engineer spent more than an hour on a problem that had already been solved and discussed in a previous standup. There is no searchable record.

**Meeting-to-value ratio.** The standup averages 14 minutes. Analysis of the past month shows an average of 4.2 minutes of content that changed someone's behavior - a blocker raised, a dependency flagged, a context shared. The remaining 10 minutes is status that required no response from anyone.

Alternatives considered: rotating the meeting time (solves equity but adds overhead and still does not create persistence), eliminating standup entirely (loses coordination value), and adopting an async tool like Geekbot (rejected on cost and added tooling complexity - Slack templates serve the same function).

## Decision

Replace the synchronous daily standup with an async standup update in #team-standup. Engineers post by 10am their local time using a pinned template:

- **Shipped:** what completed in the last 24 hours
- **In progress:** current focus
- **Blocked / at risk:** anything that needs attention, with @mention of the person who can resolve it

The on-call engineer reads the channel by 9am Pacific and responds to blocked items within 30 minutes during business hours. The synchronous standup slot is replaced with a 60-minute Thursday working session - not a status meeting, reserved for discussion requiring real-time exchange.

## Consequences

### Positive

- All engineers participate on a schedule that fits their timezone
- Status information is persistent and searchable
- Blocked items route directly to the person who can resolve them via @mention
- Engineers recover 70 minutes per week previously spent in synchronous status reporting

### Negative

- Social cohesion that comes from shared daily presence is reduced; the Thursday session is a partial substitute but not equivalent
- The format depends on consistent participation - if engineers stop posting, the channel's value drops for everyone
- Blockers that require nuance are harder to surface in a structured three-field template than in a live conversation

### Neutral

- On-call rotation adds a daily channel-reading responsibility, but this replaces the meeting facilitation responsibility previously on the same rotation
- The Thursday working session is new overhead for some engineers who previously skipped standup

---

## B: `meeting-notes`

# Platform Eng Weekly - Standup Format Review

**Date:** 2026-05-14 (Thursday)
**Time:** 09:00 - 09:45 Pacific
**Location:** Zoom + #eng-platform thread
**Facilitator:** Maya Chen
**Notes:** Priya Raman

## Attendees

Present (9): Maya Chen, Priya Raman, Devon Park, Sara Okafor, Jamie Liu, Tom Bradley, Aditi Sharma, Ravi Krishnan, Nikhil Iyer
Absent (2): Emma Walsh (PTO), Oliver Hughes (on-call handoff)

## Agenda

1. Q1 standup attendance and time-cost data (Maya, 10 min)
2. Proposed async-first format (Maya, 15 min)
3. Trial scope, success metrics, concerns (group, 15 min)
4. Decisions and owners (5 min)

## Decisions

- **D1.** The team will run a 30-day async standup trial starting Monday May 19. The 9am Pacific sync slot is paused for the trial duration.
- **D2.** Daily updates are posted in #team-standup by 10am local time using the three-field template: Shipped / In progress / Blocked or at risk.
- **D3.** The Thursday 9am Pacific slot is repurposed as a 60-minute working session (not status). Agenda required, posted Wednesday EOD.
- **D4.** On-call engineer owns daily channel triage by 9am Pacific and 30-minute blocker response during business hours.
- **D5.** Trial review checkpoints are day 15 (lightweight pulse) and day 30 (go / no-go / extend).

## Discussion summary

Maya presented Q1 data: India attendance 3.2/5 vs US 4.6/5, 14-min average standup with ~4 min driving any action, and three documented duplicate-work incidents that a searchable record would have caught.

Aditi and Nikhil supported the change and noted 9:30pm IST is particularly hard on evenings with family commitments. Devon raised concern that async loses the social moment that makes the team feel like a team. Maya acknowledged this is the strongest argument against and is the reason the Thursday session is being added rather than the time fully reclaimed.

Tom asked what happens if someone consistently misses async posts. Group agreed the on-call engineer pings missing posters at 11am local, and persistent gaps escalate to Maya at day 7. Sara asked about PTO and on-call days - resolved by adding an explicit "out" or "on-call, no update" line, captured in the reference doc.

Jamie raised a tooling question (Geekbot vs Slack pinned template) - group decided to start with the pinned template and revisit at day 30 if friction warrants tooling spend.

## Action items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| A1 | Pin standup template to #team-standup with field definitions | Priya | 2026-05-16 |
| A2 | Send trial kickoff email to eng-platform | Maya | 2026-05-15 |
| A3 | Draft standup format reference doc (PTO, on-call, partial weeks) | Priya | 2026-05-16 |
| A4 | Schedule Thursday working session series, cancel daily 9am Pacific | Maya | 2026-05-15 |
| A5 | Brief on-call rotation on daily triage responsibility | Tom | 2026-05-18 |
| A6 | Set up day-15 pulse survey (3 questions) | Priya | 2026-05-29 |
| A7 | Day-30 review meeting on calendar | Maya | 2026-05-15 |

## Open questions

- **OQ1.** Do we need a separate channel for blockers or does #team-standup with @mentions work? Revisit at day 15 if signal-to-noise is a problem.
- **OQ2.** How do we surface async updates to stakeholders outside the team (PM, design)? Owner: Maya, by day 15.

## Next meeting

Day-15 async pulse review, Friday 2026-05-29, async in thread (no live meeting).
