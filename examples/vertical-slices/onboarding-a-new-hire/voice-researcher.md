---
entry_id: researcher
axis: voice
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Two weeks is long enough to build structural conditions; it is not long enough to know whether a new engineer has found real belonging on the team. The distinction matters, because what can be arranged in a fortnight and what accumulates over months are different kinds of things. Onboarding plans that conflate the two tend to optimize for the wrong signal.

What the evidence supports. The pattern across onboarding post-mortems on service-oriented teams is consistent enough to treat as a finding: access latency is the most reliable predictor of first-contribution timing. Engineers who cannot run the service without workaround on day one tend to reach their first real change later, controlling for seniority. The mechanism is plausible - a broken environment forecloses exploration and forces reliance on others for each small step - but the causal chain is inferred, not measured. A confound worth naming: teams with fast access setup also tend to have better internal documentation and more deliberate pairing culture, so the effect may be compositional rather than attributable to tooling setup alone.

A paired first change in week two has a different evidentiary status. The observation is behavioral: engineers who ship something real, even small, before the end of their first fortnight report higher confidence and ask more exploratory questions in the following weeks. These are self-reports; treat them as directionally useful, not precise.

What the evidence does not settle. Belonging resists the same instrumentation as productivity. We observe that engineers who know who owns what - a specific person, not a team name - ask questions at a higher rate and with a shorter latency. We infer this reduces the social cost of not-knowing. We cannot determine whether that is a sufficient condition for belonging or merely a correlate of it.

The inference I am willing to make. The evidence licenses this priority order: access and tooling first, because it sets the ceiling on everything else; a pairing structure for week two with a change small enough to ship but real enough to matter; and an explicit ownership map handed to Priya as a document, not described verbally. A written map can be consulted at 9pm during an on-call incident; a remembered one cannot.

What I would track. By end of week one: service runs locally without workaround. By end of week two: one change shipped to production. Neither metric measures belonging. The proxy I find most useful: question latency. Does Priya ask within hours of a blocker, or absorb delays quietly? A declining gap between blocker and question is the early indicator I find most predictive.
