---
entry_id: friendly-mentor
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Friendly Mentor on: Choosing between Postgres and DynamoDB

Okay, so you have got an architecture meeting Wednesday and a Friday deadline to pick a database for the Lattice Notify notifications service. Let me walk you through how I would think about this kind of choice. Not what to pick - that is your call. How to frame the call so you can pick with confidence.

First, the thing that usually trips people up here is treating "Postgres versus DynamoDB" as a comparison of two databases. It is not, really. It is a comparison of two organizations: the version of your team that ships on the database you already know, and the version of your team that takes on a new operational concern at the same time it is trying to ship a feature. Those organizations have different capacities. The database is just where that difference shows up.

So why does that matter? Because at 500K events a day, both options work technically. Postgres handles that comfortably with a queue and a partitioned table. DynamoDB handles it too, and probably scales more naturally if the Slack partnership lands and you suddenly have 5 million a day. If you only looked at the throughput question, you might lean DynamoDB. But that is not the whole picture.

The part that helps most people land this kind of decision is asking: "what does the worst plausible day look like for each option?" For Postgres, the worst day is probably six months in, traffic has 10x'd, and Ana has to lead a three-week migration. Painful but rehearsed. For DynamoDB, the worst day is probably two months in, Marcus is on vacation, someone misconfigures a partition key, and the four-person on-call rotation is debugging a database nobody in the room has shipped to production before. Painful and unrehearsed.

Now that you have got both worst days in your head, the framing for Wednesday gets easier. You are not picking the better database; you are picking which kind of pain you would rather buy insurance against. Priya will want you to say it that way out loud. Ana and Marcus will both feel heard if you do.

You have the information you need to make this call by Friday. Trust the work you have already done.
