---
diff_pair_id: style-procedural-vs-diataxis-explanation-onboarding-a-new-hire
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
axis_varied: style
entry_a: procedural
entry_b: diataxis-explanation
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `procedural` vs `diataxis-explanation`

**Topic:** Getting a new engineer productive in their first two weeks
**Axis varied:** style
**A:** `procedural` - Task-first writing that takes a reader from "I don't know how" to "I did it" by organizing every decision around user goals, not system features.
**B:** `diataxis-explanation` - The Diataxis "Explanation" mode - oriented toward understanding rather than action, building a conceptual model for the reader.

## What to notice

The same fortnight, once as something to execute and once as something to understand.

**A is executable and states its prerequisites.** It opens on the outcome, "Get Priya from day
one to shipping her first real change by the end of week two", then a `Before you begin` block
listing the conditions: a confirmed start date, permissions in hand. Prerequisites are a move
only a procedure makes, because only a procedure can fail for want of them.

**B refuses the schedule framing entirely.** "The two-week onboarding structure is not a
schedule; it is a theory of belonging. New engineers rarely struggle because they lack access to
the repository." That sentence is doing the explanation's whole job: replacing the reader's
model before offering anything built on it.

**The sharpest single tell.** A has prerequisites; B has a thesis. Hand A to someone on Sunday
night and they can run it. Hand B to the same person and they will design a better version of A
than the one you would have written for them.

---

## A: `procedural`

Get Priya from day one to shipping her first real change by the end of week two.

**Before you begin**

- Priya's start date is confirmed as the coming Monday.
- You have permissions to request accounts on her behalf in the version control system, the ticket tracker, the deployment pipeline, and the monitoring dashboard.
- A small, scoped ticket sits unassigned in the backlog - one that touches a real code path but where a mistake reverts cleanly.
- One team member besides yourself is available to pair with Priya during week two.

**Week one: access, tooling, and orientation**

1. Submit account access requests for Priya in the version control system, the ticket tracker, the deployment pipeline, and the monitoring dashboard. Do this on Friday before her start date.

   Expected outcome: All four accounts are active by Monday morning, or by Tuesday at the latest.

2. Send Priya a welcome message in the chat tool before she logs in on Monday. Include the internal wiki URL, the onboarding checklist, and a link to your calendar so she can book time with you.

3. Walk through the team's local development setup guide with Priya on Monday morning. Sit with her rather than handing off the document.

   Expected outcome: Her local environment runs the service and she can reach a development endpoint.

4. Trace the path of one recent pull request with Priya, from the entry point to the response. Skip the full directory tour.

   Expected outcome: She can describe what the service does and where the code for one flow lives.

5. Walk Priya through the on-call runbook: who owns each service, how alerts route, and who to call if she is ever paged before she feels ready.

   Expected outcome: She understands the rotation schedule and knows she is not exposed alone.

6. Have Priya submit a pull request that adds her name to the team roster file - she types the commit message, creates the PR, and merges it.

   Expected outcome: She has walked the full deployment path before she owns a real change.

**Week two: first real change**

The pairing partner's role is to answer questions, not to type the solution. Agree on this with the partner before the session begins.

7. Assign Priya the pre-selected ticket and introduce her to her pairing partner.

8. Have Priya manage her own pull request - she writes the description, assigns reviewers, and responds to comments herself.

9. When the change ships, post an acknowledgment in the team chat that names the ticket and names Priya.

   Expected outcome: The team sees her as a contributor, not an observer.

Priya has shipped a real change to production and the team has recognized it; the two-week onboarding is complete.

---

## B: `diataxis-explanation`

The two-week onboarding structure is not a schedule; it is a theory of belonging.

New engineers rarely struggle because they lack access to the repository or have not been shown the deployment pipeline. They struggle to thrive because no one explained why the team works the way it does, which means they must infer every decision from its visible artifacts alone. A codebase without context is archaeology, and archaeology is exhausting.

The first priority is removing friction rather than transmitting knowledge, because a new engineer who cannot get her environment running cannot learn anything else. Access and tooling come first not because they are the most important things, but because they are prerequisites for everything else. Without them, even the best orientation collapses into theory with nowhere to land.

Orientation - the reading, the walkthroughs, the architecture conversations - matters because it gives Priya a map she can refer back to. But a map is not the territory. She will not know which parts of the codebase are stable and which are contested, which decisions are settled and which are perpetually argued, until she has moved through the territory herself. This is why pairing on a real change belongs in the middle of the two weeks rather than at the end: it converts the map from abstract to navigable.

The choice of first change matters for reasons that are not purely technical. A change that is too small signals that the team does not trust Priya with anything real. A change that is too large risks a blocked first week, which generates anxiety rather than momentum. The right first change is one where the scope is bounded but the consequence is genuine, because genuine consequence is what makes the work feel like membership rather than a test.

Belonging and function are related, but they are not the same thing. A new engineer can be fully functional - able to access systems, understand the codebase, respond to incidents - and still feel like a visitor. Belonging emerges from a different source: being trusted with something real, being included in a decision, having someone explain the unwritten reason behind a written rule. This is why the human side of the two weeks is not a supplement to the plan but a dimension of it. The plan fails if Priya ships a change and still feels like a guest.

The on-call rotation sits at the intersection of function and belonging because of what it signals about trust. Being added to the rotation before Priya is ready is overwhelming; being excluded indefinitely is isolating. The right answer is not a date but a conversation - one where she and the team agree on what readiness actually means, which is itself an act of inclusion.
