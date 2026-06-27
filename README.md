<a id="readme-top"></a>

<h1 align="center">
  <a href="https://github.com/product-on-purpose/writing-style-catalog">Writing Style Library</a>
</h1>

<h4 align="center">A composable catalog of writing instructions organized along orthogonal axes - Voice, Tone, Style, and Format - so you can compose precise, reusable writing instructions for any LLM instead of retyping vibes.</h4>

<p align="center">
  <a href="https://github.com/product-on-purpose/writing-style-catalog/issues/new?labels=bug">Report a Bug</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/product-on-purpose/writing-style-catalog/issues/new?labels=enhancement">Request a Feature</a>
  &nbsp;·&nbsp;
  <a href="https://product-on-purpose.github.io/writing-style-catalog/">Read the Docs</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Experimental-orange?style=flat-square" alt="Project Status: Experimental">
  <a href="https://github.com/product-on-purpose/writing-style-catalog/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache%202.0%20%2F%20CC--BY--4.0-blue.svg?style=flat-square" alt="License: Apache-2.0 (code) / CC-BY-4.0 (content)">
  </a>
  <img src="https://img.shields.io/badge/version-0.2.0-blue.svg?style=flat-square" alt="Version">
  <a href="#the-three-axis-model">
    <img src="https://img.shields.io/badge/entries-60-brightgreen.svg?style=flat-square" alt="Catalog entries">
  </a>
  <a href="https://agentskills.io/specification">
    <img src="https://img.shields.io/badge/spec-agentskills.io-orange.svg?style=flat-square" alt="Agent Skills Spec">
  </a>
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
</p>

<p align="center">
  <a href="https://github.com/product-on-purpose/writing-style-catalog/stargazers">
    <img src="https://img.shields.io/github/stars/product-on-purpose/writing-style-catalog?style=flat-square" alt="Stars">
  </a>
  <a href="https://github.com/product-on-purpose/writing-style-catalog/network/members">
    <img src="https://img.shields.io/github/forks/product-on-purpose/writing-style-catalog?style=flat-square" alt="Forks">
  </a>
  <a href="https://github.com/product-on-purpose/writing-style-catalog/issues">
    <img src="https://img.shields.io/github/issues/product-on-purpose/writing-style-catalog?style=flat-square" alt="Issues">
  </a>
  <a href="https://github.com/product-on-purpose/writing-style-catalog/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/product-on-purpose/writing-style-catalog?style=flat-square" alt="Contributors">
  </a>
  <img src="https://img.shields.io/github/last-commit/product-on-purpose/writing-style-catalog?style=flat-square" alt="Last Commit">
</p>

<p align="center">
  <a href="#the-big-idea">About</a> •
  <a href="#quick-start">Install</a> •
  <a href="#the-three-axis-model">The Model</a> •
  <a href="#whats-in-the-catalog">Catalog</a> •
  <a href="#documentation-site">Docs Site</a> •
  <a href="#project-status">Status</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

> [!WARNING]
> **Early and experimental (v0.2.0).** This project is in active early development. The catalog, schema, skill interface, and docs may change without notice; entries are still under review; and the planned Composer and SDK surfaces are not built yet. Use it, learn from it, and expect rough edges. Not recommended for production reliance.

<details>
<summary><strong>Table of Contents</strong></summary>

- [Quick Start](#quick-start)
- [The Big Idea](#the-big-idea)
- [The Three-Axis Model](#the-three-axis-model)
  - [Axis 1 - Voice and Tone](#axis-1---voice-and-tone)
  - [Axis 2 - Style / Mode / Genre](#axis-2---style--mode--genre)
  - [Axis 3 - Format / Output Structure](#axis-3---format--output-structure)
- [What's in the Catalog](#whats-in-the-catalog)
- [Documentation Site](#documentation-site)
- [Project Structure](#project-structure)
- [Project Status](#project-status)
- [Contributing](#contributing)
- [License](#license)
- [About the Author](#about-the-author)

</details>

---

## Quick Start

Install through the Product on Purpose marketplace, then compose. Run these inside Claude Code:

```bash
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install writing-style-catalog@product-on-purpose
```

Already installed? Pull the latest with `/plugin update writing-style-catalog`. Using
Claude.ai or Claude Desktop? See the [installation guide](https://product-on-purpose.github.io/writing-style-catalog/guides/install/)
for the ZIP path.

Then compose a writing instruction from any combination of axes:

```bash
/writing-style-catalog:writing-instruction-builder voice=pragmatic-architect tone=candid style=problem-solution format=adr
```

The `writing-instruction-builder` skill assembles a structured prompt prefix that you can prepend to any writing task. Mix and match entries across axes to get exactly the register, reasoning pattern, and layout you need.

> Browse the full catalog, worked examples, and side-by-side diff-pairs on the [documentation site](https://product-on-purpose.github.io/writing-style-catalog/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## The Big Idea

LLM-generated writing is uneven because the instructions are uneven. "Write a professional blog post" gets generic AI-prose; "write a PRD in a pragmatic-architect voice with a candid tone, structured as Problem/Goals/Non-Goals/Risks" gets something usable. The gap is not typing skill - it is access to a vocabulary that names the moves a writer can make.

The Writing Style Library is that vocabulary. It decomposes the overloaded idea of "style" into orthogonal, composable parts, ships worked examples that show what each named value actually produces, and packages the whole thing as a Claude Code plugin so any combination assembles into a ready-to-use instruction.

**Who is this for:** PMs, engineers, technical writers, marketers, pastors, and anyone who wants AI writing to land in a specific voice, register, and shape - and who would rather select named building blocks than re-explain the same tone every time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## The Three-Axis Model

### Axis 1 - Voice and Tone

Voice and Tone are two dimensions within the first axis. Voice captures persistent identity (how you always sound). Tone captures situational register (how you sound right now). They are kept as separate catalog directories (`taxonomy/voices/` and `taxonomy/tones/`) because they have different frontmatter and entry counts, but conceptually they belong to the same axis. When using the `writing-instruction-builder` skill, you pass both `voice=` and `tone=` as separate parameters because each is a distinct catalog lookup within Axis 1.

**Voice** is the persistent identity of the writer: their worldview, characteristic concerns, and the professional archetype they embody. Voice is stable across contexts. The `pragmatic-architect` voice, for example, always reasons from constraints and trade-offs, regardless of whether it is writing a slack message or a technical RFC.

**Tone** is situational coloring layered on top of voice. The same pragmatic-architect voice can deliver a message with a `candid` tone (direct, no softening) or a `warm` tone (patient, explanatory). Tone entries are orthogonal to voice entries, so any combination is valid.

### Axis 2 - Style / Mode / Genre

Style entries describe the cognitive and rhetorical pattern of the writing: how ideas are structured and sequenced. `problem-solution` moves from diagnosis to remedy. `layered-disclosure` leads with the answer and buries supporting detail for readers who want depth. Entries on this axis are independent of voice and tone, so the same style can be applied across a wide range of purposes.

### Axis 3 - Format / Output Structure

Format entries define the visual and structural container: headings, bullet depth, table layouts, ADR sections, standup fields. Format is purely presentational and can be composed with any voice/tone/style combination. A `daily-standup` format entry, for example, specifies the three canonical fields and their order, without dictating voice or rhetorical pattern.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## What's in the Catalog

| Axis | Entries | What it controls | Example entries |
|------|--------:|------------------|-----------------|
| **Voice** | 15 | Persistent writer identity: worldview, archetype, concerns | `pragmatic-architect`, `pastoral`, `journalist`, `coach` |
| **Tone** | 15 | Situational register layered on top of voice | `candid`, `warm`, `reverent`, `urgent` |
| **Style** | 15 | Cognitive and rhetorical pattern: how ideas are sequenced | `problem-solution`, `layered-disclosure`, `socratic-inquiry`, `dialectic` |
| **Format** | 15 | Visual and structural container: headings, sections, layout | `adr`, `daily-standup`, `slack-message`, `devotional-entry` |

Plus the assets that make the catalog teachable:

- **720 worked examples** - every one of the 60 entries rendered across all twelve anchor topics (async standups, morning routine, a Postgres-vs-DynamoDB decision, a roadmap deprioritization, onboarding a new hire, thanking a mentor, keeping a day of rest, a retirement send-off, a team milestone, a return-to-office position, a product launch, and a hard year in review), so you can see each entry rendered on real content.
- **130 diff-pairs** that hold a topic constant and vary one axis, so the effect of a single choice is visible side by side.
- **14 horizontal-slice recipes** - named, ready-to-use four-axis combinations for common writing tasks.
- **15 format templates** giving the canonical structure for each format (plus 9 draft candidate formats under review from the Stream-B breadth program).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Documentation Site

The full catalog is browsable as an [Astro Starlight site](https://product-on-purpose.github.io/writing-style-catalog/). Every entry has its own page with language patterns, when-to-use guidance, cross-references to compatible and confusable neighbors, and its worked examples embedded inline. The catalog pages are generated from `taxonomy/` and `examples/`, so the site never drifts from the source.

| If you want to... | Go to |
|---|---|
| Browse every entry by axis | [Reference](https://product-on-purpose.github.io/writing-style-catalog/reference/) |
| See one axis swapped on a fixed topic | [Diff-pairs](https://product-on-purpose.github.io/writing-style-catalog/examples/diff-pairs/) |
| Start from a ready-made combination | [Recipes](https://product-on-purpose.github.io/writing-style-catalog/recipes/) |
| Grab a canonical format structure | [Templates](https://product-on-purpose.github.io/writing-style-catalog/templates/) |
| Understand the design | [Concepts](https://product-on-purpose.github.io/writing-style-catalog/concepts/three-axis-model/) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Structure

| Path | Type | Purpose |
|------|------|---------|
| `taxonomy/voices/` | Content | Voice entries (persistent writer identity) |
| `taxonomy/tones/` | Content | Tone entries (situational register modifiers) |
| `taxonomy/styles/` | Content | Style/mode/genre entries (rhetorical patterns) |
| `taxonomy/formats/` | Content | Format/output-structure entries |
| `examples/vertical-slices/` | Content | Full worked examples for a single topic across all axes |
| `examples/horizontal-slices/` | Content | Cross-topic samples for a single axis value |
| `examples/diff-pairs/` | Content | Side-by-side pairs showing the effect of changing one axis |
| `schemas/` | Code | JSON Schema files for all entry types |
| `skills/writing-instruction-builder/` | Code | The writing-instruction-builder plugin skill |
| `library.json` | Config | Canonical plugin manifest (family Standard, Section 5) |
| `docs/` | Docs | Astro Starlight site (catalog pages generated from `taxonomy/` and `examples/`; narrative pages authored) |
| `tools/` | Code | Validation and index-generation scripts |
| `scripts/` | Code | Site page generator and freshness guard |
| `tests/` | Code | Pytest tests for the generator |
| `docs/internal/adr/` | Docs | Architecture Decision Records |
| `.claude-plugin/` | Config | Claude Code plugin manifest and config |
| `.github/` | Config | CI workflows and issue templates |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Status

**v0.2.0 - marketplace launch (early / experimental).** The plugin is now listed in the Product on Purpose marketplace and installable with the two commands in [Quick Start](#quick-start). Expect change: the schema, the skill interface, entry wording, and the docs are all still settling. Entries currently carry an optimistic review status and have not all been through formal maintainer review.

**What exists today:**

- 60 stable taxonomy entries (15 each across Voice, Tone, Style, Format), plus 9 draft format candidates under review (Stream-B breadth, batches 1-2)
- 720 worked examples across twelve anchor topics, plus 130 diff-pairs and 14 horizontal-slice recipes
- Working `writing-instruction-builder` skill
- An Astro Starlight documentation site, generated from the catalog and deployed to [GitHub Pages](https://product-on-purpose.github.io/writing-style-catalog/)
- Validation and freshness checks wired into CI

**Planned but not built yet:** a Composer web app, an MCP server, and TypeScript/Python SDKs.

Distributed through the Product on Purpose marketplace (`product-on-purpose/agent-plugins`), with a ZIP path for Claude.ai / Claude Desktop as the fallback (see the [installation guide](https://product-on-purpose.github.io/writing-style-catalog/guides/install/)). See [ROADMAP.md](ROADMAP.md) for upcoming phases.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are welcome. To add a taxonomy entry, submit an example, or improve the docs:

1. Fork the project
2. Create your feature branch (`git checkout -b feat/amazing-entry`)
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (`git commit -m 'feat(taxonomy): add amazing voice entry'`)
4. Run validation locally: `python tools/validate.py`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full entry-authoring checklist, schema conventions, and the house writing rules.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

This project is dual-licensed:

- **Code** (schemas, skills, tools, scripts, tests): [Apache-2.0](LICENSE)
- **Content** (taxonomy entries, examples, docs): [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

See [NOTICE](NOTICE) for full attribution details, including the provenance of LLM-generated example content.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## About the Author

<p align="center">
  <a href="https://github.com/jprisant">
    <img src="https://img.shields.io/badge/Created_by-Jonathan_Prisant-blue?style=for-the-badge&logo=github" alt="Created by Jonathan Prisant">
  </a>
</p>

Howdy, I'm Jonathan Prisant, a product leader/manager/nerd in the church technology space who gets unreasonably excited about understanding and solving problems, serving humans, designing elegant systems, and getting stuff done. The Writing Style Library started as a question - what would it take to instruct an LLM on writing as precisely as we instruct it on code? - and grew into a composable catalog I use in my own work.

*If the Writing Style Library helps you get better writing out of your tools, consider giving the repo a star and sharing it.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<p align="center">
  <strong>Built with purpose by <a href="https://github.com/product-on-purpose">Product on Purpose</a></strong><br>
  <sub>Build products on purpose, not by accident.</sub>
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
