---
entry_id: newsletter
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**Subject:** Product Pulse - Why Insights is moving to Q1 (and what ships instead this month)

Hi all,

This issue leads with the harder story first, because I'd rather you hear the full reasoning from me than piece it together secondhand. Insights, the analytics dashboard we committed to for this quarter, is moving to Q1 2027. Here's what happened, and what's shipping in the meantime.

---

**Insights moves to Q1. Here's why, and what ships instead.**

We went into Q3 with a firm date on the Insights dashboard. Sales had used that date to close several enterprise deals, and four key accounts were told exactly when to expect it. Then the billing-system migration, the one supporting the new plan structure currently in pilot, ran long. That work isn't optional: regulatory and contract dependencies require it to land before year-end. It absorbed the engineering capacity we'd set aside for Insights, and the two workstreams couldn't run in parallel without putting both at risk.

That left two options: ship Insights on the original date in whatever state the build was in, or pull it so the billing migration finishes without a competing deadline. The current build is missing saved-view persistence and scheduled-report delivery, the two capabilities our committed customers specifically asked for. Shipping without them would mean handing people a product that fails at the exact use case we sold them on, and cleaning up after a disappointing launch costs more than an honest delay does. So we're taking the delay.

We're not leaving customers empty-handed for the quarter, though. The data Insights will eventually surface is already sitting in the data layer, queryable today. Dario has the backend endpoint done by the 19th, frontend and QA wrapped by the 24th, and the export live for customers on the 26th, so anyone who needs their numbers now can pull them into a spreadsheet or BI tool of their choice while the full dashboard gets built properly. It's a smaller experience than the dashboard, and I'd rather say that plainly than oversell it.

Insights is now targeted for Q1 2027, with a release date of March 13, 2027. That target is a directional commitment, not a closed capacity plan, since Q4 planning still has to confirm it, and I'd rather tell you that now than have it slip quietly later. The scope is locked with engineering: six views, filter controls, date-range selection, and the saved-view persistence and scheduled reports we weren't willing to ship without. Those two capabilities are the reason we didn't ship in Q3, so a March date that includes them is worth more to our customers than a rushed Q3 date that doesn't.

Written notice goes out to the four key accounts this week, with individual calls for anyone who wants to talk it through rather than read it in an email. That's Jordan's outreach; if you're fielding questions from an account that isn't on the list, loop Jordan in directly.

---

**What I'm pointing you to this week:**

- [ADR-0027: Defer Insights Dashboard to Q1; Ship CSV Export as Q3 Stopgap](docs/adr-0027-defer-insights.md) - the full decision record, including the option we ruled out and why. Read this if you want the unfiltered version instead of my summary above.
- [Billing migration notes](docs/billing-migration-q3.md) - the workstream that displaced Insights. It moves to production the week of September 19, which is most of why I trust the Q1 target.
- [Export column definitions](docs/export-schema.md) - what's actually in the CSV: user, event, timestamp, session, and plan tier. Worth a look if your team wants to plan against it before the 26th.
- [Q1 Insights scope](docs/roadmap-q1.md) - the locked feature list for March, for anyone who wants to see what we protected by not shipping a rushed version now.

---

Delay announcements are never the fun issue to write, but I'd rather you get the reasoning straight from me than filtered through three retellings. Questions go to me directly, always.

Maya

Product Pulse is written by Maya Chen (Product) for Meridian stakeholders subscribed to product updates. Manage preferences or unsubscribe anytime from the link in your account settings.
