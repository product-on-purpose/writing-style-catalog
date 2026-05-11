---
entry_id: pragmatic-architect
axis: voice
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

We should move to async-first standups. The synchronous daily standup has two failure modes we are currently experiencing: attendance friction (timezone spread from UTC-8 to UTC+5 means someone always joins at an awkward hour), and low information density (the 15-minute call routinely delivers 3 minutes of actual signal).

The constraint that makes this decision is team composition, not preference. We have 11 engineers across 4 timezones. A synchronous standup that works for all of them requires either a very early slot for the west coast or a late slot for India. Either way, someone bears a cost that accumulates over months.

The failure mode of async standups is different: staleness and inconsistency. If the format is "post what you did yesterday," the responses drift toward summaries that exclude blockers. The mitigation is a structured prompt, not a free-form text field. Three questions, answered in Slack by 10am local time: what shipped, what is in flight today, what is blocked or at risk. The on-call engineer reads and responds to blockers within 30 minutes.

What this does not solve is the social cohesion function of standups. Some teams use daily standup as the only ritual that creates a sense of shared presence. If that describes your team, a full async switch will hurt morale in ways that will not show up in engineering metrics for two or three months. The mitigation is a weekly synchronous touchpoint - not a standup, a working session - where presence is real and the agenda is not status.

My recommendation: run the async format for 30 days with a structured Slack template. Track blocker response time and self-reported friction. At 30 days, decide whether to extend or revert. The revert path is low cost. The experiment is worth running.
