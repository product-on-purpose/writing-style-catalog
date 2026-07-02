---
entry_id: resume
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Priya Vasquez

priya.vasquez@example.com | (614) 555-0138 | linkedin.com/in/priyavasquez | Columbus, OH

## Experience

Program Lead, Platform Engineering | Thornbury Retail | February 2023 - Present
- Led Project Halyard, a 14-month parallel-run rebuild of the company's checkout platform (shipped as Checkout Reflow v2.0), coordinating engineering, infrastructure, and analytics through a phased cohort rollout that started at 1% of traffic and reached full cutover with no customer-facing incident.
- Held the launch when a final dress-rehearsal test surfaced a race condition between the payment-processor callback and the session store, delaying go-live eleven days rather than ship with an unresolved defect; the fix required rewriting the callback handler outright, and the issue never reached production.
- Delivered the final cutover in June 2026, moving all checkout traffic off a five-year-old system and holding through the first peak-traffic weekend with no rollback and no latency-threshold breach.
- Addressed a three-year elevated cart-abandonment trend; the migrated cohort's abandonment rate improved ahead of full cutover, confirming the rebuild's hypothesis with live production data.
- Sequenced the 31-day legacy regression freeze and archive window following cutover, setting up final decommission of the old checkout system for mid-July without disrupting the archive period.

Technical Program Manager | Ashgrove Systems | August 2016 - January 2023
- Coordinated release planning across three backend teams for a subscription commerce platform, standardizing sprint cadences and reducing cross-team dependency conflicts flagged at planning.
- Ran technical planning for two platform migrations, including a database failover redesign completed without unplanned downtime.
- Introduced a risk-register practice for cross-team initiatives, adopted by two additional program teams within a year.

## Education

B.S., Computer Science | Kestrel State University | 2016

## Skills

Program leadership: Phased migration planning, launch/no-launch risk decisions, cross-functional coordination, executive status reporting
Technical: Distributed systems fundamentals, checkout and payments domain, session-state architecture, monitoring and rollback design
Practices: Architecture decision records, regression-freeze planning, legacy decommission sequencing, incident-risk assessment
Tools: Jira, Confluence, Datadog, PagerDuty
