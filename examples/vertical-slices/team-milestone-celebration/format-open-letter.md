---
entry_id: open-letter
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# An Open Letter to Renata Cole, VP of Engineering

*Posted to #eng-all-hands and cross-posted to the internal engineering blog. June 30, 2026.*

Dear Renata,

On June 20 I closed the Halyard status report with a promise: a separate document would follow today, because fourteen months of parallel-track work is too long to fit into a normal retro format. This is that document. It is not the retro. The retro happens this afternoon, and it will do what retros do well - what went well, what to improve, an action list somebody will own for a quarter and then forget. I am writing to you directly, and I am putting it where the whole engineering org can read it, because I have watched good retros turn into good documents that nobody reopens.

I ran Halyard for fourteen months and signed my name to the close-out report you read last week, so I am the person best placed to tell you, specifically, who made this project succeed and what it cost them. You have the summary numbers already: two near-misses caught before launch, zero customer-visible incidents, a full cutover on June 13 that held through its first peak weekend. What the numbers do not carry is who is attached to each one. Marcus Teel found a cart-state bug in staging in February and treated it as urgent when he had every reason to file it low-severity and let it ride into production. Dani Rowe called the hold that gave Marcus the three weeks he needed, absorbed the schedule conversation that followed, and closed out the runbook handoff on schedule despite it. Jordan Osei found a payment-callback race condition in April during the final dress rehearsal and rewrote the handler instead of patching around it, on a schedule that was already behind, costing eleven more days he did not have to spend. Sam Wickfield held the regression bar on June 9, the day the pressure to ship was highest, when waving it through would have been the easier and the invisible choice. None of that is in a commit count. None of it is in a ticket velocity chart. If it is not written into this cycle's promotion and calibration packets by name, with the specific call each of them made, it will not exist anywhere the committee looks.

You backed the expensive option when the cheap one was sitting right there: patch the old checkout in place, ship faster, take the regression risk as it came. Instead you backed fourteen months of two live systems running side by side, with nothing the rest of the company could see until the very end. That was the right call, and I am not writing to relitigate it. I am writing because of how it gets remembered. If Halyard files away as "the checkout project that took a really long time," the next engineer who finds a five-year-old coupling problem in a system nobody wants to touch will read the room correctly and choose the visible fix instead of the honest one. The debt does not go away when that happens. It just waits for someone else, in five more years, to spend fourteen invisible months paying it down again.

You are one of the people in this building who can change what "reading the room correctly" means. That is why this is going to the whole org instead of your inbox. I know you have already thanked Marcus, Dani, Jordan, and Sam privately, and I know it was sincere. But a private thank-you does not survive the next headcount review, and it does not tell the next program lead, watching from outside, whether volunteering for the invisible fourteen-month project is a good bet or a quiet way to disappear from the room where credit gets handed out. Right now the whole org is watching what happens to Halyard's credit, whether they say so or not. On July 14 the old system comes down for good, and this stops being a live story with people still watching and starts being one more line in the archive.

So: two asks, and neither is technical.

Put Marcus, Dani, Jordan, and Sam's names in this cycle's promotion and calibration packets, attached to the specific calls above, not folded into "contributed to Halyard." And say publicly, this week, that the next team that proposes the expensive, invisible, fourteen-month option gets the same backing this one got, before they have to build a business case to justify asking for it. I can draft the first one myself; I already have the timeline written down. The second one has to come from you, on the record, or it is not a commitment. It is a mood.

Priya Vasquez
Program Lead, Project Halyard
Written with the Halyard team's agreement, June 30, 2026
