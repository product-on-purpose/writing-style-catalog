---
entry_id: first-principles-derivation
axis: style
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

## Deriving the datastore for Lattice Notify's notification service

The Wednesday meeting split between Marcus, who prefers DynamoDB, and Ana, who prefers Postgres. Both of them are reading the same facts. So the disagreement is probably about an assumption nobody has written down. Here are the premises. Grant or refuse each one before reading further.

### Premises

1. **P1 (input).** Launch volume is 500K notification events per day. This is the number from the PRD that Ana drafted with Priya.
2. **P2 (input).** The 10x scenario, 5M events per day, happens only if the Slack-partnership deal closes. The deal has not closed.
3. **P3 (input).** The team is 8 backend engineers and a 4-person on-call rotation. All 8 run Postgres today. Only Marcus has touched DynamoDB, on a side project.
4. **P4.** A system on call is only as safe as the least experienced person who may be paged for it.
5. **P5.** Each additional datastore adds its own runbook, alerts, backup process, and failure modes that someone on the rotation must learn.
6. **P6 (input).** Moving between the two stores later costs 3 to 6 weeks of rework in either direction.

### Derivation

**Step 1, from P1.** 500K events per day is about 6 events per second on average. Peaks will be higher, but the launch load is small for a database that every engineer already operates. Launch volume therefore does not by itself force a new datastore.

**Step 2, from P2 and P6.** The 10x load is uncertain, and a wrong guess costs the same 3 to 6 weeks in either direction. We are paying a price for one of two futures. The cheaper bet is on the future we can observe today, and a revisit threshold lets the other future wake us up.

**Step 3, from P3, P4 and P5.** Choosing DynamoDB adds a second datastore. By P5 that adds a second runbook. By P3, at least three of the four people on call have never debugged it. By P4, the safety of the whole rotation is set by that gap, not by Marcus's skill.

**Step 4, from Steps 1 to 3.** Launch volume does not need DynamoDB (Step 1). The later volume that would need it is uncertain, and the cost of waiting is bounded (Step 2). The cost of adopting it now is paid every night, by people who cannot yet fix it (Step 3).

### Conclusion

Therefore the notification service should launch on Postgres, in a new `notifications` schema, with a revisit trigger at 5M sustained events per day. The trigger is the part Step 2 requires: it turns the 10x bet into a measured event rather than a guess.

### The load-bearing premise

P4 carries the weight. If on-call safety is set by the best-informed engineer rather than the least, then Step 3 weakens. Marcus's skill would cover the gap, and DynamoDB's better fit for point-lookups by user would win. Anyone who rejects the conclusion should reject P4, and should say so on Friday before sprint planning.

One premise is a number rather than a claim. If P6 were 1 week rather than 3 to 6, Step 2 would matter less, because a wrong guess would be cheap to fix, and the on-call cost in Step 3 would still decide it.
