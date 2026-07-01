---
entry_id: user-manual
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Backend Services Onboarding User Manual

## Table of Contents

- Getting Started
- Accounts and Access
  - Requesting Your Access
  - Verifying Access Landed
- Local Environment
  - Bootstrapping Your Machine
  - Running the Services Locally
- Codebase Orientation
  - Tracing a Request
  - Finding Who Owns a Service
- The On-Call Rotation
  - Viewer Access vs. Active Rotation
  - The On-Call Alert Drill
- Shipping Your First Change
  - Finding a Starter Ticket
  - Getting Reviewed and Deployed
- Working With Your Buddy
  - The Guided Pairing Schedule
  - Weekly Check-Ins
- Troubleshooting
- Reference

## Getting Started

This manual covers what a new backend services engineer needs to look up during the first two weeks: requesting access, setting up the local environment, orienting in the codebase, understanding the on-call rotation, and shipping a first change. It is a lookup document, not a script to read start to finish - Priya, the current cohort's new hire, uses it the same way any future new hire will: find the section that matches the question, read it, get back to work.

Before Day 1, confirm the following are true. If any is not, contact the onboarding DRI - currently Mei, see `docs/ownership.md` for the current DRI rotation:

- A company laptop with VPN client software is provisioned and IT portal credentials have been sent.
- A buddy is assigned by name.
- A `good-first-issue` ticket is already scoped and visible on the team board.

The team ships to production daily and runs a shared on-call rotation. Both are normal parts of the job here, not exceptions to brace for.

## Accounts and Access

### Requesting Your Access

Use this section to request a system credential or check whether one you requested has landed.

Steps:
1. Open the IT portal with the credentials sent before Day 1.
2. Submit a request for any item below not already marked "approved":
   - Source control org membership
   - VPN credentials and SSO setup
   - CI/CD pipeline access
   - Observability platform (logs, traces, metrics)
   - On-call rotation viewer
   - Secret manager read access for staging
3. Ask your buddy to add you to the team's chat channels directly - these are not provisioned through the IT portal.

Options / Parameters:
- Chat channels: `#backend-services` (primary team channel), `#incidents`, `#deployments`, `#team-random`

Notes:
- Staging secret manager access is historically the slowest item in the queue. If it is still pending by the middle of week one, ask your buddy to escalate rather than wait it out - see Troubleshooting.
- On-call rotation viewer access is read-only. It does not place you on the active rotation; see The On-Call Rotation.

### Verifying Access Landed

Use this section to confirm an access item actually works, not just that the portal shows it as approved.

Steps:
1. Connect to VPN with the credentials from your request.
2. Confirm you can post a message in `#backend-services`.
3. Confirm you can view pipeline run history in CI/CD.
4. Confirm you appear in the on-call rotation tool as a viewer.

Notes:
- A portal status of "approved" is not the same as working access. Verify each item by using it once.

## Local Environment

### Bootstrapping Your Machine

Use this section the first time you set up the codebase locally, or any time you need to rebuild your environment from scratch.

Steps:
1. Clone the repository:
   ```bash
   git clone git@source.example.internal:backend/services.git
   cd services
   ```
2. Run the bootstrap script:
   ```bash
   ./scripts/bootstrap.sh
   ```
3. Confirm the script exits with status 0.

Notes:
- `bootstrap.sh` installs local tooling, sets environment variables, and runs the local health check suite.
- A non-zero exit prints what access is still missing. Resolve the listed item under Accounts and Access before re-running.
- The VPN certificate step is sometimes missing from the IT-issued package. If bootstrap fails there, ask your buddy for the cert file directly rather than filing a second IT ticket.

### Running the Services Locally

Use this section any time you need to start the environment, confirm it is healthy, or inspect a running service.

Steps:
1. Start all services:
   ```bash
   make start-local
   ```
2. Run the smoke test:
   ```bash
   make smoke-test
   ```
3. Tail a specific service:
   ```bash
   make logs SERVICE=orders
   ```

Options / Parameters:
- `SERVICE`: the name of any service defined in `docs/service-map.md`. `orders` above is an example - substitute the service you are working in.

Notes:
- A passing `smoke-test` means the environment is healthy. If it fails, see Troubleshooting before asking a teammate.

## Codebase Orientation

### Tracing a Request

Use this section to build a working model of how a request moves through the system.

Steps:
1. Read `docs/architecture-overview.md` and `docs/service-map.md`.
2. Open the observability platform and locate a real production request.
3. Trace that request from the API gateway to the data store, noting each service it passes through.

Notes:
- Reading without tracing leaves the architecture abstract. Do both.

### Finding Who Owns a Service

Use this section any time you need to know who to ask about a specific service.

Steps:
1. Open `docs/ownership.md`.
2. Locate the service by name.
3. Reach out to the listed owner directly for questions specific to that service.

Notes:
- In week one, prioritize one-on-ones with the owners of the services you are most likely to touch first; `docs/ownership.md` marks these.

## The On-Call Rotation

### Viewer Access vs. Active Rotation

Use this section to understand what your on-call access does and does not mean during your first weeks.

Notes:
- On-call rotation viewer access (requested under Accounts and Access) lets you see the schedule and receive paged alerts as an observer. It does not place you on the active rotation.
- Active on-call participation starts in week five, consistent with a 30-day exclusion from being paged as primary or secondary responder.
- Watching a live deploy with the on-call engineer at least once before the end of week one is expected. Ask your buddy to arrange it if it is not already on your calendar.

### The On-Call Alert Drill

Use this section to prepare for the alert routing and escalation drill scheduled in week two.

Steps:
1. Read `docs/on-call-runbook.md` before the drill.
2. Confirm your staging secret manager access is live (see Accounts and Access) - the drill requires it.
3. Attend the drill and walk the escalation path with your buddy.

Notes:
- If staging access is not live by the time the drill is scheduled, flag it to your buddy immediately. Shifting the drill date is preferable to running it incomplete.

## Shipping Your First Change

### Finding a Starter Ticket

Use this section if your pre-scoped first ticket falls through, or to understand what makes a ticket appropriate for a first change.

Steps:
1. Open the team board and filter by the `good-first-issue` label.
2. Confirm the ticket touches one service and one data model.
3. Confirm the ticket has a test that can be written in under an hour.
4. Confirm the ticket does not require on-call context to understand.

Notes:
- Normally your buddy has already scoped this ticket before Day 1. Use this section only if that ticket is blocked or was picked up by someone else.

### Getting Reviewed and Deployed

Use this section when your first change is ready for review, and again for every change after it.

Steps:
1. Open a pull request against `main`.
2. Request review from your buddy. Arjun can pair as an additional reviewer if useful.
3. Address review feedback and push updates.
4. Once approved, run the deploy yourself, with your buddy present.

Notes:
- You drive the deploy; your buddy does not take the keyboard.
- Your name in the deployment log is the practical marker that your first change shipped. See `docs/deployment-guide.md` and `docs/code-review-guide.md` for the full process.

## Working With Your Buddy

### The Guided Pairing Schedule

Use this section to see what your buddy owns at each stage, and what is yours.

Steps:
1. Days 1-2: your buddy owns a checklist for access and tooling. Nothing on it counts as done until you have verified it yourself.
2. Week one: your buddy runs two 90-minute guided walkthroughs with you - one on service topology, one on deployment and on-call tooling. You keep your own notes; your buddy does not maintain them for you.
3. Week two: you drive the first real change. Your buddy reviews and pairs only on blockers.

Notes:
- Your buddy's sprint capacity is intentionally reduced while you onboard (roughly 30-40% in week one, 15-20% in week two). Reaching out is expected, not an imposition.

### Weekly Check-Ins

Use this section to know what to expect from the two scheduled check-ins and how to raise something that is not on the agenda.

Steps:
1. Attend the Friday week-one check-in (30 minutes). Come ready to answer: is anything blocked, can you navigate the codebase on your own, is anything missing from your access list.
2. Attend the two-week retrospective at the end of week two (30 minutes). This closes the formal onboarding window.

Notes:
- These check-ins are also where "do I feel like I belong here" is a legitimate answer, not just "is my access working." Raise it even if nobody asks directly.

## Troubleshooting

**`smoke-test` fails after bootstrap.** Check `docs/troubleshooting.md` first. Most failures trace back to an access item that shows "approved" in the portal but has not actually propagated.

**Bootstrap fails on the VPN certificate step.** Ask your buddy for the cert file directly rather than filing a second IT ticket.

**An access request has been pending more than two business days.** Do not wait it out. Ask your buddy to escalate through the engineering manager, especially for staging secret manager access - it blocks the week-two on-call alert drill.

**Your pre-scoped first ticket is blocked or was picked up by someone else.** Use Finding a Starter Ticket to identify a replacement before the start of week two. Do not begin week two without a ticket in hand.

**You are not navigating the codebase independently by the end of week one.** Say so at the Friday check-in. Extending orientation by a few days costs less than starting the first change on a shaky foundation.

## Reference

**Glossary**

- **DRI**: directly responsible individual. The onboarding DRI is the named owner of your onboarding workstream.
- **Buddy**: the peer engineer assigned to guide you through setup, orientation, and your first change. Not your manager.
- **good-first-issue**: the label marking tickets scoped as appropriate first changes - one service, one data model, low risk, testable in under an hour.

**Document index**

- Architecture overview - `docs/architecture-overview.md`
- Service map and ownership - `docs/ownership.md`
- Local setup troubleshooting - `docs/troubleshooting.md`
- How we deploy - `docs/deployment-guide.md`
- On-call runbook - `docs/on-call-runbook.md`
- Code review process - `docs/code-review-guide.md`
- Rationale for the guided pairing protocol - ADR-0023

**Quick reference: make targets**

| Target | What it does |
|---|---|
| `make start-local` | Starts all services in Docker Compose |
| `make smoke-test` | Runs the minimal end-to-end suite |
| `make logs SERVICE=<name>` | Tails one service's logs |
