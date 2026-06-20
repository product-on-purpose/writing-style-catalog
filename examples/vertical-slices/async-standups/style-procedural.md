---
entry_id: procedural
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to roll out an async standup in your team

This guide walks a team lead through replacing a synchronous daily standup with an async update across four timezones. It is written for a lead running an 11-person engineering team distributed across US Pacific, US Eastern, UK, and India.

## Prerequisites

Before you start, confirm the following:

- Your team has a shared Slack workspace (or equivalent) where you can create a dedicated channel.
- You have a recurring sync meeting slot you can repurpose. You will not delete it - you will reuse the time.
- You have at least two weeks of attendance data showing the cost of the current schedule. This makes the case if anyone resists.
- Your manager is informed. Async standups are not controversial, but they look like a meeting being cancelled, and that is a thing managers like to know.

## Steps

### 1. Create the channel

Create `#team-standup` in Slack. Set the channel description to: "Daily async standup. Post by 10am your local time. Three fields: Shipped, In progress, Blocked or at risk."

### 2. Pin the template

Pin a message to the channel with the exact three-field template:

```
Shipped: [what merged or shipped in the last 24h]
In progress: [what you are working on today]
Blocked or at risk: [what is stuck, @mention who can unblock]
```

A pinned template removes the need for anyone to remember the format.

### 3. Announce the 30-day trial

Post in the team channel that the team will run async standups for 30 days, with a revert option. Name the start date. Name the success criteria: blocker resolution time, channel engagement, team survey.

### 4. Cancel the daily sync

Cancel the recurring 9am Pacific standup on the calendar. Do not just stop attending. Cancelling the invite signals the change is real.

### 5. Create the Thursday working session

Add a recurring 60-minute Thursday meeting at a time that works for all four timezones. This is your new sync slot. Use it for discussion that needs real-time exchange.

### 6. Post first, ask others second

On day one, post your own update by 9am Pacific before anyone else. Modeling is faster than instructing.

### 7. @mention blockers explicitly

When you see a blocked item without an @mention, reply in thread and ask who owns it. Do this for the first week. After that the pattern is self-sustaining.

## Confirming it worked

After 30 days, check three things:

- Median time from "Blocked" post to first reply from the unblocker. Target: under 2 hours during overlap windows.
- Number of team members posting at least 4 of 5 weekdays. Target: 9 of 11.
- A short survey: "Do you have more or less context on what your teammates are doing than 30 days ago?"

If two of three are positive, keep the change. If two of three are negative, revert and write up what you learned.
