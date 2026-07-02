---
entry_id: product-description
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Notification Service

*Real-time delivery for every Lattice Notify team, on infrastructure you already trust.*

The notification service is the fastest way for any Lattice Notify team to reach a user in-app, by email, or in Slack, without standing up your own delivery infrastructure. It runs on the primary Postgres cluster instead of a new datastore, plugs into your existing schema, and can carry your first notification within an afternoon of integration.

- **Sub-second delivery.** Events reach a user's in-app inbox in under a second at p95, so a mention or a comment reply feels instant, not delayed.
- **No new datastore to learn.** The service lives on the same Postgres cluster as the rest of Lattice Notify, so your joins against users, accounts, and workspaces stay plain SQL. (ADR-0023 has the full reasoning on Postgres over DynamoDB, if you want the detail.)
- **Retries and dead-letter handling included.** A `pg_notify`-backed job queue picks up your event in about 50 milliseconds and absorbs the failure cases, so you never write your own worker pool.
- **Three lines to integrate.** Call `NotifyClient.send()` with a user, a channel, and a template, and delivery is handled end to end.
- **Room to grow with you.** Sized for 500K events a day today, with a documented threshold at 5M events a day where the team revisits the datastore, so your roadmap will not outrun ours.

A dedicated 4-person on-call rotation and a documented runbook stand behind every event, so once you integrate, paging is not your problem. Message #notify-service, or grab Ana, Marcus, or Sam to get your first event flowing this sprint.
