---
entry_id: definitional
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# What an async-first standup is

**Definition.** An async-first standup is a daily team ritual in which each member posts a short, structured status update in a shared written channel during their own working hours, with the explicit expectation that no synchronous meeting will replace or repeat the post. The post is the standup. The channel is the room. The artifact persists.

That definition does work. It rules out several things that get called async standups but are not.

## What it is not

**It is not a sync standup that some people skip.** A team that has a 9am Pacific meeting and tells the Bangalore engineers "just post in Slack if you cannot make it" does not have an async standup. It has a sync standup with a second-class participation tier. The default is still the meeting. The text post is a fallback.

**It is not a status report sent to a manager.** A status report flows upward to one reader. The async standup flows laterally to a team that reads each other. The audience is the difference.

**It is not "we use Slack." Tool is not format.** A team can run a Slack-native async standup or a Notion-native one or a Linear-native one. The defining property is the structure of the ritual, not the surface it appears on.

**It is not the absence of synchronous contact.** Most teams running async standups still meet synchronously, for retros, planning, demos, or weekly social calls. Going async on the daily standup does not mean going async on everything.

## The required facets

Three properties have to be present for the definition to hold.

1. **A fixed structure.** The team agrees on the fields. For this team: yesterday, today, blockers. Three fields, not three paragraphs. Structure makes the post scannable and reduces the cognitive load of writing it.

2. **A posting window, not a posting moment.** "By 10am local" is a window. "At 9am sharp" would defeat the purpose - it would re-create the synchronous burden that motivated the change. The window has to be wide enough to accommodate the actual variance in how people start their days.

3. **A clear escalation path.** Blockers cannot just sit in the post. The @mention is the mechanism. If the post says "blocked on X, @Sarah" and Sarah does not respond within her working hours, there is a defined next step (escalate to channel). Without escalation, the async standup degrades into a write-only ritual.

## The edge cases

**Edge case 1: A teammate forgets to post.** The post is missing. Does this count as a skipped standup? Treat it like a skipped sync standup: noticeable, addressable, not catastrophic. Two misses in a week is a signal, not a violation.

**Edge case 2: Someone posts but no one reads.** This is the failure mode the definition has to guard against. If the team is writing into a channel that nobody opens, the ritual is dead. The team lead reading and reacting to posts (a one-line "saw this, ack" or an emoji) is the cheap fix.

**Edge case 3: A blocker that needs the group, not one person.** The @mention pattern handles 1-to-1 blockers. For 1-to-many blockers, the right move is a follow-up thread or a 15-minute call. The async standup is not a substitute for the call, it is the trigger for it.

**Edge case 4: A genuinely synchronous moment is required.** Release coordination, incident response, a difficult cross-team decision. These were never standup work. Going async on the standup does not change what they require.

## Why the precision matters

A team that adopts an async-first standup without being precise about what it is will end up with a vague hybrid: half the team treating it as a status report, half treating it as optional, the sync meeting quietly reappearing as "just a quick sync to align." Precision is not pedantry. It is the difference between adopting a new ritual and slowly drifting back to the old one.
