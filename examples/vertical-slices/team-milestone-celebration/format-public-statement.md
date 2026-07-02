---
entry_id: public-statement
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**Northfield Commerce - Statement on Checkout Reliability**
June 29, 2026

For much of the past three years, checkout on Northfield Commerce has failed more customers than it should have, and we take responsibility for how long it took us to fix it. As of June 13, 2026, the checkout flow has been fully rebuilt end to end and is now handling all customer traffic.

During that period, customers using Northfield Commerce ran into dropped sessions mid-checkout, payments that failed on the first attempt and had to be retried, and a mobile checkout that in some cases would not render at all. Individually, our support team could resolve each case as it came in. Together, they meant carts were abandoned that should not have been, and customers lost time, and sometimes the item they were trying to buy. We heard about this directly from customers for at least three years before the work to fix it was finished. The length of that delay is on us, not on the customers who kept running into it.

Rather than patch a system we no longer fully understood, we built the new checkout as an independent service and spent fourteen months moving traffic to it gradually, cohort by cohort, so a new problem would surface in a small slice of traffic and could be caught before it reached most customers. Program lead Priya Vasquez and infrastructure lead Marcus Ferreira ran that migration from the first cohort to the final cutover; backend engineer Dev Okonkwo kept the old and new systems running side by side for the full fourteen months so that no customer saw a degraded checkout while the work was underway. We found two serious defects internally before a single customer did, in February and again in April of this year, and both times we chose to delay the launch rather than ship around the risk. Full cutover completed on June 13, 2026, and the new checkout held through its first weekend of peak demand without incident. Sam Wickfield's team has since finished the regression work needed to retire the old system, which is now in a thirty-day read-only archive.

The old system will be fully decommissioned on July 14, 2026, once that archive window closes; until then it stays available as a fallback, out of caution rather than expectation. We are not claiming this fixes every problem a checkout can ever have. We are saying the chronic ones customers told us about for three years are gone, and we built this the slow way specifically so that would be true on day one instead of something we had to walk back later. If checkout gives you trouble now, that is the exception, not the pattern, and we want to hear about it.

Priya Vasquez
Program Lead
Northfield Commerce
