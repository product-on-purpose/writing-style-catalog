---
diff_pair_id: style-decision-log-vs-problem-solution-roadmap-deprioritization
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
axis_varied: style
entry_a: decision-log
entry_b: problem-solution
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `decision-log` vs `problem-solution`

**Topic:** Telling stakeholders a committed feature is being cut this quarter
**Axis varied:** style
**A:** `decision-log` - A real-time record of context, options considered, criteria used, and reasoning - capturing how a decision was reached, not justifying it after the fact.
**B:** `problem-solution` - Frames the piece as a diagnosis followed by a remedy - establishes the pain before the cure.

## What to notice

Both explain a cut, and they answer to different readers.

**A is written for the record.** It opens on `## Context` and reconstructs the state before
the decision: Insights was committed for Q3, and the commitment was made to the sales team as
a close tool for named accounts. That detail exists so a future reader can judge whether the
decision was reasonable on what was known at the time. The reader is implicitly a colleague,
possibly a later one.

**B is written for the person holding the broken commitment.** Its heading is the reader's own
question, "## What Happened to Insights, and What Ships Instead", and its second sentence is
about their exposure: "You made plans around that commitment - sales conversations, customer
expectations, roadmap conversations with your own stakeho[lders]."

**The sharpest single tell is who appears in the second person.** A has no "you" to speak of;
B is built around one. A decision log that starts addressing the affected party has become a
communication, and a communication that starts reconstructing the decision timeline has
started asking the reader to audit rather than to adapt.

**Both are needed, and they are not substitutes.** The log is what you keep; the
problem-solution piece is what you send.

---

## A: `decision-log`

## Context

At the start of Q3, Insights was committed as a Q3 deliverable - a real-time analytics dashboard surfacing product usage data. The commitment was made to the sales team as a close tool for several in-flight deals, and to key customers who had requested the capability explicitly. Two engineering teams were allocated.

In week seven of Q3, a mandatory billing-system migration - a compliance requirement triggered by a vendor contract change - overran its projected timeline by four weeks. Both teams were reassigned to prevent the billing system from entering an unsupported state before the contract deadline. Neither team could continue Insights work during that period. When the migration completed, six weeks remained in Q3. Completing Insights to a stable, testable state required nine to ten weeks of remaining engineering work.

## Options Considered

Three options were on the table as of August 19, once the migration overrun was clear:

1. Ship on the original Q3 date, with the export, filtering, and drill-down features incomplete.
2. Move Insights to Q1 with no interim deliverable.
3. Move Insights to Q1 and ship a CSV export of the underlying data in September, usable in a spreadsheet or BI tool.

## Criteria

Three constraints governed the evaluation, in order of weight:

- Do not ship a partial product against a full promise. A half-built dashboard resets customer expectations downward.
- Provide something of value before year-end to the customers who waited. A pure deferral is harder to absorb than a deferral with interim capability.
- The interim capability must be low-risk. The team is stretched after the migration; a complex stopgap adds compounding risk.

## Decision

Insights moves to Q1. A CSV export of the underlying data ships in September before Q3 closes.

Option 1 was eliminated: shipping a partial dashboard against a full-scope promise sets an expectation we cannot sustain. Option 2 was viable but left customers with nothing for two quarters. Option 3 is chosen because a CSV export is low-scope, low-risk, and genuinely useful. Customers who need the data can load it into a spreadsheet or BI tool and begin analysis now. It does not substitute for Insights, but it delivers the underlying data access that motivated the original request.

The migration overrun is the proximate cause of this change, not a shift in product priority. The reasoning behind the Q3 commitment was sound when it was made. The capacity that would have delivered Insights was consumed by a compliance dependency that could not itself be deferred.

---

## B: `problem-solution`

## What Happened to Insights, and What Ships Instead

We committed Insights for Q3. You made plans around that commitment - sales conversations, customer expectations, roadmap conversations with your own stakeholders. We owe you a clear account of why that date is not holding and what we are doing about it.

## The Problem

Partway through August, we were six weeks behind on Insights. The cause was a billing-system migration that ran longer and deeper than the estimate we built the quarter's capacity plan around. The migration is not optional - it closes a compliance gap that would otherwise affect every customer's billing accuracy. But it consumed the engineering time allocated to Insights.

At that point, we had a choice: ship what was done on the original date, or move the full feature and ship something useful in its place.

Shipping the partial build was the wrong call. The version of Insights that was shippable in Q3 was missing date-range filtering, multi-metric overlays, and CSV export - the three capabilities named in nearly every sales conversation and customer discovery call. A dashboard that can display only a single metric for the current period is not the product you committed to. Shipping it would have required a second onboarding when the rest of the features arrived, and it would have anchored your customers' first experience to something we know is incomplete.

## The Path Forward

By the end of September, we are shipping a CSV export of the underlying Insights data. The export includes the same event streams Insights will visualize: session activity, feature-interaction rates, and funnel completion broken down by cohort. You can load it into a spreadsheet or BI tool you already use and run the analysis you have been waiting for.

The full Insights dashboard - with date-range filtering, overlays, and saved views - ships in Q1. We are locking scope now so engineering can start immediately after the billing work wraps, with no planning gap between.

We will send the export field guide and file format on September 15. When the Q1 launch date is confirmed, you hear it before anyone else does.

If there is a specific workflow - a customer-facing report, a board deck, a quarterly review - that the delay creates a concrete problem for, tell us now. We will work out a bridge.
