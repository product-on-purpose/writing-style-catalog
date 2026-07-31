---
diff_pair_id: format-runbook-vs-readme-onboarding-a-new-hire
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
axis_varied: format
entry_a: runbook
entry_b: readme
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `runbook` vs `readme`

**Topic:** Getting a new engineer productive in their first two weeks
**Axis varied:** format
**A:** `runbook` - A step-by-step operational procedure for a recurring task or incident, written to be followed correctly under pressure.
**B:** `readme` - The front-door document for a software project - tells a first-time visitor what it is, why it exists, how to use it, and where to go next.

## What to notice

Both document the same onboarding, and each announces its reader in its first lines.

**A names a trigger.** "Trigger this runbook when a new backend services engineer has a
confirmed start date." A runbook exists to be executed at a moment, by whoever is on the hook,
and stating the trigger is what makes it findable at that moment.

**B opens on badges.** A CI badge for bootstrap status and another for on-call eligibility.
That is a README move: it orients someone who has just arrived at the repository and wants to
know, at a glance, whether the thing is healthy and where they stand.

**The sharpest single tell.** A tells you *when* to start reading; B tells you *what state
things are in*. One is retrieved under time pressure, the other is browsed. It follows that a
runbook can be terse to the point of curtness and lose nothing, while a README that reads that
way has failed its only reader.

---

## A: `runbook`

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

---

## B: `readme`

# Backend Services Team - Engineer Onboarding

![setup status](https://ci.example.internal/badge/onboarding-bootstrap-passing) ![on-call eligible](https://ci.example.internal/badge/oncall-week-five) ![ship target](https://ci.example.internal/badge/first-ship-week-two)

> Two-week onboarding guide for engineers joining the backend services team: access to shipping, start to belonging.

This guide covers what a new engineer needs in their first two weeks: access and tooling, codebase orientation, team context, a first real change shipped, and enough of the human side to feel like they belong and not just function. It is also for the teammate doing the pairing - the guide tells you both what week one looks like and what success at the end of week two means.

The team deploys daily and runs a shared on-call rotation. Getting comfortable with both is the orientation goal, not a test.

## Setup

Request any of the following that are not yet provisioned through the IT portal:

- Source control org membership
- VPN credentials and SSO setup
- CI/CD pipeline access
- Observability platform (logs, traces, metrics)
- On-call rotation viewer (actual on-call starts week five)
- Secret manager read access for staging
- Chat tool: add to `#backend-services`, `#incidents`, `#deployments`, `#team-random`

Once access lands, bootstrap the local environment:

```bash
git clone git@source.example.internal:backend/services.git
cd services
./scripts/bootstrap.sh
```

`bootstrap.sh` installs local tooling, sets environment variables, and runs the local health check suite. It exits non-zero and prints what is missing if any access is still pending.

## Quick start

```bash
make start-local          # starts all services in docker compose
make smoke-test           # runs the minimal end-to-end suite
make logs SERVICE=orders  # tail one service to see the shape of a real request
```

If `smoke-test` passes, the environment is healthy. If it fails, start with `docs/troubleshooting.md` before asking a teammate.

## Week one

The goal of week one is orientation, not output. Three things matter:

**Trace the system.** Read `docs/architecture-overview.md` and `docs/service-map.md`, then use the observability platform to trace one real production request from the API gateway to the data store. Reading without tracing leaves the architecture abstract.

**Meet the owners.** The `docs/ownership.md` file lists which teammates own the services Priya will most likely touch first. One-on-ones with those three people in week one are worth more than any doc.

**Watch a deploy.** Pair with the on-call engineer on one daily deploy before week one ends. The release process is not abstract when you have seen it once.

Hold a thirty-minute check-in on Friday of week one: is anything blocked, can Priya navigate the codebase on her own, are there gaps in the access list above?

## Week two

Pick one ticket from the `good-first-issue` label. Good criteria: touches one service and one data model, has a test that can be written in under an hour, does not require on-call context to understand.

The pairing engineer reviews the PR. Priya does the deploy. The point is not the change itself - it is that she owns the full cycle end to end.

The belonging side matters as much as the output. By the end of week two, Priya should know who to ask, not just where to look.

## Documentation

- [Architecture overview](docs/architecture-overview.md)
- [Service map and ownership](docs/ownership.md)
- [Local setup troubleshooting](docs/troubleshooting.md)
- [How we deploy](docs/deployment-guide.md)
- [On-call runbook](docs/on-call-runbook.md)
- [Code review process](docs/code-review-guide.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to open a PR, get it reviewed, and merge it.

## License

Internal use only.
