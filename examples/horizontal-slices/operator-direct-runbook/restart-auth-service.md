---
entry_id: operator
axis: voice
topic_slug: restart-auth-service
topic_label: Restart the auth service
voice_id: operator
tone_id: matter-of-fact
style_id: procedural
format_id: technical-reference
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Restart the auth service

## When to use this runbook

The `auth-service` 5xx rate on `/login` or `/session/validate` is above 1% for more than 5 minutes, and a restart is the chosen remediation. Do not run this runbook for elevated 4xx, for latency without errors, or while a deploy is in progress.

## Prerequisites

- `kubectl` access to the `prod-auth` cluster with the `auth-oncall` role
- Access to the Grafana dashboard `auth-service / overview`
- Slack access to `#auth-oncall`
- The Datadog query `service:auth-service` open in a tab

## Steps

### 1. Confirm the symptom

```
kubectl -n auth top pods -l app=auth-service
```

Confirm at least one pod shows memory or CPU above its request. If all pods look healthy, stop. Restart will not help.

### 2. Announce the action in Slack

Post in `#auth-oncall`:

```
Restarting auth-service per runbook. Owner: @<your-handle>. Start: <UTC time>.
```

This prevents a second responder from taking conflicting action.

### 3. Drain the first pod from the load balancer

```
kubectl -n auth label pod <pod-name> ready=false --overwrite
```

The service uses `ready=true` as its endpoint selector. The pod stops receiving new traffic within 10 seconds. In-flight requests continue.

### 4. Wait for in-flight requests to finish

```
kubectl -n auth exec <pod-name> -- /bin/sh -c 'ss -tan | grep ESTAB | wc -l'
```

Wait until the established connection count drops below 5, or until 60 seconds have passed - whichever comes first.

### 5. Delete the pod

```
kubectl -n auth delete pod <pod-name>
```

The Deployment controller schedules a replacement. The replacement is ready when readiness probes pass at `/healthz`.

### 6. Validate the replacement is healthy

```
kubectl -n auth get pod -l app=auth-service -w
```

Watch for the new pod to reach `1/1 Running`. This typically takes 30 to 60 seconds.

### 7. Repeat for remaining pods one at a time

Do not restart pods in parallel. The service has 3 replicas; losing 2 at once will overload the third.

### 8. Confirm error rate has returned to baseline

Open Grafana `auth-service / overview`. The `/login` 5xx rate should return below 0.5% within 3 minutes of the last pod restart.

## Expected outcome

All `auth-service` pods show `Running` with restart count incremented by 1. The Grafana `5xx rate` panel is below 0.5%. The Datadog error stream shows no recurring stack traces from `auth-service` in the last 2 minutes.

## If the runbook does not work

If the error rate stays above 1% after all pods have restarted, the cause is not transient. Stop running restarts and do the following:

1. Page `@oncall-platform` in PagerDuty
2. Check for a recent deploy: `kubectl -n auth rollout history deployment/auth-service`
3. If a deploy in the last 30 minutes correlates with the alert, roll it back: `kubectl -n auth rollout undo deployment/auth-service`
4. Capture the current error stack from Datadog and post it in the incident channel

## Related runbooks

- [Investigate elevated p99 latency](investigate-p99-latency.md)
- [Fail over the primary database](database-failover.md)
