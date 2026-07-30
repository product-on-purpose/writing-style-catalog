---
diff_pair_id: tone-candid-vs-diplomatic-service-database-choice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
axis_varied: tone
entry_a: candid
entry_b: diplomatic
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `candid` vs `diplomatic`

**Topic:** How to choose between Postgres and DynamoDB for a new service
**Axis varied:** tone
**A:** `candid` - Names the uncomfortable truth directly - not harsh, but unwilling to pretend the hard thing is not there.
**B:** `diplomatic` - Careful, face-saving communication that is soft on people and firm on positions, especially across power differentials.

## What to notice

This is the tightest content parity of any pair on this topic, which makes it the best one
for isolating tone. Both are letters from Ana. Both propose the identical plan: ship on
Postgres, design the schema and event model for portability, give Marcus ownership of the
DynamoDB migration document, and revisit at 3M events per day or partnership signing,
whichever comes first. Not one substantive term differs. What changes is **where the
disagreement is put.**

**A puts the disagreement in the open and names its cost.** It is addressed to all three
("Ana, Marcus, Priya"), so the dissent happens in front of everyone. It announces its own
evasion twice - "I think we have been talking around the real question," then "here is the
thing I have been avoiding saying" - which is the candid move: the reticence itself becomes
reportable. It restates the choice in unflattering terms the participants had not used
("we are choosing between 'the system the 8 of us know how to operate' and 'a second system
that solves a problem we have not yet had'"). It absorbs the interpersonal cost directly
rather than routing around it: "I know this is not what Marcus wanted to hear." And it owns
the conclusion in the first person: "What I think we should do."

**B moves the disagreement off the speaker and into the record.** It is addressed to Marcus
alone, so the dissent is settled privately before the meeting. It opens by conceding
influence, not just offering praise ("several points in the document have already changed my
own reading"). Then the key maneuver: the objection arrives in the agentless passive with an
institutional source attached - "**Concerns have been raised**, both in the engineering
channel and in the operations review last Friday." Nobody is named as the objector, least of
all the writer. The proposal is hedged into an invitation ("We **may want to explore**," "One
framing **worth surfacing**"), and it is framed as *serving* the position it overrides:
"preserves the option you are advocating for," "preserves the optionality your analysis
identified as valuable." It closes by crediting him again, unconditionally.

**The sharpest single tell.** Compare the two ways of introducing the same objection. A:
"here is the thing I have been avoiding saying." B: "Concerns have been raised." A locates
the objection in the speaker and marks it as costly to say; B locates it in the organization
and makes it nobody's. Watch the grammar, not the politeness: candid prefers first-person
active, diplomatic reaches for the passive with an institutional subject.

**The failure modes are mirror images.** Over-hit candid and the reader gets bluntness
performed as virtue, where naming the discomfort becomes the point instead of resolving it.
Over-hit diplomatic and the recommendation disappears into hedges, so a reader can finish the
letter without knowing what was decided. Note that B avoids that trap only because the
concrete plan (portable schema, named owner, numeric threshold) survives intact inside the
softening.

**If you are choosing between them:** the axis is not honesty. Both are honest and both
reach the same plan. Pick `candid` when the group needs the real disagreement on the table to
decide well. Pick `diplomatic` when the relationship has to outlast the decision and the
person you are overruling needs to stay invested in the outcome.

---

## A: `candid`

## Candid on: Choosing between Postgres and DynamoDB

Ana, Marcus, Priya,

I want to be direct about where I have landed before Wednesday's meeting, because I think we have been talking around the real question.

Here is the honest picture. We are not actually choosing between Postgres and DynamoDB. We are choosing between "the system the 8 of us know how to operate" and "a second system that solves a problem we have not yet had." 500K events a day is not a scale problem for Postgres. It is a schema and queue design problem. The 10x Slack-partnership scenario is real, but it is also speculative, and it is 12 months out. We have 8 engineers and a 4-person on-call rotation. Adding a second database doubles the operational surface area for a team that already has a full backlog.

I know this is not what Marcus wanted to hear, and I do not want to dismiss his case. DynamoDB is genuinely better for the steady-state access pattern. If the partnership lands and we are at 5M events a day next spring, we will probably wish we had built on it. That is a real risk and I am not pretending it is not.

But here is the thing I have been avoiding saying: if we pick DynamoDB and the partnership does not land, we have taken on permanent ops complexity to hedge against a scenario that did not happen. And the 3 to 6 weeks of rework if we have to migrate from Postgres later is cheaper than 12 months of paying the two-database tax for a 10x that never came.

What I think we should do: ship on Postgres with a clean enough schema and event model that a future migration to DynamoDB is mechanical, not a rewrite. Revisit at 3M events a day or when the partnership signs, whichever comes first. Marcus owns the migration design doc so we are not flat-footed if we trip the threshold.

Priya, you will have the decision by Friday. I wanted you to know where my head is before Wednesday so the meeting is a conversation, not a surprise.

- Ana

---

## B: `diplomatic`

## Diplomatic on: Choosing between Postgres and DynamoDB

Marcus,

Thank you for the thorough DynamoDB writeup you circulated Monday. The depth of the access-pattern analysis and the load projections under the 10x Slack-partnership scenario have meaningfully sharpened how the team is thinking about this decision, and several points in the document have already changed my own reading of the tradeoffs.

While the case for DynamoDB on the steady-state access pattern is well constructed, there are considerations worth weighing alongside it as we approach Wednesday's meeting. Concerns have been raised, both in the engineering channel and in the operations review last Friday, about the cumulative load on a four-person on-call rotation that would now be responsible for two production data stores rather than one. The team has shipped at the 500K-events-per-day scale on Postgres before, and the institutional knowledge in that area is substantial. The 10x scenario, while real and worth planning for, remains contingent on a partnership decision outside our control, and the timeline for that decision is not yet firm.

We may want to explore a path that preserves the option you are advocating for without committing to it ahead of the evidence. One framing worth surfacing in the meeting: ship the launch on Postgres with a schema and event model designed for portability, while you maintain ownership of a DynamoDB migration design document that we could execute on if and when we cross a defined threshold (perhaps 3M events per day, or partnership signing, whichever arrives first). This preserves the optionality your analysis identified as valuable, while allowing us to defer the operational complexity until it is clearly justified by load.

I would welcome the opportunity to discuss this framing with you ahead of Wednesday, so that whatever recommendation we bring to Priya reflects the strongest version of both positions rather than a compromise neither of us fully endorses. I am available before noon Pacific tomorrow if a thirty-minute conversation would be useful.

Either way, the work you have put into this analysis has improved the decision, and I want that acknowledged regardless of where we land.

Best,
Ana
