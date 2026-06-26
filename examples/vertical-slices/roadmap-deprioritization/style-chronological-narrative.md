---
entry_id: chronological-narrative
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

When we entered Q3 in early July, Insights was at the top of the engineering queue. We had scoped it in June, confirmed the build capacity, and committed September as the ship date. Several of you had already aligned internally around that date, and we knew it carried real weight.

Work began in the first week of July. The team broke ground on the data pipeline and the dashboard interface simultaneously, and by mid-July the core query layer was taking shape.

Around the same time, a mandatory migration of our billing system entered the schedule. The migration had a hard deadline set by our payments processor and could not be deferred. We estimated four weeks of engineering work, enough to run it alongside Insights without collision.

By the end of July, the billing migration had consumed more than the four weeks we had planned for it. Integration testing surfaced edge cases in our subscription logic that required rework, and the dependency on a third-party payments API introduced latency we had not anticipated. The team pulled additional engineers from Insights to stabilize the billing work before it could slip past the payments processor's cutover window.

Through August, as the billing work continued to absorb capacity, the Insights build slowed. By late August, we could see clearly what the September date would produce: a dashboard that rendered but could not support the filtering, segmentation, and export features that made the product useful. Shipping that version would have meant shipping something we would immediately need to apologize for.

We decided not to ship Insights in Q3.

Instead, by the end of September, we will deliver a CSV export of the underlying usage data so you can pull it into a spreadsheet or BI tool and work with it in the meantime. It is not the dashboard, and we know it is not what you planned for, but it gives you access to the data while we complete the build.

Insights is now scheduled for Q1. We will share a more specific date once the billing migration is fully closed out and we have a clean sprint plan in front of us.
