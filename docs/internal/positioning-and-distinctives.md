---
title: Positioning and Distinctives
date: 2026-06-09
status: living
type: positioning
related:
  - docs/internal/scaling-the-library-100x.md
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md
  - docs/internal/release-plans/plan_v0.3.0/decisions.md
  - docs/internal/adr/0010-domain-and-family-organization.md
---

# Positioning and Distinctives

A short, living statement of what the writing-style-catalog is, what genuinely makes it
different, and how it sits among its sibling repos. Written to keep the story honest as the
catalog scales agentically.

## What it is

A composable catalog of writing instructions for LLMs, decomposed into four orthogonal axes
(Voice, Tone, Style, Format). A user selects named building blocks and the composer
assembles a reusable instruction prefix. Today: 60 reviewed baseline entries plus worked
examples. Goal: roughly 600 best-in-class entries carrying tens of thousands of worked
samples.

## The core distinctive: provable distinguishability, not authorship or count

The catalog's value does not come from the entries being expert-hand-written (they are
LLM-generated and maintainer-curated), nor from the entry count. It comes from one
falsifiable property: the named distinctions actually steer a model's output in perceptible,
attributable ways. The evidence is the blind 8-of-8 attribution result against a chance
baseline near 0.4 percent.

What a competitor offers is a description of a style. What this catalog offers, uniquely, is
the measured difference plus the demonstration: a distinguishability score (the quantitative
claim) and a diff-pair (the qualitative evidence a human can read), generated from the same
gate run. "We can prove these are different, and show you the difference" is the moat.

This is why the honest positioning is provability, not craftsmanship. Correcting the earlier
"human-authored" framing (see `decisions.md`, C3 - held-out reference set) is part of
keeping that story straight: the entries are not artisanal, they are gate-proven.

## The operating model: agentic-first

The expansion is run by agentic processes, not a funded review team (decision F3 - resourcing
posture). Automated generation plus the adherence gate carry the quality load; the maintainer
provides a capacity-bounded spot-audit. This makes the gate the load-bearing mechanism and
the single most important thing to build well.

## How it relates to the fleet, and what is genuinely unique

writing-style-catalog is one of four plugin repos in the Product on Purpose family, alongside
the neutral `agent-plugins` hub. It consumes two kinds of shared infrastructure rather than
reinventing them:

- **Fleet orchestration** (owned by `agent-plugins/docs/internal/orchestration/`): how
  consistent changes roll across the four repos. WSC conforms to the consistency specs (CI
  shape, folder structure, page formatting, processes).
- **The Bronze/Silver/Gold Standard** (owned by `agent-skills-toolkit`): the
  plugin-engineering quality bar. WSC is graded by, and consumes, that grader.

What is genuinely WSC-only, and must not be confused with the above, is the **content
adherence gate.** The Standard grades plugin *engineering* quality (does the plugin have the
right files, CI, manifests). The adherence gate grades *content* quality (are the writing
entries provably distinguishable). No sibling repo has the latter, and there is nothing in
the family to reconcile it against. The gate is WSC's distinctive contribution.
