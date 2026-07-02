---
entry_id: listicle
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# 6 Things to Know About the Insights Delay This Quarter

Insights was supposed to ship as a full in-app dashboard before this quarter closes, and four accounts already have that date in writing. It's not shipping on schedule. If you're fielding questions about it from a customer, a rep, or your own team, the reasoning matters more than the headline, and it's easy to get wrong secondhand.

1. **The Q3 dashboard isn't shipping.** Insights, the in-app analytics dashboard, was committed for Q3 2026 delivery to the sales team and four key accounts. That date is being missed. The dashboard is being deferred, not shipped in a reduced state just to hit the date.

2. **A mandatory billing migration ate the capacity.** The billing-system migration supporting the new plan structure in pilot isn't optional; it has regulatory and contract dependencies that have to close before year-end. It expanded past its original estimate and consumed the engineering time set aside for Insights. The two workstreams couldn't run in parallel without putting both at risk, and billing doesn't lose that trade-off.

3. **Shipping now would have meant shipping it broken.** The build in progress is missing saved-view persistence and scheduled-report delivery, the two capabilities the four committed accounts specifically asked for. Releasing without them hands people a dashboard that fails at the exact use case they were sold. Cleaning up after a disappointing launch costs more than an honest delay does.

4. **A CSV export ships September 26 in the meantime.** The data Insights will eventually surface is already queryable, so a CSV export of it ships before the quarter closes. Pull it from Settings > Data and Analytics > Export > Download CSV; most accounts get their file within a few seconds, covering every usage event from account creation through the previous calendar day. It's a smaller experience than the dashboard, and it beats waiting until Q1 to touch your own data.

5. **Q1 2027 has a locked scope and a real date.** Engineering has committed six views, filter controls, date-range selection, saved views, and scheduled reports for a March 13, 2027 release. The design document starts October 6, once the billing release has stabilized. That date is directional until Q4 planning closes the capacity plan, and that caveat is worth saying out loud instead of letting people assume it's final.

6. **The four key accounts get a call, not just an email.** Written notice goes out this week, but a notice alone isn't the plan for anyone who built commitments around the Q3 date. Jordan Park is scheduling individual calls with every account that flagged a strong dependency on that date. Sales has until Thursday to flag any account that needs one before the written notice lands.

None of this makes the missed Q3 date easier to hear. It does mean the March 13, 2027 target is one the team checked before saying it out loud, rather than one we're hoping holds.
