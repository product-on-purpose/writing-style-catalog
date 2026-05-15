---
entry_id: pragmatic-architect
axis: voice
topic_slug: sunset-legacy-auth
topic_label: Sunset the legacy auth service
voice_id: pragmatic-architect
tone_id: candid
style_id: decision-log
format_id: adr
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# ADR-0044: Sunset auth-v1 in 90 Days

## Status

Accepted

## Context

We currently run two authentication services in production.

**auth-v1** is the homegrown service we built three years ago. It was the right call at the time. Two engineers - Priya and Marcus - designed it under real constraints: we did not have budget for a vendor solution, our identity model had quirks that no off-the-shelf product fit cleanly, and we needed something running in six weeks. They delivered. auth-v1 has handled billions of authentication events with strong reliability. The shape of our current login flow, our session model, and most of our product engineers' mental model of "how auth works here" all come from their design. I want to name that explicitly because the decision below is about retiring their work, and the retirement is not a judgment on the work itself.

**auth-v2** is our Auth0-backed implementation, shipped two years ago. It exists because the requirements that justified building in-house no longer hold: we now pay for vendor solutions, our identity model has converged toward standards (OIDC, SAML), and Auth0 covers the surface area we used to maintain ourselves. auth-v2 has been the default for all new signups since 18 months ago.

The current traffic split is roughly 80% auth-v2, 20% auth-v1. The 20% on auth-v1 is users who created accounts before the auth-v2 cutover and have not been migrated. They are real customers - some of them are our oldest and most valuable accounts.

Three forces push the decision:

**Operational cost.** auth-v1 requires its own deploy pipeline, on-call rotation slot, security patching cadence, and dependency maintenance. The cost is roughly one engineer-quarter per year of attention. We have not been investing in it; we have been keeping it alive.

**Security surface.** auth-v1 implements its own password storage, session management, and MFA flow. Each of these is a category where the industry has moved fast and we have not. Our last security audit flagged auth-v1's MFA implementation as below current standards. We have a remediation plan, but the honest framing is that we are continuing to defend an implementation we should not be defending.

**Cognitive overhead.** Every new product engineer learns two auth systems instead of one. Every cross-cutting change - rate limiting, audit logging, anomaly detection - ships twice.

Alternatives considered:

1. Maintain both indefinitely. Continue paying the costs above.
2. Sunset auth-v1 over 12 months. Lower migration risk; longer carrying cost.
3. Sunset auth-v1 in 90 days. Higher migration urgency; sharply reduces the carrying cost and forces resolution of the long-tail migration that has been pending for 18 months.

## Decision

Sunset auth-v1 in 90 days. The 20% of traffic still on auth-v1 will be migrated to auth-v2 through a forced password reset flow on next login, with email and in-app notifications starting on day 1.

The 90-day window is firm. We have been doing this slowly for 18 months and the long tail has stopped shrinking. A firm deadline is the lever that converts "we will migrate eventually" into "we are migrating now."

Priya and Marcus are leading the migration plan. This is deliberate. They know auth-v1's edge cases better than anyone, and they should get to be the engineers who land its sunset, not engineers who watch others retire their work.

## Consequences

### Positive

- auth-v1 retires. We recover an engineer-quarter per year of attention.
- The security audit finding closes by retirement rather than by remediation we would then immediately deprecate.
- Onboarding gets simpler. New engineers learn one auth system.
- The team's cross-cutting work (rate limiting, audit logging) ships once.

### Negative

- The 20% of users on auth-v1 will be forced through a password reset. Some of them will experience this as a service disruption. Some of them will not complete the reset and will churn. Based on the migration data we have from earlier voluntary cohorts, I estimate we lose between 0.5% and 2% of the affected users - that is roughly 0.1% to 0.4% of total active users. We should treat this as a known cost and not pretend the migration is friction-free.
- Some of those users are our oldest accounts. The customer success team needs to be ready to handle escalations from named accounts during the migration window. We will pre-brief CS the week before launch.
- The 90-day timeline is aggressive. If we discover a class of users that cannot be migrated cleanly - users with legacy SSO integrations, for example - we may need to extend or carve out an exception. We are committing to the deadline but not to the deadline at any cost.
- This is an interruption to other planned work. The auth team's Q4 roadmap shifts to absorb migration work. Two features that were planned for Q4 move to Q1.

### Neutral

- Communications start on day 1: in-product banner, two email touches (day 1 and day 30), and a help-center article. The CS team gets a runbook for migration-related tickets.
- We will run weekly migration metrics review for the full 90 days. If we are off pace by day 45, we trigger a contingency review rather than a deadline slip by default.
- After sunset, auth-v1's code remains in the repository for 6 months as reference, then is removed in a follow-up cleanup ADR.
