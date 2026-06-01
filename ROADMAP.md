# Roadmap

The Writing Style Library is a composable catalog of writing instructions on four orthogonal axes: Voice, Tone, Style, and Format. As of v0.1.0 the catalog is public, the documentation site is live, and the core mechanism is proven. A blind adherence test attributed 8 of 8 confusable composition pairs correctly (chance is roughly 0.4 percent), which means the per-entry instruction phrasings genuinely steer model output.

That result sets the direction. The catalog works, so the roadmap is about making it sharper and easier to find: depth and instructional leverage over raw breadth. We are deliberately not building a multi-surface product (SDKs, a composer app) that a catalog of this size does not need and a small team cannot maintain well.

## Now - surface and sharpen

- **Sharpen the two "subtle" confusable pairs.** The adherence test rated two pairs only "subtle": `pragmatic-architect` vs `senior-consultant`, and `narrative-case-study` vs `chronological-narrative`. These are the weakest seams in the one result the whole library rests on, so tightening their `confusable_with` distinctions from both sides is worth more than ten new entries.
- **Add diff-pairs to the `service-database-choice` anchor topic.** It currently has none, despite being the best-isolated topic. Diff-pairs are the catalog's sharpest teaching tool.
- **Deepen existing entries toward the pedagogical bar.** Add tells, anti-patterns, failure modes, and before/after micro-examples to the entries that carry the most weight, rather than adding new entries to chase coverage.

## Next - make composition real

- **Make composition conflict-aware.** Read each entry's `pairs_well_with` and `avoid_with` relationships, flag incompatible selections, and apply a clear precedence order (voice, then tone, then style, then format), instead of concatenating strings. The relationship data already lives in the catalog; this turns "composable" from a claim into a guarantee.
- **Repository legibility.** A generated repository map, per-folder READMEs on the source directories, and a documentation convention adopted from the family standard. See ADR 0013.

## Later - reach, not commitment

- **An MCP server** that exposes composition to any MCP-compatible agent. This is the one piece of new machinery worth considering, and only after composition is conflict-aware. It would reuse the proven pattern from the sibling `pm-skills-mcp` rather than start fresh.

## Hygiene (continuous)

- Keep CI runtimes current (Node 24).
- Resolve the `review_status` governance question: new entries should start at `draft`, not `stable`.
- Reconcile the "three axes vs four directories" framing so the model is described consistently in the README, the taxonomy, and the contributor docs.

## Deliberately deferred

The first roadmap imagined a Composer single-page app, a TypeScript SDK, a Python SDK, and a community quality-scoring program. These are deferred indefinitely, for concrete reasons:

- The documentation site already lets people browse and compose from the catalog, so a separate composer app duplicates it.
- The SDK surfaces have no consumer yet. The empty `packages/` stubs that implied them are being removed (recoverable from git if a real need appears).
- Generic skill-quality scoring and authoring machinery is already provided by sibling projects in the same family. This project should consume those rather than rebuild them.

What stays unique to this project is the catalog itself: a proven, conflict-aware, composable set of writing instructions that no sibling and no external tool provides.
