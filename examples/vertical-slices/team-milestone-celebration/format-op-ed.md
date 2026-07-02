---
entry_id: op-ed
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Nobody Noticed We Rebuilt Checkout. That Was the Point.

*By Yuki Tanaka*

Two weeks ago my team finished a fourteen-month rebuild of our checkout system, and if everything went the way it was supposed to, you never noticed. That is not a failure of our communications. It is the only honest measure of the work, and it is exactly the kind of measure most organizations are not built to reward.

The checkout had been broken for three years in ways that cost real money every week: cart abandonment stayed elevated, session-state bugs and payment-step drop-offs bled revenue, and the system underneath it all had absorbed five years of emergency patches with no meaningful test coverage to catch what any of them broke. Two earlier attempts to fix it in place had already failed. Early last year we chose from three paths: keep patching for another eighteen months with no guarantee we would land anywhere better, replace the whole system in a single release window and hope it held, or build the new system alongside the old one and move traffic over gradually, cohort by cohort, starting at one percent, with the old checkout standing by the entire time as a working fallback. Priya, our engineering lead, put the case for the third option plainly: the only way to validate a system built to handle checkout load is to route real checkout load through it. We chose the expensive option, before a single line of the new system existed.

Here is what that expense bought us. In February, an engineer named Marcus Teel found a silent cart-state mismatch in staging that would have corrupted multi-item orders under split payment; catching it cost three weeks and pushed a March launch to April. In April, Jordan Osei found a race condition between the payment callback and the session store during the final dress rehearsal, rewrote the handler instead of patching around it in a weekend sprint, and cost eleven more days. Neither issue was caught by the automated test suite alone. Both were found because an engineer was reading real production traffic carefully enough to notice something wrong, which is only possible when real traffic is already flowing through the new system while the old one is still standing there to catch what falls through it. A single-cutover migration does not give you that option. It gives you one shot, and a rollback plan that has never been tested against real load.

That fallback was not theoretical, either. We exercised rollback twice, in October and December, and neither time did a customer feel it happen. But I want to be honest about the bill, because pretending the slow path is free is its own kind of dishonesty: two on-call rotations for fourteen months, two runbooks, a growing pile of session-compatibility shims, and a team that had to hold both systems in its head at once for over a year. Slow and safe is not a synonym for easy. It is a trade you make on purpose, and you keep paying for it every sprint until the day you finally don't.

The hardest part of that year was not the engineering. It was that almost none of it showed up anywhere an organization usually looks for evidence of work. No feature shipped. No line moved on a roadmap slide. When Dani Rowe called a hold on the March date over a bug that was not yet fully understood, or when Sam Wickfield held the regression bar on June 9, with every hour of delay feeling enormous and the pressure to ship at its peak, those were the decisions that kept this migration a status update instead of an incident report. A commit count will never show you a hold that got called. It will only ever show you the ones that didn't. An organization that only has language for what shipped has no language for the decision that kept something from breaking, and it will eventually stop making room for the people willing to make that call.

The next time a team you manage asks for fourteen months to build something you will never see, resist the instinct to ask what they will have to show for it. Ask instead who would be explaining the outage if you had said no, and give them the time before you need the excuse.

*Yuki Tanaka managed the fourteen-month checkout migration described here and is the program manager who ran its dual-track rollout plan.*
