---
entry_id: technical-reference
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Lattice Notify Datastore Selection Matrix

The reference rubric the architecture review board (ARB) uses to evaluate a new datastore for a new service. Used in the Wednesday 2026-05-13 review for the notification service (Postgres vs DynamoDB).

## Signature

```
evaluate_datastore(
    candidate: DatastoreOption,
    workload: WorkloadProfile,
    team: TeamProfile,
    horizon_months: int,
) -> EvaluationResult
```

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| candidate | DatastoreOption | yes | The datastore being evaluated (e.g. `postgres-extended`, `dynamodb-new`) |
| workload | WorkloadProfile | yes | Read/write rates, access pattern, consistency requirements, peak/average ratio |
| team | TeamProfile | yes | Headcount, on-call rotation size, existing operational knowledge per datastore |
| horizon_months | int | yes | Planning horizon for the evaluation (typically 12 for service-level decisions) |

## Evaluation Dimensions

| Dimension | Weight | Postgres (notification svc) | DynamoDB (notification svc) |
|-----------|--------|-----------------------------|-----------------------------|
| Access-pattern fit | 0.15 | Adequate; needs schema design + indexes | Strong; native fit for point-lookup writes |
| Throughput at launch (500K events/day) | 0.10 | Strong; well within current cluster headroom | Strong |
| Throughput at 12-month upside (5M events/day) | 0.10 | Adequate with partitioning + queue tuning | Strong; scales without intervention |
| Team operational knowledge | 0.25 | Strong; 3 years of production experience | Weak; one personal-project spike |
| On-call rotation surface area | 0.20 | No change | Doubles (new runbook, monitoring, alerts) |
| Cross-database query needs | 0.10 | Strong; joins to existing user/account data are SQL | Weak; cross-store joins become application code |
| Recovery cost if wrong | 0.05 | 3-6 weeks; predictable | 3-6 weeks; less predictable |
| Vendor lock-in / portability | 0.05 | Open source; high portability | AWS-only; high lock-in |

## Outputs

The evaluation produces a weighted score per candidate and a recommendation. The recommendation is not the highest score; it is the highest score whose downside scenarios are recoverable given the team profile.

```
EvaluationResult(
    candidate="postgres-extended",
    weighted_score=0.79,
    recommendation="adopt",
    revisit_threshold="5M events/day sustained",
    rationale_doc="adr/0023-postgres-notification-service.md",
)
```

## Examples

```yaml
# Notification service evaluation, 2026-05-13
workload:
  writes_per_day: 500_000
  upside_writes_per_day: 5_000_000
  read_pattern: point_lookup_by_user
  consistency: read_your_writes
team:
  backend_engineers: 8
  on_call_rotation: 4
  postgres_ops_years: 3
  dynamodb_ops_years: 0
horizon_months: 12
result:
  recommendation: postgres-extended
  revisit_threshold: 5M events/day sustained
```

```yaml
# Counterexample: a future workload where the recommendation would flip
workload:
  writes_per_day: 50_000_000
  upside_writes_per_day: 200_000_000
  read_pattern: point_lookup_by_user
  consistency: eventual
team:
  backend_engineers: 40
  on_call_rotation: 12
  postgres_ops_years: 5
  dynamodb_ops_years: 2
horizon_months: 18
result:
  recommendation: dynamodb-new
```

## Notes / Constraints

- The Team Operational Knowledge dimension is the highest-weighted single dimension by design. The ARB raised this weight from 0.15 to 0.25 in 2025 after two incidents where a technically-superior datastore was adopted by a team that could not operate it under load.
- Revisit thresholds are mandatory for any recommendation; an evaluation without a threshold is rejected on submission.
- The matrix is for service-level datastore decisions only. Application-level cache choices use a separate rubric (see `caches-selection-matrix.md`).
- Version 2.3 of this rubric (current) added the Cross-database query needs dimension after the 2024 search service decision.

## See Also

- ADR-0023: Postgres for notification service - the canonical worked example of this matrix
- WorkloadProfile schema specification - `schemas/workload-profile.yaml`
- ARB charter and decision process - `governance/arb-charter.md`
- Lattice Notify capacity planning guide - `ops/capacity-planning.md`
