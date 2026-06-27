---
entry_id: design-doc
axis: format
topic_slug: retirement-send-off
topic_label: Marking a long-serving colleague's departure
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Knowledge Continuity System Design - Howard Thayer Departure

## Status

Accepted

## Problem

Howard Thayer is retiring from Crestfield Group on June 27, 2026, after twenty-six years as Operations Coordinator. The knowledge transfer problem this creates is not routine. Howard did not accumulate scope or headcount over his tenure; he accumulated context. The gap is structural, not positional.

The constraints shaping the solution space:

**Time bound:** Structured sessions with Howard were limited to May and June 2026. Two sessions are complete. His last day is June 27. No extension is possible.

**Knowledge type:** The majority of Howard's value was procedural and relational - how to navigate a vendor dispute, which contacts respond to which communication style, how to read an ambiguous alert correctly. These do not extract cleanly into reference documentation.

**Capacity:** The team cannot assign a full-time documentation effort. Dana Reyes and Marcus Okonkwo have operational workloads that preclude more than one weekly session each.

**Freshness risk:** Documentation created under time pressure tends to go stale quickly if not embedded into active operational workflows. A one-time knowledge dump is likely to be correct at creation and wrong by Q4 2026.

**Coverage asymmetry:** What Howard knows he knows is documentable. What he knows without knowing he knows it is not. The second category may be larger than the first.

## Proposed Design

The system has four components. Each targets a distinct knowledge type and has a defined owner, delivery format, and location.

### Component 1 - Incident-Response Runbook

**Owner:** Dana Reyes
**Delivery:** `docs/ops/incident-response.md`
**Coverage:** Vendor escalation paths, four utility contacts not present in any official directory, automated alert interpretation heuristics, sequence-of-events decision tree for ambiguous incidents

**Structure:**
```
docs/ops/incident-response/
  vendor-escalation/
    tier-1-contacts.md         # Howard's four utility contacts, with per-contact notes
    escalation-thresholds.md   # When to escalate vs. resolve internally
  alert-interpretation/
    ambiguous-alerts.md        # Patterns Howard recognized that monitoring does not surface
  incident-sequence/
    initial-assessment.md      # First 15 minutes
    cross-team-coordination.md
```

The runbook captures process, not judgment. The judgment gap is acknowledged in Risks below.

### Component 2 - Mentee Practice Archive

**Owner:** Carolyn Marsh
**Delivery:** `team/former-mentees.md`
**Coverage:** Howard's observable coaching behaviors - how he framed problems for people who were panicking, the question sequences he used to surface problems without stating them directly, his practice of absorbing a situation before speaking

**Structure:**
```
team/mentee-archive/
  practices/
    problem-framing.md         # Sourced from: Priya Sandhu, Ben Holter
    question-sequencing.md     # Sourced from: Marcus Okonkwo
    pre-response-pause.md      # Named and described by four contributors
  critical-incidents/
    [year-event-slug].md       # One file per incident recalled in contributor notes
```

Contributors: Priya Sandhu, Ben Holter, Marcus Okonkwo, and four additional colleagues. Contribution method: written notes submitted by June 24. Editorial pass by Carolyn Marsh to remove eulogy framing and retain practice-level specificity.

### Component 3 - Vendor and Contact Transfer

**Owner:** Three named successors (listed in `team/contact-owners.md`)
**Delivery:** Contact records updated in the internal CRM by June 20
**Coverage:** All contacts Howard maintained personally, with ownership explicitly reassigned

Transfer is complete. No contacts in the CRM list Howard as sole owner. Relationship quality is not transferable; the contacts exist and will be owned by named humans. That is the best achievable state.

### Component 4 - Send-Off Event

**Owner:** Carolyn Marsh
**Date:** June 25, 2026
**Format:** In-person and remote hybrid; recorded for regional sites that could not send a representative
**Duration:** 90 minutes allocated. Howard spoke for four minutes.

The send-off serves two functions the other components cannot: it creates a shared organizational timestamp for the departure, and it allows Howard to speak in his own voice. Both matter. Neither is documentable in retrospect.

## Alternatives Considered

**Documentation sprint (rejected):** A concentrated 40-hour extraction effort in May 2026, with Howard in the room full-time. Rejected for three reasons: the output would be dense and hard to maintain; Howard's knowledge is not structured as documentation - forcing it into that form produces a document nobody reads; 40 hours of his time in his final weeks is not the right use of that time.

**Formal mentoring assignment (rejected):** Assigning Howard a "Mentor" title for his final six months and creating a structured program. Rejected because this title has historically read as sidelining at Crestfield rather than recognition, and because formalizing his mentoring function would have changed its nature. Howard mentored by working alongside people, not above them. Formalization would have ended that.

**Recording all sessions (rejected):** Video or audio recording the knowledge sessions with Dana Reyes and Marcus Okonkwo. Rejected because recordings are not searchable and are typically not watched under pressure. The marginal value over structured written notes was assessed as low. The interpersonal cost of being recorded was assessed as non-trivial for sessions requiring candor.

**Delay retirement date (not pursued):** Not considered a real option. Howard had set his date. The system was designed to the constraint, not to override it.

## Risks and Open Questions

**Tacit knowledge gap (accepted risk):** The runbook captures Howard's documented decision sequences, not his judgment under genuine ambiguity. The team will not know the full shape of this gap until the first novel incident he is not available for. No mitigation exists beyond naming it. The risk is real and will surface on its own schedule.

**Runbook staleness:** The runbook is accurate as of June 2026. Operational context changes. Target: quarterly review against actual incident patterns. Owner: Dana Reyes. First review: September 30, 2026. There is no enforcement mechanism beyond the calendar item; this is a known gap in the design.

**Morale lag:** Howard's absence will become concrete six to eight weeks after his last day, when the reflex to call him is still present but he is not. No structural mitigation is planned. Open question: should there be? Managers with Howard's former mentees should check in during July and August. Whether that constitutes sufficient coverage is unknown until tested.

**Archive discoverability:** The mentee archive is only as useful as its findability under pressure. If no one searches it during an incident, it provides no value at the moment it is most needed. Open question resolved as of June 27: add cross-reference links from the incident-response runbook to the mentee archive before July 15. Owner: Carolyn Marsh.

**Contribution completeness:** Howard contributed through knowledge he held without knowing he held it. By definition, the capture is incomplete. The runbook and archive represent what was recoverable in the available time. This is a known residual, not a failure of the process. It should be named as such in the runbook's own header.
