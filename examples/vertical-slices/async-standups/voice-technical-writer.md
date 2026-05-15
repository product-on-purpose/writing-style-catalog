---
entry_id: technical-writer
axis: voice
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

This document proposes replacing the daily synchronous standup with an async-first format for a 30-day trial. It summarizes the current state, the proposed change, the rationale, and the revert path.

## Current state

The team includes 11 engineers across 4 timezones: 3 in US Pacific, 3 in US Eastern, 2 in the UK, and 3 in India. The synchronous standup runs at 9am Pacific, which is 9:30pm in India. In Q1, India engineers attended an average of 3.2 of 5 standups per week. US-based engineers attended 4.6 of 5. The meeting averages 14 minutes. About 4 of those minutes produce actionable information.

## Proposed change

Replace the daily synchronous standup with a daily async update in #team-standup. Each engineer posts by 10am local time. Each post contains three fields:

- Shipped
- In progress
- Blocked or at risk

Blocker entries @mention the person who can unblock. The recovered 9am Pacific slot is repurposed to a 60-minute Thursday working session. The working session is not a status meeting. Its agenda is set the day before.

## Rationale

Three observations support the change.

1. The current meeting time is not equitable. India engineers attend at 9:30pm local, and their attendance reflects that cost.
2. Information density is low. A 14-minute meeting that produces 4 minutes of action is not a good use of 11 people's time.
3. Standup discussion is not searchable. On a recent incident, Priya diagnosed a specific 401 error during standup. Five hours later, another engineer hit the same error and spent 45 minutes re-diagnosing it. A Slack post would have been findable.

## What this does not change

It does not change on-call rotation, escalation paths, or the 1:1 cadence. It does not eliminate synchronous time. The Thursday working session preserves a real-time touchpoint with a different purpose.

## Trial and revert

The trial runs for 30 calendar days. At the end of the trial, the team reviews three measures: India attendance and contribution rates, blocker response time, and self-reported friction in a short survey. If the team decides to revert, the synchronous standup returns the following Monday. No further approval is required.
