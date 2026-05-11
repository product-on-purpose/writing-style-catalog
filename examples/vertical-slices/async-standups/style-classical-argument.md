---
entry_id: classical-argument
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Distributed teams should replace synchronous daily standups with async standup updates. The synchronous format was designed for co-located teams and imposes costs that distributed teams bear unevenly, while delivering most of its value in a form that does not require shared presence.

**The grounds**

The primary purpose of a daily standup is status visibility: making blockers known, making progress visible, and surfacing coordination needs before they become delays. A survey of engineering teams at GitLab, where async-first work is documented extensively, found that async standup formats reduced blocker-to-resolution time compared to synchronous equivalents - not because the meetings were bad, but because async channels produce written records that route information to the right person directly, independent of who attended a meeting.

The secondary cost of synchronous standups in distributed teams is timezone asymmetry. In a team spread across four timezones, the meeting time is convenient for some and inconvenient for others. The inconvenience is not random - it concentrates on the engineers whose location is furthest from the timezone anchor of the rest of the team. Over a year, an engineer joining standups at 9pm local time has absorbed hundreds of hours of scheduling friction that their co-located colleagues have not.

**The warrant**

This evidence supports the claim because the value of status visibility is in the information being accessible, not in the information being spoken aloud at a shared moment. If information in a Slack channel is as accessible as information spoken in a meeting - and for distributed teams it is more accessible, because it is persistent and searchable - then the synchronous meeting is adding no incremental value over the async format while still imposing the timezone cost.

**The rebuttal**

One might object that synchronous standups build social cohesion that async formats cannot replicate, and that cohesion has downstream effects on collaboration quality. This objection is correct. Shared presence does create connection that text in a channel does not. The response is that this function can be addressed through a different format - a weekly synchronous working session - rather than preserved in a daily status meeting that is a poor vehicle for social bonding. Retaining the daily synchronous standup for its cohesion value is the wrong tool for the job it is being asked to do.

Distributed teams should move to async standup formats and invest the recovered synchronous time in working sessions that can actually build the relationships that standups were never designed to build.
