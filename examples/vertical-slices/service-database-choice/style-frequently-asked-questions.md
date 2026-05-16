---
entry_id: frequently-asked-questions
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Frequently Asked Questions on: Choosing between Postgres and DynamoDB

### What did we actually decide?

We are shipping the Lattice Notify notification system on Postgres with a queue in front. If real volume crosses 2M events/day on a 30-day rolling average, we trigger a planned migration to DynamoDB the following sprint. Ana owns the build; Marcus has a preserved Dynamo design in the design-docs repo for the trigger case.

### Why not just go with DynamoDB now?

Two reasons. First, our four-person on-call rotation has not operated DynamoDB in production, and the team agreed that adding a storage system the rotation cannot debug is unsafe at launch. Second, the 10x growth scenario is conditional on the Slack-partnership deal closing (currently 60% per the CRO). At that probability, the expected cost of running two storage systems for a year is higher than the expected cost of a deferred migration. The decision is rational only if you believe the Slack deal is closer to certain than the CRO thinks it is.

### What happens if the Slack deal closes faster than expected?

We hit the 2M events/day trigger and run the Dynamo migration project the following sprint. Marcus's preserved schema design shortens the lead-in. Realistic timeline: 3-6 weeks of work, two engineers, with a known migration plan rather than a discovery project. This is the worst case in our scenario tree, and it is recoverable.

### Why are we using a queue in front of Postgres?

The launch access pattern is write-heavy and time-ordered. A queue (SQS or our internal event bus, TBD by Marcus's schema review) absorbs spikes so writes to Postgres stay paced. It also gives us a clean buffer if we later want to write to a second store in parallel during the migration window.

### Who decided this and when?

The architecture meeting on Wednesday 2026-05-13 at 2pm Pacific. Decision committed to channel on Friday 2026-05-15 by Ana (Tech Lead, Notifications), with input from Marcus (Senior Eng), Priya (PM), and the on-call rotation. Sprint planning ran Friday afternoon against the decision.

### Why is Ana the owner if she leaned Postgres? Isn't that confirmation bias?

The Wednesday meeting moved off the "which database is better" framing into "how confident are we in the Slack deal." Once the team agreed the question was probabilistic, Ana's lean and Marcus's lean both became conditional rather than oppositional. The current plan covers both of their concerns: ship on Postgres now (Ana's preference) with a binding trigger for migration if the volume scenario she discounted actually materializes (Marcus's concern made operational).

### How does this affect the on-call rotation right now?

It does not. The four-person rotation stays on one storage system at launch. If the migration trigger fires, we will revisit the rotation composition before the second system goes live - likely by adding training time and possibly a fifth rotation member.

### What happens to Marcus's prototype work?

Preserved in the design-docs repo under `notifications/dynamodb-schema-v1.md` with a status header of "deferred design, ready to revive." Not deleted, not productionized. If the trigger fires, the prototype becomes the starting point for the real schema rather than a from-scratch effort.

### Can I read the full decision document?

Yes. The decision log is in `docs/decisions/2026-05-15-notification-storage.md`. It includes the options considered, criteria used, and the reasoning Ana captured at decision time. The full set of architecture meeting notes is in the engineering wiki under Architecture Meetings / 2026-05-13.

### What if I think this is the wrong call?

The 2026-Q3 architecture review is the formal moment to revisit. Bring real volume data and the current Slack-deal status; both will be different inputs than what we had this week. If you have a strong objection before then, talk to Ana directly; the decision is not sealed, just committed for execution.
