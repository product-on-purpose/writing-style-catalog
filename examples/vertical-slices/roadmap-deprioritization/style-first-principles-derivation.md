---
entry_id: first-principles-derivation
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

Insights was committed for Q3, and this note works out whether it can still ship in Q3. I will start with six premises. Grant or refuse each one on its own before reading further.

**Premises**

1. **Capacity.** The engineering team has a fixed number of people and weeks between now and September 30. Nothing in the plan adds to it.
2. **The migration cannot move.** The billing-system migration is required, because regulatory and contract dependencies need it to finish before year-end. It cannot be dropped or deferred past that point.
3. **The migration grew.** As of this period, the migration needs more engineering time than was planned for it. This is an observation from the September 1 - 12 work, not a forecast.
4. **What was promised.** The four key accounts were given a Q3 date for Insights, and what they asked for specifically was saved views and scheduled reports.
5. **Build state.** The current Insights build does not yet contain saved-view persistence or scheduled-report delivery. This is an input from the build, stated as one.
6. **The data is already reachable.** The data Insights will display can already be queried, and exporting it as CSV needs about two weeks of work.

**Derivation**

From premise 1, every week spent on one workstream is a week unavailable to another. Capacity can be moved, but it cannot be created.

From premises 2 and 3 and the step above, the migration takes the capacity it needs, and that capacity comes out of what was reserved for Insights. The migration is the only workstream that cannot give any back.

From premises 4 and 5, the build on its original date would arrive without the two things the committed accounts asked for. A product that fails the stated use for which it was promised does not meet the commitment, even though it ships on the date.

So there are two outcomes available in Q3, and only two. Insights ships on time and incomplete, or Insights does not ship in Q3. The step above says the first outcome does not meet the commitment, so the commitment is already unmet under both. The remaining question is which unmet outcome costs the committed accounts less.

An incomplete build in customers' hands has to be finished while they are using it. That means changes landing during their year-end quarter, on top of a missing feature. Not shipping costs them the date and nothing else. From premise 1, finishing the build properly needs capacity that only exists after the migration completes, which puts it in Q1.

From premise 6, one part of the commitment can still be honored. The data can reach the accounts by CSV before September 30, and the export work is small enough to fit around the migration. The target release is September 26, owned by Dario Reyes.

**Conclusion**

Insights is cut from Q3 and moves to Q1 2027, with a target of March 13, 2027. A CSV export of the underlying data ships on September 26. This follows from the chain above. It is not a preference, and I would have reached the opposite answer if any link above had failed.

**Where to push**

The load-bearing premise is number 2. If the migration could be deferred past year-end, premise 3 would no longer take capacity from Insights, and shipping Insights complete in Q3 would be possible. I do not believe it can be deferred, but that belief is the whole case, so refuse it here if you can.

The second joint is premise 4. If the four accounts would accept the dashboard without saved views and scheduled reports, the incomplete build would meet the commitment, and the cut would not be needed. Jordan Park is confirming this account by account this week.

The Q1 date rests on premise 1 holding through Q4. It is a target, and it becomes a firm date only after Q4 planning confirms the capacity.
