---
entry_id: playful
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Playful on: Choosing between Postgres and DynamoDB

Subject: the Wednesday meeting, in which we will pick a database and pretend it was easy

Team,

By 3pm Wednesday, Lattice Notify will have committed itself to a row store or a key-value store for approximately one million notification events per week. By 3:01pm, half of us will be quietly relitigating the decision in DMs. This is the standard architectural lifecycle and I want us to enjoy it.

Here is what I have observed.

Marcus has been carrying his DynamoDB writeup around like a man who has found religion at a conference. Ana has the energy of someone who has personally apologized to a Postgres database after a long deploy and is not willing to do that to a second one. Priya has the particular flat expression of a PM who has heard "it depends" said with confidence by two different engineers in the same standup.

The actual situation, stripped of all the dignity we have been wrapping it in: we have to pick between the database we already know how to run badly at 3am and a database we would have to learn how to run badly at 3am. Both options end with someone paged at 3am. The question is which 3am we are training for.

500K events a day is not, in the grand cosmic scheme, a lot of events. Postgres has been quietly handling worse from less competent teams since before half of this office was old enough to use a database. DynamoDB will also handle it, in exchange for a small monthly tithe and the soul of whoever has to write the migration script later. Neither outcome is tragic. Neither outcome is heroic. Most architecture decisions are like this; we just usually let ourselves believe otherwise.

What I would like us to do on Wednesday: pick the one we will resent least at 3am, name the threshold at which we will revisit it (I propose "when the partnership signs or when on-call gets paged about throughput three weeks in a row"), and then go plan the sprint. Priya gets her answer by Friday. The notifications go out. Someone, somewhere, finds out they have been mentioned in a Slack thread. Civilization continues.

See everyone at 2pm. Bring opinions and snacks.

- Ana
