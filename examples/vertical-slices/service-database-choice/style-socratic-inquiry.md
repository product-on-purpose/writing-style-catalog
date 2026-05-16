---
entry_id: socratic-inquiry
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Socratic Inquiry on: Choosing between Postgres and DynamoDB

What are Ana, Marcus, and Priya actually disagreeing about on Wednesday at 2pm?

It looks at first like a database choice: Postgres or DynamoDB. But notice how often the conversation in the design doc keeps drifting away from the databases themselves and toward something else, something the engineers seem more reluctant to name. What is that something else?

Consider the access pattern. Lattice Notify's notification system is write-heavy, key-lookup, time-ordered. Both databases can serve this pattern; one is more naturally suited. If access-pattern fit were the load-bearing criterion, would the decision still be difficult? Or would it be a foregone conclusion that both engineers would have agreed to by Monday?

Now consider the four-person on-call rotation. None of them have operated DynamoDB in production. If on-call safety were the load-bearing criterion, would the decision still be difficult? Or would the answer be obvious in the other direction?

What does it mean that the decision is still difficult? Perhaps that both criteria are real, that neither dominates, and that the team is being asked to weigh them against each other. But against what scale? Engineering decisions get framed as engineering questions, but is this one really?

The 10x growth scenario depends on the Slack-partnership deal closing. The CRO says 60% confidence. What is the meaning of a 60% number in a decision that has to be made by Friday? Is it telling us something we did not know, or is it asking us a question we had been hoping someone else would answer?

Suppose the probability were 95%. What would you choose, and why?

Suppose it were 25%. What would you choose, and why?

What changed between those two answers? It was not the access pattern. It was not the team's familiarity with either system. It was not the on-call rotation size. What did change?

If your answer changed when the probability changed, then perhaps the decision is not really about databases at all. Perhaps it is about how confident the team is willing to be about a future event, and how much operational cost they are willing to pay to insure against being wrong.

If that is right, what is the question Ana should actually be asking in the Wednesday meeting?

Is it "which database is better for our access pattern"? Or is it something closer to "given that we cannot know whether the Slack deal will close, how do we make a choice that we can live with in either case"?

If the question is the second one, does either of the original positions, Ana's Postgres or Marcus's Dynamo, actually answer it? Or do they each answer half of it?

What would a path look like that answered both halves?

Consider a third option that neither engineer proposed initially: ship on the familiar system today, but pre-commit to a measurable trigger that fires a migration if the high-volume scenario actually materializes. Is that a compromise, or is it something different from a compromise? What does it cost? What does it preserve?

Who would feel that this path failed to honor their concern, and on what grounds?

If both Ana's concern (operational safety) and Marcus's concern (10x scenario fit) are addressed (the first at launch, the second through the trigger), what would the meeting on Wednesday look like? Would it still be a debate, or would it be a working session on the trigger threshold?

And if it is the second kind of meeting, what does that tell you about what the meeting was always going to be about, once the framing was right?

So: what is Friday's decision really for?
