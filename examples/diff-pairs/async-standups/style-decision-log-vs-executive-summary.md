---
diff_pair_id: style-decision-log-vs-executive-summary-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: style
entry_a: decision-log
entry_b: executive-summary
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `decision-log` vs `executive-summary`

**Topic:** Should we adopt async-first standups?
**Axis varied:** style
**A:** `decision-log` - A real-time record of context, options considered, criteria used, and reasoning - capturing how a decision was reached, not justifying it after the fact.
**B:** `executive-summary` - Inverted-pyramid writing for decision-makers - recommendation first, supporting analysis second, structured so that stopping after paragraph one still leaves the reader equipped to act.

## What to notice

Both examples address the same topic and (by default) share every axis other than style. 
The only deliberate variable is which style the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The style 
swap is the entire cause of those differences.

---

## A: `decision-log`

# Decision: 2026-Q2 Standup Format

**Status:** Decided
**Date:** 2026-04-08
**Owner:** Lina Acosta (Platform Eng Manager)
**Stakeholders:** Platform team (11 engineers); Head of Engineering (informed, not approving)

## Context

The Platform team is 11 engineers across four timezones: US Pacific (3), US Eastern (3), UK (2), India (3). The current synchronous daily standup runs at 9am Pacific, which is 9:30pm IST for the three India-based engineers.

Two recurring problems are now well-evidenced rather than anecdotal:

1. **Attendance inequity.** Q1 attendance data: India engineers averaged 3.2 of 5 weekly standups; US-based engineers averaged 4.6. The gap correlates with the meeting time, not with the engineers.
2. **Information loss.** Standups run 14 minutes on average. Roughly 4 minutes drive concrete action. The remainder is verbal status that does not persist. We have multiple recent instances of engineers re-diagnosing problems that teammates solved earlier the same day. The most concrete: a 401 auth fix discussed in standup on March 3, then re-diagnosed by a different engineer on March 4 because they were not on the call.

The status quo is not free. It is paid disproportionately by the India engineers and intermittently by anyone who misses a meeting.

## Options Considered

### Option A: Keep the current sync standup

Cost concentrated on India team. Information loss continues. No change required, no risk introduced.

### Option B: Rotate the standup time weekly across timezones

Spreads the inequity rather than removing it. Calendar churn for everyone. Still does not solve the information persistence problem.

### Option C: Two sync standups (Americas + Europe/India)

Splits the team into two information silos. Doubles the meeting load on anyone bridging both. Cross-region context gets worse, not better.

### Option D: Async-first standup with weekly sync working session

Eliminates the timezone tax. Creates a searchable record. Preserves a real-time slot for discussion that benefits from it. Requires behavior change.

### Option E: No standup at all

Lowest meeting cost. Highest information cost. Rejected without serious consideration; the team is not co-located enough to absorb the loss of any structured status mechanism.

## Criteria

The decision is being made against these criteria, in priority order:

1. **Equity across timezones.** No single timezone should bear a disproportionate share of off-hours meeting cost.
2. **Information persistence.** Daily status should be searchable, not ephemeral.
3. **Blocker resolution speed.** Blocked items should route to the right person quickly.
4. **Real-time bandwidth preserved.** The team still needs occasional real-time exchange for hard problems.
5. **Reversibility.** Whatever we choose should be revertible within a sprint if it does not work.

## Decision

**Adopt Option D for a 30-day trial starting 2026-04-13.**

Specifics:

- Daily async post in `#team-standup`, three fields: Shipped, In progress, Blocked or at risk. Posted by 10am local time. Blockers @mention the unblocker.
- 9am Pacific sync slot becomes a 60-minute Thursday working session.
- Day 15 informal check-in. Day 30 formal evaluation against success criteria.

### Success criteria at day 30

The trial extends if at least two of three are positive:

1. Median blocker resolution time during overlap windows under 2 hours.
2. At least 9 of 11 engineers posting at least 4 of 5 weekdays.
3. Team survey shows equal or better context on teammates' work versus the sync model.

If two of three fail, revert to a rotating-time sync standup (not the current fixed time, which is the worst option).

## Reasoning

Option D scores best on criteria 1, 2, and 3, neutral on 4, and equivalent to most other options on 5. Option A scores poorly on 1 and 2. Options B and C reduce one cost while introducing a new one. Option E is dominated by D on every criterion except meeting count, which is not in our top five.

The deciding factor was criterion 1. The current attendance gap is not a behavior problem; it is a schedule problem. Once we accepted that, the options that preserved the schedule were no longer viable.

## Open Questions

- Does the Thursday working session need a standing agenda template, or is a free-form shared doc sufficient? Defer to day 15 check-in.
- Should "Blocked or at risk" be split into two fields? Some engineers may underreport "at risk" items. Defer to day 30 review.
- If we revert, what is the rotating-time schedule? Owner: Lina. Due before day 30 in case revert is needed.

---

## B: `executive-summary`

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
