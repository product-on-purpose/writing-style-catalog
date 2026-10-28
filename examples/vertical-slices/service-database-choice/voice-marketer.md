---
entry_id: marketer
axis: voice
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

Your feature needs to tell a user something happened - a comment, a mention, a workspace invite - and right now that means one of two things. You write your own delivery pipeline, on top of whatever queue you can stand up this sprint, and you own its failures. Or you file a ticket with the platform team and wait for a roadmap slot that may not open this quarter.

The notification service already does this, and it is live today.

Three lines of code put a notification in front of a user:

```python
client.send(user_id="usr_xyz789", channel="in_app", template="comment_mention", payload={"actor": "Marcus", "thread_id": "th_42"})
```

From that call, the event lands in the `notifications` schema, a worker picks it up in about 50ms, and the user sees it in their in-app inbox in under a second. That is a measured number, not a target: sub-second p95, at the volume the service runs today.

Here is what you are not taking on. The service runs on the same Postgres cluster Lattice Notify already operates in production, so you are not learning a new datastore to use it. The 4-person on-call rotation that already covers this cluster covers your notifications too. No second runbook, no new paging surface, no new failure mode for you to debug at 2am. That decision - Postgres over a separate datastore - is recorded in ADR-0023, and it was made for exactly this reason: one operational surface, not two.

One real limit, stated plainly: the service is built for 500K events a day, with headroom to grow from there. If your feature's eventual volume is going to run past 5M events a day sustained, that is the documented threshold where the team revisits this architecture, and you should loop in Ana before you build on top of it. Most features sending in-app, email, or Slack notifications are nowhere near that line. If yours might be, ask first - the answer is still probably yes, just with a conversation attached.

For everything under that line, there is nothing to design, provision, or get paged for. You call `client.send`, and the delivery, retries, and queue depth are already somebody else's dashboard.

Clone `notification-service`, run `make setup`, and send your first real notification before your next standup.
