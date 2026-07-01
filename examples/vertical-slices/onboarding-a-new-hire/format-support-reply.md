---
entry_id: support-reply
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**Subject:** Re: Staging environment access (INFRA-2287)

Hi Priya,

Thanks for your patience - the staging access ticket opened on Jun 23 sat in our queue longer than it should have, and Mei's follow-up Friday moved it to the top of my list.

Your individual staging credentials are live as of Monday morning (Jun 29):

1. Your own login to the staging namespace under `backend-services`, replacing the team's shared credential
2. A personal staging database credential, active now
3. Individual staging scope in the secret manager, separate from the team's broad grant

Connect to staging directly today, before Thursday's on-call alert drill, to confirm everything resolves cleanly while there is still time to fix anything that does not. This does not change your schedule - you are clear for Thursday as planned.

Let me know if this does not resolve the issue or if you have any questions.

Felix
Infra / Platform Support
