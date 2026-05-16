---
entry_id: product-thinker
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Product Thinker on: Choosing between Postgres and DynamoDB

Before Wednesday, I want to reframe what we are actually deciding for Lattice Notify, because the Postgres-versus-DynamoDB debate is downstream of a product question we have not closed.

### Who is this for and what job are they hiring us to do?

The notification system exists to help two users. The Lattice Notify customer who needs to know that something they care about happened - a deadline moved, a review request landed, a stakeholder commented. And the Lattice Notify customer-success team that loses retention when those notifications arrive late, in the wrong channel, or not at all. The job they are hiring our service for is "tell me what I need to know, fast enough that I can act on it, without overwhelming me." Everything we choose about storage should be measured against that job.

### What does success look like for this user?

Delivery within 30 seconds of the triggering event for 99% of notifications. Zero loss of high-priority notifications. The ability to mark notifications read across devices without confusion. If the database choice makes any of those harder, we have chosen wrong, regardless of how elegant the architecture is.

### Where does the database choice actually meet the user?

Honestly, in only a few places. Read latency on the unread-count badge. Write reliability when the upstream event arrives. Queryability when the customer-success team needs to investigate "why did Acme's VP not get her notifications last Thursday." The third one matters more than Marcus's analysis has weighted it. If we go DynamoDB and Sarah from CS messages us asking "show me everything we sent to user 47281 between 2pm and 4pm grouped by channel," we need to be able to answer that without a multi-hour data dump.

### My recommendation to Ana and Marcus

Pick the option that makes the customer-success investigation flow easy on day one. That is Postgres. The 10x scenario is real, but the customer-success debugging pattern is real now, for every notification we ship, forever. Optimize for the always-true case.

Friday works. I will write the one-pager Thursday.
