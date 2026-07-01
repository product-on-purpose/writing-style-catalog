---
entry_id: cold-outreach
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Cold outreach - Postgres partitioning question

**Subject:** Partitioning pg_notify before you have to

Renata, your meetup talk on how your team picked a partition boundary for a pg_notify-backed job queue before write volume forced the question was the clearest account of that decision I've found anywhere, especially the part where you weighed a full move to DynamoDB and stayed on Postgres instead.

We landed the same call last week for a new notification service: Postgres over DynamoDB, mostly on operational grounds, with 5M events/day as our own revisit line. I'll be the one scoping the partitioning work when we hit it, and yours is the only real account of that fork I've found.

Would you have 15 minutes in the next few weeks to walk through how you set your boundary?

Ana Rivera
Tech lead, Lattice Notify
