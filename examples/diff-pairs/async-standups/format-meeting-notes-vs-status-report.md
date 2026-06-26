---
diff_pair_id: format-meeting-notes-vs-status-report-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: meeting-notes
entry_b: status-report
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `meeting-notes` vs `status-report`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `meeting-notes` - A structured capture of what was decided and what was assigned - not a transcript. Organized by outcome so someone who missed the meeting can act without asking follow-up questions.
**B:** `status-report` - A periodic async update covering progress since the last report, what is next, and what is blocked - the working unit of distributed-team visibility.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `meeting-notes`

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

---

## B: `status-report`

# Async standup trial - Week 2 status report

**Period:** Days 8 to 14 of the 30-day trial
**Author:** Engineering manager
**Audience:** Director of engineering, team, peer EMs

## Headline

The trial is on track. Participation is up, blockers are getting resolved faster than under the sync model, and India engineers are now contributing every weekday for the first time in this team's history. Two friction points have surfaced and are tracked below.

## Progress this week

- **Post completion:** 47 of 55 expected posts arrived by the 10am local cutoff. That is 85.5 percent on-time, up from 78 percent in Week 1.
- **Blocker resolution:** Median time from `@mention` to first substantive reply was 18 minutes. P90 was 2 hours 40 minutes. Compare to the sync standup baseline, where blockers raised at 9am often did not get a real conversation until the afternoon.
- **India participation:** All 4 IST-based engineers posted every weekday this week. Under the sync model this group attended 3.2 out of 5 standups on average.
- **Time recovered:** With the sync standup gone, the team got back approximately 16 person-hours this week. The Thursday working session used 11 of those. Net recovery: 5 person-hours.

## What is next

- Run the Week 3 cycle without process changes. Holding the design stable so the retro data is comparable.
- Pull the first qualitative signal: 10-minute 1:1 with each engineer Thursday and Friday. One question only: "What do you want to keep, change, or kill after the trial?"
- Prep the retro deck for the Day 30 review. Skeleton landing in `docs/trial-retro.md` by EOD Tuesday.

## Blocked or at risk

- **At risk: async posts trending long.** Three engineers are writing 200+ word posts. The format is meant to be skimmed in under 60 seconds per teammate. Plan: share two exemplar posts in the channel pinned message and demo the three-bullet ceiling at the Thursday session.
- **At risk: on-call triage load.** The on-call engineer this week spent roughly 25 minutes per morning on `#team-standup` triage, higher than the 10 minute target. Likely cause: blockers are surfacing earlier and louder than they did in sync. Watching this for one more week before deciding if the on-call role needs to be split.

## Asks

- None this week.

## Next report

Week 3 status report will land in `#team-standup` and via email by EOD next Monday.
