---
diff_pair_id: style-narrative-case-study-vs-chronological-narrative-service-database-choice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
axis_varied: style
entry_a: narrative-case-study
entry_b: chronological-narrative
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `narrative-case-study` vs `chronological-narrative`

**Topic:** How to choose between Postgres and DynamoDB for a new service
**Axis varied:** style
**A:** `narrative-case-study` - A story with a before, a turning point, and an after - using one specific real situation to make a general principle concrete and trustworthy.
**B:** `chronological-narrative` - Time order is the primary organizing principle - first this, then that, then what came after - with no thematic restructuring.

## What to notice

These two are the closest confusable pair in the Style axis. Both tell the same week as a
story, with the same cast and the same Tuesday whiteboard session. The difference is what
the shape of the story **obligates the writer to know.**

**A has to know how it turned out.** `narrative-case-study` runs Before, Turning point,
After, The principle, and each of those headings is a debt the writer must pay. "After"
cannot be written without an outcome, so A jumps six months to November 2026 and reports
actuals: 700K events/day, the Slack deal closed in October but rolled out
customer-by-customer, volume at 1.2M rather than the projected 5M, the 2M trigger never
fired, two incidents both resolved in under thirty minutes. "The principle" then cannot be
written without a transferable claim, so A extracts one: a choice made under uncertainty is
more durable when it converts a future architecture decision into a present trigger
condition. A is arguing, using a story as evidence.

**B only has to know what happened next.** `chronological-narrative` is pure sequence, and
its only structural obligation is the clock: Monday morning, that same afternoon, Tuesday
morning, Tuesday afternoon, Wednesday at 2pm, Thursday afternoon, Friday at 10am. It ends
where the week ends, with sprint planning at 2pm, and it draws no lesson. B is reporting.

**The sharpest single tell.** A's ending generalizes past its own case ("Teams that
pre-commit to the trigger preserve the option to be wrong"); B's ending is a timestamp
("Sprint planning ran at 2pm"). If a narrative closes by telling you what it means, it is a
case study. If it closes by telling you what time it was, it is chronological.

**One honest caveat about this pair.** A and B reach *different decisions*: A lands on
Postgres with a binding 2M events/day trigger, while B ends with Ana saying "At sixty
percent, I think we should go with Dynamo and accept the operational cost." That divergence
is **not** an effect of the style. Each vertical-slice render in this catalog was generated
independently per entry, so nothing forced the two to agree on a verdict. Read this pair for
what the form obligates, not for what the teams decided; the ADR-versus-whitepaper pair on
this same topic is the cleaner one to read for content parity, since both of those land on
Postgres.

---

## A: `narrative-case-study`

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

---

## B: `chronological-narrative`

## Chronological Narrative on: Choosing between Postgres and DynamoDB

On Monday morning, May 11, Priya pinged the architecture channel and said the notification system needed a storage decision by Friday. The Slack-partnership conversation had moved to a term sheet stage over the weekend, and if it landed, Lattice Notify would be staring down ten times the daily volume by next spring. The team needed to commit to a path before sprint planning.

That same afternoon, Ana opened a draft doc and laid out the Postgres case. She had shipped the monolith at 500K events per day before, on Postgres, with a queue in front. She knew the runbooks. The on-call rotation knew the runbooks. The work was unglamorous but mapped.

Tuesday morning, Marcus pushed back in the doc comments. He said the access pattern for notifications, write-heavy, key-lookup, time-ordered, was exactly what DynamoDB was built for. He noted that the 10x growth scenario would force a Postgres sharding project in twelve months that nobody on the team had done before. He attached a benchmark he had run on a personal account over the weekend.

Tuesday afternoon, Ana read the benchmark, then read it again, then walked over to Marcus's desk. They spent ninety minutes whiteboarding. By the end of the session, Ana had granted that DynamoDB matched the access pattern. Marcus had granted that adding a second database meant the four-person on-call rotation now needed to be on-call for two systems instead of one, and that cross-database joins for the analytics dashboards would become application-layer code.

Wednesday at 2pm Pacific, the architecture meeting opened with Priya restating the deadline. Ana presented the Postgres-with-queue option. Marcus presented the DynamoDB option. Then, instead of the debate Priya had been bracing for, Ana said something the room had not expected: "If the Slack deal closes, we should be on Dynamo. If it does not, we should stay on Postgres. The decision we are actually making is how much we believe in the Slack deal."

The room got quiet. Priya said she could get a probability estimate from the CRO by end of day Thursday. Marcus said he could prototype the Dynamo schema in parallel so that either decision Friday morning would have a real artifact behind it. The meeting ended without a verdict.

Thursday afternoon, the CRO came back with sixty percent confidence on the Slack deal closing in Q3. Priya routed that number to the channel. Ana posted a single sentence: "At sixty percent, I think we should go with Dynamo and accept the operational cost."

Friday at 10am, the decision shipped to the team. Sprint planning ran at 2pm.
