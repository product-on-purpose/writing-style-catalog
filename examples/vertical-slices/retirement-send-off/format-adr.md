---
entry_id: adr
axis: format
topic_slug: retirement-send-off
topic_label: Marking a long-serving colleague's departure
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# [ADR-0047] Backfill and Knowledge Architecture Following Howard's Departure

## Status

Accepted

## Context

Howard Kessler is retiring after twenty-six years with Meridian Systems. He held the same position - Senior Operations Coordinator - for the last nineteen of those years while the organization around him was restructured three times and lost roughly half its institutional knowledge in two rounds of reductions.

Howard did not accumulate authority. He accumulated clarity. When a vendor contract dispute surfaced in late 2019 and the team lead who had owned that relationship was gone, Howard produced the original scope-of-work, the 2017 amendment, and the name of the right contact at the vendor. When a production incident required a rollback that our documented runbook no longer matched due to a platform migration nobody had fully recorded, Howard sketched the actual system state from memory on a whiteboard. He was correct.

He also kept junior members from making expensive mistakes - quietly, without making anyone feel corrected. Three people on this floor have said, separately and unbidden, that Howard is the reason their career at Meridian survived the first two years.

We have an approved backfill budget and a formal job requisition. The forces at play now:

- The institutional memory Howard carried is largely unwritten and cannot be extracted in his remaining weeks.
- His informal mentoring function has no defined owner and no formal acknowledgment anywhere in our org structure.
- His steady, unflappable presence during crises was itself a stabilizing input to decisions made under pressure. That is not a deliverable we can assign to a job description.
- A replacement into his formal role will cover the operational coordination load, but will not carry what Howard carried.

## Decision

We will fill the posted position and we will not treat that backfill as equivalent to Howard's departure. The new hire covers real work that must continue.

We will also stand up a quarterly knowledge capture practice - not a one-time documentation sprint. Team leads will record the decisions and constraints that shaped each major area of operations. We are naming this practice after what it actually is: it exists because Howard is leaving and we have now confirmed we had a single point of memory.

We will designate informal mentoring as an explicit expectation for two senior individual contributors, without creating a formal "mentor" title, because that title has historically read as sidelining rather than recognition at Meridian.

## Consequences

### Positive

- Operational coordination work continues without a queue gap.
- The quarterly knowledge capture practice, if sustained, reduces single-point-of-memory risk over time across all senior departures, not only Howard's.
- Naming the gap honestly gives leadership a real picture rather than a false assumption that a backfill closes it.

### Negative

- The new hire will carry missing context for at least the first year. We are accepting this rather than pretending we can prevent it.
- The knowledge capture practice requires scheduled senior time that is currently unallocated. The opportunity cost is real and will be felt.
- No one will replace Howard as a calming presence when something breaks at 11 p.m. That capability does not reconstruct by process. We will be less stable in those moments for a while.

### Neutral

- Howard's vendor relationships will transfer during a negotiated handoff period. Those relationships will change in character. That is not a problem to solve; it is a fact to manage.
