---
entry_id: user-manual
axis: format
topic_slug: retirement-send-off
topic_label: Marking a long-serving colleague's departure
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Operations Coordinator Role: User Manual

*Crestfield Group - Internal - Version 1.0 - Maintained by Dana Reyes and Marcus Okonkwo - Last reviewed with Howard Thayer: June 24, 2026*

## Table of Contents

- Getting Started
- Vendor and Contract History
  - Locating contract history for a vendor dispute
- Incident Response Coordination
  - Reconstructing system state when the documented runbook is out of date
  - Escalating when automated alerts do not tell the full story
- Utility and Facilities Escalation
  - Reaching a utility contact outside the standard queue
- Informal Mentoring and New-Hire Support
  - Getting a second read on a decision before it goes out
- Troubleshooting
- Reference

## Getting Started

This manual documents the Operations Coordinator role at Crestfield Group as it stands after June 27, 2026, Howard Thayer's last day following twenty-six years in the role. It replaces the channel most of this knowledge used to travel through, which was asking Howard directly.

Before your first shift covering this role:

- Request access to the shared operations drive (`/ops/`), including the vendor contract archive and the knowledge-transfer folder, if you do not already have it.
- Read the mentee notes archived at `/ops/knowledge-transfer/mentee-notes/` once, in full, before you need any single entry in it.
- Introduce yourself to the four utility and facilities contacts listed under Reference. Do this before an outage, not during one.
- Know that Dana Reyes and Marcus Okonkwo co-maintain this manual. If a task is not covered here, ask one of them before improvising.

This manual does not cover judgment calls made under genuine ambiguity with no precedent. Nothing does. See Troubleshooting for what to do when you hit one anyway.

## Vendor and Contract History

### Locating contract history for a vendor dispute

Use this when a vendor dispute or billing disagreement requires the original agreement terms and nobody currently on the vendor's side remembers the history either.

Steps:
1. Check `/ops/vendor-archive/[vendor-name]/` for the original scope-of-work and any signed amendments. Files are named by year.
2. If the folder is empty or incomplete, check the conversion log at `/ops/vendor-archive/_conversion-log.md`. Not everything Howard held on paper had been digitized as of his last day.
3. If the record still is not there, contact the vendor's account representative directly and ask for their copy of the signed agreement. Do not assume Crestfield's copy is the only surviving one.
4. Log whatever you find back into the archive folder so the next lookup does not repeat this path.

Options / Parameters:
- Archive scope: contracts opened in 2015 or later are archived in full. Contracts before 2015 are partial, pending the digitization backlog.
- Escalation contact: for a vendor with no responsive account representative, escalate to Carolyn Marsh (cmarsh@crestfieldgroup.internal).

Notes:
- A contract dispute in 2019 was resolved this way when the archive existed only in Howard's memory. The path above is the same path, now written down.
- Some amendments from before 2018 exist only as scanned images without text recognition. Search by filename and date, not by text search, for anything that old.

## Incident Response Coordination

### Reconstructing system state when the documented runbook is out of date

Use this when responding to an incident requires the actual current configuration of a system, and the written runbook no longer matches it, typically after an undocumented migration.

Steps:
1. Pull the current system-state diagram from `/ops/knowledge-transfer/system-diagrams/`. Diagrams are dated and versioned as of each quarterly knowledge-capture session.
2. Compare the diagram against the monitoring dashboard. Flag any discrepancy in the incident log rather than resolving it silently.
3. If the diagram does not resolve the discrepancy, page Dana Reyes or Marcus Okonkwo. Both worked the 2026 knowledge-transfer sessions and can reconstruct undocumented history faster than starting from the ticket tracker.
4. After the incident closes, update the system-state diagram with what you learned. This step is not optional. It is the reason the quarterly capture practice exists.

Options / Parameters:
- Diagram refresh cadence: quarterly. If an incident revealed drift, file an out-of-cycle update rather than waiting for the next quarter.

Notes:
- Before 2026, this step depended on one person's memory of a platform migration nobody had fully recorded. It is written down now. Treat a gap you find in this diagram as a gap that already existed, not a new failure.

### Escalating when automated alerts do not tell the full story

Use this when an alert is technically accurate but does not point you to the actual cause, which is a known gap in current alerting coverage rather than a one-off.

Steps:
1. Check `/ops/knowledge-transfer/alert-gaps.md` for a matching alert type. This log lists alerts known to be incomplete and what to check instead.
2. If the alert type is not listed, treat it as a new gap: resolve the incident first, then add an entry to the log afterward.
3. Contact the vendor or utility contact named for that system under Reference rather than waiting for the alert to update.

Notes:
- This was Howard's most-used pattern and the hardest to write down, because he was not consciously following steps. He was recognizing situations. What is written here is a reconstruction, not the original.

## Utility and Facilities Escalation

### Reaching a utility contact outside the standard queue

Use this when the standard facilities ticket queue is too slow for an active issue with power, HVAC, water, or building access, and you need a direct line.

Steps:
1. Check the table under Reference for the four direct contacts. These existed only in Howard's personal phone before this manual; they are logged here with his agreement, recorded before his last day.
2. Call rather than email for anything time-sensitive. Each contact responds faster to a call than to a ticket.
3. Identify yourself as calling on behalf of Crestfield Group Operations and reference the standing account if asked.
4. Log the call and its outcome in the facilities ticket regardless of which channel you used, so the record stays complete.

Notes:
- These four relationships were personal to Howard before this manual existed. They may not respond with the same speed to a new caller. Expect a slower response for the first few months. That is not the contact being unreliable.

## Informal Mentoring and New-Hire Support

### Getting a second read on a decision before it goes out

Use this when you are new to the role, or new to Crestfield Operations generally, and want a second opinion before a decision or communication goes out. This is the function Howard performed informally, across twenty-six years, without a title for it.

Steps:
1. Bring the specific decision or draft to Dana Reyes or Priya Sandhu. Both were designated as points of contact for this in June 2026.
2. State the decision and your reasoning in two or three sentences before asking your question. This is a request for a second read, not a request for someone else to decide for you.
3. Expect a question back, not a verdict. That is the format this takes here. It is not a rubber stamp and not a formal review gate.

Notes:
- This is not a required step in any process document and does not appear as a gate. It is offered, not mandated. See ADR-0047 (backfill and knowledge-capture decision made after Howard's departure was announced) for why it was kept informal rather than turned into a title.

## Troubleshooting

- **A vendor contact does not recognize your name or respond with the urgency Howard used to get:** personal relationships do not transfer with a role. Reference the standing account number and the specific contract or ticket, and escalate through Carolyn Marsh if urgency is required rather than waiting for rapport to build.
- **The system-state diagram does not match what you are seeing in production:** the diagram is only as current as the last quarterly capture session, and drift between sessions is expected rather than a sign the diagram is wrong. File an out-of-cycle update per Incident Response Coordination, and treat the live system as the source of truth in the meantime.
- **A task you need is not documented anywhere in this manual:** this manual reflects what was captured in the May and June 2026 knowledge-transfer sessions and is not exhaustive. Ask Dana Reyes or Marcus Okonkwo first. If neither knows, log the gap in `/ops/knowledge-transfer/gaps.md` so it does not stay undocumented twice.
- **Two long-tenured colleagues describe the same informal process differently:** several of Howard's practices were personal habits that different people partially absorbed. There is no single correct version for a practice that was never formalized. Use the version that fits your situation and document your own version afterward.

## Reference

### Manual contacts

| Name | Role | Contact for |
|---|---|---|
| Dana Reyes | Operations Coordinator | Incident reconstruction, system-state diagrams, second reads on decisions |
| Marcus Okonkwo | Operations Coordinator | Incident reconstruction, alert-gap questions |
| Priya Sandhu | Operations Analyst | Second reads on decisions |
| Carolyn Marsh | Operations Lead | Escalation when the above are unavailable, vendor relationship handoffs |

### Utility and facilities contacts

| System | Contact | Notes |
|---|---|---|
| Electrical / power | Bracken County Power, Commercial Accounts Desk | Call rather than email for same-day issues |
| HVAC | Northline Mechanical Services | Separate after-hours line; see `/ops/knowledge-transfer/facilities-contacts.md` |
| Water / plumbing | Vantage Utilities | Shares combined-outage reporting with the electrical desk |
| Building access / badges | SecureAccess Building Systems | Only 24-hour live line of the four |

### Related documents

- ADR-0047 (backfill and knowledge-capture decision) - the decision record behind this manual's existence
- System-state diagrams - `/ops/knowledge-transfer/system-diagrams/`
- Alert-gap log - `/ops/knowledge-transfer/alert-gaps.md`
- Mentee notes archive - `/ops/knowledge-transfer/mentee-notes/`
- Vendor contract archive - `/ops/vendor-archive/`

### Glossary

- **Knowledge-transfer sessions** - the two working sessions Dana Reyes and Marcus Okonkwo held with Howard Thayer in May and June 2026 to document decision paths that previously existed only informally.
- **Quarterly knowledge-capture practice** - the standing practice established by ADR-0047, under which team leads record the decisions and constraints shaping their area of operations every quarter, independent of any single person's departure.
- **Second read** - the informal practice of bringing a decision to a designated senior contact before it goes out. See Informal Mentoring and New-Hire Support.
