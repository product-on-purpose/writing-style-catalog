---
entry_id: diataxis-explanation
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Why Async Standups Work the Way They Do

An async standup is not a standup without the video call. It is a different kind of coordination mechanism, built on different assumptions about when and how information should move.

To understand why the distinction matters, it helps to understand what a standup is actually trying to accomplish. The daily standup has two functions that usually coexist in the same meeting without being separated: status visibility (who is doing what, what is blocked) and team cohesion (the daily ritual of shared presence, the sense of a team operating together). Synchronous standups do both at once because everyone is in the room at the same time. Async standups separate them.

The status-visibility function works differently in async format because information becomes persistent and addressable. In a synchronous standup, a blocker mentioned verbally reaches everyone in the room, but only for the duration of the sentence. The person who can resolve it must remember it, and the people who might have the same problem next must either have been present or get told separately. In an async channel, the same information is posted, searchable, and accessible to anyone on the team regardless of timezone or work schedule. The blocker reaches the right person not because they were present but because they are mentioned directly.

The team-cohesion function does not transfer to async in the same way, and this is why async-only teams sometimes feel fragmented. Daily synchronous standups create what anthropologists call "phatic communion" - interaction whose function is social bonding rather than information transfer. "How's it going?" is not a request for information; it is a gesture of acknowledgment. Async updates can approximate some of this through informal additions to the update template, but a Slack thread is not a room. The teams that sustain cohesion in async-first environments almost always supplement their async standup with a different synchronous ritual - a weekly working session, a monthly retrospective - that exists specifically for the cohesion function that async cannot provide.

The reason async standups often produce higher-quality status information than synchronous ones is cognitive: writing forces more clarity than speaking. A person who says "working on the auth refactor" in a standup has technically satisfied the format. A person writing the same update often notices the vagueness before they post it and adds the detail that makes it useful. The act of writing creates a moment of reflection that verbal turn-taking does not.
