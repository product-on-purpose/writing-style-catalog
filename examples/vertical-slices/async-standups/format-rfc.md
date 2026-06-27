---
entry_id: rfc
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# RFC-0012: Switch to Async-First Standup

## Status

Under Review

## Author(s)

Engineering Manager - opened for review after Q1 retrospective

## Problem

Our current synchronous daily standup is a 9am Pacific meeting that all 11 engineers are expected to attend. The team has grown from 6 to 11 engineers over the past 18 months and now spans four timezones: US Pacific, US Eastern, UK, and India. That scheduling arithmetic does not work.

For our three India-based engineers, 9am Pacific is 9:30pm IST. Q1 attendance data confirms the effect: India engineers averaged 3.2 standup appearances per week out of 5; US-based engineers averaged 4.6. The shortfall is not disengagement. It is a timezone that makes a nightly meeting unsustainable.

Beyond the equity problem, the meeting produces little durable output. The standup averages 14 minutes. Analysis of the past month puts the content that changed someone's behavior at roughly 4.2 minutes - a blocker raised, a dependency flagged, a context shared. The other 10 minutes is status that required no response from anyone. And even the useful 4.2 minutes disappears afterward: nothing is written down, nothing is searchable. In Q1 we documented three incidents where an engineer spent more than an hour on a problem that had already been discussed in a previous standup.

The problem is not that people are attending badly. The problem is that we designed a synchronous meeting for a team that is no longer synchronous.

## Proposed Approach

Replace the daily synchronous standup with an async update posted to `#team-standup` by 10am each engineer's local time.

The template would be three fields:

- **Shipped:** what completed in the last 24 hours
- **In progress:** current focus
- **Blocked or at risk:** anything that needs attention, with @mention of the person who can resolve it

The on-call engineer reads `#team-standup` once between 10am and 11am Pacific and responds to any blocked items within 30 minutes during business hours. On-call rotation stays the same - the responsibility shifts from running the meeting to monitoring the channel.

The 9am Pacific standup slot gets repurposed rather than eliminated. I am proposing a 60-minute Thursday working session in its place - explicitly not a status meeting, reserved for topics that need real-time exchange. If there is nothing on the agenda by Wednesday evening, we cancel.

Before committing permanently, I propose a 30-day trial starting from a date the team agrees on, with a retro at the end to decide whether to make the change permanent.

## Alternatives Considered

**Rotate the standup time.** We could change the meeting time each week or each sprint to distribute the timezone burden more fairly. This addresses the equity problem but does not solve information persistence, and adds scheduling overhead on a team already managing cross-timezone calendar complexity. The India engineers still get a late-evening meeting every few weeks.

**Eliminate standup entirely.** The meeting is low-signal, so one response is to stop having it. I am not proposing this because some coordination value does persist - the "blocked" information in particular needs a home. The proposal preserves that signal while removing the synchronous overhead.

**Adopt a purpose-built async standup tool (Geekbot or similar).** Several tools automate async standup collection with reminders and digest formatting. I looked at Geekbot. The cost and the additional tooling layer did not seem worth it when Slack templates can serve the same function at zero marginal cost. If the Slack-native approach proves too manual to sustain, a dedicated tool is worth revisiting.

**Keep the meeting and add a writeup requirement.** Require engineers to post a written summary after the standup to address the persistence problem. This stacks more process on the existing burden rather than replacing it, and still does not solve the 9:30pm IST problem.

## Open Questions

**What is the right posting deadline?** I proposed 10am local time, but I am not confident this works for every timezone. For UK engineers, 10am GMT means their posts arrive before the Pacific team is at their desks. Does that matter for coordination? Is there a structure - a window rather than a hard cutoff - that serves both IST and UK engineers better?

**How do we prevent the Thursday session from becoming a second standup?** My intent is a working session for topics that require real-time exchange, not a status meeting with a different name. What guardrails would actually hold for this team? Should we require a written agenda at least 24 hours in advance?

**What does "trial succeeded" look like?** 30 days is a guess, and I do not have clear criteria for what we would need to see before committing. Should we set participation-rate targets? Blocker resolution time? I want us to agree on the decision criteria before we start the trial, not after.

**How much does the on-call monitoring role actually cost?** I am estimating 10 to 15 minutes per morning to scan the channel and handle mentions. That estimate might be too low, especially in the first weeks when blockers are more likely to surface through an unfamiliar format. I would rather know that before locking in the on-call spec.

## Consequences

If accepted:

**Benefits:** India-based engineers participate on a schedule that fits their timezone. Status information persists and is searchable, which addresses the duplicate-work incidents from Q1. Blocked items route directly via @mention rather than surfacing verbally in a meeting no one can search later. Engineers recover the time previously spent in synchronous status reporting.

**Costs:** Some social cohesion from daily shared presence is reduced. The Thursday session is a partial substitute but not an equivalent. The format depends on consistent participation - if engineers stop posting, the channel's value drops for everyone. Blockers requiring nuanced discussion may be harder to surface through a three-field template than through a live conversation.

**If rejected:** The current format continues to impose a 9:30pm IST obligation on three engineers. That is the strongest argument for changing something, even if this specific proposal is wrong. If reviewers reject this approach, I am asking for a counter-proposal rather than a return to the status quo.
