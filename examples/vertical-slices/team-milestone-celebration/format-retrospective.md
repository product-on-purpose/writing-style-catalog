---
entry_id: retrospective
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Retrospective: Project Halyard - Checkout Rebuild (Full Project Arc)

## Date

June 30, 2026

## What Went Well

- **Parallel-run architecture justified its cost.** Running both checkout flows simultaneously for fourteen months was operationally expensive, but it paid off directly: the February and April near-misses were caught and fully resolved before any user saw them. The rollback path was not theoretical.
- **Both slip decisions were called correctly and held.** Dani Rowe called the hold on the March window; Priya Vasquez called the hold on the second. Both were made under real schedule pressure. The February near-miss (Marcus Teel's cart-state mismatch in multi-item orders under split payment) and the April near-miss (Jordan Osei's payment-callback race condition under load) would have reached production if either call had bent to that pressure.
- **Shadow-comparison tooling surfaced issues the automated suite missed.** Dom Ferreira's shadow-mode infrastructure made the first near-miss visible during the Phase 3 ramp. The test suite did not catch it on its own; the comparison layer did.
- **The final cutover held through peak load.** June 13 went cleanly. The June 13-14 peak weekend ran without latency spikes, rollback triggers, or customer impact. Cart completion rate held at the modeled target.
- **Yuki Tanaka held the "ship when it is ready" line with stakeholders through both slips.** The team never had to choose between shipping safely and shipping on a date. That protection required sustained effort across fourteen months and was not free to maintain.
- **Sam Wickfield held the regression bar at the end when the pressure was at its highest.** The June 9 freeze call was contested. It was correct, and the cutover was clean because of it.

## What Did Not Go Well

- **Automated test coverage did not surface either near-miss.** Both the February and April issues were found through manual inspection - one via shadow-mode comparison, one during a live dress rehearsal. Payment-critical paths required human attention to validate; the test suite alone was not sufficient.
- **On-call burden concentrated on a small set of engineers for the full 14-month parallel-track period.** Maintaining two live checkout systems required sustained coverage that did not rotate evenly across the team. The people who carried the most operational load had no meaningful relief window.
- **The work was largely invisible to the rest of the organization.** No shippable features came out of the migration period. Communicating progress to non-engineering stakeholders required repeated framing, and protecting the team's capacity during the final push was harder than it should have been.
- **Decision criteria for calling a launch hold were not documented in advance.** Both slip decisions were made well, but they required individuals to absorb pressure without a shared frame for what justified a hold. A new team inheriting this architecture would have to reconstruct that frame under identical pressure.

## What Will We Change

- [ ] Define and assign explicit on-call rotation ownership for any future parallel-track project before the parallel run begins, not after it is under way. - Owner: Priya Vasquez - By: before next parallel-track kick-off
- [ ] Write a test coverage standard for payment-critical paths that specifies which scenarios require manual rehearsal in addition to automated tests. Ground the standard in the February and April near-miss scenarios as the minimum required cases. - Owner: Marcus Teel - By: July 31, 2026
- [ ] Document the decision criteria for calling a launch hold - what evidence is sufficient, who has authority, and what the escalation path looks like - so the next team does not reconstruct this under pressure. - Owner: Dani Rowe - By: July 7, 2026 (alongside the operational runbook handoff)
- [ ] Build a progress-communication template for long-running platform rebuilds that translates traffic-migration percentages into terms stakeholders outside engineering can track. - Owner: Yuki Tanaka - By: July 14, 2026

## Notes

This retrospective covers the full project arc: ADR-0017 acceptance (February 2025) through final cutover (June 13, 2026) and the first post-launch peak weekend (June 14-15, 2026). It is not a sprint retro. The working period is 14 months, and the format was adapted accordingly, as noted in the June 20 close-out status report.

The cart-abandonment baseline report from Mia Chen's analytics team is due July 7. Post-launch outcome data will be a separate artifact; clean attribution requires 21 days of post-cutover data without the parallel-period overlap. That document is not part of this retrospective.

The two near-miss postmortems are archived separately and carry more detail than the mentions here. Anyone using this retrospective for lessons-learned should read those documents alongside it.
