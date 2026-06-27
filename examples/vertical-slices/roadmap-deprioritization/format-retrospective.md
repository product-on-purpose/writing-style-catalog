---
entry_id: retrospective
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Retrospective: Q3 2026 - Insights / Platform Team

## Date

September 30, 2026

## What Went Well

- The billing-system migration was prioritized correctly. Completing it before year-end removes a hard regulatory dependency, and the team executed without production incidents.
- The decision to ship a CSV export rather than release a half-built dashboard was sound. Customers get access to their underlying data before the quarter closes, and the team avoids creating a credibility hole going into Q1.
- Outreach to the four key accounts was proactive. Individual calls were offered alongside written notice, and communication went out before the quarter closed rather than after.
- ADR-0027 gave the deferral decision a permanent, searchable record. Anyone who needs the reasoning later can find it without asking.

## What Did Not Go Well

- The billing migration scope was not visible at Q3 planning. The work was non-optional, but the estimate was wrong early enough that it set a false expectation with sales and enterprise customers before anyone had a chance to course-correct.
- The sales-to-engineering loop moved too slowly. Sales positioned Insights as a closing point for enterprise accounts before engineering had validated the Q3 capacity plan. There was no checkpoint where a qualified estimate could have surfaced the risk before customers received a delivery date.
- Customers were given a quarter label rather than a target date, which left the four key accounts without a concrete anchor when the deferral notice arrived. The news landed abruptly for accounts that had planned around the original commitment.
- The team carried two major workstreams into Q3 without a formal prioritization decision. When the trade-off became unavoidable, it required an escalation that took time the team did not have.

## What Will We Change

- [ ] Add an engineering capacity review gate to the pre-commitment process for customer-facing delivery dates. No date leaves the team without a named engineer signing off on feasibility. Owner: Maya Chen. By: Q4 planning kickoff (October 6, 2026).
- [ ] Define a single-priority rule for the team: when two major workstreams compete for capacity in the same quarter, one is paused rather than both slowed. Codify this in the team operating agreement. Owner: Maya Chen + Dario Reyes. By: October 13, 2026.
- [ ] Introduce a mid-quarter scope check at week four of each quarter. If any workstream shows a twenty-percent-or-greater schedule slip, the product lead and engineering lead convene within forty-eight hours to make an explicit trade-off decision, not absorb the slip quietly. Owner: Dario Reyes. By: week five of Q4 (November 3, 2026).
- [ ] For the next customer delivery commitment, include a specific target date alongside the quarter label, and state one named contingency risk in writing at the time of commitment. Owner: Jordan Park + Maya Chen. By: next outbound commitment (Q1 2027 Insights, targeting March 13, 2027).

## Notes

The Q1 2027 Insights target (March 13, 2027) is directional and not yet backed by a closed capacity plan. Engineering design begins October 6 and the design document is the first real signal on whether March 13 is achievable. If scope concerns surface before the end of October, Maya owns raising them with leadership and key accounts before the expectation hardens.

Jordan Park should collect feedback from the four key accounts by October 14 on whether the CSV export (released September 26) is meeting their interim data needs. That feedback should inform whether any Q1 Insights scope needs to be reordered before the design document closes.
