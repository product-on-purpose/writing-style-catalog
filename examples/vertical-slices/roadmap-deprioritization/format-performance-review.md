---
entry_id: performance-review
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Performance Review: Maya Chen

## Period
July 1, 2026 to September 30, 2026 (Q3 2026)

## Reviewer
Owen Marsh, VP of Product

## Summary
Maya's Q3 centered on the Insights dashboard: a Q3 date already committed to all four affected accounts became unworkable once the billing migration consumed the capacity Insights depended on, and Maya led the team to a resolution that protected the customer relationship instead of the calendar. Insights did not ship. The judgment and communication in that response carry real weight in the rating below, despite the miss.

## Performance Against Goals

### Ship Insights on the Q3 Commitment
Rating: Not Met
All four accounts had a Q3 delivery date from sales before engineering had validated capacity against it. When the billing migration displaced that capacity, Maya evaluated shipping the current build anyway and rejected it: it was missing saved-view persistence and scheduled-report delivery, the two capabilities those accounts had specifically asked for, and shipping without them would have failed the exact use case it was sold against. Insights was deferred to Q1 2027 and recorded in ADR-0027. Not Met on its own terms; the decision itself is credited under Strengths.

### Land the Billing Migration Without Destabilizing Payments
Rating: Met
The migration was contractually required before year end and stayed on track despite absorbing scope that was not visible at Q3 planning. Payment flows were validated in staging, and the production release went out the week of September 19 with no rollback. Letting the migration take the capacity it needed, rather than splitting the team across two at-risk projects, is why both workstreams ended the quarter defensible instead of both in trouble.

### Maintain Stakeholder Trust Through the Change
Rating: Met
Written notice reached all four accounts by mid-September, with individual calls lined up through Jordan Park for the accounts with the strongest Q3 dependency rather than one form notice for everyone. Maya flagged the project Red as soon as the date stopped being defensible instead of waiting for the miss to surface on its own, and brought leadership a specific ask, sign-off on citing March 13, 2027 to customers, rather than an open-ended request for patience.

## Strengths
- Named the trade-off instead of splitting the difference. Rather than shipping a partial dashboard or slowing the migration to protect Insights, Maya made the harder call explicitly and put it in writing (ADR-0027) rather than letting it happen by default through slippage.
- Built a real stopgap, not just an apology. The CSV export shipped September 26, inside the original Q3 window, turning "we missed the date" into "here is what you can use today, and exactly when you get the rest."
- Sequenced the communication on purpose: internal Red status, then sales talking points, then account outreach, so no one downstream was improvising an answer before the official notice landed.

## Development Areas
- Two major workstreams entered Q3 without a formal prioritization call between them, and the eventual conflict required an escalation that cost time the team did not have. That call is Maya's to make before a capacity conflict becomes a scramble. She has already committed to the fix: an engineering capacity review gate for customer-facing dates, due at Q4 planning kickoff.
- The original commitment gave customers a quarter label instead of a target date, so accounts had no concrete anchor when the deferral notice landed. That gap sat upstream of Maya's control this quarter, but the fix forward does not: she and Jordan Park have agreed to pair every customer-facing commitment with a named date and one stated contingency risk, starting with the Q1 2027 Insights commitment.

## Goals for Next Period
- Land the engineering capacity review gate so no customer-facing delivery date ships without a named engineer's feasibility sign-off - by October 6, 2026.
- Codify the single-priority rule with Dario Reyes: when two workstreams compete for capacity in one quarter, one is paused rather than both slowed - by October 13, 2026.
- Confirm the Q1 2027 Insights capacity plan in Q4 planning and apply the target-date-plus-risk standard to that commitment, so March 13, 2027 becomes committed engineering time instead of directional - by end of Q4 2026 planning.

## Overall Rating
Meets Expectations. One committed deliverable slipped a full two quarters, which keeps this short of Exceeds Expectations. The judgment and cross-team coordination in the response are what the next level of this role looks like, which keeps it well clear of Below Expectations.

## Additional Notes
Full decision record: ADR-0027, Defer Insights Dashboard to Q1; Ship CSV Export as Q3 Stopgap. The Q1 2027 date carries real risk until Q4 planning closes it; a second missed date to the same four accounts would be a very different conversation than the first.
