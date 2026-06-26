---
diff_pair_id: format-daily-standup-vs-meeting-notes-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: daily-standup
entry_b: meeting-notes
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `daily-standup` vs `meeting-notes`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `daily-standup` - A brief daily status communication with three fixed sections - done, next, blockers. Surfaces information and flags what needs action. Not a progress report; a coordination tool.
**B:** `meeting-notes` - A structured capture of what was decided and what was assigned - not a transcript. Organized by outcome so someone who missed the meeting can act without asking follow-up questions.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `daily-standup`

**#team-standup - Devon Park - Tue May 27, 9:42am PT (day 9 of trial)**

**Shipped**
- Rate-limiter rollout to staging; 0 errors over 18h soak
- PR #4412 merged (auth token rotation runbook)

**In progress**
- Production rollout of rate-limiter, gated behind `rl_v2` flag, 5% traffic by EOD
- Pairing with Aditi 10am PT on the IST-hour metrics dashboard

**Blocked / at risk**
- Waiting on @sara for sign-off on the rotation runbook before I close the parent ticket (not urgent, EOW is fine)
- (meta) Async format participation was 9/11 yesterday - @oliver and @emma did not post. Oliver was on-call handoff, fine. Emma I will DM. Flagging so @maya has visibility before the day-15 pulse.

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
