---
diff_pair_id: format-adr-vs-prd-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: adr
entry_b: prd
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `adr` vs `prd`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `adr` - A short structured document that captures a significant architectural decision, its context, and its consequences.
**B:** `prd` - A structured document that defines what a product or feature should do, for whom, and why - without specifying how to build it.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `adr`

# ADR-0014: Adopt Async-First Standup Format

## Status

Accepted

## Context

The engineering team has grown from 6 to 11 engineers over 18 months. The team now spans four timezones: US Pacific (3 engineers), US Eastern (3 engineers), UK (2 engineers), India (3 engineers). The current synchronous standup is scheduled at 9am Pacific, which is 9:30pm India Standard Time.

Three forces pushed this decision:

**Timezone asymmetry.** The India-based engineers are disproportionately burdened by the meeting schedule. Attendance data from Q1 shows the three India engineers averaged 3.2 standup appearances per week out of 5, compared to 4.6 for US-based engineers. The shortfall is not disengagement - it is 9:30pm.

**Information loss.** Status shared verbally in the meeting does not persist. We have documented three incidents in the past quarter where an engineer spent more than an hour on a problem that had already been solved and discussed in a previous standup. There is no searchable record.

**Meeting-to-value ratio.** The standup averages 14 minutes. Analysis of the past month shows an average of 4.2 minutes of content that changed someone's behavior - a blocker raised, a dependency flagged, a context shared. The remaining 10 minutes is status that required no response from anyone.

Alternatives considered: rotating the meeting time (solves equity but adds overhead and still does not create persistence), eliminating standup entirely (loses coordination value), and adopting an async tool like Geekbot (rejected on cost and added tooling complexity - Slack templates serve the same function).

## Decision

Replace the synchronous daily standup with an async standup update in #team-standup. Engineers post by 10am their local time using a pinned template:

- **Shipped:** what completed in the last 24 hours
- **In progress:** current focus
- **Blocked / at risk:** anything that needs attention, with @mention of the person who can resolve it

The on-call engineer reads the channel by 9am Pacific and responds to blocked items within 30 minutes during business hours. The synchronous standup slot is replaced with a 60-minute Thursday working session - not a status meeting, reserved for discussion requiring real-time exchange.

## Consequences

### Positive

- All engineers participate on a schedule that fits their timezone
- Status information is persistent and searchable
- Blocked items route directly to the person who can resolve them via @mention
- Engineers recover 70 minutes per week previously spent in synchronous status reporting

### Negative

- Social cohesion that comes from shared daily presence is reduced; the Thursday session is a partial substitute but not equivalent
- The format depends on consistent participation - if engineers stop posting, the channel's value drops for everyone
- Blockers that require nuance are harder to surface in a structured three-field template than in a live conversation

### Neutral

- On-call rotation adds a daily channel-reading responsibility, but this replaces the meeting facilitation responsibility previously on the same rotation
- The Thursday working session is new overhead for some engineers who previously skipped standup

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
