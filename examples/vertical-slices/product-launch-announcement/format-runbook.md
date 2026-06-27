---
entry_id: runbook
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Tidemark Public Launch Announcement

## Overview

Execute the Tidemark public announcement sequence on June 30, 2026, opening the product to the public and activating all pre-staged launch assets.

## Prerequisites

- [ ] Help documentation (8 articles) is staged and passes a final link check
- [ ] Landing page at tidemark.io shows correct pricing: free solo plan, $29/month team plan, and custom plan for SSO/audit-log organizations
- [ ] Self-serve sign-up flow has been tested end-to-end and returns a confirmation email without manual intervention
- [ ] Waitlist notification email is drafted, addressed to the full waitlist, and queued but not yet sent
- [ ] Early-access cohort offboarding email (including the direct community-sharing ask) is drafted and queued
- [ ] Press brief has already been sent; confirm launch@tidemark.io inbox is staffed and monitored
- [ ] Launch assets (product screenshots, 90-second demo video, one-page product summary) are accessible from a shared folder reachable by the whole team
- [ ] Usage monitoring and the 90-day free-plan volume threshold alert are active

## Procedure

1. **Deploy the staged help documentation**
   Expected output: All 8 help articles load at their public URLs with no 404 responses; the "Getting started" article is linked correctly from the tidemark.io landing page.

2. **Open the waitlist to all new sign-ups**
   Expected output: The waitlist sign-up form at tidemark.io accepts a test submission and returns a confirmation message indicating the submission entered the rolling queue.

3. **Send the waitlist notification email to all existing waitlist members**
   Expected output: The send completes without bounce errors; existing waitlist members receive a message granting same-day access with a direct link to the sign-up flow.

4. **Send the early-access cohort offboarding email**
   Expected output: Email delivered to all 22 teams in the cohort. The message includes the direct community-sharing ask and links to the relevant community spaces. Confirm delivery in the outbound mail log.

5. **Confirm press contacts can reach launch assets**
   Expected output: Navigate to the shared asset folder and verify screenshots, demo video, and one-page product summary are all present and downloadable. Send a brief confirmation note to launch@tidemark.io - this creates an audit record in the inbox.

6. **Verify the walkthrough booking link is accepting reservations**
   Expected output: The 20-minute walkthrough booking link on the landing page opens a calendar with at least one available slot in the next 7 days and accepts a test booking without errors.

7. **Record the launch timestamp and initial sign-up count**
   Expected output: Time the waitlist opened and the sign-up count at T+0 are logged in the launch tracking document. This baseline is required for the July 7 retrospective with the early-access cohort.

## Verification

Fifteen minutes after completing the procedure, confirm all of the following from a browser session with no saved login:

- tidemark.io loads and displays current pricing (free solo, $29/month team, custom)
- All 8 help doc links in the documentation index resolve without errors
- The waitlist sign-up form accepts a new submission and returns a queue-confirmation message
- launch@tidemark.io is reachable: send a test message and confirm receipt in the inbox

If any check fails, do not treat the launch as complete. Identify which step produced the broken state and re-run from that step.

## Rollback

Press outreach and cohort emails cannot be unsent. Rollback applies only to the public-facing sign-up flow and help documentation.

If the sign-up flow is confirmed broken after Step 2 completes:

1. **Disable the sign-up form** on the landing page.
2. **Replace the form** with a static message: "Sign-up is temporarily unavailable. Check back shortly or email launch@tidemark.io."
3. **Send a follow-up email** to the waitlist notification list acknowledging the delay and providing an estimated restoration time.
4. **Leave the help documentation live** - do not roll back the Step 1 deployment.

Once the sign-up flow is repaired, re-run Steps 2 and 6, then repeat the full Verification section before treating the launch as complete.

If fewer than 8 help articles are accessible after Step 1: mark unavailable articles as "coming soon" in the documentation index rather than pulling the entire index offline. Proceed with remaining steps and notify Marisol Veen.

## Escalation

**Sign-up flow not restored within 30 minutes:** Marisol Veen (Head of Product) posts a hold notice on tidemark.io and sends a direct note to the press contact list acknowledging the delay.

**Unexpected infrastructure load from free-plan volume:** Flag to Marisol Veen immediately; the team holds a threshold review before the 90-day free-plan window closes, per the plan established during early access.

**Any other unresolved failure:** Contact Marisol Veen directly and halt remaining procedure steps until the failure is diagnosed.
