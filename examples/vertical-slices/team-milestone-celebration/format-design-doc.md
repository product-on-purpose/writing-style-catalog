---
entry_id: design-doc
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Checkout Rebuild: Parallel-Run Architecture Design

## Status

Draft - January 2025

## Problem

The production checkout system cannot be safely modified. It has accumulated five years of emergency patches, carries no meaningful test coverage, and couples session state to payment logic in ways that are partially undocumented. Two prior attempts to refactor it in place both stalled: the risk surface was too wide to contain, and both teams eventually cut losses rather than ship a regression.

The consequence is visible in the metrics. Cart abandonment has been elevated for three years. Instrumentation points to the payment flow as the primary failure zone, but improving the payment flow requires touching the session layer, and touching the session layer without adequate test coverage is how the system arrived at its current state.

The constraints that shape the solution space:

- No full-downtime migration window. Checkout runs continuously. A planned outage long enough to support a cutover requires board-level approval, and that path is closed for this project.
- No in-place refactor. Two teams established that the existing coupling prevents safe incremental modification at any reasonable pace. A change to one subsystem creates regression surface in another; the coverage to protect against that regression does not exist.
- Must be validatable under real load before full cutover. Staging environments do not reproduce the edge cases that live sessions generate at volume. The only meaningful test of a checkout system is real checkout traffic.
- Must preserve rollback capability throughout. Any architecture that eliminates fallback to the current system before the new one is validated is unacceptable given the revenue exposure.

These constraints eliminate the in-place refactor and the big-bang cutover as viable paths. The remaining design space is a parallel-run approach: build a new pipeline alongside the current one, route real traffic to it incrementally, and decommission the old system only after sufficient validation under production conditions.

## Proposed Design

### Component Boundaries

The new checkout is deployed as a separate service (`checkout-v2`). A traffic router at the session boundary determines which pipeline handles each session. The legacy system (`checkout-v1`) remains live and on-call throughout the migration.

```
Client
  |
  v
[Session Gateway]  (unchanged)
  |
  +--[Traffic Router]--+---> checkout-v2  (new pipeline)
  |                    |
  +-> checkout-v1  <---+
  (legacy, fallback)   |
        |              |
        +--[Session Store (shared)]--+
```

The Session Gateway is the only public entry point and is not modified. The Traffic Router reads a routing key from session metadata to decide which pipeline receives the request. Both pipelines read from and write to a shared Session Store during the parallel period.

### Traffic Routing

Routing is cohort-based on a hash of `user_id mod N`, where N is a configurable shard count. This ensures that:

- A given user routes consistently to the same pipeline for the duration of their session.
- Rollback for a cohort is a configuration change, not a code deploy. Recovery time from a routing-level rollback is under five minutes.
- Coverage expands by widening the shard range in config, without a service deployment.

### Session Schema Contract

Both pipelines must read and write a compatible session format during the parallel period. All v2 extensions are namespaced under `v2_ext` so that v1 reads are unaffected by keys it does not recognize.

```json
{
  "session_id": "...",
  "cart_id": "...",
  "checkout_state": "...",
  "v2_ext": {
    "pipeline_version": "v2",
    "routing_shard": 42,
    "step_entered_at": "2025-03-01T14:22:00Z"
  }
}
```

The `v2_ext` key is absent for v1-routed sessions. The router populates it at session creation for v2-routed sessions. v2 must not remove or rename any field that v1 reads; removals require a compatibility shim reviewed before decommission.

### Observability

Both pipelines emit to a shared metrics namespace so that A/B comparison is possible at the dashboard level. Required instrumentation per pipeline:

- Step completion rate per checkout step, tagged by pipeline version
- Payment authorization latency (p50, p90, p99)
- Cart abandonment rate per session cohort
- Error rate per step, tagged by error class and pipeline version

A shadow comparison job runs on a 5-minute cadence and emits a divergence metric when v1 and v2 behavioral metrics differ by more than a configurable threshold for the same cohort. This is the primary signal for gate decisions.

### Rollout Phases

| Phase | Live traffic coverage | Gate to advance |
|---|---|---|
| Shadow | 0% (replaying v1 events) | No behavioral regressions over 7-day window |
| Canary | 1-5% of sessions | Cart completion rate within 2% of v1 for same cohort |
| Ramp | 5% to 80% | No divergence alerts; at least one peak-load period covered |
| Cutover | 100% | Two peak-load periods without a rollback trigger |

Advancing between phases requires explicit sign-off; there is no automatic promotion. Each gate decision is recorded.

### Decommission Criteria

Decommission of `checkout-v1` begins only after:

1. `checkout-v2` has handled two peak-load periods at 100% traffic without a rollback event.
2. All session-compatibility shims have been reviewed for removal safety.
3. A 31-day archive window for v1 logs and session state has elapsed.

Decommission is a separate milestone and is not in scope for this design document.

## Alternatives Considered

**In-place refactor with incremental coverage.** Build test coverage incrementally while modifying the existing system. Rejected because two prior attempts established that the existing coupling defeats this approach at any reasonable pace. The coverage required to make in-place changes safe would take 18 or more months to accumulate, during which the system remains fragile. This path also does not satisfy the "validatable under real load" constraint.

**Big-bang cutover.** Build a new system, validate it in staging, and cut over in a single deployment event. Rejected because staging does not reproduce the edge cases that emerge at production session volumes, a failed cutover at peak load has no fast rollback path, and the revenue exposure of an emergency rollback during a checkout outage is unacceptable. This approach requires one shot to work; the parallel-run approach does not.

## Risks and Open Questions

**Session compatibility across the migration boundary.** The shared Session Store creates a living contract between two independently evolving codebases. If v2 modifies the session schema in a way that breaks v1 reads, a rollback could corrupt in-flight sessions. Mitigation: strict namespace isolation for all v2 extensions; integration tests that confirm v1 can round-trip any session written by v2.

**Dual on-call surface.** Running two live checkout pipelines doubles the on-call surface for the duration of the parallel period. There is no architectural way to eliminate this overhead; it is inherent to the parallel-run approach. The team needs to plan on-call rotations and runbook coverage for both systems for approximately fourteen months.

**Cohort edge cases at session boundaries.** Users who switch devices mid-session, share cart links, or enter checkout through deep links may land in an unexpected pipeline if the routing key is session-based but the entry point is link-based. These paths have not been fully mapped. They must be cataloged before the Canary phase advances.

**Shadow comparison blind spots.** The shadow phase divergence metric is only as good as the events that v1 produces. The legacy codebase has behavioral paths that do not emit structured events. Before treating shadow-phase results as conclusive, we need an audit of v1 event coverage.

**Peak-load validation timing.** The rollout gates require two peak-load periods at full traffic before decommission can begin. The peak calendar is not in engineering's control. If the migration reaches the Cutover phase during a low-traffic window, the decommission gate cannot advance until the next natural peak. This may extend the parallel-run period past the planned fourteen months.

**Callback and session-store ordering under concurrent sessions.** The payment processor callback and session-store write are currently assumed to be ordered correctly in the legacy system, but the ordering is not enforced in code. In v2, this ordering must be explicit. If it is not, concurrent mobile and desktop sessions accessing the same cart could produce inconsistent state. This needs to be resolved in the v2 payment callback handler design before the Canary phase.
