---
entry_id: release-notes
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Checkout Service v2.0.0 - June 13, 2026

## Rebuilt from the ground up: a new checkout pipeline live for all sessions

## What's new

- **Rebuilt checkout pipeline**: The checkout flow is now a separate, event-driven service with a clean session model. The v1 checkout depended on session coupling that was not fully documented and not safely modifiable. v2 has no such coupling. Integrate via `POST /v2/checkout/sessions`; the new API is backward-compatible with existing cart identifiers.

## Improvements

- **Concurrent device sessions**: A mobile session and a desktop session open at the same time on the same account now complete independently and correctly. In v1, concurrent sessions could collide silently - no visible error appeared at the payment step, which made the problem difficult to detect and diagnose.

- **Reliability under peak load**: The new checkout processed two peak-load periods during the traffic migration and the full June 6-7 peak weekend at 100% traffic without latency anomalies or rollback triggers. The parallel-track migration let the team validate under real load before committing to cutover.

- **Cart completion**: Early-cohort migration data showed payment-step completion improving before the full cutover. Full clean attribution will be available from the analytics team on July 7.

## Fixes

- **Silent cart corruption on split-payment orders**: Multi-item orders processed with a split payment method could produce corrupted cart state in v1. The corruption was silent - no error appeared at payment, but order accuracy could be affected downstream. This does not occur in v2.

- **Payment confirmations silently discarded**: A timing gap between the payment processor callback and the session store could cause payment confirmations to be silently dropped under specific conditions in v1. The callback handler in v2 has been rewritten so this cannot occur.

- **Mobile payment-step failures**: Intermittent failures at the final payment step on mobile sessions are resolved. The new session model handles mobile and desktop concurrency without the re-render failures present in v1.

## Known issues

- **Early analytics baseline**: Cart-attribution data from the four-month parallel-track overlap period reflects both checkout versions simultaneously. The analytics team will publish the first clean post-cutover baseline on July 7, 2026, and will annotate the overlap window. Numbers pulled before that date should be treated as preliminary.

## Deprecations and breaking changes

- **v1 checkout is archived as of June 13, 2026** and will be fully decommissioned on July 14, 2026. If your integration still references v1 paths, follow the [migration guide](docs/migration-v1-to-v2.md) before that date.
