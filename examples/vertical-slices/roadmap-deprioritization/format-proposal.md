---
entry_id: proposal
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Proposal: Insights Dashboard Deferral and Q3 Stopgap Plan

**Prepared for:** Product Leadership Team
**Prepared by:** Maya Chen, Product Lead
**Date:** September 5, 2026

## Executive Summary

The Insights analytics dashboard cannot ship by October 1 without releasing a product that is missing the two features your committed customers specifically asked for. This proposal asks the Product Leadership Team to approve deferring the full Insights dashboard to Q1 2027, shipping a CSV export of the underlying event data before September 30 as an immediate stopgap, and authorizing direct outreach to the four affected enterprise accounts this week. Approving this plan protects the customer relationship more than a half-built release would, and the stopgap gives those customers usable access to their data before the quarter closes.

## The Problem

The team entered Q3 with a firm commitment to ship the Insights analytics dashboard before quarter-end. Sales used this commitment as a closing point with enterprise accounts, and four customers were given a specific delivery date.

The mandatory billing-system migration that was already in progress expanded significantly past its original estimate. The migration is not optional: regulatory requirements and active contracts require it to complete before year-end. Completing it to a production-ready standard requires the full capacity of the engineering team through the week of September 19. That leaves no capacity to bring Insights to a shippable state by October 1 without pulling engineers off the migration mid-stream and risking both workstreams.

The Insights build is currently missing its saved-view persistence layer and its scheduled-report delivery feature. Those are the two capabilities the committed customers specifically requested when Sales closed their agreements. Releasing without them does not fulfill the commitment that was made - it ships a product that fails at the exact use cases for which it was sold. That outcome creates a harder recovery problem than a well-communicated delay does.

## Proposed Approach

We propose three concurrent actions:

**Defer Insights to Q1 2027.** The full dashboard - including saved views, scheduled reports, date-range controls, and the six views in the original spec - ships in Q1 2027 with a target release of March 13. The Q1 scope will be confirmed and frozen in the Q4 planning cycle, giving the team a clean runway once the billing migration stabilizes.

**Ship a CSV export by September 26.** The underlying event data that Insights will eventually visualize is already queryable from the data layer. A CSV export of that data can be built and released in approximately two weeks without touching the billing migration workstream. Customers who receive the export can load it into a spreadsheet or BI tool of their choice and begin working with their data inside the quarter.

**Reach the four affected accounts directly this week.** Written notices go out during the week of September 8. Accounts that flagged a strong dependency on the Q3 date receive a direct call before the written notice arrives. The message will be honest: the date has changed, here is why, here is what you can use now, and here is the confirmed Q1 target.

This approach is right for Meridian because the CSV export keeps the customer relationship active during the deferral. A delay alone is a broken promise; a delay paired with immediate access to the underlying data is a partial delivery that gives customers something to work with while the team completes the product correctly.

## Scope and Deliverables

**Included in this proposal:**

- CSV export of the Insights event data layer, available to all accounts before September 30. The export contains one row per event, with columns for user ID, event name, UTC timestamp, session ID, and plan tier at the time of the event.
- Written notice to all four committed accounts during the week of September 8, with the new Q1 2027 target date and instructions for accessing the CSV export.
- Direct call to any account that requests one, or that customer success identifies as high-dependency before notices go out.
- Q1 2027 Insights dashboard, scoped to six views, filter controls, date-range selection, saved views, and scheduled summary emails. This is the original Q3 spec; no additions will be folded in before Q1 planning closes.
- Q1 scope confirmation in the Q4 planning cycle, to be completed by the first week of November.

**Not included in this proposal:**

- A partial or reduced-scope dashboard release in Q3. No in-app analytics interface ships before the full dashboard is ready.
- Scope changes to Insights during the deferral period. Requests received between now and the Q1 planning cycle are queued for review; none will be accepted without a formal scope decision.
- Commercial resolution for affected accounts. If any account requests a credit or other remedy, that conversation is owned by Sales and their account executive. Engineering and product will provide the technical facts; pricing and compensation decisions are not part of this plan.

## Timeline

| Milestone | Owner | Target Date |
| --- | --- | --- |
| Leadership approval of this proposal | Product Leadership | September 8, 2026 |
| Written notices to all four committed accounts | Jordan Park | September 12, 2026 |
| CSV export backend endpoint complete | Dario Reyes | September 19, 2026 |
| Billing migration production release | Dario Reyes | September 19, 2026 |
| CSV export frontend integration and QA | Dario Reyes | September 24, 2026 |
| CSV export live for all accounts | Dario Reyes | September 26, 2026 |
| Insights engineering design document begins | Maya Chen / Dario Reyes | October 6, 2026 |
| Q1 Insights scope confirmed in Q4 planning | Maya Chen | Early November, 2026 |
| Insights Q1 dashboard release | Dario Reyes | March 13, 2027 |

One risk applies to the CSV export date: if the billing production release on September 19 surfaces regressions, the engineering team will triage those before returning to export integration. In that scenario, the CSV export could slip to the week of September 30. There is a one-week buffer before the quarter closes, so a modest slip is recoverable, but September 30 is a hard deadline - not a target.

## Team and Credentials

- **Maya Chen, Product Lead** - owns the Insights roadmap, the Q1 scope definition, and the communication strategy for affected accounts. Authored this proposal and will lead the Q4 planning engagement to confirm the Q1 build.
- **Dario Reyes, Engineering Lead** - owns the CSV export build and the billing migration production release. Sized the export at two weeks of work and confirmed it can run in parallel with billing stabilization without dependency conflicts.
- **Jordan Park, Customer Success** - owns direct outreach to all four committed accounts, will manage call scheduling for high-dependency accounts, and will serve as the customer-facing point of contact through the deferral period.

## Investment

The CSV export requires approximately two weeks of engineering time from Dario Reyes, working in parallel with billing migration QA. No incremental headcount or budget outside the existing Q3 allocation is required for this work.

The Q1 Insights build will be planned and sized during Q4 planning; no additional budget is requested as part of this proposal.

The cost of not acting is a Q3 release that fails at the committed use cases, followed by emergency rework during a period when the team is also stabilizing the billing system, onboarding Q4 priorities, and managing customer escalations from a disappointing first impression. That sequence carries more risk to the engineering roadmap and to the four customer relationships than a transparent delay paired with a working stopgap does.

## Next Steps

To move forward, the Product Leadership Team needs to provide three approvals by end of day September 8, 2026:

1. **Approval to defer Insights to Q1 2027.** This authorizes the team to communicate the new date to customers and to the Sales organization.
2. **Approval to include March 13, 2027 as the customer-facing Insights target date.** Customer success needs this date in writing before notices go out; we will not commit to it externally without your sign-off.
3. **Confirmation that Sales owns any commercial escalations from affected accounts.** Engineering and product will supply the technical facts; account executives handle any pricing or credit conversations.

Please reply to Maya Chen by September 8 with your approval or any modifications. If no objections are received by end of day, the team will treat the plan as approved and begin customer outreach on September 9.
