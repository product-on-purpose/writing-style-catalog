---
entry_id: memo
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

TO: Sales, Customer Success, Engineering, and Product
FROM: Priya Nambiar, VP Product, Meridian Labs
DATE: September 14, 2026
RE: Insights Dashboard Deferred to Q1 2027 - CSV Export Confirmed for September 26

This memo confirms the final decision on the Insights analytics dashboard: the Q3 2026 commitment is deferred to Q1 2027, with a target release of March 13, 2027. A CSV export of the underlying data ships September 26, 2026, as the interim deliverable for the four enterprise accounts affected by the change.

The Q3 commitment was made to close several in-flight sales deals and to key customers who requested the dashboard directly. In early Q3, the mandatory billing-system migration - a compliance requirement tied to a vendor contract change - overran its projected timeline and consumed the engineering capacity allocated to Insights. The current build is missing saved-view persistence and scheduled-report delivery, the two capabilities the affected accounts specifically asked for. Shipping against the original date would have delivered a product that fails at the use cases it was sold on. That option was reviewed and rejected.

The billing migration reaches production the week of September 19. The CSV export is scoped as a two-week build: backend endpoint complete by September 19, frontend integration and QA closed by September 24, export delivered to affected accounts on September 26. Dario Reyes owns the export build. Design work on the Q1 Insights release begins October 6, once the billing release has stabilized, with the full six-view dashboard, saved views, and scheduled reports targeted for March 13, 2027.

Customer-facing outreach is authorized to proceed on this basis, and the March 13, 2027 target is cleared for use in that outreach. Jordan Park leads notice to the four affected accounts this week, with individual calls offered to any account that has flagged a strong dependency on the original Q3 date.

This memo establishes September 26, 2026 as the confirmed CSV export date and March 13, 2027 as the confirmed Insights release target. The Q3 commitment to the four affected accounts is not being met as originally scoped; the record above reflects the revised commitment and the reasoning behind it. Any further change to either date will be documented in a follow-up memo.
