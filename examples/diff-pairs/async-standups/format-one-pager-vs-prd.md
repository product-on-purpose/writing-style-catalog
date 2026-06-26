---
diff_pair_id: format-one-pager-vs-prd-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: one-pager
entry_b: prd
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `one-pager` vs `prd`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `one-pager` - A single-page document that makes one argument or presents one situation. The page constraint is the discipline - everything that does not fit does not belong.
**B:** `prd` - A structured document that defines what a product or feature should do, for whom, and why - without specifying how to build it.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `one-pager`

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

---

## B: `prd`

# Async Standup Bot - Product Requirements

## Problem Statement

Engineering teams using Slack for team communication have no structured way to run async standups within the tool they already use. Current approaches require either a separate SaaS product (Geekbot, Standuply), which adds cost and context-switching, or a manual template posted to a channel, which requires someone to enforce the format and generates no structured data. Teams that need to review standup history, track blocker patterns, or report on team activity cannot do so without manually reading thread-by-thread.

The users who feel this most are engineering managers and team leads at companies with distributed teams (at least two timezones). They run standups daily. They need blockers to surface and resolve without requiring a meeting. They cannot afford a per-seat SaaS subscription for a feature they could implement natively.

## Goals

- Enable any Slack workspace to run structured async standups with no external tool
- Reduce time-to-resolution for blockers by routing them to the named person via direct @mention
- Produce a structured weekly digest that engineering leads can use for 1:1 and planning prep
- Support teams of 4 to 50 engineers without configuration complexity

## Non-Goals

- This release does not replace synchronous standup tooling (Zoom, Meet integrations)
- This release does not include time-tracking or sprint velocity metrics
- This release does not support custom standup prompts in v1 - the three-field template is fixed
- This release is not intended for non-engineering teams (sales, marketing standup formats are different)

## User Stories

- As a team lead, I want to configure a standup channel and prompt schedule once so that I am not manually reminding my team to post each day
- As an engineer, I want to post my standup update in a format that takes less than two minutes so that the daily ritual does not feel like overhead
- As an engineer with a blocker, I want my blocker to reach the specific person who can help so that I am not waiting for them to notice it in a channel they may not read attentively
- As a team lead, I want a weekly summary of standup activity so that I can see blocker patterns and prepare for 1:1s without reading 50 individual posts

## Success Metrics

- Average time from blocker posted to first response from @mentioned person: target under 30 minutes during business hours
- Daily participation rate: target 85% of team posts on any given weekday
- Setup time: a team lead can configure and launch a standup channel in under 10 minutes
- Weekly digest open rate: target 70% of team leads open the digest within 24 hours of delivery

## Open Questions

- Does the bot need to handle engineers across more than two timezones in a single team? If so, how does the "post by 10am local" constraint work when "local" varies by 13 hours?
- Should the bot send direct reminders to engineers who have not posted by their deadline, or only post a channel reminder?
- What happens when someone is out of office - does the bot need OOO awareness, or does the team handle this manually?
- Is there a meaningful integration with GitHub or Jira that would let the bot pre-populate the "shipped" field from closed PRs or resolved tickets?
