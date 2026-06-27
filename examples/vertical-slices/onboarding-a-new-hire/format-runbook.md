---
entry_id: runbook
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Backend Engineer Two-Week Onboarding

## Overview

Trigger this runbook when a new backend services engineer has a confirmed start date. It covers the full sequence from pre-arrival setup through the new hire's first shipped change and two-week retrospective.

## Prerequisites

- [ ] New hire's start date is confirmed and a named onboarding DRI is assigned (see `docs/ownership.md` for the current DRI rotation)
- [ ] A buddy is designated - a peer engineer, not the tech lead
- [ ] One `good-first-issue` ticket is scoped, written, and on the board before Day 1: one service, one data model, no on-call risk if the change goes wrong
- [ ] The buddy's Week 1 sprint capacity is reduced by 30-40% in sprint planning; Week 2 by 15-20%
- [ ] You have access to the IT portal to submit provisioning requests on the new hire's behalf if needed

## Procedure

### Phase 1: Access and Environment (Days 1-2)

1. **Submit access requests** through the IT portal for all of the following on Day 1 morning:
   - Source control org membership
   - VPN credentials and SSO
   - CI/CD pipeline access
   - Observability platform (logs, traces, metrics)
   - On-call rotation viewer (read-only; active rotation starts Week 5)
   - Secret manager read access for staging
   Expected output: IT portal shows each item as "pending" or "approved." If any item is missing from the list, the provisioning will be incomplete.

2. **Add the new hire to chat channels** manually without waiting for IT: `#backend-services`, `#incidents`, `#deployments`, `#team-random`.
   Expected output: New hire is visible in all four channels and can post messages.

3. **Verify VPN connection** by having the new hire connect with the credentials from step 1.
   Expected output: VPN connects without error. If the VPN cert step is missing from the IT-issued package, provide the cert file directly and patch `docs/troubleshooting.md` before continuing.

4. **Clone the repository and run bootstrap** once VPN and source control access are both confirmed:
   ```bash
   git clone git@source.example.internal:backend/services.git
   cd services
   ./scripts/bootstrap.sh
   ```
   Expected output: `bootstrap.sh` exits 0 and prints "Environment ready." A non-zero exit prints what access is still missing; resolve before continuing.

5. **Run the smoke test** to confirm the local environment is healthy:
   ```bash
   make start-local
   make smoke-test
   ```
   Expected output: All tests pass and `smoke-test` exits 0. If it fails, direct the new hire to `docs/troubleshooting.md` before re-running.

6. **Confirm the pre-scoped first-change ticket is on the board** and visible to the new hire. The task must already be written.
   Expected output: New hire opens the ticket and can describe the scope without further explanation. If the ticket is not ready, escalate to the engineering manager immediately - do not proceed to Phase 2 without it.

### Phase 2: Codebase Orientation (Week 1)

7. **Run a 90-minute architecture walkthrough** covering `docs/architecture-overview.md` and `docs/service-map.md`. The new hire takes their own notes; the buddy does not maintain notes on their behalf.
   Expected output: New hire can name the three services they will work on first and locate the test harness for each without guidance.

8. **Run a 90-minute deployment and on-call tooling walkthrough**, using the on-call platform in read-only mode.
   Expected output: New hire can trace a production request in the observability platform from the API gateway to the data store.

9. **Book one-on-ones** between the new hire and the three service owners listed in `docs/ownership.md` for the services they will touch first. Book these within Week 1.
   Expected output: Calendar invites accepted by all three owners.

10. **Arrange pairing with the on-call engineer** for one live deploy before Friday of Week 1.
    Expected output: New hire has observed a deploy and can describe the release sequence unprompted.

11. **Run the Friday Week 1 check-in** (30 minutes). Confirm: all access items from Phase 1 are fully provisioned, local environment runs, new hire can navigate the three target services without hand-holding.
    Expected output: No open access gaps. If gaps exist, open follow-up tickets with named owners before the check-in ends. Staging access is the highest-risk item - confirm it is either live or has an active escalation.

### Phase 3: First Shipped Change (Week 2)

12. **Confirm the scoped change is ready to code** on the first day of Week 2. The new hire drives; the buddy pairs on blockers only.
    Expected output: Pull request open and CI passing by Wednesday of Week 2.

13. **Complete code review** with the buddy (Arjun as additional reviewer if needed) and merge.
    Expected output: Change merged to main and new hire's name appears in the deployment log.

14. **Have the new hire run the deploy** with the buddy present and ready to intervene.
    Expected output: Deploy completes without incident. The new hire performs the deploy action themselves - the buddy does not take the keyboard.

15. **Run the two-week retrospective** (30 minutes) on the last day of Week 2. Ask explicitly: does Priya know who to ask for what, not just where to look? Does she feel she belongs, not just that she functions?
    Expected output: Retro notes created. Any remaining gaps have a named owner and a target date. Formal onboarding window is closed.

## Verification

The procedure is complete when all of the following are true:

- Priya's change is merged and visible in the deployment log before the end of Week 2.
- All access items from step 1 are provisioned under Priya's own credentials; no shared team credentials remain in use.
- Priya can navigate the three target services and their test harnesses without assistance.
- Priya is scheduled for on-call eligibility starting Week 5.
- The two-week retrospective has been held and no blocking gaps remain open.

## Rollback

Not applicable in the system-operation sense. Onboarding steps cannot be undone. If the procedure stalls - access delayed, scoped task not ready, buddy unavailable - pause at the blocked step and escalate. Do not skip steps and attempt to resume; the Week 2 first-change sequence depends on Week 1 being complete.

## Escalation

- **Access provisioning delayed past Day 2:** Engineering manager. Do not wait; a new hire blocked on credentials on Day 2 signals a gap that requires manager-level escalation into the infra queue.
- **Staging access not provisioned by start of Week 2:** Submit an infra escalation immediately. Staging access is required for the on-call alert drill; if unresolved before the drill date, the drill must shift and the manager must be informed.
- **Scoped first-change ticket not ready on Day 1:** Engineering manager. This is a sprint planning failure, not an individual failure, and the engineering manager owns resolution.
- **Buddy capacity collapses mid-week:** Engineering manager to arrange named coverage. Do not redistribute onboarding responsibility without a designated replacement.
