---
entry_id: blog-post-long-form
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# What We Owe You When a Commitment Changes

We promised you Insights this quarter. We are not delivering it this quarter.

That sentence is the hardest thing to write in this post, so let's get it out front where it belongs. Insights - the in-app analytics dashboard we committed to ship in Q3 - is moving to Q1 of next year. If you are on our sales team reading this, or if you are a customer who asked us directly about Insights and heard us say "Q3," you have every right to be frustrated. We heard you, we said yes, and now we are saying something different.

What we want to do in this post is give you the full picture: what happened, what we decided, what we are shipping as a bridge, and when you can actually count on Insights. Not because transparency is a good brand posture - that framing makes the whole thing feel managed - but because you made decisions based on what we told you, and you deserve to understand what changed and why.

## The Migration That Changed Our Quarter

In May, our legal and finance teams flagged a compliance requirement in our billing infrastructure that we could not defer past the end of Q3. The specifics are operational, but the short version is that our billing system needed to be migrated to a new provider to satisfy a contractual obligation with one of our payment processors. This migration was not discretionary. If we did not complete it by September 30, we would have been in breach of terms that affect every customer's ability to pay us.

We started the migration in early June with what we believed was a solid timeline. Our infrastructure team estimated six weeks of work. That estimate turned out to be wrong in the way that estimates about legacy billing systems are often wrong: we encountered undocumented dependencies and data integrity issues that we could not have anticipated without doing the work. By mid-July, it was clear that the migration was going to consume the engineering capacity we had planned to spend on Insights.

At that point we had a decision to make. We could push the migration to the side and try to ship Insights on schedule, which would have meant putting a compliance requirement at risk. We could try to do both, which would have meant understaffing both and likely shipping neither well. Or we could finish the migration, protect the thing we did not have a choice about, and be honest with you about what that meant for Insights.

We chose the third option. What the rest of this post is about is what that choice means in practice.

## Why We Did Not Ship Insights Anyway

Here is the part we want to be direct about, because we think it matters more than the explanation above.

Even setting the migration aside, we could not have shipped Insights in its current state and called it done. The core data pipeline works. The underlying data is solid. But the dashboard layer - the filters, the date-range controls, the visualization components, the ability to drill into individual records - is roughly sixty percent complete. The remaining forty percent is not polish. It is core functionality that determines whether the product is actually useful.

We considered shipping what we had under a "beta" label. We considered calling it an early access release. We turned those options over for a week and kept coming back to the same problem: an analytics dashboard that cannot filter by date range or break down data by the dimensions you actually care about is not a beta product. It is a broken product with a beta label on it. Sending you to a broken product while calling it the thing we promised would have been worse than saying what we are saying now.

An in-app analytics dashboard exists to save you time. Its whole value proposition is that you can answer questions about your data inside the product, without pulling data out and doing the work elsewhere. A dashboard that does not do that does not give you a beta version of the value. It gives you no version of the value, with an extra step of logging into a new part of the product to discover the gap.

We have seen what happens when teams ship something that looks like the promised feature but is not. Users explore it, find the gaps, and stop trusting the product's changelog. Getting that trust back takes longer than the delay would have. We have been on the receiving end of that as users ourselves, and we decided we were not willing to do it to you.

## What We Are Shipping Before Q3 Ends

We are not going to leave you with nothing.

By the end of September, we will ship a CSV export of the underlying Insights data. This is not Insights. We want to be clear about that so there is no confusion. You will not get a dashboard. You will not get in-product filters or visualizations. What you will get is a structured, well-documented export of the same data that Insights will eventually surface - your event counts, your user activity records, your conversion funnel data - formatted so it can be loaded directly into a spreadsheet or BI tool you already use.

This gives you something real. If you have been waiting for Insights because you have reporting questions you cannot currently answer, the CSV export will let you start answering them now. The format will match the eventual Insights schema, so any analysis you build in a spreadsheet or BI tool today will map cleanly to Insights when it ships. We are treating the export as a compatibility bridge, not a throwaway feature.

What it does not give you is the in-product experience. You will still need to pull the data out, load it somewhere, and do the analysis in a separate tool. We know that is the thing you were trying to avoid by asking for Insights. We know this is a partial answer. We are offering it because it is the honest partial answer - something with actual utility, clearly labeled for what it is, rather than a product that looks complete but delivers nothing when you try to use it.

The export will ship to all accounts before September 30. You will receive a product announcement when it is live, with documentation on the data structure and example queries to get you started quickly.

## Where Insights Goes From Here

Insights is now a Q1 commitment. That means a ship target in the January-to-March window of next year. We are not putting a specific date on it today because the right thing to do is let the team close out the billing migration, finish Q3 cleanly, and then plan Q4 work with an honest view of capacity. We will share a firmer timeline in October, when we have that view.

What we can tell you about Q4 is that it is budgeted primarily around Insights. The migration is done; it will not bleed into the next quarter. The Insights work that exists - the data pipeline, the backend services, the initial dashboard components - is solid and will carry forward. We are not starting over. We are finishing.

A few things will be different in the Q1 build compared to what we had originally scoped for Q3. Based on the questions we heard most often from customers and from the sales team over the past several months, we are moving the filter and breakdown experience to the top of the priority list. Those capabilities were part of the original release plan but were ranked below the core metrics views. They are now ranked first.

The reason for the change is what we learned from scoping the CSV export. The most common question customers bring to us is "show me this number broken down by this dimension over this time period." If we ship Insights without that being fast and obvious, we will have a dashboard that technically shows data but does not answer the question people actually have. That is not acceptable. We would rather take the extra weeks to get the filter experience right than ship on an earlier date with a product that disappoints the moment someone tries to do real analysis.

If you would like to be notified when we have a firmer Q1 date, reply to this post and we will add you to the direct update list. The sales team is also tracking Insights as a named priority item and can follow up individually if you would prefer a conversation to an email thread.

## What This Actually Costs

We want to end here - not with a recap, because you have read the recap above and you do not need it repeated.

What this costs is a quarter. Specifically, it costs the quarter you were counting on. If you made a commitment to your leadership or your customers based on what we told you about Insights, you now have to go explain a change you did not make. That is a real cost, and we are not going to minimize it by pivoting immediately to how excited we are about Q1.

We made you a promise. The right move when you break a promise is not to immediately make a new, shinier promise and hope the first one gets forgotten. The right move is to account for the one you broke, explain what happened, and make the next commitment in a way that gives you some reason to believe it.

What we hope this does not cost is your confidence that we will tell you the truth when things change. We cannot unsay what we said about Q3. We cannot give you the dashboard before it is ready. What we can do is be the kind of team that tells you what happened when something goes sideways, explains the tradeoff instead of hiding it, and ships the bridge instead of pretending nothing changed.

The CSV export is real and ships before the end of this quarter. The Q1 commitment is serious and carries the full weight of what we still owe you. And this post is us saying: we know what we owe you, and we intend to spend the rest of this year paying it.
