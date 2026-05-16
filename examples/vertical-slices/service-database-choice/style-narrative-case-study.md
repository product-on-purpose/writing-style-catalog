---
entry_id: narrative-case-study
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Narrative Case Study on: Choosing between Postgres and DynamoDB

### Before

In May 2026, Lattice Notify was a 50-person Series B startup with a monolith running on Postgres and eight backend engineers. The product was stable. The runbooks worked. The four-person on-call rotation had been quiet for two months. Then Priya, the PM, brought the team a real-time notification system to build, with 500K events/day at launch and a 60% chance of 10x growth in twelve months if the Slack-partnership term sheet closed.

The architecture meeting was scheduled for Wednesday 2pm Pacific. By Monday morning, two camps had formed in the design doc. Ana, the tech lead, had drafted a Postgres-with-queue proposal: known infrastructure, familiar operational profile, work she had shipped at this scale before in a prior role. Marcus, a senior engineer, had countered with a DynamoDB proposal: natural fit for the access pattern, transparent scaling, the right answer for the 10x scenario.

The team had four days to a decision and no agreement on what the decision was actually about.

### Turning point

On Tuesday afternoon, Ana walked over to Marcus's desk after reading his weekend benchmark. They spent ninety minutes at the whiteboard. Ana granted the access-pattern fit. Marcus granted the on-call cost. But they were still at impasse on which cost was binding.

On Wednesday at 2pm, Ana opened the meeting not with a recommendation but with a reframe. "The decision is not Postgres versus Dynamo," she said. "It is how much we believe the Slack deal will close. If we are confident it lands, Dynamo is right. If we are not, Postgres is right. The architecture question is downstream of the probability question."

The room got quiet. Priya, who had been preparing for a debate, instead committed to getting a probability estimate from the CRO by end of day Thursday. Marcus offered to prototype the Dynamo schema in parallel so the team had a real artifact for either path. The meeting ended with no vote.

Thursday afternoon, the CRO came back with 60%. Priya routed the number to the channel.

Friday at 10am, Ana posted the recommendation: ship on Postgres with a queue, pre-commit to a Dynamo migration if real volume crossed 2M events/day on a 30-day rolling average. The trigger was binding. The Dynamo prototype was preserved. Sprint planning ran at 2pm.

### After

Six months later, in November 2026, Lattice Notify was running notifications on Postgres at a stable 700K events/day. The Slack-partnership deal had closed in October but was rolling out customer-by-customer, with volume on the notification system tracking closer to 1.2M events/day rather than the 5M scenario the original 10x projection had assumed. The 2M threshold had not been crossed.

The four-person on-call rotation had taken two incidents on the notification system in that period; both were resolved in under thirty minutes by engineers using Postgres tools they already knew. Marcus had begun a quarterly review against the trigger threshold and reported each cycle to the architecture forum.

The migration to Dynamo, the work Marcus had prototyped, had not been needed. The preserved design sat in the design-docs repo, status unchanged, ready if and when the threshold fired.

In a retrospective at the end of the year, Ana wrote: "The decision we made was not Postgres. The decision we made was to convert a future architecture choice into a present trigger condition. That is what made the trade-off survivable."

### The principle

A service database choice made under uncertainty is more durable when it includes a binding trigger condition than when it makes a permanent commitment in either direction. The trigger converts the high-volume scenario from a guess about the future into a measurable event in the present. Teams that pre-commit to the trigger preserve the option to be wrong without paying the cost of being wrong every day until the future arrives.
