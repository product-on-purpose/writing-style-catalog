---
entry_id: postmortem
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Q3 Insights Dashboard Commitment Miss

## Severity

SEV-3

## Summary

The team committed the Insights analytics dashboard for a Q3 2026 release. A mandatory billing-system migration expanded past its planned scope mid-quarter and consumed the engineering capacity allocated to the dashboard. The Q3 commitment cannot be met. Four enterprise accounts were given a Q3 delivery date and will require direct outreach. A CSV data export ships September 26 as a stopgap; the full dashboard moves to Q1 2027 (target March 13, 2027).

## Timeline

- 2026-06-10 - Q3 planning completed. Insights dashboard committed for Q3 release. Billing-system migration scoped as a parallel workstream with its own capacity allocation. The two workstreams are treated as capacity-independent in the plan.
- 2026-07-07 - Q3 begins. Insights and billing migration enter active development concurrently.
- 2026-07-21 - Billing migration team surfaces a dependency on a third-party payment processor API that requires a custom adapter not included in the original estimate. Internal projection grows by approximately three weeks.
- 2026-08-04 - Engineering flags that the extended billing migration and the Insights dashboard cannot both complete in Q3 with available capacity. This is the first explicit cross-workstream escalation; the conflict had been developing since July 21 without being surfaced to product or leadership.
- 2026-08-11 - Product, engineering, and leadership review three options: ship a reduced Insights build on schedule, slip the billing migration, or defer Insights entirely. Shipping a reduced build is ruled out because the two capabilities the committed accounts specifically requested (saved views and scheduled reports) are not present in the current build. Slipping the billing migration is ruled out because of regulatory and contract requirements.
- 2026-08-18 - Decision recorded (ADR-0027): defer Insights to Q1 2027; ship a CSV export of the underlying data layer by September 26 as a stopgap.
- 2026-08-25 - Sales and customer success notified internally. Account-level plans prepared for the four key accounts.
- 2026-09-01 - Written notices begin going to the four key accounts. Calls scheduled for accounts that flagged strong dependency on the Q3 date.
- 2026-09-19 - Billing migration production release targeted (billing migration backend endpoint complete; Insights CSV export backend endpoint also targeted complete this date).
- 2026-09-24 - Insights CSV export frontend integration and QA targeted complete. Owner: Dario Reyes.
- 2026-09-26 - CSV export target ship date.

## Root Cause

The Q3 planning process did not model capacity risk across concurrent mandatory workstreams. Insights and the billing migration were planned as if their capacity pools were independent, but the engineers with the relevant expertise overlap significantly across both projects. When the billing migration expanded, no pre-agreed priority rule or reallocation trigger existed. The discovery that the two workstreams were competing for the same capacity happened five weeks into the quarter, too late for the Insights commitment to be recovered within Q3.

The proximate trigger was an undiscovered payment-processor API dependency that expanded billing migration scope by three weeks. The systemic condition was a planning process that treated parallel workstreams as capacity-independent when they were not, and that lacked a formal escalation path to surface scope expansion before it became a commitment miss.

## Impact

- Stakeholders affected: four enterprise accounts given a Q3 delivery commitment; the sales team that positioned Insights as a closing point; internal stakeholders relying on Q3 delivery for downstream planning
- Duration of exposure: commitment given June 2026; miss confirmed August 18, 2026; customer notification began September 1, 2026
- Features affected: Insights analytics dashboard (deferred to Q1 2027); CSV export stopgap added to Q3 scope to partially offset the gap

## Contributing Factors

- Q3 planning used point estimates for the billing migration without a risk buffer appropriate for a dependency-heavy infrastructure project
- No cross-workstream capacity model existed to detect overlapping engineering ownership between Insights and billing migration
- The three-week scope expansion was not surfaced to product or leadership until week five of the quarter; the team's internal escalation path for scope changes was informal and produced no visible signal
- Insights was committed to customers before the billing migration was technically de-risked; the sequencing assumption that billing would land cleanly before Insights needed full capacity was never made explicit in the planning artifacts

## Action Items

- [ ] Add a cross-workstream capacity model to Q4 planning that maps shared engineering ownership across all parallel mandatory workstreams - Owner: Maya Chen - Due: 2026-10-06
- [ ] Define a scope-change escalation protocol for infrastructure projects: any workstream whose estimate grows more than 20% must surface to product and leadership within five business days - Owner: Dario Reyes (engineering) - Due: 2026-10-06
- [ ] Require that customer commitments on features with a dependency on a parallel infrastructure workstream include an explicit sequencing assumption and a stated risk condition in the commitment artifact - Owner: Maya Chen - Due: 2026-10-15
- [ ] Run a trust-repair review with the four affected accounts after the CSV export ships; document what further action each account requires - Owner: Jordan Park (customer success) - Due: 2026-10-10

## Lessons Learned

Capacity models that treat parallel workstreams as independent are fragile when engineering expertise overlaps across them. The billing migration and Insights dashboard were not competing for generic bandwidth; they were competing for the specific engineers who understood both systems. That dependency was invisible in the planning artifacts and went undetected for five weeks.

The lag between when the scope expansion became apparent internally and when it was formally escalated cost the team its options. Earlier escalation would not have prevented the commitment miss entirely, but it would have moved customer communication from September to July and created room to explore partial mitigations before they became infeasible.

A commitment given to a customer before the dependencies enabling it are de-risked is a bet presented as a plan. Q4 planning will make that distinction explicit and require that any feature commitment dependent on a parallel mandatory workstream carry a named risk condition.
