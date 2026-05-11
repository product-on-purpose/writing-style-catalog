---
entry_id: operator
axis: voice
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Here is what happens at 9am on a bad standup day. Three engineers have been working since 7am. Two engineers are on the west coast and join 10 minutes late. The engineer on-call from last night's incident is barely conscious. Someone starts talking about their PR. Nobody asks about the deploy that broke the staging environment at 8:45. The meeting ends at 9:17. At 9:30, @sam pings @alex to ask if the staging issue is known. It was. Nobody said so.

That is not an edge case. That is Tuesday.

The coordination failure is not that standups are bad. It is that synchronous standups do not wait for the right people to be present, and they do not persist the information in a findable place. The on-call handoff note from 8am is in a Slack thread. The PR status is in GitHub. The staging issue is in someone's head. The standup adds a fourth place where information lives, briefly, before evaporating.

Async standup in Slack fixes the evaporation problem. The update is there. @prasad posted at 8:15 India time that the deploy is blocked on a config change. @sam reads it at 9am Pacific and responds in thread. The blocker is resolved before the standup would have even started.

The setup: post to #team-standup by 10am local. Three fields - shipped, in progress, blocked. Anything blocked requires a @mention of the person who can unblock it. On-call reads the channel daily by 9am Pacific and responds to blocked items within 30 minutes.

What this does not fix: people who do not read the channel. You still need someone to own that. Set a reminder in the channel. Make it a team norm. Check the receipts.
