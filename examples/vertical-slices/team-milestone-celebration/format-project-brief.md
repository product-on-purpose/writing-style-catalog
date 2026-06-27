---
entry_id: project-brief
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Project Halyard - Project Brief

## Goal

Eliminate the checkout system as a source of elevated cart abandonment by rebuilding it as a parallel service, migrating real traffic incrementally, and decommissioning the legacy flow only after the new system proves itself under production load.

## Background

Cart abandonment has been elevated for three years and instrumentation points consistently to the payment flow as the primary driver. The existing checkout system is not safely modifiable: it was built through five years of emergency patches, carries no meaningful test coverage, and is coupled to the session layer in ways the team does not fully understand. Two prior refactor attempts stalled and were abandoned.

Engineering lead Priya Nakamura and PM Linh Tran evaluated three options in early 2025. A parallel-run replacement - building the new system alongside the existing one and migrating traffic by user cohort - was recommended as the only approach that allows live validation under real load with a safe rollback if the new system fails. It is also the most expensive option to build and operate.

## Scope

### In scope

- Design and build a new checkout service as a separate system, not a modification of the existing one
- Incremental traffic migration by user cohort starting at one percent
- Dual instrumentation and rollback capability throughout the migration period
- Decommission of the legacy checkout after the new service handles at least two peak-load periods without incident

### Out of scope

- Changes to the payment processor integration beyond what the new service requires
- Cart, discovery, or session features outside the checkout flow itself
- Mobile app or third-party channel experiences not routed through the web pipeline
- Performance work unrelated to the cart abandonment problem

## Constraints

- The existing checkout must remain live and fully supported for the entire migration period - no planned downtime
- No single cutover window is permitted; the new system must be validated under real traffic before the legacy system is decommissioned
- The team will carry dual operational overhead throughout: two runbooks, two on-call rotations, and session compatibility across the boundary
- Full migration is estimated at twelve to fourteen months from kickoff to decommission

## Success Criteria

- Cart abandonment drops in migrated cohorts before full cutover, confirming the hypothesis with live data
- The new checkout handles at least two peak-load periods without latency degradation or rollback events
- The rollback path is exercised and confirmed to work before full traffic is committed
- The legacy system is decommissioned without a customer-visible incident

## Team

- Owner: Linh Tran (product), Priya Nakamura (engineering)
- Contributors: Dev Okonkwo (backend), Marcus Ferreira (infrastructure)
- Informed: Engineering leadership, product leadership, stakeholders tracking cart abandonment metrics
