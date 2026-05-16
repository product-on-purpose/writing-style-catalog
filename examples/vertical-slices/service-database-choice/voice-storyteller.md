---
entry_id: storyteller
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Storyteller on: Choosing between Postgres and DynamoDB

The whiteboard in the Lattice Notify engineering room had been wiped down twice in two weeks, and the same two columns kept reappearing. Postgres on the left. DynamoDB on the right. Underneath each, in Ana's small careful hand, the same five rows: throughput, ops, team skill, cost, rollback. The marker had started to dry out.

It was Tuesday evening. Ana was the last one in the office. Marcus had been there until 6, then left for a run, the laces on his sneakers already loose at his desk before he stood up. Priya had stopped by twice. The second time she had stood in the doorway for a long moment and said, "Just to be clear, I am okay with either one. I am not okay with neither."

The whiteboard did not answer. Ana looked at the row labeled "rollback" and thought about the dashboard she would build on Wednesday morning if they went with DynamoDB - the one that would have a row for partition heat and another for throttled requests and another for items she did not yet know to track - and she thought about the four-person on-call rotation, Jess and Wei and Tomas and Sarah, and the Tuesday night two months from now when one of them would page her at 2am and she would have to be the one who knew the answer.

She thought about the partnership too. The 10x scenario. The Slack logo on the slide Priya had shown the board last quarter. The cells in the spreadsheet that would all need to be rewritten if it landed and the existing schema started groaning.

The marker, she noticed, was almost gone.

She picked up a different one, blue this time, and drew a line under "rollback" in the Postgres column. Then she wrote, in slightly bigger letters than the rest:

_3-6 weeks. Painful. Known._

In the DynamoDB column, under the same row, she wrote:

_None. Unknown._

She stepped back. She looked at the two phrases for a long time, the way you look at a hand of cards you have just been dealt. Then she capped the marker, picked up her phone, and texted Marcus: "I think we are doing Postgres. Want to argue about it on the walk in tomorrow?"

The response came back before she had reached the elevator. "Yes. But also: yeah."
