# Roadmap

The Writing Style Library is a composable catalog of writing instructions on four orthogonal axes: Voice, Tone, Style, and Format. As of v0.2.0 the catalog is public, the documentation site is live, the plugin is installable through the Product on Purpose marketplace, and the core mechanism is proven. A blind adherence test attributed 8 of 8 confusable composition pairs correctly (chance is roughly 0.4 percent), which means the per-entry instruction phrasings genuinely steer model output.

That result sets the direction. The catalog works, so the roadmap is about making it sharper and easier to find: depth and instructional leverage over raw breadth. We are deliberately not building a multi-surface product (SDKs, a composer app) that a catalog of this size does not need and a small team cannot maintain well.

## Now - surface and sharpen

- **Sharpen the "subtle" confusable pairs.** Done (2026-06-17). A blind gate pilot, confirmed cross-vendor (8/8 attribution by both an Anthropic and an OpenAI judge), re-rated the seams: `pragmatic-architect` vs `senior-consultant` came back "clear" and needs no work, while three pairs were genuinely subtle and have now been tightened from both sides - `narrative-case-study` vs `chronological-narrative`, `warm` vs `empathetic`, and `confident` vs `resolute`.
- **Add diff-pairs to the `service-database-choice` anchor topic.** It currently has none, despite being the best-isolated topic. Diff-pairs are the catalog's sharpest teaching tool.
- **Deepen existing entries toward the pedagogical bar.** Add tells, anti-patterns, failure modes, and before/after micro-examples to the entries that carry the most weight, rather than adding new entries to chase coverage.

## Next - make composition real

- **Make composition conflict-aware.** Shipped (2026-06-17, ADR 0016). The builder now reads each entry's `pairs_well_with` and `avoid_with`, flags incompatible selections with a symmetric rule, and applies voice -> tone -> style -> format precedence instead of concatenating strings. "Composable" is now a checked guarantee, which also clears the prerequisite for the MCP server below.
- **Repository legibility.** A generated repository map, per-folder READMEs on the source directories, and a documentation convention adopted from the family standard. See ADR 0013.

## Later - reach, not commitment

- **An MCP server** that exposes composition to any MCP-compatible agent. This is the one piece of new machinery worth considering, and only after composition is conflict-aware. It would reuse the proven pattern from the sibling `pm-skills-mcp` rather than start fresh.

## Hygiene (continuous)

- Keep CI runtimes current (Node 24).
- Resolve the `review_status` governance question: new entries should start at `draft`, not `stable`. Resolved - the validator enforces it, and 57 Stream-B breadth format candidates currently sit at `draft` awaiting maintainer promotion review (tracker: `docs/internal/release-plans/stream-b-breadth-status.md`).
- Reconcile the "three axes vs four directories" framing so the model is described consistently in the README, the taxonomy, and the contributor docs.

## Deliberately deferred

The first roadmap imagined a Composer single-page app, a TypeScript SDK, a Python SDK, and a community quality-scoring program. These are deferred indefinitely, for concrete reasons:

- The documentation site already lets people browse and compose from the catalog, so a separate composer app duplicates it.
- The SDK surfaces have no consumer yet. The empty `packages/` stubs that implied them are being removed (recoverable from git if a real need appears).
- Generic skill-quality scoring and authoring machinery is already provided by sibling projects in the same family. This project should consume those rather than rebuild them.

What stays unique to this project is the catalog itself: a proven, conflict-aware, composable set of writing instructions that no sibling and no external tool provides.
