---
entry_id: blog-post-long-form
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Fourteen Months Under the Ice

**What It Actually Cost to Rebuild Checkout While the Store Stayed Open**

There is a category of engineering work that is almost impossible to see from the outside. The systems are running. The customers are checking out. Nothing looks broken, and nothing looks fixed, because nothing looks changed at all - except that it is. Somewhere underneath the visible surface, a team has been rebuilding the foundation while the building stayed open, and the measure of how well they did it is precisely the absence of anything dramatic to point to.

That is what the checkout team at Marlowe Commerce spent fourteen months doing.

On June 12th, they flipped the last routing flag. The old checkout flow - a system that had accumulated more workarounds than original lines over six years - was retired. The new system handled its first full peak-load day without a single escalation. Cart-abandonment rates dropped to a range the business had not seen since its early years. And the team, who had been carrying two production systems simultaneously for most of a year, finally got to carry just one. This post is an attempt to give that work its due - to name what it actually cost and what it took, because this kind of project does not speak for itself.

## The Problem Was Not What It Looked Like

When Carmen Orozco joined the data team in early 2024, one of her first assignments was to dig into the cart-abandonment numbers. The business knew the rate was high. It had been high for two years. The standard explanations had already been explored: friction in the form fields, slow page loads, an unclear total-cost display before the final confirmation step.

Carmen's analysis agreed with those findings - but it also found something underneath them. The abandonment was not randomly distributed across users. It was heavily concentrated in sessions where a user encountered a timeout error, a state mismatch between the cart and the payment step, or a silent failure that showed no error at all but simply failed to commit the transaction. These were not user-experience problems. They were system-integrity problems. The checkout flow had been extended so many times, by so many hands, that it could no longer guarantee its own state.

This finding changed the conversation. Patching the user interface - adding clearer error messages, reducing form fields, speeding up the page - would address visible friction. But it would not fix the silent failures, because the silent failures were not about friction. They were the result of a system that no longer had clean contracts between its own pieces. You could not make that system reliable without rebuilding it.

Priya Sundaram, who led engineering on the project, later described the decision this way: the question was not whether to rebuild - the question was whether to admit that the rebuild was the cheaper path. It felt more expensive. It felt like the kind of decision that requires explaining every quarter for the next year. But the alternative was to keep patching a system that had become structurally unpatchable. The decision was made in April 2024. The project got a name - internally, the team called it Keel - and a target: have a new system in production before the following peak season.

## What Running Two Systems Actually Costs

The word "migration" undersells what Keel required. Migrations move data or traffic from one place to another. What the checkout team built was a fully functional parallel system that had to be correct and current every day, while the old system remained authoritative for every transaction that had not been explicitly moved over.

For the first three months, this was largely invisible to the rest of the company. The team was building. They were not yet maintaining two production systems; they were maintaining one and building a second. But as Keel moved into integration testing and began handling small percentages of real traffic, the maintenance burden began to double. Every incident in the old system had to be triaged against the new one. Every schema change on the old system had to be evaluated for compatibility with the new one. Every edge case discovered in production had to be reproduced, understood, and handled in both codebases.

Dev Matsuda, who owned the backend integration layer, later estimated that for a six-month stretch, roughly a third of his team's capacity was consumed by this synchronization work - work that produced no visible features, no shipped improvements, no changelog entries. It was the kind of labor that does not appear on a roadmap and does not earn a slide in the all-hands deck.

And then came the near-misses.

The first happened in October 2024. A routine change to the payment-provider integration introduced a subtle race condition in the new system's state handling. It was caught in load testing - barely. The root cause took four days to isolate. Had it reached production, it would have manifested as exactly the kind of silent failure the project was built to eliminate: transactions that appeared to succeed to the customer but were not actually committed. The team fixed it, but the discovery was sobering. The new system was not yet safe enough to ship.

The second near-miss was quieter and, in some ways, more expensive. In February 2025, a miscommunication between the data team and the infrastructure team created a window where both systems were writing to the same downstream table during a data-sync event. Nothing broke visibly. But for roughly eighteen hours, the reconciliation data that the business depended on for financial close was inconsistent. Tobias Wren, who led infrastructure, caught the discrepancy before it propagated further. Fixing it required four days of careful data archaeology and a late night that nobody has put on a slide yet. These near-misses did not make the project leaderboard. They are the kind of event that gets handled, gets documented internally, and then disappears from the visible record of a project. But they shaped everything that came next.

## The Slips

The original launch target was February 2025. The team had reasonable confidence in December that they would hit it.

They did not hit it.

The first slip was a direct consequence of the second near-miss. The data-sync issue, once fully understood, revealed a broader class of consistency risk that had not been adequately tested. Rushing to the February deadline would have meant launching a system with a known gap in its consistency guarantees. Priya made the call to slip to April. The conversation with stakeholders was not easy. The project had already been running for ten months. The business was watching the cart-abandonment numbers and asking when the investment would pay off.

The April target held until it didn't. Three weeks before the planned launch, load testing under simulated peak conditions revealed performance degradation in a specific path: bulk-order processing, which accounted for a small fraction of transactions but a significant share of revenue. The path had been tested, but not under the combination of conditions that peak season would produce. The team needed more time.

Priya slipped it again, to June 12th.

The second slip was harder to communicate than the first. By April, stakeholders were not angry - they were beginning to wonder whether the team knew what they were doing. The project had been running for over a year. It had slipped twice. The old system was still running. What was taking so long?

Annika Larsen, who had been managing the stakeholder relationship throughout, later said that the hardest part of the second slip was not the conversation itself - it was the two weeks before it, when the team knew they needed to slip but had not yet made the call. "Everyone was carrying the decision," she said. "You can feel it when a team is waiting for permission to do the right thing."

The call came from Priya, clearly and without hedging: they would not ship until the bulk-order path was solid. The June date was realistic. The April date was not. That distinction - between a date that can be defended and a date that feels defensible - is one of the harder things a technical leader has to hold. Priya held it twice.

## The Night It Held

June 12th was a Thursday. The team began the final rollout at 6 AM, routing ten percent of traffic to the new system. By noon, they were at fifty percent. By 3 PM, they were at one hundred.

The load tests had predicted what would happen. The load tests were right. Traffic routed cleanly. The silent failures did not appear. The performance metrics stayed inside the bounds the team had spent months establishing. Cart-abandonment in the first twelve hours of full traffic was tracking at the level Carmen's models had projected.

At 7 PM, the team stood down from active monitoring. Not because the monitoring stopped - the monitoring never stops - but because the moment had passed where active intervention was likely to be required. Tobias had been watching infrastructure dashboards since 5 AM. Dev had been tracking transaction logs since before breakfast. The system had handled its first full afternoon of production traffic, and it had handled it without event.

There was no launch party. The team was too tired, and the nature of the work - the invisible kind, where success looks like nothing happened - did not lend itself to celebration in the usual way. What most people outside the team saw was: checkout is running. What the team knew was: the thing we built is holding.

A few days later, Priya sent a note to the team. She did not summarize the project or list its outcomes. She named the specific moments: Carmen's original analysis that reframed the problem, the October near-miss and the four-day root-cause hunt, Tobias's call on the data-sync issue, the two slip decisions, the Thursday morning when Dev sat down at 5 AM to watch the logs. She named the people. She said what they had done. It was a short note, and it was more accurate than any project retrospective I have read.

## What This Kind of Work Asks

Not all hard work produces visible artifacts. Not all fourteen-month projects produce a feature you can point to in a changelog. Some work produces something harder to name: a system that does not fail in the ways the old one did, a reliability that reads as absence rather than presence, a customer experience where the test of success is that nothing happens.

The checkout team built that. They did it under a constraint - keeping the old system running throughout - that multiplied their burden without multiplying their recognition. They made two decisions to slip, which took more discipline than launching on the original date would have. They caught two near-misses that most of the company never heard about, and they handled both correctly. The discipline to hold those calls, while stakeholders are asking questions and the calendar keeps moving, is not a skill that shows up in a performance review rubric. It is the skill of knowing what you are actually building and refusing to ship something that is not it.

That work deserves to be named clearly, because the thing that makes it hard is exactly the thing that makes it easy to undervalue: it worked. The fact that it worked looks, from the outside, like it was easy. It was not easy. It was the result of fourteen months of careful, compounding judgment made by people who were tired and still getting it right.

The store stayed open. The new system held. That was the job, and the team did the job.
