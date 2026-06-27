---
entry_id: rfc
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# RFC-0031: Defer Insights Dashboard to Q1; Ship CSV Export as Q3 Stopgap

## Status

Under Review

## Author(s)

Maya Chen, Product Lead - September 8, 2026

## Problem

The team entered Q3 with a firm commitment to ship the Insights analytics dashboard by September 30. Three key enterprise customers received delivery dates and Sales has been using the Q3 commitment as a closing point for at least one additional account.

In early Q3, the mandatory billing-system migration surfaced scope that was not visible during Q3 planning. The migration is non-optional: regulatory and contract dependencies require it to complete before year-end. Current estimates put the migration engineering work at consuming the capacity block originally reserved for Insights. Both projects cannot share that capacity without putting both deliverables at risk.

At the same time, the Insights build is not in a state that could ship to customers without harm. The two capabilities customers specifically asked for - saved-view persistence and scheduled-report delivery - are not complete. Shipping the dashboard now would deliver a product that fails at the exact use cases that were sold.

We need to decide how to allocate remaining Q3 capacity, what to tell customers, and whether a stopgap can reduce the cost of the delay.

## Proposed Approach

Defer the Insights dashboard to Q1 2027, targeting March 13. Complete the billing-system migration cleanly in Q3. Ship a CSV export of the Insights data layer before September 30, giving customers access to their underlying event data while the full dashboard is under development.

Delivery timeline under this proposal:

- CSV export backend endpoint: September 19 target. Owner: Dario Reyes (engineering).
- CSV export frontend integration and QA: September 24 target.
- CSV export release: September 26 target.
- Billing migration production release: week of September 19.
- Direct written notice to the four key accounts: this week. Individual calls for accounts with hard dependencies on the Q3 date. Owner: Jordan Park (customer success).

The Q1 Insights scope is frozen at the current committed spec: the full dashboard with saved views, scheduled reports, and the six views originally planned. Scope change requests received during the deferral period are queued for Q1 planning and are not folded in silently.

## Alternatives Considered

**Ship Insights on the Q3 date in its current state.** The build is missing saved-view persistence and scheduled-report delivery. These are the two capabilities that were sold to enterprise customers. Shipping without them delivers a product that fails at the use cases it was promised for. We would face immediate trust damage, and rework against a live product with real customer data is more expensive than a delay negotiated before release.

**Split engineering to work both projects in parallel.** The billing migration has a sequential critical path; the capacity-intensive work cannot be parallelized with Insights development without significant handoff risk and context-switching overhead. A split approach would extend both timelines and put both deliverables at risk. The migration has a hard year-end deadline.

**Delay the billing migration and keep Insights on schedule.** The migration is non-optional. Regulatory and contract dependencies require completion before year-end. This option does not exist.

## Open Questions

**1. Is the CSV export sufficient for the three customers who were given a Q3 delivery date?**
Jordan Park should confirm whether any of them has a hard contractual or operational dependency on the in-app dashboard specifically, not just the underlying data. If one does, that shapes the outreach and may require a different commitment than "access to your data via CSV." This needs an answer before the notices go out, not after.

**2. Can Q1 capacity be confirmed in time to put a hard date in customer communications?**
March 13, 2027 is a directional target. The Q1 capacity plan does not close until Q4 planning. Telling customers "March 13" carries commitment weight we may not be able to back yet. Should we offer a range, or hold the specific date until Q4 planning confirms it? If we defer the date, we should say so explicitly, not leave it vague.

**3. Who owns the customer-facing message?**
Engineering can provide a technical facts sheet: what was committed, what changed, what ships by September 30, and what ships in Q1. Sales and customer success should own the words that go to customers and the tone of each conversation. This RFC proposes the path and the stopgap; it does not propose the message. A separate brief should cover customer communication and I am not the right author for it.

**4. Should any Insights scope additions be considered now, while the deferral window is open?**
My recommendation is no: freeze the spec and ship what was committed. But if Sales has accounts that will only accept the delay with a specific addition to the Q1 scope, that should surface now, not in Q4 planning.

## Consequences

Accepting this proposal means no half-built dashboard ships in Q3. The committed spec - saved views, scheduled reports, the six originally planned views - ships in Q1. The billing migration completes without competing capacity pressure, reducing defect risk from context switching. Customers get access to their underlying event data before September 30 via CSV export, with no installation or onboarding step required.

The costs are real and should be named directly. Three customers who were given a Q3 delivery date will need direct communication. Trust was set on a commitment that is now being broken, and a CSV export does not substitute for the dashboard those customers were sold. The repair is in the honesty of the communication, not in the stopgap itself. The Q1 target is also directional until Q4 planning closes; it should not appear in customer-facing communications as a hard date until capacity is confirmed.

If this proposal is not accepted and Insights ships on the Q3 date in its current state, the billing migration absorbs competing capacity pressure, increasing defect risk from a divided workstream. Customers receive a dashboard missing the two features they specifically requested.

In either direction, customer communication needs to happen this week. The window to manage this proactively is closing.
