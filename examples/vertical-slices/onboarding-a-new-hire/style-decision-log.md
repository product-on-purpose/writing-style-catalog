---
entry_id: decision-log
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Decision: Priya's First Two Weeks

**Status:** Decided
**Date:** 2026-06-26
**Owner:** Roshan Mehta (Engineering Lead)

## Context

Priya started Monday on a team that ships a service-oriented backend daily and runs a rotating on-call schedule she will join in week four. She has solid fundamentals but has not touched our service mesh, deployment pipeline, or the ownership model that coordinates work across six engineers. Two weeks is a fixed window. Marco, her primary pair, has capacity for roughly three focused hours per day in week one, less in week two as a customer migration runs.

## Options Considered

**Option A: Self-directed ramp.** Reading list, documentation, a service map, check-in at end of week one. Low team cost, high cost to Priya. Engineers ramping alone in a complex service topology accumulate gaps they don't know they have.

**Option B: Full-pair for two weeks.** Marco shadows every PR in real time. Comprehensive, but his bandwidth drops in week two, and the result is often learned dependency rather than independence.

**Option C: Structured sequence with a paired first change.** Explicit milestones (access, walkthroughs, paired ticket) with named owners, anchored to a real shipped change by end of week two.

## Criteria

1. **She ships something real.** A diff merged to main - the full deploy path navigated - is the threshold for genuine ramp completion.
2. **Buddy cost must be sustainable.** Exhausting Marco in week one risks cutting corners in week two when she needs him more.
3. **She learns ownership, not just operation.** An engineer who can deploy but cannot identify who to escalate to is unblocked only until the first incident.
4. **She belongs, not just functions.** Engineers who function but feel isolated start leaving by month three.

## Decision

Option C. Week one: Marco runs morning walkthroughs, one service per day. Access and tooling are handled by the admin checklist in parallel. By Thursday, Priya and Marco pick a ticket together; Priya drives the scoping discussion. Week two: Priya drives the ticket; Marco is available but not reviewing every line before commit.

The load-bearing call is the specific paired change over open exploration. An open ramp leaves Priya knowing the codebase without knowing whether she can ship under real conditions. One merged diff closes that gap before on-call begins. It also gives her a social entry point: "I shipped X" reads differently than "I've been reading the docs."

Marco's involvement is front-loaded into week one mornings rather than distributed evenly - that matches where uncertainty is highest and keeps his bandwidth available in week two.

Open question logged now: who handles introductions to the other six engineers? Marco will not cover this during walkthroughs. Owner: Roshan. Due Monday of week two.
