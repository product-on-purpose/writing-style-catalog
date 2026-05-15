---
entry_id: one-pager
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Proposal: Async-First Standup Trial

**Author:** Maya Chen, EM Platform | **For:** Priya Raman, Head of Engineering | **Date:** 2026-05-14 | **Decision needed by:** 2026-05-16

## The situation

Platform is 11 engineers across 4 timezones (US Pacific 3, US Eastern 3, UK 2, India 3). The daily 9am Pacific standup is 9:30pm IST. Q1 data:

- Attendance: India 3.2/5, US 4.6/5
- Average length: 14 min; content that changed someone's behavior: 4 min
- Three documented duplicate-work incidents traced to status that was shared verbally and not searchable later

The meeting is paid for by the people who have the least flexibility in their day, and most of what is said is not actionable.

## The proposal

Replace the daily sync standup with an async post in #team-standup by 10am local time, three fields: Shipped, In progress, Blocked or at risk (with @mention). Reclaim the 9am Pacific slot as a 60-minute Thursday working session for discussion that genuinely needs real-time exchange. On-call engineer triages the channel and responds to blockers within 30 minutes during business hours. 30-day trial, day-15 pulse, day-30 go / no-go.

## Why now

- New hires in India onboarding next quarter; the current schedule sets a precedent we should not lock in
- Working session is a forcing function for cross-timezone discussion we have been deferring
- Cost of the change is low (pinned template, no new tooling) and reversible

## What success looks like

| Metric | Today | Day-30 target |
|---|---|---|
| Participation rate (posts / engineers / workday) | 3.9 / 11 | 9+ / 11 |
| Avg synchronous time on status per engineer per week | 70 min | < 15 min |
| Blocker time-to-first-response | not measured | < 30 min business hours |
| Duplicate-work incidents (rolling quarter) | 3 | 0 |

Trial stops at day 30 if participation is below 7/11 or the team votes against continuing.

## Asks

1. **Approve the 30-day trial** starting Monday May 19.
2. **Approve pausing the daily 9am Pacific meeting** for the trial duration.
3. **15-min slot in your week of June 22** to review day-30 results and decide whether to make permanent.

No budget, tooling, or headcount requested. The Thursday working session is on the engineering calendar already.
