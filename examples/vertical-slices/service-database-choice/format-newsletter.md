---
entry_id: newsletter
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Backend Weekly #58

Subject: We picked the boring database on purpose

Hey backend-eng - it's Ana's turn on the digest this week, which means you're getting entirely too many words about databases. Sprint planning wrapped an hour ago, so if you're reading this Friday evening, that's your cue to log off.

---

**This week's story: the database we didn't pick**

We closed out the Postgres-vs-DynamoDB question for the new notification service, and I want to walk through the reasoning, not just the answer.

The service needs to handle around 500K events a day at launch, with a possible 10x jump within a year if the Slack partnership deal closes. DynamoDB is, on paper, the better technical fit: write-heavy, point lookups by user, scales without anyone paging Jordan at 2am. Marcus built the case for it, and the spike he ran (linked below) confirmed the access-pattern fit is real. If we were optimizing purely for "what shape of database matches this workload," DynamoDB wins that argument cleanly.

We didn't pick it. We're building on Postgres: a new schema in the existing primary cluster, a job queue backed by `pg_notify`, and a documented threshold of 5M events/day sustained before we revisit DynamoDB at all.

Here's the part worth keeping: the deciding factor wasn't the access pattern, it was us. We run a 4-person on-call rotation across 8 backend engineers. A second database means a second runbook, a second monitoring surface, a second thing someone has to remember at 2am. We've paid that tax before on a different project and it's real. The 10x growth scenario also isn't locked in yet since the Slack deal hasn't closed, so we chose not to design for a load we might not get. Either direction is recoverable if we're wrong: a few weeks of migration work, not a rewrite.

Marcus's argument was correct in isolation. We optimized for team capacity over workload fit, on purpose, with the tradeoff written down. That's ADR-0023, first link below, if you want the full version with the parts I compressed out of this note.

---

**Worth your attention this week**

- [ADR-0023: Postgres for the notification service](https://wiki.latticenotify.com/adr/0023) - the full context, the three forces we weighed, and the exact threshold where we'd reopen this. If you click one thing, click this.
- [DynamoDB spike results](experiments/notify-ddb/) - Marcus's writeup of the access-pattern fit. Read it before you tell me we made the wrong call; he already made your argument, and made it well.
- [notification-service README](README.md) - Sam's install and quickstart docs are live now that the schema direction is locked. First PRs against `notification_jobs` welcome once the table spec is posted.
- [On-call runbook updates](docs/runbook.md) - Jordan's adding queue depth and write-rate panels so the 5M threshold shows up on a dashboard instead of in a postmortem. Worth bookmarking if you're on the rotation.

---

Coming up: Sam's schema spec lands next week, and we've got end-to-end traffic moving on the Postgres path by the end of the month. I'm handing the pen to whoever ships the loudest thing between now and then - if that's you, say so.

Manage your Backend Weekly subscription, or make someone else read this instead, in #notify-arch.

- Ana
