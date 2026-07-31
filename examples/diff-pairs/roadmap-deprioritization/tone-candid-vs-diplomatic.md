---
diff_pair_id: tone-candid-vs-diplomatic-roadmap-deprioritization
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
axis_varied: tone
entry_a: candid
entry_b: diplomatic
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `candid` vs `diplomatic`

**Topic:** Telling stakeholders a committed feature is being cut this quarter
**Axis varied:** tone
**A:** `candid` - Names the uncomfortable truth directly - not harsh, but unwilling to pretend the hard thing is not there.
**B:** `diplomatic` - Careful, face-saving communication that is soft on people and firm on positions, especially across power differentials.

## What to notice

Breaking a commitment is the sternest test of these two tones, because both are trying not to
make it worse and they choose opposite methods.

**A owns the promise as a promise.** "I want to be direct with you about where Insights
stands. I know this is not what you were promised, and I know some of you have made
commitments to customers based on that promise." It is first person, and it names the
second-order damage, that the reader has now broken promises of their own, before offering
anything.

**B keeps the promise at arm's length.** "We want to address a change to the Q3 roadmap that
directly affects a commitment made to you." The commitment appears as a thing that exists
rather than something the writer made and is now breaking, and "we" spreads the ownership
across an organisation.

**The sharpest single tell is the grammar of the promise.** A says *what you were promised*
and puts a person behind it. B says *a commitment made to you*, agentless. Both sentences
concede the same fact; only one concedes an author.

**Neither is wrong here, and the choice is a real one.** Candour costs the writer standing and
buys trust. Diplomacy protects the relationship and risks reading as evasion at exactly the
moment the reader is looking for someone to be accountable. Read them back to back and decide
which risk you would rather carry.

---

## A: `candid`

I want to be direct with you about where Insights stands.

I know this is not what you were promised, and I know some of you have made commitments to customers based on that promise. That makes what I need to say harder, not easier. Insights is not shipping in Q3.

Here is what happened. A mandatory billing-system migration that had to be completed this quarter ran significantly over projection. It consumed the engineering capacity we had allocated to Insights. When we looked at the resulting timeline, the choice was to ship Insights in an incomplete state or move the date. Shipping half-built analytics to customers counting on it would not serve you or them, so we moved the date.

Insights is now targeted for Q1. We will have a firm date to you before the end of September.

In the meantime, we are shipping something before Q3 closes. In September, we will release a CSV export of the underlying data. It is not Insights. It does not have the in-app dashboards or the visualizations we committed to. But it gives you and your customers access to the data so analysis does not have to stop while we finish building the product.

A CSV is not what you were promised, and I am not presenting it as equivalent. It is a bridge. If you need help talking to your customers about this change, or you need talking points, reach out directly. We will work through that with you.

---

## B: `diplomatic`

We want to address a change to the Q3 roadmap that directly affects a commitment made to you.

Insights (the in-app analytics dashboard) was planned for delivery this quarter, and we understand that many of you have built real expectations around that date. The commitment was genuine, and we recognize that it shaped planning on your side.

A mandatory migration of our core billing infrastructure, initiated earlier this quarter, has expanded well beyond its projected scope. Engineering capacity that was allocated to Insights has been consumed by that work, and we have concluded that shipping Insights before the close of Q3 would mean releasing it in a materially incomplete state. While we considered narrowing the feature scope to preserve the original date, the result would not have served the purpose the dashboard was designed for.

Insights will move to Q1 next year. We want to be clear about that so you have time to adjust plans before the quarter ends.

As a practical bridge, before the end of September, we will ship a CSV export of the underlying analytics data that Insights was built to surface. You will be able to pull that data into your own tools and begin working with it while the full dashboard is in development. This is a narrower capability than what was promised. We are offering it as a stopgap, not a substitute.

We welcome the chance to walk through the Q1 timeline in more detail or to discuss what the CSV export covers. Please reach out and we will make time for a direct conversation.
