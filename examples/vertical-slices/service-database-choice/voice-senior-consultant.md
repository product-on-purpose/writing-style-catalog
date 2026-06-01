---
entry_id: senior-consultant
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Senior Consultant on: Choosing between Postgres and DynamoDB

### Diagnosis

The Lattice Notify decision is best read through a reversibility-versus-optionality lens. The two candidates differ less in raw technical capability than in what they buy and what they spend. The relevant question is not "which database is better for notifications" - both are defensible - but "which option preserves the most strategic flexibility for a 50-person, eight-engineer Series B with a contingent 10x growth scenario." Viewed through that frame, three findings emerge.

First, the engineering risk profile is asymmetric. Postgres carries known unknowns the team has solved before. DynamoDB carries unknown unknowns the team has not yet encountered. At this stage of company, organizational learning capacity is the binding constraint, not infrastructure capacity. The strongest read of the evidence is that team focus is a more scarce resource than write throughput.

Second, the optionality cost is real but bounded. Choosing Postgres now does not foreclose DynamoDB later. A migration at the point of demonstrated need is approximately the 3-6 weeks of rework Priya has already accepted as the downside scenario. Choosing DynamoDB now, by contrast, foreclosures simplicity for the duration of the service's life; the operational surface area does not shrink back.

Third, the partnership scenario is a forcing function but not a fait accompli. The data are consistent with a Slack deal closing in the next six months, but the analysis should not assume it. On balance, the right move is to optimize for the modal case and prepare for the upside, not the reverse.

### Recommendation

We would recommend Option A, Postgres, with two conditions. First, instrument the service from day one with the metrics that would signal a need to migrate - write contention, queue depth, p99 latency under load. Second, scope a DynamoDB readiness spike for Q3 that the team can pull off the shelf if the partnership lands. This assumes the team's Postgres operational competence holds at 10x; if Ana believes it does not, the call changes.

The Friday deadline is achievable on this recommendation. Wednesday's meeting should ratify the call and assign the instrumentation work.
