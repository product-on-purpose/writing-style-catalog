---
entry_id: adr
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

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
