---
entry_id: postmortem
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Cart-State Mismatch Under Split Payment - Near-Miss in Parallel Checkout

## Severity

SEV-1 (near-miss; issue contained in staging before production promotion)

## Summary

On February 18, 2026, during a data audit of Phase 3 canary sessions, a silent cart-state mismatch was found in the new checkout pipeline that would have corrupted multi-item orders processed under split payment. No customers were affected; the issue was caught in staging before the canary cohort reached full cutover. The March 2026 launch window was placed on hold. The fix shipped on March 7, 2026, and the launch target was rescheduled to April.

## Timeline

- 2026-02-18 09:14 UTC - During routine review of Phase 3 canary session snapshots, Marcus Teel flags divergent state records in a subset of multi-item cart sessions.
- 2026-02-18 11:30 UTC - Mismatch confirmed reproducible in staging. Split-payment flows with three or more line items show divergent state between the new checkout service and the session store; extra line items are silently dropped from the cart record on session resume.
- 2026-02-18 13:00 UTC - Incident declared. Production promotion of the canary cohort placed on hold. Priya Vasquez notified.
- 2026-02-18 15:45 UTC - Root cause isolated: the new checkout service applies a cart-merge strategy that diverges from a 2022 patch in the legacy session layer. The divergence is silent; the new service returns a 200 and the session store reflects a corrupted cart with no error surfaced anywhere in the stack.
- 2026-02-19 - Dani Rowe calls the formal hold on the March launch window. Fix scope assessed at three weeks minimum, making the March target unworkable.
- 2026-02-19 to 2026-03-06 - Corrected cart-merge logic implemented, integration tests written for split-payment multi-item paths, and the canary regression suite re-run against the corrected implementation.
- 2026-03-07 - Fix verified clean across all canary cohorts. March launch window formally rescheduled to April.

## Root Cause

The new checkout service's cart-merge strategy was modeled on the original design document for the legacy system. That design was superseded in 2022 by a production patch that altered merge behavior for sessions resumed under split payment. The patch was applied without a corresponding ADR, test coverage, or explicit documentation; it lived in the legacy codebase as a silent behavioral variant with no record outside of the commit that introduced it.

When the new service was designed and reviewed, the 2022 patch was not surfaced as a divergence to reconcile. There was no process requiring an inventory of undocumented behavioral patches before a replacement service entered design. The new service faithfully implemented the documented design. The documented design was incomplete.

The proximate trigger was the split-payment path with three or more line items. The systemic condition was the absence of any mechanism for surfacing undocumented behavioral patches during the design phase of a replacement service.

## Impact

- Users affected: 0 (issue contained in staging before production promotion)
- Potential production impact if promoted: silent corruption of cart records for multi-item split-payment orders, estimated at 8-12% of checkout sessions by order type
- Duration: Detected and contained within 6 hours on 2026-02-18; fix period February 18 to March 7, 2026
- Services affected: New checkout service canary environment only; legacy checkout remained live and unaffected throughout
- Schedule impact: March 2026 launch window postponed three weeks; new target April 2026

## Contributing Factors

- No documented inventory of behavioral patches applied to the legacy checkout after its original design; engineers building the new service had no systematic way to identify silent divergence points without reading years of uncommitted patch history
- The shadow-mode phase (months 1-4) compared response payloads between old and new services but did not include session-store state snapshots; the mismatch was invisible to the existing comparison tooling
- The cart-merge path under split payment had no integration test coverage in the legacy test suite, because the 2022 patch had been applied without accompanying tests
- The canary ramp to 80% generated enough real-session volume that the mismatch became statistically detectable in aggregate audit data; at lower canary percentages it had been within noise

## Action Items

- [ ] Conduct a full audit of undocumented behavioral patches in the legacy checkout service and produce a written inventory that the new-service team can use as a reconciliation checklist - Owner: Marcus Teel - Due: 2026-03-21
- [ ] Extend shadow-mode session comparison to include session-store state snapshots, not only response payloads - Owner: Dom Ferreira - Due: 2026-04-04
- [ ] Add integration test coverage for all split-payment cart-merge paths with two or more line items - Owner: Dev team lead - Due: 2026-03-14
- [ ] Add a "legacy behavioral divergence" section to the design document template used for any replacement service; require explicit sign-off from the engineer with the most recent working knowledge of the legacy system before design is finalized - Owner: Priya Vasquez - Due: 2026-04-15

## Lessons Learned

An undocumented behavioral patch does not just create risk in the legacy system it lives in. It creates an invisible specification gap that any replacement system will silently fail to reproduce. The gap surfaces either in production, where it becomes user impact, or late in a long migration, where it becomes schedule impact and rework. The correct countermeasure is a process for surfacing undocumented variants before design begins, not more thorough review during it.

The parallel architecture performed its intended function. The canary ramp created conditions that made the mismatch statistically visible in staging before any production promotion. The issue was costly - three weeks and a launch window - but it was contained. That is the expected result of a correctly designed parallel rollout, and it is a better result than finding the same issue after full cutover with no fallback path.
