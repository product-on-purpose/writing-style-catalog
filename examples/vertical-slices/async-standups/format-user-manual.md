---
entry_id: user-manual
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Team Standup User Manual

## Table of Contents

- Getting Started
- Posting Your Daily Update
  - Writing and posting your update
  - Marking a blocker resolved
- Reading the Channel (On-Call Duties)
  - Daily triage
  - Escalating a blocker
- The Thursday Working Session
- Special Cases
  - PTO
  - On-call days
  - No update to give
  - Sensitive or people-related blockers
  - Public holidays
- Troubleshooting
- Reference

## Getting Started

This manual covers the #team-standup async process used by the eng-platform team (11 engineers across US Pacific, US Eastern, UK, and India). It replaced the team's synchronous daily standup and is running as a 30-day trial, 2026-05-19 through 2026-06-19, owned by Maya Chen (EM Platform).

Requirements:
- Access to the #team-standup channel in the eng-platform Slack workspace.
- If you are on the on-call rotation, access to #on-call-schedule and #on-call-log as well.
- Five minutes a day to write and post an update.

First session:
1. Read the pinned message in #team-standup. It holds the current template and house rules.
2. Note your own posting deadline: 10am in your local timezone, not Pacific.
3. Check #on-call-schedule to see whether you are on the on-call rotation this week (see Reading the Channel).

## Posting Your Daily Update

What this covers: the daily status update every engineer posts, and how to close the loop once something you flagged gets resolved.

### Writing and posting your update

What it does: records what you shipped, what you are working on, and what is blocking you, in a format the rest of the team can skim in under a minute.

Steps:
1. Copy the pinned template from #team-standup, or trigger it with the `/standup` shortcut.
2. Fill in the three fields: Shipped, In progress, Blocked or at risk.
3. In the Blocked or at risk field, @mention the specific person who can resolve each item.
4. Post before 10am your local time.

Template:
```
Shipped:
 - <what landed since your last post>

In progress:
 - <what you are actively working on today>

Blocked or at risk:
 - <what is stuck, and who or what you need>
```

Options / Parameters:
- Empty field: write "nothing today" rather than deleting the field.
- Skipping a field entirely: acceptable on Fridays only.
- Backfill window: same day, until 17:00 your local time, if you miss the 10am cutoff.
- Cannot post before 10am (early meeting, travel): post the previous evening instead, with a "tomorrow:" prefix on the In progress line.

Notes:
- A valid blocker names three things: what is blocked, who can unblock it, and when you need it. "@user, can you review #4412 today?" is a blocker. "Reviews are slow" is not, and will not route anywhere.
- Sensitive or PTO-affected updates follow different rules. See Special Cases.

### Marking a blocker resolved

What it does: closes the loop on a blocker you previously posted, so the channel stays a reliable record of what actually happened.

Steps:
1. Edit your original post to reflect the resolution, or
2. Reply in the same thread with `resolved:` and the outcome.

Notes:
- Do not delete the original line. The searchable record of what was blocked and how it resolved is part of the point of moving async.

## Reading the Channel (On-Call Duties)

What this covers: the daily triage responsibility assigned to whichever engineer is on the on-call rotation that week. If you are not on-call this week, you do not need this section.

### Daily triage

What it does: confirms every blocker posted that day gets a response, and surfaces anyone who has not posted.

Steps:
1. Between 10:00 and 11:00 Pacific, open #team-standup and review the day's posts.
2. Tally posts received against today's expected headcount (11 minus anyone confirmed on PTO).
3. If fewer than 80 percent of expected posts have arrived by 10:30 Pacific, direct-message anyone missing: "Hey, no standup post yet today, any blockers?"
4. Read every post and identify each @mention inside a Blocked or at risk field.
5. Reply in-thread to every @mention (a resolution, a diagnostic question, or a handoff) within 30 minutes of your first read.
6. For any at-risk line with no @mention, reply in-thread asking whether the engineer needs help.
7. Post a triage summary in #on-call-log: "Standup triage [date]: [N] posts received, [N] blockers found, [N] resolved, [N] escalated."

Options / Parameters:
- Rotation: the same engineers who previously facilitated the synchronous standup.
- Response SLA: 30 minutes during the resolver's business hours.
- Time budget: 10 minutes per morning under normal conditions.

Notes:
- Triage running closer to 25 minutes on a given morning usually means blockers are surfacing earlier than they did under the old sync model. That is the system working, not a sign it is broken. See Troubleshooting before asking to split the rotation.
- Triage is read-and-respond only; there is no system state to roll back. If you reply in the wrong thread, post a correction in the same thread.

### Escalating a blocker

What it does: moves an unresolved blocker up the chain when the normal @mention and reply does not clear it.

Steps:
1. Day 0, at post time: the engineer @mentions the resolver in their update.
2. Plus 4 business hours: the on-call engineer nudges the resolver in-channel.
3. Plus 1 business day: on-call escalates to the resolver's manager.
4. Plus 2 business days: escalates to Maya Chen.

Notes:
- This ladder runs alongside the 30-minute first-response SLA. The SLA covers acknowledgment; the ladder covers what happens if acknowledgment does not turn into resolution.

## The Thursday Working Session

What this covers: the 60-minute weekly slot that replaced the block of synchronous standups, reserved for anything that genuinely needs real-time discussion.

Steps:
1. Check the agenda at `docs/thursday-agenda.md` before the session.
2. Add a topic to the agenda by 17:00 Pacific Wednesday if you need real-time discussion time.
3. Attend Thursdays at 8:00 Pacific / 20:30 IST.

Options / Parameters:
- Length: 60 minutes.
- Cancellation: if the agenda is still empty by 17:00 Pacific Wednesday, the session is cancelled and the time is given back.

Notes:
- This is not a status meeting. Status belongs in #team-standup. Bring decisions, design questions, and anything that needs real-time back-and-forth.

## Special Cases

What this covers: how to post when your day does not fit the standard pattern.

### PTO

Post one line on your last working day before you leave: "OOO `<date range>`, back `<date>`. Coverage: @user." Do not post while on PTO.

### On-call days

Post your normal update, plus a fourth line: "On-call: responding to pages, async post may be late." On-call days do not count against your participation metrics.

### No update to give

Post anyway, with "nothing today" in each field that does not apply. A thin update is easier to interpret than no update at all.

### Sensitive or people-related blockers

Post "Blocked: DMing @maya" in the channel and take the actual content to a direct message. Do not name the person involved in the channel.

### Public holidays

Post on the days you work. On a public holiday for your locale, skip without notice.

## Troubleshooting

**Posts are running long, 200 words or more:** The three fields are prompts for short bullets, not headers for paragraphs. Point to the exemplar posts pinned in the channel and hold the three-bullet ceiling at the Thursday session.

**A timezone cluster is consistently late or silent:** Check whether the 10am local cutoff is achievable for that group. If their workday starts at or after 10am local, the cutoff is a scheduling problem, not a compliance one. Move their window.

**A thread under a blocked item runs past a few messages:** Standup threads are for clarifying questions, not decisions. Move the conversation to a DM or add it to the Thursday agenda.

**On-call triage is regularly running over the 10-minute budget:** See the note under Daily triage. Give it a week before restructuring the rotation.

**An engineer has not posted and has not replied to a DM within 60 minutes:** Escalate to Maya Chen with the engineer's name and last known context.

## Reference

**Template fields**

| Field | Includes | Excludes |
|---|---|---|
| Shipped | Work merged, deployed, or otherwise complete in the last 24 hours | Work in review, planning, meetings attended |
| In progress | Current focus through your next workday | Backlog items, speculative work |
| Blocked or at risk | Anything where someone else's input changes your day | Vents, status with no ask |

**Timing at a glance**

| Event | Time |
|---|---|
| Daily post deadline | 10:00 local time |
| Backfill window | Same day, until 17:00 local |
| On-call triage window | 10:00 to 11:00 Pacific |
| Blocker response SLA | 30 minutes, resolver's business hours |
| Thursday working session | 8:00 Pacific / 20:30 IST, 60 minutes |
| Thursday agenda cutoff | 17:00 Pacific Wednesday |

**Metrics tracked** (pulled weekly by Priya)

| Metric | Target |
|---|---|
| Participation rate (posts / engineers / workday) | 9 of 11 or better |
| Blocker response time (post to first substantive reply) | Under 30 minutes |
| Stale blockers (open more than 2 business days) | Zero |

**Glossary**

- **On-call reader**: the engineer assigned to daily channel triage that week.
- **Blocker**: an item that needs another person's input, tagged with an @mention.
- **At risk**: an item trending toward becoming a blocker, not yet actionable by anyone else.

**Related documents**

- Process playbook: `docs/playbook.md`
- Thursday agenda: `docs/thursday-agenda.md`
- Trial retro: `docs/trial-retro.md`
- Decision record: ADR-0014, Adopt Async-First Standup Format
- Channels: #team-standup, #on-call-log, #on-call-schedule
