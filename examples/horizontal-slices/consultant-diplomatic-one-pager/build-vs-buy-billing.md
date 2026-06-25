---
entry_id: senior-consultant
axis: voice
topic_slug: build-vs-buy-billing
topic_label: Whether to build or buy a billing system
voice_id: senior-consultant
tone_id: diplomatic
style_id: executive-summary
format_id: one-pager
author_type: llm
llm_model: claude-sonnet-4-6
review_status: draft
---

# Billing Infrastructure: Buy Now, Build Later If Needed

**Recommendation:** License a purpose-built billing platform within the next quarter. Do not build in-house.

The decision maps cleanly to a build-vs-buy framework. The relevant axis is not cost - it is where differentiation lives. Billing is not a domain where your product competes; it is infrastructure that enables the domain where you do compete. The case for building rests on the assumption that your billing requirements are unusual enough to justify the ongoing cost of ownership. That assumption does not hold at your current scale and product surface.

**What the analysis found.** The three most commonly cited reasons for building billing in-house - pricing flexibility, revenue recognition control, and avoiding vendor lock-in - are each addressable through the leading managed billing vendors. Mature billing platforms routinely support tiered, usage-based, and hybrid pricing models. Revenue recognition aligned to ASC 606 is a standard capability in this market, not a premium add-on. Migration paths between vendors exist and have been tested at companies of comparable size. The lock-in concern, while worth monitoring, does not justify the 12 to 18 months of engineering time a build would consume.

**The cost the organization may be underweighting.** Building billing in-house means owning dunning logic, proration edge cases, tax jurisdiction handling across your active markets, and PCI compliance surface - permanently. These are not one-time engineering costs; they are an operational tax on every future sprint that touches payments. The team has excellent engineers, and that is precisely the argument against putting them here.

**There are factors worth weighing.** If pricing model complexity is expected to grow significantly - for example, into marketplace splits or multi-party revenue flows - the case for a more purpose-built or hybrid approach strengthens over time. The current recommendation is calibrated to the next 18 months of roadmap, not to a hypothetical future state. A revisit point in 18 months is reasonable.

**The ask.** Approve a structured evaluation of three leading billing platforms with a decision by end of quarter. Engineering time saved returns to the product surfaces where you have a genuine competitive advantage.
