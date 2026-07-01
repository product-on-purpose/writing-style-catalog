---
entry_id: cold-outreach
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Subject: Question about the orders idempotency window (ORD-1188)

Dana, the comment on the idempotency-window constant in orders/checkout.go points back to a design note you wrote before moving to the payments team, explaining why the window is capped at 90 seconds.

I am the new engineer on backend services, started June 22, and I am in that same file this week for ORD-1188 - my first scoped change extends the window to close a retry gap we caught in design review. The note covers the abuse case clearly, but I cannot tell if 90 seconds is also protecting something it does not mention.

If the answer is a quick yes or no, a reply works - if it needs more context, fifteen minutes would clear it up.

Priya, backend services, new as of June 22
