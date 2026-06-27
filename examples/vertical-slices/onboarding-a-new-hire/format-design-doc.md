---
entry_id: design-doc
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Onboarding Bootstrap Tooling Design Document

## Status

In Review

## Problem

The backend services team ships to production daily and runs a shared on-call rotation. New engineers are excluded from on-call for their first thirty days, which makes the two-week window to first productive contribution load-bearing: Priya (starting Mon Jun 22, buddy Arjun, DRI Mei) needs credentials, repository access, tooling configuration, and enough codebase familiarity to ship a real change before the two-week mark.

The current setup process is unstructured. The buddy walks the new hire through access and tooling verbally on day one, which takes two to four hours of buddy time, produces no machine-readable record, and leaves access gaps undiscovered until they block work mid-week. There is also no early-warning mechanism for the failure mode where the pre-scoped week-two task has not been selected before day one, which causes week two to collapse without a visible signal.

The constraints shaping the solution space:

- Buddy capacity is fixed. The pairing protocol targets 30-40% of the buddy's time in week one and 15-20% in week two. Tooling must reduce access-verification overhead, not add coordination cost on top of it.
- The existing `scripts/bootstrap.sh` runs on every local environment setup and must not be broken. The design extends it rather than replacing it.
- The tooling must be operational before Jun 22. Anything requiring a multi-sprint build cycle is out of scope.
- Staging secret manager access for Priya went into the infra queue Jun 23. Her own credentials must be verifiable before the on-call alert drill on Jul 2. The tooling needs to surface this gap automatically if it persists.

## Proposed Design

### Access verification module

A new script at `scripts/check-access.sh` is called at the end of `bootstrap.sh`. It runs each required access grant against a live endpoint and prints a result line per item:

```
[PASS]  source-control
[PASS]  vpn-sso
[FAIL]  secret-manager-staging  - open: https://it.internal/request/secret-manager
[WARN]  sso-propagation  - SSO credentials may take up to 4h to propagate; verify manually with buddy
```

Verification methods per item:

| Item | Method |
|---|---|
| Source control | `git ls-remote git@source.example.internal:backend/services.git HEAD` |
| VPN / SSO | TCP probe to `vpn-healthcheck.internal:443` |
| CI/CD pipeline | `GET /api/v1/pipelines?user=<email>` on the CI host; expects 200 and a non-empty list |
| Observability platform | Authenticated `GET /api/dashboards`; unauthenticated 200 is not sufficient |
| Secret manager (staging) | `vault list secret/staging` with the engineer's token |

Exit code equals the count of `[FAIL]` items. `[WARN]` lines do not affect the exit code. The IT portal URL printed on failure is derived from a static map in `config/access-portal-urls.json`, keyed by item ID.

### Machine-readable onboarding file

A JSON file committed to main at `onboarding/priya-2026-06-22.json` before Priya's first day:

```json
{
  "engineer": "Priya",
  "start_date": "2026-06-22",
  "buddy": "Arjun",
  "dri": "Mei",
  "oncall_eligible_date": "2026-07-22",
  "first_ship_target": "2026-07-03",
  "access_items": [
    { "id": "source-control", "label": "Source control org membership", "verified_by": null, "verified_at": null },
    { "id": "vpn-sso", "label": "VPN credentials and SSO", "verified_by": null, "verified_at": null },
    { "id": "cicd", "label": "CI/CD pipeline access", "verified_by": null, "verified_at": null },
    { "id": "observability", "label": "Observability platform", "verified_by": null, "verified_at": null },
    { "id": "secret-manager-staging", "label": "Secret manager read access (staging)", "verified_by": null, "verified_at": null },
    { "id": "chat-channels", "label": "#backend-services, #incidents, #deployments, #team-random", "verified_by": null, "verified_at": null }
  ],
  "first_issue_id": null,
  "first_pr_merged_at": null,
  "onboarding_closed_at": null
}
```

The buddy marks items verified by running:

```bash
scripts/verify-onboarding.sh source-control
```

The script writes the verifier's username and a UTC timestamp into `verified_by` and `verified_at` for that item and commits the change. When `check-access.sh` passes a check automatically, `verify-onboarding.sh` is called by `bootstrap.sh` to populate that item without requiring buddy action. Items the script cannot verify (SSO propagation, chat channels) remain `null` and require explicit buddy sign-off.

### Pre-day-one preflight gate

`scripts/verify-onboarding.sh --preflight onboarding/priya-2026-06-22.json` is intended to be run by Mei or Arjun before Jun 22. It checks:

1. An issue tagged `onboarding:priya` exists in the issue tracker.
2. That issue carries no more than one service label (cross-referenced against `docs/service-map.json`).
3. The issue is not tagged `oncall-risk`.

If any check fails, the script exits non-zero and names the missing item. This surfaces the "task not ready on day one" failure mode before Priya arrives, not after.

### CI badge wiring

Three badges are wired to the onboarding file and the CI pipeline:

- `onboarding-bootstrap-passing`: CI runs `check-access.sh` nightly against Priya's credentials while `onboarding_closed_at` is null. Badge is green when exit code is 0.
- `oncall-week-five`: Static metadata badge generated from `oncall_eligible_date` in the JSON file.
- `first-ship-week-two`: Webhook triggered when a PR tagged `onboarding:priya` is merged. The CI bot writes the merge timestamp into `first_pr_merged_at`, closes the onboarding window by setting `onboarding_closed_at`, and notifies Mei in #backend-services.

The nightly check run stops automatically once `onboarding_closed_at` is set.

## Alternatives Considered

**Unstructured verbal walkthrough (current state).** The buddy walks through access verbally on day one. Rejected: leaves no record, does not surface access gaps until they block work, and fully loads the buddy during the highest-cost part of week one without producing a verifiable artifact.

**Full onboarding web dashboard with a database backend.** A web UI tracking checklist state with history and a reporting view. Rejected on scope: the dashboard can be built later on top of the JSON file. A committed JSON file is verifiable, diffable, and can be operational before Jun 22. A web dashboard cannot.

**Tech lead as sole onboarding owner.** Remove the buddy role and have Mei run all pairing sessions directly. Rejected: concentrates the highest-cost time resource on administrative work, and removes the peer buddy relationship, which carries distinct belonging value that the DRI role cannot replicate.

**Single combined bootstrap script.** Fold access verification and onboarding tracking into the existing `bootstrap.sh`. Rejected: `bootstrap.sh` runs on every local environment setup. Onboarding verification runs once per engineer. Merging them tightly makes both harder to maintain and test.

## Risks and Open Questions

**Risk: false positives from check-access.sh.** Authenticated endpoint checks can pass while individual credential propagation is still in flight (SSO in particular has up to a four-hour window). Mitigation: checks that cannot verify individual credentials emit `[WARN]` rather than `[PASS]` and require explicit buddy verification in the JSON file. The warn-vs-pass distinction must be documented in the script so future maintainers do not promote warns to passes without understanding the tradeoff.

**Risk: staging access not resolved before Jul 2.** Priya's staging secret manager request has been in the infra queue since Jun 23. She needs her own credential before the on-call alert drill on Jul 2. The nightly CI run will report `[FAIL]  secret-manager-staging` and keep the badge red, creating a visible signal. The escalation path when the badge stays red - Mei escalates through the engineering manager - is a process dependency this tooling cannot enforce, only surface.

**Open question: onboarding window close when first PR misses target.** The design closes the window on first merge of a PR tagged `onboarding:priya`. If no such PR merges by `first_ship_target` (Jul 3), the window stays open indefinitely and CI keeps running nightly checks. Proposal: if `first_pr_merged_at` is still null on `first_ship_target`, the CI bot posts a notification to Mei and halts the nightly run pending her decision to extend or close. This needs explicit sign-off before implementation.

**Open question: simultaneous onboarding of two engineers.** The current design stores one file per engineer. If two engineers onboard at the same time, the nightly CI run must discover and iterate over all open onboarding files (glob `onboarding/*.json` where `onboarding_closed_at` is null). This is a straightforward extension but has not been prototyped. The immediate case (Priya only) does not require it.
