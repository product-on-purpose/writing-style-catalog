---
entry_id: product-thinker
axis: voice
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Before we decide on the format, it is worth asking what job our engineers are hiring the standup to do. Listen to how people describe it and a few jobs surface: "I want to know if anyone is stuck so I can help." "I want to surface my own blocker without sending a 1:1 ping." "I want to know what is shipping this week so I am not surprised." Those are real jobs. The current 9am Pacific meeting is doing a mediocre version of all of them, and for our India teammates, it is failing the most basic job of all: being attendable.

The Q1 attendance numbers are not just a fairness issue, they are a product signal. When a third of your users only adopt your product 64% of the time and the other two-thirds adopt it 92% of the time, something about the offering is misaligned with the users it underserves. The standup is a product. The engineers are the users. We have a usability problem in one of our three primary segments.

The Priya incident is the kind of story I would put in a research deck. She diagnosed a 401 error in real time. Five hours later, another engineer hit the same error and spent 45 minutes re-solving it, because the original diagnosis had evaporated into a Zoom transcript no one can search. That is the job-to-be-done of "I want to find out if this has been solved before," and our current format does not serve it. An async post in #team-standup with a 401 in it is findable forever.

The async-first format addresses both the equity job and the searchability job in one move. It risks under-serving the connection job, which is real and which I do not want to dismiss. The Thursday working session is the hedge: a deliberate space for the kind of unstructured exchange that a status meeting was never the right container for anyway.

What does success look like? Three measures: blocker mention rate goes up (people feel safer surfacing them in writing), India attendance and contribution converges with the rest of the team, and we cut at least one duplicated debugging incident in the 30-day window. Run it. Watch the users. Decide on the data.
