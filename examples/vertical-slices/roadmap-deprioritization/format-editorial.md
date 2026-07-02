---
entry_id: editorial
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Better Late Than Half-Built

*The Editorial Board*

We are not shipping the Insights dashboard this quarter. We would rather deliver it complete in the first quarter of 2027 than deliver it broken in September, and we are saying so before the date quietly slides past.

Insights, our in-app analytics dashboard, was committed for the third quarter of 2026. Sales had positioned it as a closing point for several enterprise accounts, and four of those customers were given a specific delivery date. Early in the quarter, a mandatory billing-system migration - required to meet regulatory and contractual deadlines before year-end - surfaced scope that was not visible during planning. The migration and the dashboard draw on the same engineering capacity, and there was never enough of it to protect both.

Two paths were open to us. We could ship Insights on the original date, against whatever state the build happened to be in when the date arrived. Or we could finish the migration cleanly, tell the affected customers the truth, and move Insights to the next quarter in which it could be built properly. We chose the second path. The reasoning matters more than the apology attached to it, so we want to state it plainly.

The Insights build sitting in our repository today is missing saved-view persistence and scheduled-report delivery - the two capabilities every one of the affected customers specifically asked for. A dashboard without them is not a smaller version of what we promised. It is a different product, one that fails at the exact tasks it was sold to do. Shipping it on schedule would have converted a delay into a defect: customers would have opened a tool that could not do the one thing they bought it to do, and we would have spent the following quarter apologizing for a release instead of finishing one.

This is not a new problem, and it will not be the last time we face it. Roadmaps absorb dependencies that are invisible at planning time. When that happens, the choice narrows to the same two options every time: ship what exists, or hold the date and finish the work. We have watched half-built releases cost more in rework and in trust than an honest delay ever does. We are not willing to relearn that lesson on this dashboard.

Here is what we are doing instead. Before the end of this quarter, on September 26, we are shipping a CSV export of the same data the dashboard will eventually surface, so the affected customers are not left with nothing while the full build finishes. The Insights dashboard itself moves to the first quarter of 2027, with a target release of March 13 - a date now locked with engineering, not a placeholder we are hoping holds. We will not fold new scope into that build quietly between now and then. If the plan changes, we will say so in the same place we are saying this.

We would rather be judged against a specific date in public than protect a comfortable one we already knew we could not keep. That is the standard we are holding ourselves to on Insights, and it is the standard we intend to hold ourselves to the next time a dependency eats a quarter, because at some point, it will happen again.
