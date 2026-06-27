---
entry_id: pitch-deck
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Slide 1: The standup is failing half the team

- Team: 11 engineers across 4 timezones - US Pacific, US Eastern, UK, India
- 9am Pacific is 9:30pm IST
- India engineers averaged 3.2 of 5 standups in Q1; US engineers averaged 4.6
- This is not a discipline problem. It is a scheduling problem.

## Slide 2: Swap the meeting for a three-field Slack post

- Engineers post to #team-standup by 10am local time
- Three fields: Shipped, In progress, Blocked or at risk
- Blockers @mention the person who can resolve them - no waiting for 9am Pacific
- Status persists in Slack; searchable; no information lost between sessions

## Slide 3: The team crossed the timezone threshold

- At 6 engineers: a 9am Pacific slot fits the whole team
- At 11 engineers across 4 timezones: it does not
- India headcount grew across the last two hiring rounds
- We are already operating async in practice - only the standup pretends otherwise

## Slide 4: One post per engineer, by 10am local time

- **Post:** Shipped / In progress / Blocked or at risk in #team-standup
- **On-call engineer:** reads the channel by 9am Pacific, responds to @mentions within 30 min
- **Thursday:** 60-minute working session at 8am Pacific replaces the weekly sync slots - reserved for discussion that requires real-time exchange
- No new tools. Slack templates only.

## Slide 5: 14-minute meeting, 4 minutes of signal

- The standup averaged 14 minutes per session
- Past month analysis: 4.2 minutes per session changed someone's behavior
- The remaining 10 minutes was status that required no response from anyone
- Last quarter: 3 incidents where an engineer spent 1+ hour on a problem already solved in a prior standup - no persistent record existed

## Slide 6: Recover 70 minutes per engineer per week, add nothing new

- **Recovered:** 70 person-minutes per engineer per week (the 14-minute daily slot disappears)
- **Thursday session:** 60 minutes replaces the five daily sync slots for the week
- **New overhead:** On-call engineer adds a daily channel-read to existing scope
- **Tooling cost:** Zero - Slack templates, no new subscriptions

## Slide 7: The infrastructure is already in place

- Engineering manager: owns the template, the process doc, and the 30-day retro
- On-call rotation (already running): adds daily channel triage to existing scope
- No new roles. No new tools. No new budget.

## Slide 8: Thirty days, then a decision

**Ask:** Approval to run a 30-day trial starting next Monday

At Day 30, the director of engineering reviews:

- Participation rate by timezone
- Blocker resolution time vs sync baseline
- Qualitative signal from 1:1 check-ins with all 11 engineers

**Decision:** Adopt, modify, or revert - with evidence.
