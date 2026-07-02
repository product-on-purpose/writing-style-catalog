---
entry_id: open-letter
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# An Open Letter to Ana Rivera: Keep the Threshold Real

*Posted to #notify-arch. cc: Priya, Jordan, Sam, engineering leadership.*

Dear Ana,

ADR-0023 says Accepted now. Lattice Notify's notification service runs on Postgres. I made the case for DynamoDB at Wednesday's meeting, you and the rest of the room heard it out, and we landed on Postgres anyway, for reasons I still agree with. I am not writing to reopen that. I am writing because one line in the document we shipped is carrying more weight than a single line should have to carry by itself, and I want it somewhere more people than the two of us can see it.

The line is in the consequences section, and you wrote it: "we are accepting a worse fit for the access pattern in exchange for a better fit for the team's operational reality." That is a fair trade. Eight engineers and a four-person on-call rotation cannot run two databases well, and I would rather ship on a platform we already know than learn DynamoDB's failure modes at 2am during launch week. But a trade has two sides, and the other side is the number we stayed up writing together the night before the sync: 5M events per day, sustained. That is not an arbitrary line. It is exactly the 10x growth scenario from the original context, the one the Slack deal would trigger if it closes on schedule. I signed off on the trade because that number was attached to it. I want to make sure the number still means something in six months.

Here is what worries me. Jordan ships queue depth and write rate to the on-call dashboard on the 22nd, and once that line exists on a screen, it is easy for it to become wallpaper. Priya's partnership tracking gives us thirty days of warning if the Slack deal closes early, which is real and I am glad it exists, but a warning about deal timing is not a trigger tied to what the database is actually doing. The neutral note in the ADR says the on-call rotation owns the dashboard. Rotations are good at answering pages. They are not built to notice a slow trend line and decide, unprompted, that it is time to reopen an architecture decision. That takes a name attached to it, not a rotation.

I could have sent you this as a direct message. A year ago I probably would have. I am posting it in #notify-arch instead, because a private agreement between the two of us is exactly the kind of thing that quietly stops being true once Q4 planning gets busy and nobody else remembers it was ever made. Priya and engineering leadership are reading this too. That is the point. If the threshold mattered enough to write into an accepted ADR, it matters enough to survive being read by people who were not in the room on Wednesday.

Here is what it means if we get this wrong. The ADR calls the decision reversible, and it is, but only if someone acts while there is still 3-6 weeks of runway to do the migration properly. Miss that window, and we are not doing a planned rework anymore. We are doing an emergency one, on the platform we chose specifically because it would not put us in an emergency. That is the one failure mode this whole decision was supposed to protect against.

So here is what I am asking, specifically. Put the 5M events/day threshold on the same quarterly roadmap review that already tracks the 3M partitioning work, with your name on it as owner, not just the rotation's, before Jordan's dashboard ships on the 22nd. If the number never crosses 5M, this costs the team one recurring agenda line. If it does, we have already agreed, in public, on record, what happens next, and neither of us has to relitigate whether DynamoDB deserved a second look. You already told the room it might. I am only asking that we keep the promise as real as the decision it came attached to.

Reply here, or at the review, whichever you would rather. I just want the answer to live somewhere the rest of the team can find it too.

Marcus
Backend engineer, notification service. I made the DynamoDB case at Wednesday's meeting; this letter is me making sure the half of that argument we kept does not quietly disappear.
