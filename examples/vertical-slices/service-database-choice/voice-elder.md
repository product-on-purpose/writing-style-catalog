---
entry_id: elder
axis: voice
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

## Elder on: Choosing Postgres vs DynamoDB

Marcus, you asked me on Tuesday what I thought you should bring to the Wednesday meeting, and I told you I would write it down instead, because I did not trust myself to say it short.

For about fifteen years I believed that the right database was the one that fit the shape of the data, and that a team which picked anything else was being lazy. I held that belief through four launches, and I was wrong about it in at least two of them, though it took me until the third to see why. The data fit was never what hurt. What hurt was the second runbook, the second set of alerts, and the night someone who had never touched the new system was the only person awake when it failed. I am not telling you that is what will happen to Lattice Notify. I am telling you that is what happened to me, and that I did not believe it until it had happened twice.

You are right about the access pattern. Writes by the hundreds of thousands, lookups by user: DynamoDB was built for exactly that, and your spike showed it. Ana is right about the four people on the rotation, and about the eight of us who would have to learn a new way of being paged. I have watched both kinds of argument win in rooms like Wednesday's, and I have watched both kinds of team recover. The first time I saw a team pick the better-fitting tool over the familiar one, it cost them about a quarter of a year before the fit paid anything back. The first time I saw a team pick the familiar one and outgrow it, it cost them a few weeks of rework and a very tired spring. Your own estimate of three to six weeks is about what I remember, though my memory of numbers is not what it was.

The 10x depends on a deal that has not closed. I have seen that kind of deal close and I have seen it quietly evaporate, and I could not have told you beforehand which it would be. Neither can you, and I think that is the honest center of Friday: nobody in that room can shorten the not-knowing. A year from now this will be a paragraph in the history of the service, and whoever reads it will not remember how heavy it felt on a Wednesday afternoon. It is heavy now, and I do not say that to make it lighter.

If you ask me which one I would pick, I would say Postgres, and I would say it quietly, with the threshold written down so that someone later has a date to be right or wrong against. But I have been sure of things before. Come find me after Friday, whichever way it goes.
