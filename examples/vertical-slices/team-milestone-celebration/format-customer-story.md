---
entry_id: customer-story
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Northlane Checkout Engineering: Zero Customer-Facing Incidents Across a Fourteen-Month Checkout Migration

## About Northlane Checkout Engineering

Northlane is an online retailer that processes every transaction through a single checkout flow. Checkout Engineering is the team that owns that flow, from cart through payment confirmation, for every order Northlane ships.

## The Challenge

Cart abandonment at Northlane had been elevated for three years, and the checkout system behind it had become too fragile to change with confidence. Five years of emergency patches had left it without meaningful test coverage and tightly coupled to the session layer in ways the team could not fully document. Two earlier attempts to refactor the flow in place had stalled and were abandoned before reaching production.

The team weighed two other paths before settling on a third. Patching around the problem indefinitely would take an estimated eighteen months to reach a maintainable state, with regression risk the whole way and no guarantee of moving cart abandonment at the end of it. A single-cutover rebuild was faster to build, but it meant one launch with no way back if the new system failed under real checkout load. Neither option gave the team a way to be wrong safely on a system that touches every order Northlane processes, and being wrong safely was the requirement that mattered most.

## The Solution

Checkout Engineering built the new checkout as a separate service and used Waymark, Northlane Platform Engineering's internal migration platform, to route live traffic to it by cohort, starting at one percent. Waymark handled the routing logic and the rollback path: the team could move a cohort back to the legacy flow in minutes if something looked wrong, without a customer-facing incident and without an emergency deploy. The legacy checkout stayed live and fully maintained as the fallback for the entire fourteen months, which meant every stage of the migration, from the one-percent canary through a five-percent rollout, an eighty-percent ramp, and finally full traffic, could be reversed.

That safety net is what let the team hold the launch twice instead of shipping around problems it found late. In February, engineer Marcus Teel found a cart-state mismatch in staging that would have corrupted multi-item orders paid with split payment; the fix took three additional weeks. In April, engineer Jordan Osei caught a race condition between the payment processor's callback and the session store during the final dress rehearsal, which required rewriting the callback handler rather than patching around it. Both were caught because engineers were reading the data carefully enough to notice something wrong, not because a test suite flagged them, and both were fixed before any customer encountered either one.

## The Results

The full migration completed on June 13, 2026, and the rebuilt checkout held through its first weekend of peak customer traffic: no latency spike above threshold, no rollback triggered, and cart completion holding at the target the team had modeled back in January.

Waymark's rollback path was exercised twice during the migration, in October and December 2025, and both times the affected cohort moved back to the legacy flow with no customer-visible impact, which is the exact scenario the parallel architecture was built to handle. Cart abandonment in the migrated cohorts was already trending down before the full cutover, ahead of a clean baseline measurement the analytics team expects to publish in July once enough post-cutover data has accumulated.

"Waymark gave us a way to be wrong safely," said Priya Vasquez, Program Lead for Checkout Engineering. "We found two serious bugs after we thought we were ready to launch. Because we could hold a cohort at five percent instead of going all in on day one, being wrong cost us three weeks in February and eleven days in April, not a middle-of-the-night page. That is the only reason both of those bugs got caught before a customer did, and it is the reason I would run a migration this size the same way again."
