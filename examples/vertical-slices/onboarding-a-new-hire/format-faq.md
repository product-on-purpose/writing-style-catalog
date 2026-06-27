---
entry_id: faq
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Frequently Asked Questions - New Engineer Onboarding

### What should I do on day one?

Work through the access checklist with your buddy. It covers source control org membership, VPN and SSO setup, CI/CD access, the observability platform, on-call viewer, secret manager, and the four core chat channels. Do not move on until every item is verified - the bootstrap script will tell you exactly what is still missing. Your buddy owns the checklist with you; nothing on it is expected to be self-solved.

### How do I get my local environment running?

Clone the services repo and run `./scripts/bootstrap.sh`. The script installs local tooling, sets environment variables, and runs the health check suite. If it exits with an error, read the output before asking a teammate - it prints exactly what is missing. When `make smoke-test` passes, your environment is healthy.

### What is the goal for week one versus week two?

Week one is orientation, not output. The three things that matter: trace one real production request from the API gateway to the data store using the observability platform, meet the owners of the services you will touch first, and watch one live deploy with the on-call engineer. Week two flips to output - you implement a scoped first change, write the test, and own the deploy end to end.

### Who is my buddy and what do they actually do?

Mei is the onboarding DRI and your point of contact for any gap in the plan. Your peer buddy handles the access checklist with you in days one and two and runs two 90-minute guided walkthroughs in week one - one on service topology and one on deployment and on-call tooling. Notes from those walkthroughs belong to you, not the buddy. In week two, Arjun is paired as a reviewer and available to pair on blockers while you drive your first change.

### What does my first real change look like?

The team picks a ticket from the `good-first-issue` label before your first day. It touches one service and one data model, has a test you can write in under an hour, and does not require on-call context to understand. You drive the implementation and the deploy; your reviewer is there for blockers and the pull request review, not to take over. The goal is that you own the full cycle end to end.

### When do I go on call?

On-call starts at week five. You are excluded from the rotation for your first thirty days. In week one you observe a live deploy and join the on-call handoff call so you know the cadence and the escalation path - that is learning, not responsibility.

### What if I am blocked or something is missing from my access?

Tell your buddy the same day. Access gaps are expected and your buddy is the named owner of resolving them. If a provisioning request is stuck in the infra queue - like a staging environment credential - Mei can escalate through the engineering manager. Do not absorb delays silently; the protocol is designed to catch these, but only if someone surfaces them.

### What happens at the end of the two weeks?

There is a thirty-minute retrospective on the last Friday to close the formal onboarding window and surface anything still open. The retro asks about belonging explicitly - functional progress does not automatically answer that question. The buddy relationship does not end at two weeks; it typically continues as an informal channel. On-call briefings continue into week three and beyond as you build system familiarity.
