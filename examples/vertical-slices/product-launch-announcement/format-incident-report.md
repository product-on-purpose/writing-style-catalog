---
entry_id: incident-report
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Incident Report: Tidemark Sign-Up Unavailable During Launch Window (INC-2026-001)

## Status

Resolved - June 30, 2026, 12:22 UTC

## Summary

On June 30, 2026, the Tidemark sign-up and waitlist flow at tidemark.io was unavailable for approximately two hours during the public launch window. Users who visited the site during that period were unable to join the waitlist or complete a new account registration.

## Impact

- Services affected: tidemark.io sign-up flow, waitlist enrollment, new account registration
- Customers affected: All new visitors to tidemark.io between 10:08 and 12:14 UTC on June 30, 2026
- Duration: 10:08 UTC to 12:14 UTC (approximately 2 hours 6 minutes)

## Timeline

- 10:00 UTC - Public launch announcement published; distribution to waitlist members, press contacts, and community channels begins
- 10:08 UTC - Sign-up flow begins returning errors; first reports arrive at launch@tidemark.io
- 10:15 UTC - Team confirms the sign-up flow is unavailable; investigation begins
- 10:40 UTC - Root cause identified: database connection limit reached under launch traffic levels
- 11:05 UTC - Configuration change applied and rollout begins
- 12:07 UTC - Sign-up flow confirmed stable; monitoring begins
- 12:14 UTC - Sign-up flow re-enabled for all incoming traffic
- 12:22 UTC - No further errors detected; incident declared resolved

## Root Cause

The sign-up service was configured for the traffic levels observed during early-access testing with the initial cohort of twenty-two teams. At public launch, incoming traffic arrived faster than that configuration could handle. When the system reached its connection limit, new requests could not complete and returned errors rather than being queued. The configuration that performed correctly in testing was not adjusted to account for the larger audience expected at launch.

## Resolution

The team updated the database connection configuration and restarted the sign-up service with the new settings. Traffic resumed without errors. No account data was lost or partially written during the outage. Users who received an error while attempting to sign up were not partially enrolled and can complete their registration at tidemark.io.

## Next Steps

- Add a traffic-profile review step to the pre-launch checklist so that service configuration limits are validated against expected launch-day volume before any future announcement goes out (owner: product team, target: July 14, 2026)
- Implement a queued fallback response so that if the sign-up service reaches capacity during a high-traffic event, users see a position-in-queue message rather than an error (target: July 31, 2026)
- Send a direct note to early-access cohort members and press contacts who received the launch announcement during the outage window, acknowledging the disruption and confirming that sign-up is now open (target: end of day June 30, 2026)
