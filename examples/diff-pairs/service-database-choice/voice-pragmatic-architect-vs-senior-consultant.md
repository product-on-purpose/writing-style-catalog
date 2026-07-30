---
diff_pair_id: voice-pragmatic-architect-vs-senior-consultant-service-database-choice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
axis_varied: voice
entry_a: pragmatic-architect
entry_b: senior-consultant
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Voice swap - `pragmatic-architect` vs `senior-consultant`

**Topic:** How to choose between Postgres and DynamoDB for a new service
**Axis varied:** voice
**A:** `pragmatic-architect` - A senior technical voice that leads with tradeoffs, names constraints explicitly, and treats every design decision as a bet with known odds.
**B:** `senior-consultant` - A polished advisory voice that diagnoses a situation against a named framework before recommending action, comfortable with hedged confidence.

## What to notice

These two are the closest confusable pair in the Voice axis, and both land on the same answer
here: Postgres. The verdict matches; the action plan does not. A prescribes a partitioned
events table, a Redis-backed queue, and a revisit at 5x volume. B prescribes day-one
instrumentation and a Q3 DynamoDB readiness spike, and makes the whole recommendation
conditional on Ana's judgment. Since each render was generated independently per entry, treat
this as verdict parity rather than a controlled voice-only experiment.

That divergence is worth reading as evidence rather than noise, because it falls along exactly
the line the two voices differ on. The distinction is not "technical versus polished." It is
**who is left holding the decision.**

**A owns the decision and hands over an implementation.** It opens with the verdict in the
first sentence ("We should ship the Lattice Notify notification service on Postgres"), then
justifies backward. It ranks its constraints out loud ("three constraints, in this order")
and does the arithmetic in the open: 500K events per day becomes "roughly 6 writes per
second," the 10x case becomes "60 writes per second." It argues by naming each option's
**failure mode** and grading them by what is known: "The failure mode of staying on Postgres
is known... The failure mode of going DynamoDB now is unknown." It closes with something a
team could build on Monday: a dedicated schema, a partitioned events table, a Redis-backed
queue. The register is first-person singular and accountable: "My call for Wednesday."

**B frames the decision and hands it back to the client.** It arrives under headings,
`Diagnosis` before `Recommendation`, so the method precedes the answer. It names its lens
before using it ("best read through a reversibility-versus-optionality lens") and it rejects
the question as posed before answering: "The relevant question is not 'which database is
better for notifications' ... but 'which option preserves the most strategic flexibility.'"
Findings are enumerated (First, Second, Third). The evidential register is hedged and
attributive: "The strongest read of the evidence is," "The data are consistent with," "On
balance." The recommendation is first-person plural ("We would recommend Option A") and it
is explicitly **conditional on someone else's judgment**: "This assumes the team's Postgres
operational competence holds at 10x; if Ana believes it does not, the call changes." It ends
by delegating: "Wednesday's meeting should ratify the call."

**The sharpest single tell.** A computes; B characterizes. Where A writes "6 writes per
second," B writes "the strongest read of the evidence." Both are rigorous, but A's rigor is
arithmetic the reader can check, and B's is a named frame the reader is asked to accept.

**If you are choosing between them:** pick `pragmatic-architect` when you have the standing
to decide and the reader needs to act. Pick `senior-consultant` when the decision is not
yours to make and the reader needs a defensible basis for making it.

---

## A: `pragmatic-architect`

## Pragmatic Architect on: Choosing between Postgres and DynamoDB

We should ship the Lattice Notify notification service on Postgres. The decision turns on three constraints, in this order: operational surface area, team skill, and the cost of being wrong.

500K events per day is not a Postgres scaling problem. It is roughly 6 writes per second sustained, with bursty peaks we can absorb with a partitioned table and a queue. The 10x Slack-partnership scenario gets us to 60 writes per second, which is still well inside what a properly indexed Postgres instance handles before we need to think about read replicas or partitioning by tenant. Ana is right that we have shipped at this scale before. We know the failure modes, we know the recovery playbooks, and the four-person on-call rotation already carries the pager for Postgres.

Marcus's argument for DynamoDB is not wrong on the access pattern - notifications are key-value writes with TTL-based reads, which is exactly what DynamoDB does well. But the cost we would pay is real: a second datastore in production, cross-database query patterns the team will reinvent badly under deadline pressure, and a learning curve that lands in the middle of the partnership push, not before it. If Slack lands, we will want senior engineers on the integration, not on figuring out why our DynamoDB partition keys are hot.

The failure mode of staying on Postgres is known: at some growth multiple beyond 10x, we hit write contention and have to migrate. Priya, that migration is the 3-6 week of rework you flagged, and it is recoverable. The failure mode of going DynamoDB now is unknown: we do not yet know what we do not know about operating it, and we will learn during the partnership window.

My call for Wednesday: Postgres, with a dedicated notifications schema, a partitioned events table, and a Redis-backed queue for delivery. We revisit at 5x current volume. If the Slack deal lands and the curve looks steeper than that, we put DynamoDB on the roadmap as a planned migration, not an emergency one. Friday deadline is achievable.

---

## B: `senior-consultant`

## Senior Consultant on: Choosing between Postgres and DynamoDB

### Diagnosis

The Lattice Notify decision is best read through a reversibility-versus-optionality lens. The two candidates differ less in raw technical capability than in what they buy and what they spend. The relevant question is not "which database is better for notifications" - both are defensible - but "which option preserves the most strategic flexibility for a 50-person, eight-engineer Series B with a contingent 10x growth scenario." Viewed through that frame, three findings emerge.

First, the engineering risk profile is asymmetric. Postgres carries known unknowns the team has solved before. DynamoDB carries unknown unknowns the team has not yet encountered. At this stage of company, organizational learning capacity is the binding constraint, not infrastructure capacity. The strongest read of the evidence is that team focus is a more scarce resource than write throughput.

Second, the optionality cost is real but bounded. Choosing Postgres now does not foreclose DynamoDB later. A migration at the point of demonstrated need is approximately the 3-6 weeks of rework Priya has already accepted as the downside scenario. Choosing DynamoDB now, by contrast, foreclosures simplicity for the duration of the service's life; the operational surface area does not shrink back.

Third, the partnership scenario is a forcing function but not a fait accompli. The data are consistent with a Slack deal closing in the next six months, but the analysis should not assume it. On balance, the right move is to optimize for the modal case and prepare for the upside, not the reverse.

### Recommendation

We would recommend Option A, Postgres, with two conditions. First, instrument the service from day one with the metrics that would signal a need to migrate - write contention, queue depth, p99 latency under load. Second, scope a DynamoDB readiness spike for Q3 that the team can pull off the shelf if the partnership lands. This assumes the team's Postgres operational competence holds at 10x; if Ana believes it does not, the call changes.

The Friday deadline is achievable on this recommendation. Wednesday's meeting should ratify the call and assign the instrumentation work.
