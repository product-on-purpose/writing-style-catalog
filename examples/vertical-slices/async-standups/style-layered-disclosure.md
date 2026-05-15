---
entry_id: layered-disclosure
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Async-first standups for the Platform team

## TL;DR

We are proposing a 30-day trial replacing the daily 9am Pacific standup with an async post in `#team-standup`, three fields (Shipped, In progress, Blocked or at risk), posted by 10am local time. The current schedule disadvantages our three India engineers (9:30pm IST), and verbal status does not persist. The trial is reversible. If two of three success criteria fail at day 30, we revert.

**If you only read this section, the action item is: react with a thumbs-up on this doc by Friday to greenlight the trial.**

## Why we are proposing this

The Platform team is 11 engineers across four timezones: US Pacific (3), US Eastern (3), UK (2), India (3). Two specific facts matter.

First, Q1 attendance: India engineers averaged 3.2 of 5 weekly standups; US-based engineers averaged 4.6. The meeting at 9am Pacific is 9:30pm IST, which competes with family time.

Second, the meeting averages 14 minutes and roughly 4 of those minutes drive any concrete action. The rest is status that does not persist. We have a recurring problem where engineers re-diagnose issues that teammates already solved earlier in the day.

## What changes

Three things change:

- **The daily sync standup is cancelled.**
- **A daily async post in `#team-standup` replaces it.** Three fields - Shipped, In progress, Blocked or at risk. Posted by 10am local time. Blocked items @mention the person who can unblock.
- **The 9am Pacific slot becomes a 60-minute Thursday working session**, reserved for discussion that genuinely requires real-time exchange.

## How we will know if it worked

At day 30, we evaluate three criteria:

1. **Blocker resolution time.** Median time from a "Blocked" post to first reply from the unblocker during overlap windows. Target: under 2 hours.
2. **Posting consistency.** At least 9 of 11 engineers posting on at least 4 of 5 weekdays.
3. **Team perception.** A short survey: do you have more or less context on teammates' work than 30 days ago?

If two of three are positive, we keep the change. If two of three are negative, we revert and write up the failure mode.

## Full mechanics (for engineers who will actually run this)

The channel template, pinned to `#team-standup`:

```
Shipped: [merged/shipped in last 24h]
In progress: [today]
Blocked or at risk: [@mention who can unblock]
```

Operational details:

- **Posting window.** By 10am local time. We are deliberately not requiring a specific UTC time. Local time tracks your workday.
- **Empty fields are allowed.** "Shipped: nothing yet" is a valid post. Pretending you shipped something to satisfy the format is worse than honesty.
- **Blockers route via @mention, not via the channel at large.** If you @mention nobody, the blocker has no owner.
- **Thursday working session agenda.** Items get added to a shared doc throughout the week. If the doc is empty by Wednesday EOD, the meeting is cancelled.
- **Day-15 check-in.** Lina sends a one-question Slack poll: "On track to keep this?" If responses skew negative, we course-correct early rather than waiting for day 30.
- **Revert procedure.** If we revert, the sync standup returns at a rotating time so that no single timezone always carries the cost. This is a worse outcome than the trial succeeding, but better than the current setup.

## Risks and what we are doing about them

- *Channel becomes noise.* Mitigated by the fixed three-field template.
- *Social cohesion drops.* Mitigated by the Thursday working session and an unchanged weekly team lunch.
- *Some engineers do not post.* Mitigated by Lina modeling on day one and explicit follow-ups in week one.

If you have other risks in mind, drop them in this doc as comments. We will respond before Friday's go decision.
