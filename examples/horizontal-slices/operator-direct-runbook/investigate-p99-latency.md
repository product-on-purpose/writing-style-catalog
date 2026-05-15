---
entry_id: operator
axis: voice
topic_slug: investigate-p99-latency
topic_label: Investigate elevated p99 latency
voice_id: operator
tone_id: matter-of-fact
style_id: how-to-tutorial
format_id: technical-reference
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Investigate elevated p99 latency

## When to use this runbook

The Grafana alert `api-gateway / p99 latency above 500ms` has fired and stayed firing for more than 5 minutes. This runbook narrows the cause to one of four categories: upstream dependency, database, cache, or recent deploy. It does not remediate; it produces a diagnosis.

## Prerequisites

- Read access to Grafana, Datadog APM, and the deploy log in `#releases`
- `kubectl` read access to the `prod-api` cluster
- Access to the `redis-prod` Redis status page
- Access to the Postgres dashboard `pg-prod / overview`

## Steps

### 1. Confirm the alert is real

Open Grafana `api-gateway / latency`. Confirm p99 is above 500ms across at least 2 of 3 availability zones. Single-zone spikes are usually noisy neighbors and resolve without action.

### 2. Check for a recent deploy

Search `#releases` for messages in the last 60 minutes. Cross-reference against the alert start time.

| Deploy timing | Likely cause | Next step |
|---------------|--------------|-----------|
| Deploy within 15 minutes before alert | Regression in new build | Step 7 |
| Deploy 15 to 60 minutes before | Possible, less likely | Continue to step 3 |
| No deploy in last 60 minutes | Not a deploy regression | Continue to step 3 |

### 3. Check upstream dependencies

Open the Datadog APM service map for `api-gateway`. Identify any downstream service with p99 above its normal baseline.

```
service:api-gateway @http.status_code:5xx
```

Note any downstream service that shows error spikes correlated with the alert start time.

### 4. Check database health

Open Postgres dashboard `pg-prod / overview`. Check:

| Metric | Healthy | Investigate if |
|--------|---------|----------------|
| Active connections | < 70% of max | Above 80% of max |
| Replication lag | < 1s | Above 5s |
| Query p99 | < 50ms | Above 200ms |
| Disk usage | < 75% | Above 85% |

If any row falls in the investigate column, the database is the most likely cause. Continue to step 6.

### 5. Check cache hit rate

Open the `redis-prod` status page. The `api-cache` hit rate should be above 90%.

```
redis-cli -h redis-prod.internal INFO stats | grep keyspace
```

A hit rate below 80% indicates either a cold cache after a flush or a workload pattern change. Both produce database pressure and explain elevated latency.

### 6. Check database query patterns

```
kubectl -n prod-api exec -it postgres-client -- psql -h pg-prod -U readonly -c "
SELECT query, calls, mean_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
"
```

Look for queries with `mean_exec_time` above 100ms that did not appear in the last known baseline. A new slow query is usually the cause when no deploy correlates.

### 7. Check the recent deploy

```
kubectl -n prod-api rollout history deployment/api-gateway
```

If a deploy correlates with the alert, capture its commit SHA. Compare the diff against `main` from the prior known-good build.

### 8. Record the diagnosis

Post in the incident channel:

```
p99 latency investigation:
- Root cause: <upstream | database | cache | deploy regression>
- Evidence: <specific metric or query>
- Proposed remediation: <link to remediation runbook>
- Owner: @<your-handle>
```

## Expected outcome

You have identified which of the four categories is responsible and have linked or paged the owning team. The investigation runbook ends here; remediation runs separately.

## If the runbook does not work

If none of the four categories shows abnormal signals and p99 remains above 500ms, the cause is one of: a load balancer issue, an instance type issue, or a network-level issue outside the application stack. Do the following:

1. Page `@oncall-platform` in PagerDuty
2. Open the AWS console and check the `api-gateway` ALB for elevated `TargetResponseTime`
3. Check the AWS Health Dashboard for the region

## Related runbooks

- [Restart the auth service](restart-auth-service.md)
- [Fail over the primary database](database-failover.md)
