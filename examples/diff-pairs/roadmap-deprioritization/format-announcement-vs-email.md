---
diff_pair_id: format-announcement-vs-email-roadmap-deprioritization
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
axis_varied: format
entry_a: announcement
entry_b: email
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `announcement` vs `email`

**Topic:** Telling stakeholders a committed feature is being cut this quarter
**Axis varied:** format
**A:** `announcement` - A direct message telling an audience about something new or changing, in the organization's own voice.
**B:** `email` - A business message designed for the inbox scan - subject line doubles as summary, body leads with action, and the reader never needs to re-read to know what is being asked.

## What to notice

Same news, same week, and the container decides who is being spoken to.

**A is a broadcast with a headline.** "**Insights Dashboard Moves to Q1 2027 - CSV Export Ships
September 26**" carries the entire story in one line, both halves of it, for a reader who may
read nothing else. There is no addressee, because an announcement is posted rather than sent.

**B is sent to named people.** It has a `To:` line, "Insights Rollout Stakeholders (Sales and
Key Customers)", and a subject that has to survive an inbox scan. It also does something the
announcement cannot: it acknowledges the act of writing. "We are writing to tell you directly"
only means something when there is a specific recipient who might otherwise have heard it
second-hand.

**The sharpest single tell.** A has a headline; B has a `To:` line. Ask who is embarrassed if
this is forwarded. For the announcement, nobody, because it was already public. For the email,
possibly someone, because it was addressed.

**Note what both do identically**, which is the part worth copying: each puts the mitigation
in the headline or subject alongside the bad news, so a reader who stops after one line still
learns that something ships in September.

---

## A: `announcement`

**Insights Dashboard Moves to Q1 2027 - CSV Export Ships September 26**

The Insights analytics dashboard is being removed from the Q3 commitment and rescheduled for Q1 2027. A CSV data export ships on September 26 as a stopgap while the full dashboard is under development.

The billing-system migration overran its planned timeline this quarter and consumed the engineering capacity allocated to the Insights build. Releasing the dashboard on the original Q3 date would have meant shipping it without saved-view persistence or scheduled-report delivery - the two capabilities the committed accounts specifically asked for. A partial release would have required immediate remediation and undermined credibility on future commitments. The team deferred rather than ship short.

The CSV export gives affected customers direct access to their underlying event data now. They can open the file in a spreadsheet or BI tool to filter, group by user or feature, and build the views they were waiting on the dashboard to provide. Jordan Park (customer success) is sending written notices to the four key accounts this week and scheduling individual calls with any account that flagged a strong dependency on the Q3 date.

The full in-app dashboard - with date-range selectors, per-feature breakdowns, saved views, and scheduled summary emails - is targeted for March 13, 2027. Engineering is beginning the Q1 design document on October 6, after the billing release stabilizes.

**What you need to do before Thursday:**

- Sales: if any of the four key accounts need a direct conversation before the written notice arrives, flag the account name to Jordan Park. Individual calls reduce the risk of the notice landing cold.
- Leadership: customer-facing outreach will reference the March 13, 2027 target. Please confirm that date is cleared for use in external communications.

Questions about the CSV export or the Q1 scope go to Maya Chen (product) or Dario Reyes (engineering).

---

## B: `email`

**Subject:** Insights dashboard moving to Q1 - CSV data export available in September as interim access

**To:** Insights Rollout Stakeholders (Sales and Key Customers)

We are writing to tell you directly: the Insights analytics dashboard, committed for Q3, is moving to Q1 next year. Before Q3 closes in September, we will deliver a CSV export of the underlying data so you can begin working with it in your own tools while the full product is in development.

The reason for the change is a mandatory billing-system migration that ran significantly over scope and consumed the engineering capacity we had set aside for Insights. We completed our review this week and faced a clear choice: ship on the original date with major functionality gaps, or delay until the product can deliver what we committed. We chose to delay.

We are not asking you to wait without anything in hand. By the end of September, all customers on the Insights rollout list will receive a scheduled CSV export of the same analytics data the dashboard will surface. The export is compatible with any spreadsheet or BI tool you already use. It is not the in-app experience we promised, and we want to be transparent about that distinction, but it gives you access to the data now.

What to expect from here:

- End of September: CSV export delivered with setup instructions from your account team
- Q1 next year: Insights dashboard releases, with priority access for customers affected by this change
- Within the next two weeks: your account manager will contact you with your specific access details and to answer questions

If you want to discuss this before then, reply to this message or reach out to your account manager directly. We recognize this affects plans you may have made around Insights, and we want to make sure you have what you need in the meantime.

Priya Nambiar
VP Product, Meridian Labs
