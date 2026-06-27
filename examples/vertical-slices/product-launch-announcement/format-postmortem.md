---
entry_id: postmortem
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Sign-up Flow Outage During Tidemark Public Launch

## Severity

SEV-2

## Summary

On June 30, 2026, from 09:17 UTC to 09:55 UTC, the waitlist sign-up form at tidemark.io returned a 502 error to all visitors attempting to join the launch waitlist. The outage coincided with the first 38 minutes of peak inbound traffic following the launch announcement. Visitors could reach the landing page and watch the demo video but could not sign up. No data was lost and the Tidemark product itself was unaffected.

## Timeline

- 08:45 UTC - Launch announcement email sent to the full early-access cohort with a link to join the public waitlist at tidemark.io.
- 09:00 UTC - Scheduled social posts begin publishing.
- 09:14 UTC - First traffic spike to tidemark.io registers in server logs.
- 09:17 UTC - 502 errors begin on the sign-up endpoint. No alert fires.
- 09:31 UTC - A member of the early-access cohort replies to the launch email: "the sign-up link seems broken."
- 09:38 UTC - Marisol Veen reads the reply, opens tidemark.io, and confirms the 502.
- 09:42 UTC - Infrastructure configuration review identifies the cause: the sign-up service is still pointing at the staging database endpoint, not the production one.
- 09:55 UTC - Configuration updated and redeployed. Sign-up form returns 200. Manual sign-up verified by two team members.
- 10:44 UTC - Monitoring confirms error rate has returned to baseline and remained there for 30 minutes. Incident closed.
- 11:00 UTC - Brief acknowledgment sent to the early-access cohort and posted to the same social channels used for the launch announcement.

## Root Cause

The sign-up service was deployed to production on June 29 but its environment configuration was carried over from the last staging test run and was never updated to point at the production database endpoint. The staging endpoint remained live and accepted connections, which is why the misconfiguration was not caught during the June 28 smoke test - the sign-up form submitted successfully against the staging path even after the production deployment.

The root cause is not a wrong configuration value in isolation. The root cause is that the launch checklist treated "deploy the sign-up service" and "verify the sign-up form works" as two separate checklist items without specifying which environment the verification step should run against. The checklist had no step that confirmed the active database endpoint in the production environment. A verification step that can pass against a live staging path is not a production verification step.

## Impact

- Visitors affected: 214 failed sign-up attempts recorded in post-incident log analysis during the 09:17 to 09:55 UTC window. Traffic volume was not instrumented before the outage, so the total number of visitors who hit the error and did not retry is unknown.
- Duration: 09:17 UTC to 09:55 UTC (38 minutes of active error); monitoring confirmed full recovery by 10:44 UTC.
- Services affected: Sign-up form endpoint at tidemark.io. Landing page, demo video, product application, and help documentation staging were unaffected throughout.

## Contributing Factors

- The launch checklist verification item for the sign-up form did not specify that verification must confirm the active database endpoint in production, not just that the form workflow completes.
- No error-rate alert was configured on the sign-up endpoint. Detection depended on a cohort member noticing and replying to an email, which added 21 minutes between first failure and team awareness.
- The staging database was not decommissioned or isolated after the production deployment. Its continued availability allowed pre-launch smoke tests to pass against a path that diverged from production.
- Social posts were queued the night before and continued publishing throughout the 09:17 to 09:55 UTC window, directing new traffic to a broken sign-up flow with no automated circuit to pause them.

## Action Items

- [ ] Revise the launch checklist sign-up verification item to explicitly require confirming the active database endpoint in the production environment, not only that the sign-up workflow completes. Owner: Marisol Veen. Due: 2026-07-14.
- [ ] Configure an error-rate alert on the sign-up endpoint: page the on-call contact when 502 errors exceed 5% of requests over any 2-minute window. Owner: Infrastructure team. Due: 2026-07-07.
- [ ] Add a step to the production deployment runbook to either decommission staging endpoints or explicitly document that staging remains live, with a corresponding note in the verification checklist. Owner: Infrastructure team. Due: 2026-07-07.
- [ ] Add a pre-launch health check to the scheduled-posts workflow: if the sign-up endpoint is degraded at post-scheduling time, hold the posts until a team member confirms the issue is resolved or clears the hold manually. Owner: Marisol Veen. Due: 2026-07-21.

## Lessons Learned

A checklist item is only as strong as its specificity. "Verify the sign-up form works" does not catch an environment misconfiguration when a staging path that happens to be functional is available. The checklist must name what is being verified and in which environment, not just that a workflow completes.

The team had no monitoring on the single endpoint most likely to be overwhelmed on launch day. The first signal was a cohort member's email reply, 21 minutes after the first error. With a 2-minute alert threshold, the incident response would have started before 09:20 UTC and the outage would have been materially shorter.

The 214 visitors who encountered the error during the window cannot be recovered. The acknowledgment sent at 11:00 UTC named the issue directly and confirmed the form was live - that post also gave context to anyone who had shared the broken link during the outage window.
