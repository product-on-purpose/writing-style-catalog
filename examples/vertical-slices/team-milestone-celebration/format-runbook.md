---
entry_id: runbook
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Legacy Checkout Decommission Runbook (v1 Final Teardown)

## Overview

Execute this runbook to decommission the legacy v1 checkout service after the 31-day archive window expires, completing the final operational step of Project Halyard and retiring the parallel-run infrastructure.

## Prerequisites

- [ ] 31-day archive window has elapsed (window started June 13, 2026; decommission is not permitted before July 14, 2026)
- [ ] No rollback events have triggered during the archive window - verify with Ket Osei or the current on-call infra engineer before starting
- [ ] The v2 checkout has processed at least two peak-load periods without incident (the June 13-14 weekend counts as the first; confirm a second has elapsed)
- [ ] Cart-abandonment baseline report is published or explicitly deferred by Mia Chen's analytics team
- [ ] Written decommission approval from Priya Vasquez (program lead) is recorded in the Project Halyard tracker
- [ ] You have write access to the infra control plane and the legacy service configuration repository
- [ ] Ket Osei or a designated infra engineer is reachable for the duration of this procedure

## Procedure

1. **Confirm the v1 checkout service is in read-only archive mode**
   Check the service config for `mode: archive-readonly` and verify no write paths are active.
   Expected output: Config shows `archive-readonly`. If the service is not in archive mode, stop and contact Ket Osei before continuing.

2. **Verify zero active traffic on the v1 checkout endpoint**
   Open the monitoring dashboard for the legacy endpoint (`/v1/checkout/sessions`) and check the past 15 minutes.
   Expected output: Request rate is 0.00 req/s across all pods. If any non-zero traffic is present, stop. Do not proceed until routing is confirmed correct by the infra team.

3. **Capture a final state snapshot of the v1 database partition**
   Run: `./scripts/archive-snapshot.sh --tier legacy --label decommission-$(date +%Y%m%d)`
   Expected output: Script exits 0 and prints a snapshot ID. Record this ID in the decommission ticket before moving to the next step.

4. **Remove the v1 service registration from the service mesh**
   In the infra control plane, locate the `checkout-v1` service entry and set its state to `deregistered`.
   Expected output: Service mesh health dashboard shows `checkout-v1` as `deregistered` within 60 seconds. No downstream health alerts fire. If any alerts fire, stop and escalate.

5. **Scale the v1 checkout deployment to zero replicas**
   Run: `kubectl scale deployment checkout-v1 --replicas=0 -n payments`
   Expected output: All `checkout-v1` pods enter `Terminating` status and clear within 2 minutes. The payments namespace shows 0 running replicas for `checkout-v1`.

6. **Remove the session compatibility shims**
   Run: `./scripts/remove-compat-shims.sh --confirm`
   The script will list shim identifiers and prompt before applying. Review the list before confirming.
   Expected output: Script prints `Shims removed: [list]` and exits 0. Run `./scripts/verify-shims.sh` immediately after; it should print `No shims found`.

7. **Remove all v1 routing references from the routing config**
   In the routing config repository, open `config/checkout-routes.yaml` and delete the `v1` block in its entirety. Commit with message: `ops: remove legacy checkout v1 routing - decommission July 2026`
   Expected output: CI pipeline passes. The routing dashboard shows only `checkout-v2` entries. No `v1` keys remain in the config file.

8. **Post decommission completion notice in the engineering channel**
   Post a brief message confirming decommission is complete, include the snapshot ID from step 3, and link to the decommission ticket. Tag Priya Vasquez and Dani Rowe.
   Expected output: Notice posted. No engineering responses flagging unexpected behavior within 30 minutes of posting.

## Verification

After completing all steps, confirm all five of the following before closing the ticket:

- The monitoring dashboard for `/v1/checkout/sessions` shows zero traffic and zero running replicas.
- The monitoring dashboard for `/v2/checkout/sessions` shows normal traffic levels with no error-rate increase relative to the past 7 days.
- `./scripts/verify-shims.sh` exits 0 and prints `No shims found`.
- The routing config repository has no references to `checkout-v1` in any file under `config/`.
- The snapshot ID from step 3 is recorded in the decommission ticket and resolves to a valid entry in archive storage.

If all five checks pass, update the decommission ticket status to `Closed` and notify Priya Vasquez.

## Rollback

Rollback is available if failure occurs before step 5 completes. After step 5 (replicas scaled to zero), automated rollback is not available - the 31-day archive window was designed to make rollback unnecessary at decommission time.

**If failure occurs before step 5 is complete:**

1. Re-register `checkout-v1` in the service mesh (reverse step 4 - set state to `registered`).
2. Scale v1 replicas back to the standby count: `kubectl scale deployment checkout-v1 --replicas=2 -n payments`
3. Confirm traffic is routing correctly on the monitoring dashboard before leaving the runbook.
4. Record the failure step and exact error in the decommission ticket.
5. Contact Dani Rowe and Priya Vasquez to schedule a retry.

**If failure occurs after step 5 is complete:** Contact Ket Osei immediately. Recovery from a post-replica-teardown failure is not covered by this runbook and requires manual infra intervention.

## Escalation

- **Non-zero v1 traffic after decommission completes:** Page the on-call infrastructure engineer. Do not attempt to reroute traffic without infra support.
- **Shim removal script fails or `verify-shims.sh` reports unexpected references:** Contact Dom Ferreira before proceeding. Do not mark step 6 complete without a clean verification output.
- **Any step produces an unexpected error or output:** Stop, document the exact error in the decommission ticket, and contact Dani Rowe.
- **No infra engineer reachable and a blocking issue occurs:** Escalate to Priya Vasquez via direct message. Do not continue the procedure unassisted past step 4.
