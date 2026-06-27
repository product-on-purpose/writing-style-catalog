---
entry_id: project-brief
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Insights Dashboard Q1 Delivery - Project Brief

## Goal

Deliver the Insights analytics dashboard - with saved views, scheduled reports, and date-range filtering - to the four committed enterprise accounts by March 13, 2027, fulfilling the Q3 2026 commitment deferred by the billing-system migration.

## Background

The Insights dashboard was promised to four enterprise accounts as a Q3 2026 deliverable. In early Q3, the mandatory billing-system migration expanded past its planned scope and consumed the engineering capacity allocated to Insights. The two capabilities those customers specifically asked for - saved-view persistence and scheduled report delivery - could not be completed without displacing the migration, which carries regulatory and contract dependencies that cannot slip. The team deferred Insights to Q1 2027 and shipped a CSV export of the underlying data as a bridge. Q1 delivery is now the outstanding commitment.

## Scope

### In scope

- Full in-app analytics dashboard: date-range selectors, trend charts, per-feature and per-user breakdowns
- Saved views and scheduled summary email delivery (the two capabilities cut from the Q3 build)
- Onboarding path for customers currently using the CSV export stopgap

### Out of scope

- Changes to the CSV export format or pipeline (maintained as-is through the Q1 release)
- Net-new analytics dimensions or event types not in the original Q3 spec
- Billing system work (migration completed Q3; treated as a stable dependency, not a scope item)

## Constraints

- March 13, 2027 is the release target; this date will be shared with committed accounts in writing this week and cannot move without another customer communication cycle
- Engineering design begins October 6, 2026, after the billing production release on September 19 stabilizes
- Feature scope is frozen at the Q3 spec for this release cycle; no new requests are folded in before launch

## Success Criteria

- Dashboard ships on or before March 13, 2027 with saved views and scheduled reports included
- Each of the four committed accounts confirms the delivered product meets the use cases originally sold to them
- No further Q1 slip occurs; if a risk to the March date surfaces, leadership is notified before any external commitment is made

## Team

- Owner: Maya Chen (product)
- Contributors: Dario Reyes (engineering), Jordan Park (customer success)
- Informed: Sales, leadership, the four key enterprise accounts
