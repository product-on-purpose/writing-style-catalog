---
entry_id: operator
axis: voice
topic_slug: database-failover
topic_label: Fail over the primary database
voice_id: operator
tone_id: matter-of-fact
style_id: procedural
format_id: technical-reference
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Fail over the primary database

## When to use this runbook

The primary Postgres instance `pg-prod-primary` is unhealthy in one of the following ways:

| Condition | Threshold |
|-----------|-----------|
| Disk usage | Above 90% and rising |
| Replication lag | Above 30 seconds on all replicas |
| Connection pool | Saturated and not draining for over 5 minutes |
| Liveness | Not responding to `SELECT 1` for over 60 seconds |

Failover is a last resort. Do not run this runbook for short-lived spikes, for a single bad query, or for replication lag under 30 seconds.

## Prerequisites

- `pg-admin` IAM role
- Access to the `pg-prod` AWS RDS console or equivalent control plane
- Access to the secrets store for the `pg-prod` credentials
- Approval from the on-call manager or, after hours, from `@db-oncall`
- Slack access to `#incident-bridge`

## Steps

### 1. Verify failover is the right action

Run through the checklist before any control plane change.

| Check | How |
|-------|-----|
| Replica `pg-prod-replica-01` is healthy | RDS console shows `available`, replication lag below 5s |
| Replica `pg-prod-replica-01` is on a current major version | Matches the primary major version |
| No active large transactions on the primary | `SELECT pid, age(clock_timestamp(), xact_start) FROM pg_stat_activity WHERE state = 'active' ORDER BY 2 DESC LIMIT 5;` |
| Approval logged | Recorded in `#incident-bridge` with approver name |

If any row fails, stop. Do not proceed.

### 2. Announce the failover in the incident channel

Post in `#incident-bridge`:

```
Initiating pg-prod failover per runbook.
Owner: @<your-handle>.
Approver: @<approver-handle>.
Target replica: pg-prod-replica-01.
Start: <UTC time>.
Expected downtime: 30-90 seconds.
```

### 3. Quiesce application writes

Scale write workers to zero. Reads continue against replicas.

```
kubectl -n prod-api scale deployment/write-worker --replicas=0
```

Wait for `kubectl -n prod-api get pods -l app=write-worker` to return zero pods. This typically takes 15 seconds.

### 4. Wait for replication to drain

```
psql -h pg-prod-replica-01 -U readonly -c "SELECT pg_last_wal_replay_lsn(), pg_last_wal_receive_lsn();"
```

Confirm `pg_last_wal_replay_lsn` equals `pg_last_wal_receive_lsn`. The replica has applied all WAL it has received.

### 5. Promote the replica

```
aws rds promote-read-replica --db-instance-identifier pg-prod-replica-01
```

The console transitions through `modifying` and `available`. This takes 60 to 120 seconds.

### 6. Update the application connection string

The connection string is stored in the secret `pg-prod-primary-url` in AWS Secrets Manager. Update the host to `pg-prod-replica-01.<region>.rds.amazonaws.com`.

```
aws secretsmanager update-secret \
  --secret-id pg-prod-primary-url \
  --secret-string '{"host":"pg-prod-replica-01.<region>.rds.amazonaws.com","port":5432,...}'
```

### 7. Restart application pods to pick up the new connection string

```
kubectl -n prod-api rollout restart deployment/api-gateway
kubectl -n prod-api rollout restart deployment/write-worker
```

Wait for both deployments to report `rollout status` complete.

### 8. Validate the new primary is accepting writes

```
psql -h pg-prod-replica-01 -U postgres -c "CREATE TABLE failover_check_$(date +%s) (ts timestamptz); DROP TABLE failover_check_$(date +%s);"
```

A successful create-and-drop confirms the new primary is writable.

### 9. Scale write workers back up

```
kubectl -n prod-api scale deployment/write-worker --replicas=4
```

### 10. Confirm application health

Open Grafana `api-gateway / overview`. Confirm error rate is below 0.5% and write throughput has returned to baseline within 5 minutes.

## Expected outcome

`pg-prod-replica-01` is the new primary. The old `pg-prod-primary` is detached and pending review. Application error rate is at baseline. Write throughput is at baseline. The incident channel has a posted message confirming completion.

## If the runbook does not work

If the promote step fails, or if the application does not recover after the new connection string is in place:

1. Page `@db-oncall` in PagerDuty
2. Do not attempt to re-promote the old primary - this creates split-brain risk
3. Capture the output of `aws rds describe-db-instances --db-instance-identifier pg-prod-replica-01` and post it to the incident channel
4. Hold all further control plane changes until the database on-call responds

## Related runbooks

- [Investigate elevated p99 latency](investigate-p99-latency.md)
- [Restart the auth service](restart-auth-service.md)
