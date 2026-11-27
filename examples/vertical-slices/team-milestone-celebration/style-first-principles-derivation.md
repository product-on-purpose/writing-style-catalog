---
entry_id: first-principles-derivation
axis: style
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

## What Project Halyard's Close-Out Should Mark

Project Halyard shipped on June 13, 2026, and the team is about to decide how to mark it. The default is to thank everyone and move on. Before accepting the default, here is what the marking has to be, built from what we already agree on.

### Premises

Each of these is an input. Grant it or refuse it.

**P1.** The project ran fourteen months, and for the whole of that time the team ran the old checkout and the new one at the same time. (An observation from our own calendar.)

**P2.** The launch slipped twice. The February slip cost three weeks and the April slip cost eleven days. (Two measurements from our own schedule.)

**P3.** Both slips were chosen. In each case someone on the team had a cheaper option available and declined it: marking the February bug low severity, or patching around the payment callback instead of rewriting it. (An observation about what was on the table at the time.)

**P4.** Neither problem was caught by the automated test suite alone. Both were caught by an engineer reading data closely enough to notice something wrong. (An observation from the two post-mortems.)

**P5.** A mark of recognition is useful to the people receiving it only if it tells them which of their actions was seen. (A premise about recognition, and the one I expect the most pushback on.)

**P6.** The checkout held through its first peak weekend, June 13 and 14, with no rollback. (A measurement from the cutover.)

### Derivation

**Step 1, from P6.** The clean result is what everyone outside the team can see. It is also the only part of the project that leaves no trace of the work behind it, because a system that does not fail produces no event to point at.

**Step 2, from P3 and P4.** The work that produced the clean result was a run of small decisions, each made when a cheaper option existed and each made by a named person. Those decisions did not appear in any dashboard, because the test suite did not surface them and a declined shortcut leaves no record.

**Step 3, from Step 1 and Step 2.** The visible outcome therefore hides its own cause. A mark that celebrates only the outcome celebrates the one thing that cannot show who did what.

**Step 4, from P1 and P2.** The cost of those decisions was real and countable. Fourteen months of doing two jobs at once, plus three weeks and eleven days of schedule pressure, were paid by specific people. A thank-you that does not carry that cost leaves it unacknowledged.

**Step 5, from Step 3 and P5.** If a mark must tell people which of their actions was seen, and the outcome cannot show which actions mattered, then the mark has to name the actions itself.

**Step 6, from Step 5 and Step 4.** The mark has to name the decisions and say what each cost.

### Conclusion

Marking Project Halyard well means listing the two decisions the premises actually carry: the February bug filed at full severity, and the callback handler rewritten instead of patched. Each is attributed to the person who made it, with its cost beside it. A general thanks to the team does not meet that standard, because it follows from none of the steps above.

### Where this could break

The load-bearing premise is P5. If recognition works by the warmth of being thanked and not by being specifically seen, Steps 5 and 6 fall, and a general celebration would do the same job at lower cost.

P3 is the second joint to test. If either of the two decisions was in fact the only option on the table, the cost in Step 4 is overstated for that decision, and it drops off the list.

I do not know how the team would answer P5 if asked. That is worth finding out before the close-out note goes out.
