---
entry_id: layered-disclosure
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Layered Disclosure on: Choosing between Postgres and DynamoDB

Lattice Notify will ship its new notification system on Postgres with a queue and a pre-committed trigger condition to migrate to DynamoDB if real volume crosses 2M events/day on a 30-day rolling average. Ana owns the build for a 2026-06-15 production target; Marcus's prototype Dynamo schema is preserved in the design-docs repo as the starting point if the trigger fires. The four-person on-call rotation stays on one storage system at launch. If you stop reading here, you have the decision, the owner, the trigger, and the operational impact.

### The reasoning behind the choice

The notification system needs to handle 500K events/day at launch with a possible jump to 5M events/day in twelve months if the Slack-partnership deal closes (currently 60% confidence per the CRO). DynamoDB fits the access pattern (write-heavy, key-lookup, time-ordered) more naturally than Postgres, but it would require the four-person rotation to be on-call for a second storage system none of them have operated in production. At 60% Slack-deal probability, the expected cost of running two storage systems for a year is higher than the expected cost of a deferred migration if and when volume actually demands it.

### How the trigger condition works

The 2M events/day threshold on a 30-day rolling average is calibrated to the point at which Postgres sharding work becomes urgent rather than discretionary. If volume reaches that threshold, the Dynamo migration project starts the following sprint. Priya owns the quarterly volume review starting 2026-Q3. The threshold is reviewable at the architecture review if real data suggests it is wrong, but it cannot be quietly raised; any change requires a new architecture-meeting decision.

### What the trade-offs look like in detail

The decision rejects three alternatives. **DynamoDB-from-day-one** was rejected because the four-person rotation cannot safely absorb a second storage system at launch and because the expected operational cost outweighs the expected migration cost at 60% Slack-deal probability. **Unconditional Postgres commitment** was rejected because it does not address the high-volume scenario at all, leaving the team to discover at 5M events/day that they should have planned for migration earlier. **Deferring the decision past Friday** was rejected because it would block sprint planning and create cascade delays in the notifications launch.

The decision accepts two risks. First, if the Slack deal closes faster than the 2M events/day threshold can catch, the migration becomes urgent under load rather than scheduled in advance. The mitigation is the preserved Dynamo design, which shortens the lead-in to roughly 3-6 weeks of work for two engineers. Second, if volume never reaches the threshold, the team has spent the trigger-condition design effort on a contingency that never fires; this is acceptable cost insurance for a recoverable downside.

### How the meeting reached this conclusion

The Wednesday 2pm architecture meeting opened with Ana presenting the Postgres-with-queue option and Marcus presenting the DynamoDB option. The pivot in the meeting came when Ana reframed the question: the decision was not really between two databases but between two theories of how to absorb risk. Marcus's prototype confirmed the access-pattern fit, but did not address the four-person rotation's capacity. Ana's familiarity argument was complete only if the 10x scenario could be deferred without crisis. The synthesis - ship on Postgres with a binding trigger tied to actual volume rather than projected volume - was neither engineer's original position. Priya secured the CRO's 60% confidence estimate on Thursday afternoon, which converted the choice from a guess about the future into a decision under quantified uncertainty. The recommendation was committed to the engineering channel Friday morning; sprint planning ran against it Friday at 2pm.

### How this will be revisited

The 2026-Q3 architecture review is the formal moment to reassess. Inputs at that point will be real launch volume data, current Slack-deal status, and any operational incidents from the first quarter of running the notification system. The decision is not sealed; it is committed for execution against today's information. If the inputs shift materially, the trigger condition or the underlying storage choice can be revisited with the same architecture-meeting process that produced this one.
