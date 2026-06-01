---
entry_id: journalist
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Journalist on: Choosing between Postgres and DynamoDB

Engineers at Lattice Notify, a 50-person Series B startup, are scheduled to decide by Friday how to store data for the company's first real-time notification system, a feature they are building under the additional pressure of a possible Slack partnership that would tenfold the projected workload within a year.

The decision will be debated at an architecture meeting on Wednesday at 2pm Pacific. Two senior engineers have taken visible positions in the week leading up to it.

Ana, the tech lead on the notifications project, said in an internal memo circulated Monday that she favors extending the company's existing Postgres monolith with a new schema and a queue. "We have shipped at this scale before," she wrote, citing two prior services that handle comparable write loads. The current ops surface, she noted, is "a single database the on-call rotation already knows how to operate."

Marcus, a senior engineer on the same team, has argued for adding DynamoDB. According to a thread in the team's design channel, he believes the notification access pattern - high-volume key-value writes with TTL reads - is "the workload DynamoDB exists for," and that taking on the learning curve now is cheaper than migrating later under partnership pressure. He acknowledged in a follow-up message that the rollback path is, in his words, "not great."

Priya, the product manager assigned to the project, said in a call this morning that she is agnostic between the options but wants a decision by end of week so the team can plan the next sprint. "I am not here to break the tie on engineering grounds," she said. "I am here to make sure we get to one."

The four engineers on the on-call rotation have not yet been polled formally, though two, who asked not to be named because the decision is not yet final, said separately that they would prefer the option that does not add a second pager. Both pointed to the same concern: that operating an unfamiliar database during the partnership push would compress their time to respond to incidents.

The architecture meeting will run until the decision is reached or until 4pm, whichever comes first.
