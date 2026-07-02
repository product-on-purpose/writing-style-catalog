---
entry_id: newsletter
axis: format
topic_slug: retirement-send-off
topic_label: Marking a long-serving colleague's departure
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Subject: The Handoff - July 2026: What Howard Left Written Down (and What Didn't Make It)

Hi, it's Carolyn. Most issues of this newsletter are me flagging a runbook gap or nudging a team about on-call coverage, and I promise we'll get back to our regularly scheduled complaining next month. This one is about a single person. If you've ever wondered where this newsletter got its name, he's most of the answer.

---

Howard Thayer's last day at Crestfield was Saturday, June 27, 2026 - twenty-six years after he joined as an Operations Coordinator in June 2000, a role he never left. If you've been here less than five years, that probably sounds like a career that stalled. It wasn't. Howard decided early that being the person who actually understood what was going on mattered more than the next title, and twenty-six years of us calling him at odd hours proved him right more times than any of us can count.

We gave him an all-hands on June 25: forty people in the room, eighteen more on the call from the regional sites. He talked for about four minutes. Mostly he said he was proud of the team, and that he didn't want to be the reason anyone felt stuck. That was Howard's whole style compressed into one sentence - even his goodbye was about making sure the rest of us were fine.

If you've read this newsletter for more than a few issues, you've seen me bring up our documentation debt more times than either of us would like. Usually I'm asking a team to write something down before the one person who understands it moves on. This time the something was Howard, and we did not have the luxury of pretending we had years to get to it. What we managed to get written down, we got written down. What we didn't - the pattern recognition, the read on a room, the twenty years of context behind a decision that looked simple from the outside - was never going to fit in a document, and pretending otherwise would have been its own kind of failure. ADR-0047 exists because we are done being surprised by that.

---

- **[Incident-response runbook](docs/ops/incident-response-runbook.md)** - Dana Reyes and Marcus Okonkwo spent May and June turning two decades of Howard's judgment calls into an actual document: vendor escalation paths, the four utility contacts that used to live only in his phone, and what to do when the alerts are technically firing but not telling the real story. Credentials and system access moved to three named successors by June 20.
- **[ADR-0047](docs/decisions/ADR-0047.md): why quarterly, and why now** - the short version is that we confirmed a single point of memory had been sitting in one person for two decades, and decided not to let that happen again by accident. Team leads, your first entry lands sooner than you think.
- **The mentee archive** - Priya Sandhu, Ben Holter, and four other colleagues Howard mentored put together notes on what he actually did in the room when someone was panicking. Worth five minutes even if you never worked with him directly.
- **Tell me what Howard taught you** - if he handed you a vendor contact, a workaround, or a piece of advice that never made it into the runbook, send it to me (cmarsh@crestfieldgroup.internal) by July 11. The runbook is a draft, not a monument.
- **Q3's real test: on-call without Howard on speed dial** - rotation runs through September 30, and Marcus is running a gap analysis against our six most common incident types ahead of an August 15 review. If something breaks in a way the runbook doesn't cover, that's information, not a failure.

---

That's the issue. Back to the usual ops griping next month - though if you have a Howard story that didn't make the cut here, send it my way and I'll probably run a few more in August.

Carolyn

---

You're getting this because you're subscribed to The Handoff, Crestfield Operations' internal monthly newsletter. Manage your subscription or unsubscribe via the internal comms portal.
