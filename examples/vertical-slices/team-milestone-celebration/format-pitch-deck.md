---
entry_id: pitch-deck
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Slide 1: The Problem We Were Carrying

- Cart abandonment elevated for three years - engineering knew the source was checkout
- Codebase: five years of emergency patches, no meaningful test coverage, session coupling the team did not fully understand
- Two previous refactor attempts stalled and were abandoned
- **The math became undeniable. We stopped deferring.**

---

## Slide 2: The Approach We Chose

We had three options. We took the expensive one.

- Option A: Keep patching - 18-month estimate, high regression risk, no guarantee of reaching targets
- Option B: Big-bang cutover - one launch window, no rollback if something failed under real load
- **Option C: Parallel run** - build the new system alongside the old, migrate by cohort, keep the fallback live until proven

The only way to validate checkout under checkout load is to route real checkout load through it.

---

## Slide 3: Why the Expensive Option Was the Right Option

- Every previous patch added debt faster than it removed symptoms
- A big-bang cutover gave the team one shot with no recovery path
- The parallel run cost more to operate but gave the team the ability to be right about readiness - not just optimistic
- **The cost of not building it right had grown larger than the cost of building it right**

---

## Slide 4: Five Phases, Fourteen Months, No User Saw the Migration

| Phase | Timeframe | Traffic | What Happened |
|---|---|---|---|
| 1 - Shadow mode | Months 1-4 | 0% live | New pipeline built and instrumented |
| 2 - Canary | Months 5-9 | 5% of sessions | A/B comparison running |
| 3 - Ramp | Months 10-12 | Up to 80% | Near-miss #1 caught and resolved |
| 4 - Pause | Month 13 | Full ramp held | Near-miss #2 found; launch date slipped |
| 5 - Launch | Month 14 | 100% | Final cutover completed under peak load |

---

## Slide 5: What the Data Says Now

- **Shipped June 13, 2026** - full cutover, zero rollback
- **Peak weekend June 14-15** - sustained load, no latency spikes, no rollback triggers
- **Cart completion rate** held at the target the team modeled in January
- **Both near-misses resolved before any user was affected**

What the parallel run actually bought us: the ability to find problems under real conditions and fix them before they counted.

---

## Slide 6: What It Actually Cost

- 14 months of dual operations - two live systems, two runbooks, two on-call rotations
- Two planned launch windows slipped - once for the February cart-state mismatch, once for the April payment callback rewrite
- Engineering bandwidth that produced no visible features for over a year
- **Every slip was the correct call. Each was cheaper than shipping a broken checkout.**

---

## Slide 7: The People Who Held This

**Dani Rowe** - called the hold on the March launch when the February near-miss was not yet resolved. The call cost three weeks. It was right.

**Marcus Teel** - filed the cart-state mismatch when he could have marked it low severity and moved on. The fix was his initiative.

**Jordan Osei** - rewrote the payment callback handler over a weekend when a smaller patch was available and tempting. He chose the right fix.

**Sam Wickfield** - held the regression bar on June 9 when the schedule pressure was at its peak and every hour of delay felt enormous.

**Priya Vasquez** - held the line with stakeholders through two slipped dates and kept "we ship when it is ready" from collapsing into "we ship on a date."

None of this appears in a commit count. It is the kind of work that determines whether a rebuilt system holds under load or fails quietly three months after launch.

---

## Slide 8: Three Things We Need to Close This Right

1. **Recognize the team publicly.** The work was invisible to the rest of the organization for fourteen months. The close is the moment to change that.

2. **Protect the June 30 retrospective.** Fourteen months is not a standard sprint. The retrospective needs space - not a calendar slot - to do justice to what the team learned.

3. **Hold the post-launch window.** Mia Chen's analytics team delivers the cart-abandonment baseline on July 7. The six weeks after that date need to be clear for the team to read the results and act before the next planning cycle.

The team earned the ask. These three things are how we close the project the same way we ran it.
