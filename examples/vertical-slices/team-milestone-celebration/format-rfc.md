---
entry_id: rfc
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# RFC-0042: Rebuild Checkout as a Parallel System with Incremental Traffic Migration

## Status

Accepted (see ADR-0017, 2025-02-14)

## Author(s)

Priya Nakamura, Engineering Lead - 2025-01-28

## Problem

Cart abandonment has been elevated for three years. Every instrumentation pass we have run points to the payment flow as the primary contributor. The underlying problem is not any single bug; it is that the checkout system is not safely modifiable. It has accumulated five years of emergency patches, carries no meaningful test coverage, and is tightly coupled to the session layer in ways the team does not fully understand. Two previous attempts to refactor it in place stalled and were abandoned.

The system is not broken enough to trigger an emergency response, which is exactly what has made it easy to defer. But the compounding cost is real, and every month we wait makes the session-layer coupling harder to unwind.

This RFC proposes a path forward and asks reviewers to push back before we commit to it.

## Proposed Approach

Build the new checkout as a separate service and run it in parallel with the existing system. Route traffic to the new system incrementally, starting at one percent of sessions and expanding by cohort as confidence builds. Keep the old checkout live and fully maintained until the new system has held through at least two peak-load periods, then decommission.

The core argument for this approach: the only way to validate a checkout system is to route real checkout load through it. Without a live fallback, the team has one shot. With a parallel run, we can roll back individual cohorts if something goes wrong, without a site incident.

The proposed rollout sequence:

- Months 1-4: new pipeline built; shadow mode only, zero live traffic
- Months 5-9: canary at five percent of sessions; A/B comparison running
- Months 10-12: ramp to eighty percent; hold for first peak-load period
- Month 13+: full cutover after second peak-load validation

Dev Okonkwo would own the backend service build. Marcus Ferreira would own the infrastructure layer and the traffic-routing mechanism. Linh Tran would manage stakeholder communication through a timeline that will not produce visible user-facing changes for the first six to nine months.

This approach costs more to operate than the alternatives. We will maintain two live checkout systems simultaneously, with separate on-call runbooks, dual instrumentation, and session compatibility requirements across the boundary. I am estimating the parallel period at ten to fourteen months. That overhead is the cost of the rollback capability, and I believe it is worth paying.

## Alternatives Considered

**Incremental patching (in place):** Continue addressing checkout debt one patch at a time. Our current estimate is eighteen months to reach a maintainable state, with meaningful regression risk throughout, and no guarantee the end state fixes cart abandonment. We have tried this twice. Both attempts stalled when session-layer coupling made "small" changes unsafe. I do not believe a third attempt reaches a different outcome.

**Big-bang replacement:** Build the new system in private and cut over in a single release window. Lower ongoing operational burden than a parallel run. The risk is that we have no fallback if the new system fails under real load. Checkout failure is not an acceptable site incident. A big-bang cutover would require a level of pre-launch confidence we have not been able to achieve even in high-fidelity staging environments.

**Defer another quarter:** Wait until current sprint priorities clear. The case against: the cart abandonment math does not improve with time, two abandoned refactor attempts have already cost the team momentum, and delay is a choice with a compounding cost - not a neutral option.

## Open Questions

**How long can the team sustain the dual-system operational burden?** I have estimated ten to fourteen months. If the parallel period runs longer due to near-misses or integration delays, the overhead compounds. I want reviewers who have run similar migrations to tell me where this estimate is optimistic and what typically extends the timeline.

**Is the session-compatibility layer a larger risk than I am representing?** Dev has done a preliminary audit and found several undocumented session-state assumptions in the old code. I am not confident we have found all of them. If we have missed something material, it will surface in the canary phase rather than at full cutover - which is survivable. But I want to hear whether anyone thinks the audit gaps are likely to be larger.

**What should the stakeholder communication plan say about visible progress?** The first six to nine months of this project will produce no visible user-facing changes. That is hard to explain while the cart abandonment metric is still visible to leadership. I am asking reviewers to identify where Linh's draft communication plan will not hold.

## Consequences

If accepted: the team will carry the operational overhead of two live checkout systems for approximately a year. No visible user-facing features will ship from the checkout team for the first two quarters. That cost is real and should not be invisible to anyone approving resourcing for this work.

If accepted and successful: we will have a checkout system validated under real production load before the old one is turned off. Cart abandonment improvements will be measurable by cohort before full cutover. The session-layer debt will be gone, and the team will have an instrumented baseline for future checkout work.

If rejected: we return to the alternatives. Incremental patching has stalled twice. A big-bang replacement remains on the table but carries the full-incident risk described above. Deferring again is also a choice, with a cost that accumulates each week.

Review period closes 2025-02-07. Please comment in the review thread or send feedback directly. I will synthesize responses and update the status by 2025-02-12.
