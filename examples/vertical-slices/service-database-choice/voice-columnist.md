---
entry_id: columnist
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Columnist on: Choosing between Postgres and DynamoDB

Lattice Notify, a 50-person Series B I have been watching with interest, is about to make exactly the wrong kind of database decision for exactly the right kind of reason. I want to flag it before they walk into Wednesday's architecture meeting, because the pattern repeats at almost every company in this stage, and I have seen how it ends.

The setup is familiar. A new real-time notifications feature. 500K events a day at launch, with a 10x growth scenario if a Slack partnership lands. Two options on the whiteboard: stay on Postgres, the database the team already runs, or add DynamoDB, which scales more naturally for the access pattern. Ana, the tech lead, wants Postgres. Marcus, a senior engineer, wants DynamoDB. Priya, the PM, wants a decision by Friday.

Here is my opinion: pick Postgres, and pick it for the boring reason.

Yes, DynamoDB is closer to the platonic ideal of "notification storage." Yes, the 10x scenario is real. I have read the same blog posts you have. But what I have also seen, again and again, is that the failure mode at 50-person companies is almost never "the database we chose could not scale." It is "the operational surface area we took on consumed the engineering focus we needed for the thing we were actually selling." Marcus is right on the engineering. He is wrong on the organizational physics.

The counterargument is real and I want to acknowledge it: if the Slack deal closes and traffic runs hotter than the 10x model, the Postgres path costs 3-6 weeks of migration rework. That is genuine pain. But it is pain at a point when you have the contract revenue to fund the headcount to absorb it. The alternative is paying the operational cost now, every day, against a contract that may not close.

The honest version of this column is shorter: do the unsexy thing. Ship on the database you know. Buy the right to be boring with your scaling story, and spend your interesting engineering on the product feature itself.

I will be wrong about this if Slack closes in Q3 and the traffic curve looks like nothing we have modeled. I am willing to be wrong on record. But I would bet Friday's coffee that I am not.
