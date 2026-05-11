---
entry_id: comparison-contrast
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

We are comparing synchronous daily standups against async standup updates across four dimensions: participation equity, information persistence, blocker resolution speed, and team cohesion.

**Participation equity**

*Synchronous:* A fixed meeting time requires all participants to be available at the same moment. For distributed teams, this means someone is always accommodating an inconvenient hour. The cost is not shared equally - it accumulates on the people furthest from the meeting's timezone anchor.

*Async:* Each participant posts on their own schedule within a defined window (typically "by 10am local time"). No one bears a timezone penalty. Part-time team members and contractors with flexible hours participate without negotiating a slot.

**Information persistence**

*Synchronous:* Information shared verbally in a meeting exists in the memory of whoever was present. A critical piece - "the auth service is throwing a 401 on the `/validate` endpoint" - survives only as long as the listener's memory or their notes. It is not searchable. It does not reach engineers who were absent.

*Async:* Every update is a written record in a searchable channel. An engineer who joins the team three weeks later can read back through updates to understand what the team has been working on. Blockers and solutions are findable.

**Blocker resolution speed**

*Synchronous:* A blocker reaches the person who can resolve it only if that person attended the meeting and noted the item. Routing to the right person depends on the right person being present.

*Async:* A blocker can include a direct @mention of the person who can resolve it. The notification reaches them regardless of whether they would have attended a meeting.

**Team cohesion**

*Synchronous:* Shared presence at a defined moment creates a daily ritual of togetherness. The meeting's social function - brief acknowledgment, casual connection - builds team fabric that is hard to replicate asynchronously.

*Async:* Updates are text on a screen. The social bonding that synchronous presence creates does not transfer. Teams that switch fully to async without a synchronous substitute often feel more fragmented over time.

**Verdict:** Async standups outperform synchronous on participation equity, information persistence, and blocker routing. They underperform on social cohesion. The practical answer for most distributed teams is async standup plus a weekly synchronous working session - not an either/or.
