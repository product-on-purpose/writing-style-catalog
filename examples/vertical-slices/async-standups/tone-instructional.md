---
entry_id: instructional
axis: tone
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How the async standup works, starting Monday

Starting Monday, we are running a 30-day trial of async standups in place of the 9am Pacific sync meeting. This guide explains what is changing, what you need to do, and how to recognize a well-formed update. Read it once, then refer back as needed.

## What is changing

**Sync standup** (the daily 9am Pacific call) is paused for 30 days.

**Async standup** is a written daily update posted in `#team-standup`. "Async" here means there is no shared meeting time - each engineer posts on their own schedule within a window.

**Working session** is a new 60-minute Thursday slot in the same calendar block. This is for real coordination work, not status. Agenda will be posted Wednesday.

## What you need to do

1. **Post your update in `#team-standup` by 10am local time each working day.** Local means your local time, not Pacific. If you are in Bengaluru and start work at 9am IST, you post by 10am IST.
2. **Use the three-field format.** Each update has exactly three sections:
   - **Shipped:** What you completed since your last update. Link the PR or doc.
   - **In progress:** What you are working on today. One or two items, not a backlog dump.
   - **Blocked or at risk:** Anything that needs help. If empty, write "None."
3. **@mention the unblocker on every blocker.** A blocker without a name attached is not actionable. If you are not sure who to mention, mention your lead and they will route it.
4. **Read the channel once per day.** You do not need to read every update, but scan for @mentions of you and for blockers in your area.

## What a good update looks like

> **Shipped:** Auth retry logic merged (#4412).
> **In progress:** Migrating session cache to Redis, expect PR by EOD.
> **Blocked:** Need staging access for new region - @priya.

That is a complete update. Three lines, specific, one named owner on the blocker.

## What we are measuring

At day 30 we will review three things: blocker resolution time, participation rate across timezones, and whether the Thursday session is delivering coordination value. We will decide together whether to keep the format, revert, or adjust.

Questions go in the thread under Monday's kickoff post.
