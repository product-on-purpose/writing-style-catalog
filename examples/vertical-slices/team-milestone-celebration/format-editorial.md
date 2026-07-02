---
entry_id: editorial
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Project Halyard Slipped Twice. That Is Why It Held.

*The Editorial Board - Engineering*

Project Halyard slipped its launch date twice, and both slips are the strongest evidence we have that the team built it correctly. We should stop scoring migrations on whether they hit the first date on the plan, and start funding, as a default, the practice that let this one miss two dates instead of shipping a defect.

The checkout rebuild ran the new payment flow alongside the old one for fourteen months, migrating traffic by cohort from a one percent canary up to full cutover on June 13, 2026, while keeping the legacy flow live and fully maintained at every step in between. No customer saw a degraded checkout on any day of that migration. For most of its run the work produced no feature anyone outside the team could see, which made it easy to overlook when attention and budget went to work that shipped something visible every sprint.

That parallel-run architecture was not the cheap option, and it was not free even after it worked. It was approved in ADR-0017 in February 2025 specifically because a one-shot cutover would have given the team exactly one chance to get checkout right under real load, with no way back if it did not. The chosen path meant fourteen months of dual instrumentation and two on-call runbooks running at once, and engineering attention the team could not spend on anything visible. That cost was known and accepted before the first line of the new flow was written.

It bought exactly what it was supposed to buy. In February, engineer Marcus Teel caught a cart-state mismatch in staging that would have corrupted multi-item orders under split payment; fixing it properly took three more weeks and pushed the March launch to April. In April, Jordan Osei found a race condition between the payment callback and the session store during the final dress rehearsal; the fix meant rewriting the handler, not patching around it, and cost eleven more days. Both times, someone with the authority to hold the launch chose to absorb the schedule hit instead of shipping a known defect: Dani Rowe called the March hold against real pressure to ship, and Priya Vasquez called the second one the same way. Two engineers, two leads, four separate decisions, and every one of them landed on the same side of the same tradeoff. That is not luck. That is a team using the architecture it built exactly as it was designed to be used.

Nothing about how this organization currently tracks migrations distinguishes that outcome from a team that hit the original date by shipping the February defect anyway. Both would have looked identical on a roadmap slide the week they closed. Only one of them is the outcome anyone actually wants running under a customer's cart.

We are asking engineering leadership to make the parallel-run pattern the funded default for any future migration that touches payment or checkout, not a case a team has to argue for from scratch, and to write down in advance who has the authority to hold a launch date and on what evidence, so the next team is not left to reconstruct that under the same pressure this one absorbed twice with no document telling them they were allowed to. Project Halyard proved the pattern works. It should not have to prove it twice.
