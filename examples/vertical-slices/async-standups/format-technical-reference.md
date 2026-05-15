---
entry_id: technical-reference
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Platform Standup Format Reference

**Applies to:** eng-platform team (11 engineers, 4 timezones)
**Channel:** #team-standup
**Status:** Trial - effective 2026-05-19 through 2026-06-19
**Owner:** Maya Chen (EM Platform)

## 1. Posting template

Post once per workday in #team-standup. Copy the pinned message and fill in.

```
*Shipped*
- <item>

*In progress*
- <item>

*Blocked / at risk*
- <item, with @mention of who can resolve>
```

If a section is empty, write `- none`. Do not omit the heading.

## 2. Field definitions

| Field | Includes | Excludes |
|---|---|---|
| Shipped | Work merged, deployed, or otherwise complete in the last 24h | Work in review; planning; meetings attended |
| In progress | Current focus through your next workday | Backlog; speculative work; "thinking about X" |
| Blocked / at risk | Anything where someone else's input changes your day, plus things trending late | Vents; status with no ask; non-actionable FYI |

A blocker requires three things: what is blocked, who can unblock, when you need it. `@user, can you review #4412 today?` is a blocker. `Reviews are slow.` is not.

## 3. Timing rules

| Rule | Value |
|---|---|
| Post by | 10:00 your local time |
| On-call triage by | 09:00 Pacific |
| Blocker first-response SLA | 30 min during business hours of the resolver |
| Backfill window for missed post | Same day, until 17:00 local |

If you will not be at a keyboard before 10am local (early meeting, school run, travel), post the previous evening with a `tomorrow:` prefix on In progress.

## 4. Blocker escalation

```
day 0 (post)        - @mention the resolver in your update
+4 business hours   - on-call engineer nudges the resolver in-channel
+1 business day     - on-call escalates to the resolver's manager
+2 business days    - escalates to Maya
```

Mark a blocker resolved by editing your original post or replying in-thread with `resolved:` and the outcome. Do not delete the line - the searchable record is part of the point.

## 5. Edge cases

### PTO
Post one line on your last working day: `OOO <date range>, back <date>. Coverage: @user.` Do not post during PTO.

### On-call
On-call engineer posts as normal plus a fourth line: `*On-call:* responding to pages, async post may be late.` On-call days do not count against participation metrics.

### Partial week / holidays
Post on the days you work. On a public holiday for your locale, skip without notice.

### No update to give
Post anyway. `Shipped: none. In progress: <thing>. Blocked: none.` Silence is harder to interpret than a thin update.

### Heads-down / deep work day
Post as normal. The five minutes it takes is the price of the team knowing where you are. If you genuinely cannot context-switch, post the night before.

### Sensitive items
If a blocker involves a person issue or anything confidential, post `Blocked: DMing @maya` and handle in DM. Do not name the person in-channel.

## 6. Metrics tracked

Pulled weekly by Priya from #team-standup history.

| Metric | Definition | Target |
|---|---|---|
| Participation rate | Posts / engineers / workday | >= 9/11 |
| Blocker response time | Time from post to first substantive reply | < 30 min business hours |
| Stale blockers | Blockers open > 2 business days | 0 |

## 7. Related

- Trial proposal: `docs/proposals/async-standup-trial.md`
- Thursday working session charter: `docs/eng-platform/thursday-session.md`
- ADR-0014: Adopt async-first standup format
- Day-15 pulse and day-30 review: calendar invites from Maya
