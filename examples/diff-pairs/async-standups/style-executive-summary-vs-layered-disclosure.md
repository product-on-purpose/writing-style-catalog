---
diff_pair_id: style-executive-summary-vs-layered-disclosure-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: style
entry_a: executive-summary
entry_b: layered-disclosure
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `executive-summary` vs `layered-disclosure`

**Topic:** Should we adopt async-first standups?
**Axis varied:** style
**A:** `executive-summary` - Inverted-pyramid writing for decision-makers - recommendation first, supporting analysis second, structured so that stopping after paragraph one still leaves the reader equipped to act.
**B:** `layered-disclosure` - Progressively reveals depth - the first paragraph serves the casual reader completely, and each subsequent section adds detail for those who want it.

## What to notice

Both examples address the same topic and (by default) share every axis other than style. 
The only deliberate variable is which style the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The style 
swap is the entire cause of those differences.

---

## A: `executive-summary`

# Executive Summary: Async Standups for the Platform Team

**Recommendation: Adopt async-first standups for the 11-person Platform team, on a 30-day trial starting next Monday, with explicit revert criteria.** This change is low-risk, reversible, and addresses a measurable inequity in the current schedule. No additional headcount or tooling is required.

## Situation

The team spans four timezones: US Pacific (3), US Eastern (3), UK (2), India (3). The current daily standup runs at 9am Pacific, which is 9:30pm in India. Q1 attendance shows India engineers averaged 3.2 of 5 weekly standups; US-based engineers averaged 4.6. The meeting runs 14 minutes on average. Roughly 4 minutes drives any concrete action. Information shared verbally does not persist, and engineers are repeatedly re-diagnosing problems already solved by teammates earlier in the day.

## Proposed change

Replace the synchronous daily standup with a structured async update in `#team-standup`. Each engineer posts by 10am local time with three fields: Shipped, In progress, Blocked or at risk. Blocked items @mention the unblocker. The reclaimed 9am Pacific slot becomes a 60-minute Thursday working session for discussions that require real-time exchange.

## Expected impact

- Attendance inequity disappears. India engineers post during their workday rather than their evening.
- Status becomes searchable. The recurring cost of re-diagnosing solved problems goes down.
- Blockers route to the right person via @mention rather than relying on meeting attendance.
- Aggregate meeting time per engineer drops from roughly 70 minutes per week to roughly 60 minutes per week, with a higher fraction of that time spent on substantive work.

## Risks

Two risks are worth naming. First, an async channel can become noise if posts are unstructured. The fixed three-field template addresses this. Second, some engineers prefer the social aspect of the sync standup. The Thursday working session preserves a real-time touchpoint without daily cost.

## Decision criteria

After 30 days, the trial extends if at least two of three indicators are positive:

1. Median blocker resolution time during overlap windows is under 2 hours.
2. At least 9 of 11 engineers post at least 4 of 5 weekdays.
3. Team survey shows equal or better context on teammates' work than under the sync model.

If two of three are negative, revert and document the failure mode.

## Cost

Zero direct cost. Roughly 2 hours of lead time to set up the channel, pin the template, cancel the sync invite, and announce the trial.

---

## B: `layered-disclosure`

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
