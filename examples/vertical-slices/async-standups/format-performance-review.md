---
entry_id: performance-review
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Performance Review: Maya Reyes

## Period

January 1 to June 30

## Reviewer

Jordan Ashworth, Director of Engineering

## Summary

Maya set out to close a real equity gap in the team's daily rituals and hold operational quality steady while the team scaled from 6 to 11 engineers across four time zones. She closed the equity gap decisively; the operational discipline around the new process needed a production incident to force the fix instead of being planned in from the start.

## Performance Against Goals

### Close the cross-timezone participation gap in daily team rituals

Rating: Met

Maya diagnosed the problem with data before proposing a fix: Q1 data showed India-based engineers averaging 3.2 standups out of 5 per week against 4.6 for US-based engineers, traced to the meeting time - 9am Pacific, 9:30pm IST - not disengagement. She weighed three alternatives in the ADR (rotating the meeting, dropping standup, a paid third-party tool) before replacing the sync meeting with an async post to #team-standup and a weekly Thursday working session, ran it as a scoped 30-day trial, reported progress weekly to me and to peer EMs, and closed it with a retrospective. By the final two weeks, IST-based engineers were posting every weekday for the first time in this team's history, and the team voted to extend the format permanently.

### Hold operational discipline steady while the team scaled from 6 to 11 engineers

Rating: Partially Met

The trial exposed gaps in how the process was operationalized. On Day 11, an @mention flagging a blocked dependency went unanswered through triage because that morning's pass had no dedicated @mention scan and missed it inside one of eleven posts; the blocked engineer escalated by direct message two hours later, and the incident did not fully close until 13:30 Pacific, four hours fifteen minutes after the original post. Triage load ran about 25 minutes per morning against a 10-minute target for most of the trial, and by Week 2 three engineers were posting past 200 words against a three-bullet, 60-second-skim goal. Maya fixed each issue as it surfaced - a dedicated mention scan the next morning, exemplar posts pinned to the channel - but none was accounted for in the original rollout plan.

## Strengths

- Led with data, not instinct: the Q1 attendance split and the meeting's own math - 14 minutes long, roughly 4 minutes of signal - made the ADR read as a decision record, not an opinion piece.
- Ran the change as a bounded, reversible trial with a fixed end date and a named retrospective, so the permanent-adoption vote was a real decision, not a default.
- Treated the Day 11 incident as a process gap to fix, not smooth over: it produced a specific checklist change, adopted before the next triage window.

## Development Areas

- On-call triage capacity was not scoped before launch. The 10-minute target reads as asserted, not tested against an 11-person channel's likely volume, and that gap is what let the Day 11 incident happen. Capacity needs to be planned before rollout, not backfilled after someone is blocked for hours.
- The three-bullet post-length ceiling had no enforcement at launch, only a stated norm - it held for a week, then eroded, the predictable result of a norm with no structural backstop. The fix that shipped - pinned exemplars, a Thursday demo - is a reminder, not a constraint; worth watching into H2.

## Goals for Next Period

- Land the on-call triage decision from the Day 37 checkpoint (split the rotation or time-box the triage pass) and confirm triage time is back near the 10-minute target - by the next retrospective.
- Replace the reminder-based post-length fix with a structural one, such as a bullet limit built into the /standup Slack shortcut - by end of Q3.
- Complete the two-session Thursday attendance check committed to at the Day 30 retro, and bring the team a proposal if IST attendance falls below 3 of 4 - by the next retrospective.

## Overall Rating

Meets Expectations

## Additional Notes

The standup trial is unusually well-documented for a mid-year cycle: the ADR, the weekly status reports, and the retrospective form a paper trail I would support using in a promotion packet if this rigor holds through H2. The open question is not whether Maya can make a good structural call. It is whether she builds the operational guardrails in at launch, not after the first incident forces them.
