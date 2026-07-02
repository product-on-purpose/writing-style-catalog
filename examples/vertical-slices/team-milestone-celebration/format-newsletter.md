---
entry_id: newsletter
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Ship Log

Subject: Ship Log #47 - Fourteen months of running two checkouts so you'd never notice either one

*July 3, 2026*

Hi all,

Most issues of this newsletter are a grab bag: three or four things happening around engineering, a couple of links worth ten minutes of your week, a short note from me. Not this one. This issue is a single story, because it's finally a story we're sure enough of to tell: the checkout rebuild shipped, held through its first full weekend of real traffic, and the old system is now counting down to retirement. We don't like writing about infrastructure work before we know it held, which is why you're only hearing about fourteen months of effort now that it's over.

---

For three years, cart abandonment had been stuck high, and the data kept pointing at the same place: the payment step. The checkout underneath it had absorbed five years of patches from whoever was on call when something broke. It had no meaningful test coverage and was wired into the session layer in ways the team didn't fully understand. Two earlier attempts to fix it in place had already died quietly. In April of last year, the team made the more expensive choice on purpose: build the replacement as a separate system, run it next to the old one, and move real traffic over cohort by cohort instead of flipping a switch all at once. That decision is the reason this is a newsletter issue and not an incident report.

It cost fourteen months of running two checkouts at the same time: two on-call rotations, two sets of dashboards, and a program that needed someone to keep believing in it while it produced nothing visible for over a year. Priya Vasquez ran that program end to end, cohort by cohort, for the full fourteen months. Ket Osei owned the infrastructure for the entire stretch, including the final cutover under peak load, and kept the old flow warm and ready right up until it was safe to let it go. I spent most of that year translating "we ship when it's ready" into something stakeholders could actually hold onto through two slipped launch dates, which is its own unglamorous kind of work.

Both slips were earned. In February, Marcus Teel found a silent cart-state mismatch in staging that would have corrupted multi-item orders under split payment - the kind of bug that doesn't throw an error, it just quietly produces the wrong answer. He could have marked it low-severity and moved on. He didn't, and the fix cost three more weeks. In April, during the final dress rehearsal, Jordan Osei caught a race condition between the payment processor callback and the session store. A smaller patch was available and tempting; he rewrote the handler instead, which cost eleven more days. The release notes will tell you what those two bugs were and that they're fixed. They won't tell you what it cost the two people who found them to fix it right instead of fast.

The new system shipped on June 13, ran clean through its first full weekend of peak traffic, and the milestone closure was recorded on June 25. The old checkout is scheduled to go dark on July 14. For fourteen months this was the biggest thing on the roadmap and also the thing with the least to show for it in any given week. That's what this issue is for.

---

**A few things worth your time, all from this project:**

- [Architecture overview](docs/architecture.md) - the event-driven design under the new pipeline, written for anyone who wants to understand why running two systems at once was survivable instead of reckless.
- [Near-miss post-mortems](docs/post-mortems/) - the full writeups behind the two bugs mentioned above, in more detail than a newsletter has room for. Worth it if you want to see what "caught in time" actually looks like from the inside.
- [Rollout playbook](docs/rollout-playbook.md) - the phase-by-phase cohort approach, documented well enough that the next team running a risky migration doesn't have to reinvent it.
- [Monitoring runbook](docs/monitoring.md) - what we actually watched, and what would have told us to stop. Most of it never fired. That was the point.

---

Priya's close-out report ended with an ask: if you manage any of the people named above, that's worth knowing, because none of it shows up in a commit count. So: Ket, Marcus, Jordan, and everyone whose name isn't in this email but is in [CONTRIBUTORS.md](CONTRIBUTORS.md), thank you for fourteen months of work that was only ever going to be visible if it went wrong. It didn't.

See you next week.

Yuki

---

*You're getting Ship Log because you subscribed to it. Manage your preferences or unsubscribe any time from the link in your inbox footer.*
