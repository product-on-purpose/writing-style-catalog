---
entry_id: decision-log
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Context

At the start of Q3, Insights was committed as a Q3 deliverable - a real-time analytics dashboard surfacing product usage data. The commitment was made to the sales team as a close tool for several in-flight deals, and to key customers who had requested the capability explicitly. Two engineering teams were allocated.

In week seven of Q3, a mandatory billing-system migration - a compliance requirement triggered by a vendor contract change - overran its projected timeline by four weeks. Both teams were reassigned to prevent the billing system from entering an unsupported state before the contract deadline. Neither team could continue Insights work during that period. When the migration completed, six weeks remained in Q3. Completing Insights to a stable, testable state required nine to ten weeks of remaining engineering work.

## Options Considered

Three options were on the table as of August 19, once the migration overrun was clear:

1. Ship on the original Q3 date, with the export, filtering, and drill-down features incomplete.
2. Move Insights to Q1 with no interim deliverable.
3. Move Insights to Q1 and ship a CSV export of the underlying data in September, usable in a spreadsheet or BI tool.

## Criteria

Three constraints governed the evaluation, in order of weight:

- Do not ship a partial product against a full promise. A half-built dashboard resets customer expectations downward.
- Provide something of value before year-end to the customers who waited. A pure deferral is harder to absorb than a deferral with interim capability.
- The interim capability must be low-risk. The team is stretched after the migration; a complex stopgap adds compounding risk.

## Decision

Insights moves to Q1. A CSV export of the underlying data ships in September before Q3 closes.

Option 1 was eliminated: shipping a partial dashboard against a full-scope promise sets an expectation we cannot sustain. Option 2 was viable but left customers with nothing for two quarters. Option 3 is chosen because a CSV export is low-scope, low-risk, and genuinely useful. Customers who need the data can load it into a spreadsheet or BI tool and begin analysis now. It does not substitute for Insights, but it delivers the underlying data access that motivated the original request.

The migration overrun is the proximate cause of this change, not a shift in product priority. The reasoning behind the Q3 commitment was sound when it was made. The capacity that would have delivered Insights was consumed by a compliance dependency that could not itself be deferred.
