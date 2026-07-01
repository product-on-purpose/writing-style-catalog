---
entry_id: memo
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

TO: Engineering Department
FROM: Priya Vasquez, Program Lead
DATE: June 25, 2026
RE: Project Halyard Closed - Parallel-Run Migration Confirmed as Standard Practice for High-Risk Rebuilds

This memo confirms that Project Halyard, the rebuild of the checkout system, is closed, and establishes the parallel-run approach used to ship it as the standard pattern for any future rebuild of a system the business cannot safely take offline. Full cutover to the new checkout completed June 13. The new system held through the first peak weekend without incident, and the legacy system is now in read-only archive mode, with full decommission on schedule for July 14.

Checkout carried three years of elevated cart abandonment before this project began. The legacy system could not be safely modified in place: it had accumulated five years of emergency patches, carried no meaningful test coverage, and was coupled to the session layer in ways no one on the team could fully account for. Two prior attempts to refactor it in place had already stalled and been abandoned. ADR-0017 recorded the decision to reject both continued patching and a single-cutover replacement in favor of building the new system alongside the old one, migrating traffic by cohort, and keeping the old system live as a fallback until the new one had proven itself under real peak load. That decision is the reason this took fourteen months instead of a single release window, and it is the reason nothing broke in front of a customer.

The parallel run earned its cost. Two defects surfaced during the migration serious enough to have reached customers had the architecture not caught them first. In February, Marcus Teel found a cart-state mismatch in staging that would have corrupted multi-item orders under split payment; the fix pushed the planned March launch to April. In April, Jordan Osei identified a race condition between the payment processor callback and the session store during the final dress rehearsal and rewrote the callback handler rather than patching around it, which pushed the following launch window back eleven days. Both delays were judged worth taking at the time, and both judgments held.

This memo also puts on record the individual decisions that made the approach work rather than merely exist on paper. Dani Rowe called the hold on the March launch date while the February defect was still unresolved. Sam Wickfield held the regression bar on June 9 rather than waive it under schedule pressure. Dev Okonkwo and Marcus Ferreira carried the operational load of running two live checkout systems for the full fourteen months. None of this shows up in a commit count, and none of it was optional to the outcome.

This memo establishes June 13, 2026 as the completion date of the checkout migration and confirms the parallel-run pattern - build alongside the existing system, migrate by cohort, keep a live fallback until the replacement is proven under real load - as the default approach for any future rebuild carrying comparable risk. Teams scoping a replacement for a system that cannot tolerate a failed single-attempt cutover should treat Project Halyard and ADR-0017 as the reference case.
