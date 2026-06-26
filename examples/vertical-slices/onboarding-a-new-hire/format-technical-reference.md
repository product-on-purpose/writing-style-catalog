---
entry_id: technical-reference
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# New-Engineer Onboarding: Two-Week Specification

The standard process for bringing a new engineer from day-one arrival to first production change within fourteen calendar days, with a defined ownership model and verifiable exit conditions at each phase.

---

## Phases

| Phase | Days | Entry Condition | Exit Condition |
|-------|------|----------------|---------------|
| Setup | 1-2 | First day of employment | All access granted; local build passes |
| Orientation | 3-5 | Setup complete | Engineer can locate any team-owned service by name |
| First Change | 6-10 | Orientation complete | PR merged to main and deployed |
| Independent Work | 11-14 | First change shipped | Second change in progress without pairing |

---

## Setup Checklist

Items that must be in place before orientation begins. The onboarding lead pre-provisions items marked `lead`; the engineer self-completes items marked `self`.

| Item | Owner | Timing | Verified When |
|------|-------|--------|--------------|
| Version control account + org membership | lead | Before day 1 | Engineer can clone any team repo |
| CI/CD pipeline access | lead | Before day 1 | Engineer can view pipeline run history |
| Ticket tracker access + assigned team board | lead | Before day 1 | Engineer can see backlog and active sprint |
| Chat tool account + team channels | lead | Before day 1 | Engineer can post to primary team channel |
| On-call rotation tool access (observer) | lead | Day 1 AM | Engineer appears in schedule as observer |
| Local dev environment build | self | Day 1 AM | See verification below |
| Dev-tier service credentials | lead | Day 1 PM | Integration test suite passes locally |
| Production read access (logs + metrics) | lead | Day 2 | Engineer can query production log stream |
| Production write access | lead | Day 8 (start of week 2) | Engineer added to deploy-authorized group |

### Setup Verification

```bash
# Run after completing local dev environment setup (Day 1 AM)
make dev-check

# Expected output:
#   [PASS] Repository: cloned and up to date
#   [PASS] Dependencies: all installed
#   [PASS] Services: api, worker, scheduler started
#   [PASS] Unit tests: all passing
#   [PASS] Integration tests: all passing against dev endpoints
```

If any check fails, the engineer stops and contacts the buddy before proceeding. The buddy owns unblocking setup failures; they do not belong to the engineer on day one.

### Constraint

Do not grant production write access before the first change is merged. Production read access is required for orientation. Write access is not required until week two and must not be granted earlier.

---

## Orientation

The orientation goal is navigational fluency. By day five, the engineer should be able to answer "where does this live and who owns it?" for any named service or component without asking.

### Service Inventory

Provide on day two, before the orientation session. One row per service the team owns or has on-call responsibility for.

| Service | Role | Repo | Primary Owner | Runbook |
|---------|------|------|--------------|---------|
| [service-name] | [one-sentence role] | [repo path] | [engineer name] | [runbook path] |

### Codebase Walkthrough Session

A 90-minute session scheduled for day two or day three. The session covers exactly these items and no others:

| Topic | Scope |
|-------|-------|
| Repository layout | Where services live; naming conventions; what does not live in version control |
| Request path (one representative service) | Entry point to data store and back; where the main logic lives |
| Deployment path | How a merge to main becomes a production change; rollback procedure |
| Alert vocabulary | The five most common page types; where to find the runbook for each |

The walkthrough does not cover history, rationale, roadmap, or architectural decisions. Those are separate conversations with separate owners.

### On-Call Observer Mode

The engineer is added to the on-call rotation as a silent observer from day two through the end of week two.

| Property | Value |
|----------|-------|
| Role | Observer only - receives all pages, no response required |
| Duration | Day 2 through end of day 14 |
| Escalation | Engineer may ask questions after any page; escalation responsibility stays with primary |
| Upgrade condition | After first change is merged; engineer moves to secondary |

---

## First Change Specification

The first change is chosen and scoped jointly by the team lead and the buddy before the engineer picks it up.

### Ticket Criteria

A valid first ticket satisfies all of the following:

| Criterion | Specification |
|-----------|--------------|
| Scope | Single service only |
| Risk tier | Low - no schema migrations, no API contract changes, no new external dependencies |
| Size | Fewer than 100 lines changed |
| Type | Bug fix, configuration change, or additive feature behind a flag |
| Testability | Existing test that can be run locally to confirm pre- and post-change behavior |
| Label | Marked `good-first-ticket` or equivalent in the tracker |

A ticket that meets four of five non-label criteria is acceptable if the buddy can close the gap in one pairing session.

### First Ticket Template

```
Title:  [verb] [what] in [service-name]

Acceptance conditions:
  - Before: [specific observable behavior]
  - After:  [specific observable behavior]

Scope constraint:
  - Touches: [service-name] only
  - Excluded: [list any related areas that are out of scope]

Labels: good-first-ticket
Size:   S (target < 1 pairing day)
Buddy:  [name]
```

### Pairing Protocol

| Stage | Who Drives | Who Navigates | Target Duration |
|-------|-----------|--------------|----------------|
| Ticket read + scope clarification | Buddy | Engineer | 15 min |
| Local reproduction or initial exploration | Engineer | Buddy | 30-60 min |
| Implementation | Engineer | Buddy | Variable |
| PR description and test plan | Engineer | Buddy | 20 min |
| Post-merge debrief | Engineer narrates what they learned | N/A | 15 min |

In the navigation role, the buddy answers questions and flags wrong turns. The buddy does not write code. If the buddy is typing implementation code, the pairing session has drifted into pair-programming-as-rescue, which delays the engineer's model-building.

### Constraint

The PR description must include a one-paragraph summary the engineer writes without help. This is not a quality bar for the prose; it is a diagnostic. An engineer who cannot summarize a 30-line change in a paragraph has not yet built the mental model the change requires. Pause, debrief, and rebuild before merging.

---

## Ownership Map

Who to contact for what during the first two weeks.

| Question Type | Contact | Not |
|--------------|---------|-----|
| "I cannot get X working locally" | Buddy | Team lead |
| "I do not know what this service does" | Service primary owner (see Service Inventory) | Buddy |
| "I am not sure this ticket is the right scope" | Team lead | Buddy |
| "I got paged and do not know what to do" | On-call primary (visible in rotation schedule) | Buddy |
| "I want to understand why we designed it this way" | ADR author (listed in `/docs/adr/`) | Team lead |
| "Something feels off about how I am settling in" | Manager | Buddy, team lead |
| "I am blocked and the buddy is unavailable" | Team lead | Wait |

### Constraint

The buddy is a technical resource, not a manager proxy. Pace, fit, and team-dynamics signals are the manager's domain. Do not route those conversations through the buddy; it puts the buddy in an ambiguous accountability position and delays the manager receiving information they need.

---

## Week-by-Week Schedule

### Week 1

| Day | AM | PM |
|-----|----|----|
| Monday | Manager 1:1 (30 min): expectations, access status, who is who | Local environment setup with buddy; complete setup checklist |
| Tuesday | Codebase walkthrough (90 min) | Service inventory review; first on-call page walkthrough with buddy |
| Wednesday | Ticket selection with team lead (30 min) | First change: ticket read + exploration with buddy |
| Thursday | First change: implementation with buddy | First change: PR draft |
| Friday | PR submitted; attend team standup or retro | Manager check-in (15 min); end-of-week debrief with buddy |

### Week 2

| Day | AM | PM |
|-----|----|----|
| Monday | Address PR review feedback | Re-submit or merge; production write access granted |
| Tuesday | Second ticket selection (engineer proposes, lead approves) | Second change: begin independently |
| Wednesday | Second change: implementation (buddy async-available) | Continue implementation |
| Thursday | Second change: PR submitted | Buddy reviews PR; minimal navigation |
| Friday | PR merged or final feedback addressed | Manager 1:1 (30 min): two-week retrospective |

---

## Outputs

At close of day 14, the following conditions must be true. The manager owns verifying this table; the buddy does not.

| Output | Verifiable State |
|--------|----------------|
| First change shipped | PR merged to main; deployed to production environment |
| Second change in progress | Ticket in active state; PR open or implementation underway without buddy pairing |
| Access complete | Production write access granted; all setup checklist items closed |
| On-call ready | Engineer listed as secondary on-call for the following rotation |
| Navigational fluency | Engineer locates any team service and its runbook without asking |

---

## Notes

- The first change takes longer than it looks. A 30-line fix on an unfamiliar codebase can be a two-day ticket until the engineer internalizes the test harness and the deploy pipeline. Pad the week-one schedule; do not compress it.

- The buddy is not a silent resource. A buddy who is reachable but never proactively checks in is not fulfilling the role. One deliberate 15-minute check-in per day (not a standup - a blocker scan) is the minimum contact pattern.

- The Friday check-ins with the manager in week one and week two are not optional. These are the only scheduled moments for the manager to surface "something feels off" signals before they compound. Do not reschedule them.

- Belonging is not a week-two deliverable; it is a week-two setup condition. The signal that an engineer belongs is that they disagree with something in a public channel and the team engages without defensiveness. That signal typically appears in week three or four, and it requires two weeks of psychological safety investment before it can appear. The "feels she belongs" goal at the end of week two means she has enough context and enough safety to voice a disagreement - not that she has already done so.

---

## See Also

- Service inventory - `/docs/services/inventory.md`
- On-call rotation schedule - `/ops/oncall/schedule.md`
- Architecture decision records - `/docs/adr/`
- Buddy program - `/docs/team/buddy-program.md`
- Access provisioning runbook - `/ops/access/new-hire.md`
- Deploy pipeline reference - `/docs/deploy/pipeline.md`
