---
entry_id: researcher
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Researcher on: Choosing between Postgres and DynamoDB

This note summarizes what the available evidence licenses us to say about the Postgres-versus-DynamoDB decision for the Lattice Notify notification service, ahead of the architecture meeting on Wednesday.

The volume estimate is 500K events per day at launch. We have not yet validated this against a working prototype; it is derived from product forecasts and the current notification rate inferred from in-app activity. The 10x scenario is a contingent forecast tied to the Slack partnership and carries the uncertainty of that deal closing. We cannot rule out a higher peak-to-average ratio than the daily total implies; we have not measured burst behavior.

On the engineering question, we have direct evidence from two prior Lattice Notify services that the team operates Postgres reliably up to and beyond the projected peak write rate. The sample is small, n equals two, and neither is structured as a high-cardinality notification workload, so the inference to this service rests on an assumption about access-pattern similarity that we have not tested. The team has shipped no production DynamoDB workloads. Our prior on a six-month DynamoDB learning curve is therefore weak and likely optimistic; the engineering literature on cross-database adoption in small teams suggests skill gaps consistently outlast their initial estimates.

The data are consistent with two readings. The first: Postgres carries lower variance because the team's operational competence is the dominant factor and is observed, not inferred. The second: DynamoDB carries lower variance at the 10x scenario specifically, but this advantage materializes only in the partnership-success branch, which is a contingent outcome with unknown probability.

What the evidence does not license us to say: that either option is unambiguously correct in expectation. The choice rests on prior beliefs about (a) the probability of the Slack deal closing, and (b) the team's actual rather than projected DynamoDB learning curve. Both are knowable through cheaper experiments before Friday. We recommend a one-day spike on each before the Wednesday meeting; the readout would tighten the calibration substantially.
