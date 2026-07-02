---
entry_id: listicle
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# 7 Things Worth Remembering From Shipping Project Halyard

Project Halyard (checkout-reflow in the repo) shipped on June 13, and it is already compressing into the two-line version that survives in company memory: fourteen months, then it worked. That version is not wrong, just thin. Here are seven specifics from the parallel-run rebuild worth keeping before the thin version is all that is left.

1. **The old checkout was not broken. It was survivable, which is worse.**
   Session-state bugs, payment-step failures, and mobile re-render issues had been showing up for years, each one survivable enough on its own to get deprioritized. Cart abandonment stayed elevated for three years because nothing about the old system ever failed hard enough to force the question, and two earlier attempts to fix it in place had already stalled for the same reason. Project Halyard happened because someone finally built the case without waiting for a fire.

2. **We chose the most expensive option in the room, on purpose.**
   Three ways to fix checkout were on the table in early 2025: keep patching it (slow, no guaranteed outcome), replace it in one cutover (cheap, no rollback if it broke under real load), or build the new system in parallel and migrate traffic by cohort (the most expensive option to build and to run). Priya Nakamura and Linh Tran pushed for the parallel build on one argument: a system built for checkout load cannot be validated without routing real checkout load through it, and that cannot be done safely without a live fallback. The team picked the expensive option because it was the only one that let them be wrong in production without turning it into an incident.

3. **Fourteen months of running two checkout systems at once shows up nowhere on a roadmap slide.**
   Every week of the parallel run meant double instrumentation, two on-call runbooks, and a session-compatibility layer bridging both systems. Dev Okonkwo and Marcus Ferreira carried that load for the full fourteen months on top of their regular work, with nothing to point to externally because the old checkout looked exactly the same to everyone outside the team. That invisibility was the actual cost of choosing the parallel-run approach, not a side effect of it - a big-bang rewrite would have been cheaper to explain and more dangerous to run.

4. **The launch date moved twice, and both times it was the correct decision.**
   In February, Marcus Teel found a silent cart-state mismatch in staging that would have corrupted multi-item orders under split payment, and fixing it properly took three more weeks and pushed the March launch to April. In April, Jordan Osei found a race condition between the payment processor callback and the session store late enough in dress rehearsal that the fix meant rewriting the callback handler instead of patching around it, and the launch slipped again. Neither slip was a schedule failure - both were the schedule working exactly as a parallel-run system is supposed to work, catching the problem before a customer did.

5. **Neither near-miss came from a dashboard.**
   The automated test suite did not catch the cart-state mismatch or the callback race condition. Engineers reading staging data and dress-rehearsal logs closely enough to notice something that looked slightly wrong caught both instead. That is not a knock on the test suite so much as a reminder that the last mile of a system this load-bearing still runs on someone paying close attention on an ordinary day, not on a coverage percentage.

6. **The riskiest day of the project produced no story at all.**
   Full cutover happened June 13. The system then had to hold through its first weekend of real peak load with the legacy system sitting in read-only fallback and no quiet way to patch around a surprise. It held: cart completion stayed at the target the team had modeled back in January, and nothing triggered a rollback. The two days that could have produced the project's worst outage instead produced nothing worth a postmortem, which was the entire goal.

7. **The work that mattered most will never show up in a ticket count.**
   Dani Rowe called the hold on the March launch when the pressure to hit the date was real and the February issue was not yet fully resolved. Marcus Teel filed the cart-state bug on his own initiative when he could have marked it low severity and let it ride. Jordan Osei rewrote the payment callback handler over a weekend instead of taking the smaller patch that was sitting right there. Sam Wickfield held the regression bar on June 9 when every additional hour of delay felt enormous, and none of that shows up in a velocity chart even though it is the actual reason Halyard shipped clean.

The retrospective doc is coming, and it will look nothing like this one. This was just the version worth putting on record before the details started rounding off.
