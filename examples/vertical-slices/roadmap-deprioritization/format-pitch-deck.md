---
entry_id: pitch-deck
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Slide 1: Title

**Insights Dashboard: Q3 Decision and Path Forward**

Product Update | September 2026 | Maya Chen, Product Lead

## Slide 2: The Commitment We Made

We promised Insights to four enterprise accounts by end of Q3.

- Sales positioned Insights as a closing point on several deals
- Customers were given a firm Q3 delivery date
- Their expectation: saved views and scheduled reports, fully working

## Slide 3: What Changed

A mandatory billing-system migration grew past its estimate and consumed all available engineering capacity.

- The migration is non-optional - regulatory and contract requirements require it before year-end
- The two workstreams cannot share capacity without risking both
- Insights and the migration cannot finish in Q3 at the same time

## Slide 4: Shipping Now Would Still Break the Promise

The current Insights build is missing the two capabilities customers specifically asked for.

- Missing: saved-view persistence layer
- Missing: scheduled-report delivery
- Releasing without these delivers exactly the wrong experience at the highest-stakes moment

## Slide 5: The Recommendation

Cut Insights from Q3. Ship a data stopgap. Deliver the full product in Q1 2027.

- Insights dashboard: deferred to Q1 2027, target March 13
- CSV export of the same underlying data: ships September 26
- Customers access their data now; the dashboard follows in Q1

## Slide 6: The Stopgap Is Real and Ready

The underlying data is already queryable. The export is a two-week build.

- Backend endpoint complete: September 19
- Frontend integration and QA complete: September 24
- Release: September 26
- Customers open the file in any spreadsheet or BI tool - no setup required

## Slide 7: Why a Clean Deferral Is the Lower-Cost Path

Rework after a disappointing release costs more than an honest delay.

- Billing migration completes without competing pressure - lower defect risk from context switching
- Q1 Insights ships to the full committed spec with no scope shortcuts
- Trust is repaired through direct outreach, not through a half-built product

## Slide 8: The Team Has a Plan

Owners are assigned. Timelines are set. Outreach starts this week.

- CSV export: Dario Reyes - build underway, September 26 release
- Customer outreach: Jordan Park - written notices to four accounts this week; calls scheduled for accounts that flagged strong Q3 dependency
- Insights Q1 kickoff: Maya Chen - design document starts October 6, after billing release stabilizes

## Slide 9: What We Need from You

Two sign-offs and one action this week.

- Leadership: confirm March 13, 2027 as the Insights date we can put in customer-facing communications
- Sales: flag any of the four accounts that need a direct call before written notices go out - send to Jordan Park by Thursday
- No objections by end of day Friday means we proceed on this plan
