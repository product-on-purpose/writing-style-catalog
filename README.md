<a id="readme-top"></a>

<h1>
  <a href="https://github.com/product-on-purpose/writing-style-catalog">Writing Style Library</a>
</h1>

<h4>Instruct an LLM on writing as precisely as you already instruct it on code. Pick one named entry on each of four axes - Voice, Tone, Style, and Format - and compose them into a reusable instruction, instead of retyping vibes.</h4>

<p>
  <a href="https://github.com/product-on-purpose/writing-style-catalog/issues/new?labels=bug">Report a Bug</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/product-on-purpose/writing-style-catalog/issues/new?labels=enhancement">Request a Feature</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/product-on-purpose/writing-style-catalog/issues/new?template=entry_proposal.yml">Propose an Entry</a>
  &nbsp;·&nbsp;
  <a href="https://product-on-purpose.github.io/writing-style-catalog/">Read the Docs</a>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Experimental-orange?style=flat-square" alt="Project Status: Experimental">
  <a href="https://github.com/product-on-purpose/writing-style-catalog/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache%202.0%20%2F%20CC--BY--4.0-blue.svg?style=flat-square" alt="License: Apache-2.0 (code) / CC-BY-4.0 (content)">
  </a>
  <img src="https://img.shields.io/badge/version-0.15.0-blue.svg?style=flat-square" alt="Version">
  <a href="#the-four-axis-model">
    <img src="https://img.shields.io/badge/entries-121-brightgreen.svg?style=flat-square" alt="Catalog entries: 121 (98 machine-verified, 23 draft)">
  </a>
  <a href="https://agentskills.io/specification">
    <img src="https://img.shields.io/badge/spec-agentskills.io-orange.svg?style=flat-square" alt="Agent Skills Spec">
  </a>
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
</p>

<p>
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

<p>
  <a href="#the-big-idea">About</a> •
  <a href="#quick-start">Install</a> •
  <a href="#does-it-work">Evidence</a> •
  <a href="#the-four-axis-model">The Model</a> •
  <a href="#whats-in-the-catalog">Catalog</a> •
  <a href="#documentation-site">Docs Site</a> •
  <a href="#project-status">Status</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

> [!WARNING]
> **Early and experimental (v0.15.0).** This project is in active early development. The catalog, schema, skill interface, and docs may change without notice; entries are still under review; and the Composer and SDK surfaces are deliberately deferred indefinitely (see [ROADMAP.md](ROADMAP.md)). Use it, learn from it, and expect rough edges. Not recommended for production reliance.

---

<details>
<summary><strong>Table of Contents</strong></summary>

- [Quick Start](#quick-start)
- [The Big Idea](#the-big-idea)
- [Does It Work?](#does-it-work)
- [The Four-Axis Model](#the-four-axis-model)
  - [Axis 1 - Voice](#axis-1---voice)
  - [Axis 2 - Tone](#axis-2---tone)
  - [Axis 3 - Style / Mode / Genre](#axis-3---style--mode--genre)
  - [Axis 4 - Format / Output Structure](#axis-4---format--output-structure)
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

Not sure which combination fits your situation? Describe it instead:

```bash
/writing-style-catalog:entry-recommender I need to tell my engineering team that a feature we committed to is getting cut this quarter, and I want them to trust the reasoning, not just accept the decision.
```

The `entry-recommender` skill scores the catalog against your description, picks a voice/tone/style/format combination with a reason quoting each entry's own language, and composes the prompt in the same step. See the [usage guide](https://product-on-purpose.github.io/writing-style-catalog/guides/recommend-entries/) for real example output.

> Browse the full catalog, worked examples, and side-by-side diff-pairs on the [documentation site](https://product-on-purpose.github.io/writing-style-catalog/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## The Big Idea

LLM-generated writing is uneven because the instructions are uneven. "Write a professional blog post" gets generic AI-prose; "write a PRD in a pragmatic-architect voice with a candid tone, structured as Problem/Goals/Non-Goals/Risks" gets something usable. The gap is not typing skill - it is access to a vocabulary that names the moves a writer can make.

The Writing Style Library is that vocabulary. It decomposes the overloaded idea of "style" into orthogonal, composable parts, ships worked examples that show what each named value actually produces, and packages the whole thing as a Claude Code plugin so any combination assembles into a ready-to-use instruction.

**Who is this for:** product managers and builders who write PRDs, ADRs, updates, and standups with an LLM every day, and anyone else who wants AI writing to land in a specific voice, register, and shape. That includes marketers, technical writers, and pastors. It suits anyone who would rather select named building blocks than re-explain the same tone every time.

**How it differs from a prompt library:** a prompt library is a pile of finished prompts, one per task. This catalog is a coordinate system: four independent axes, a named value on each, and a builder that warns you when two choices clash. See [How It Compares](https://product-on-purpose.github.io/writing-style-catalog/concepts/how-it-compares/) for the side-by-side, including where a style guide or a prompt library is the better tool.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Does It Work?

A named instruction is only worth having if it changes what the model writes. That was measured, blind, with a negative control:

- **8 of 8** near-neighbour pairs, such as `candid` versus `confident`, were attributed correctly by a blind judge from the same model family. Chance is about 0.4 percent.
- **18 of 18** samples were attributed correctly by a blind judge from a different vendor.
- **3 of 3** deliberate caricatures were rejected, each for the failure mode its own entry documents. This shows the judge says no when it should.

These are small tests. They covered sixteen, nine, and three entries respectively, the judges were models rather than people, and the judges saw short descriptions of the options. The [evidence page](https://product-on-purpose.github.io/writing-style-catalog/concepts/adherence-evidence/) records the method, the results, and every limit. Skeptical questions, including whether the examples are LLM-written (they are), are answered in the [FAQ](https://product-on-purpose.github.io/writing-style-catalog/concepts/faq/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## The Four-Axis Model

Four axes, one selection each, any combination valid. The test each axis has to pass: hold the other three constant, vary this one, and the output changes in a way you can point at.

### Axis 1 - Voice

**Voice** is the persistent identity of the writer: their worldview, characteristic concerns, and the professional archetype they embody. Voice is stable across contexts. The `pragmatic-architect` voice, for example, always reasons from constraints and trade-offs, regardless of whether it is writing a slack message or a technical RFC.

### Axis 2 - Tone

**Tone** is situational coloring layered on top of voice. The same pragmatic-architect voice can deliver a message with a `candid` tone (direct, no softening) or a `warm` tone (patient, explanatory). Tone entries are orthogonal to voice entries, so any combination is valid.

Voice and Tone are the most confusable pair in the catalog, so the rule for telling them apart is worth stating plainly: **voice is what does not change; tone is what changes per piece.** They live in separate directories (`taxonomy/voices/` and `taxonomy/tones/`), require different frontmatter, and validate against different schemas. If you come from brand-writing, where "voice and tone" is a single compound noun, note that this catalog splits them because you select them as two independent parameters at composition time. Earlier docs called this a three-axis model and grouped them; see [ADR 0018](docs/internal/adr/0018-four-axis-framing.md) for why the label changed.

### Axis 3 - Style / Mode / Genre

Style entries describe the cognitive and rhetorical pattern of the writing: how ideas are structured and sequenced. `problem-solution` moves from diagnosis to remedy. `layered-disclosure` leads with the answer and buries supporting detail for readers who want depth. Entries on this axis are independent of voice and tone, so the same style can be applied across a wide range of purposes.

### Axis 4 - Format / Output Structure

Format entries define the visual and structural container: headings, bullet depth, table layouts, ADR sections, standup fields. Format is purely presentational and can be composed with any voice/tone/style combination. A `daily-standup` format entry, for example, specifies the three canonical fields and their order, without dictating voice or rhetorical pattern.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## What's in the Catalog

The catalog holds **121 entries**. 98 of them ship in the plugin and carry `machine-verified`: each passes every automated check and has not yet been read line by line by the maintainer. The other 23 are drafts, still under review and not shipped: 20 format candidates, and one new entry each on Voice, Tone, and Style.

| Axis | Entries | What it controls | Example entries |
| ------ | --------: | ---------------- | --------------- |
| **Voice** | 17 (16 shipped, 1 draft) | Persistent writer identity: worldview, archetype, concerns | `pragmatic-architect`, `pastoral`, `journalist`, `coach` |
| **Tone** | 16 (15 shipped, 1 draft) | Situational register layered on top of voice | `candid`, `warm`, `reverent`, `urgent` |
| **Style** | 16 (15 shipped, 1 draft) | Cognitive and rhetorical pattern: how ideas are sequenced | `problem-solution`, `layered-disclosure`, `socratic-inquiry`, `dialectic` |
| **Format** | 72 (52 shipped, 20 draft) | Visual and structural container: headings, sections, layout | `adr`, `daily-standup`, `slack-message`, `devotional-entry` |

Plus the assets that make the catalog teachable:

- **1176 worked examples** - every one of the 98 shipped entries rendered across all twelve anchor topics (async standups, morning routine, a Postgres-vs-DynamoDB decision, a roadmap deprioritization, onboarding a new hire, thanking a mentor, keeping a day of rest, a retirement send-off, a team milestone, a return-to-office position, a product launch, and a hard year in review), so you can see each entry rendered on real content.
- **158 diff-pairs** across all twelve anchor topics, each holding a topic constant and varying one axis, so the effect of a single choice is visible side by side.
- **14 horizontal-slice recipes** - named, ready-to-use four-axis combinations for common writing tasks.
- **52 format templates** giving the canonical structure for each format (plus 20 draft candidate formats under review from the Stream-B breadth program).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Documentation Site

The full catalog is browsable as an [Astro Starlight site](https://product-on-purpose.github.io/writing-style-catalog/). Every entry has its own page with language patterns, when-to-use guidance, cross-references to compatible and confusable neighbors, and its worked examples embedded inline. The catalog pages are generated from `taxonomy/` and `examples/`, so the site never drifts from the source.

| If you want to... | Go to |
| --- | --- |
| Browse every entry by axis | [Reference](https://product-on-purpose.github.io/writing-style-catalog/reference/) |
| See one axis swapped on a fixed topic | [Diff-pairs](https://product-on-purpose.github.io/writing-style-catalog/examples/diff-pairs/) |
| Start from a ready-made combination | [Recipes](https://product-on-purpose.github.io/writing-style-catalog/recipes/) |
| Grab a canonical format structure | [Templates](https://product-on-purpose.github.io/writing-style-catalog/templates/) |
| Understand the design | [Concepts](https://product-on-purpose.github.io/writing-style-catalog/concepts/four-axis-model/) |
| Check the evidence that it works | [Does it actually work?](https://product-on-purpose.github.io/writing-style-catalog/concepts/adherence-evidence/) |
| Compare it with prompt libraries and style guides | [How It Compares](https://product-on-purpose.github.io/writing-style-catalog/concepts/how-it-compares/) |
| Read the skeptical questions, answered | [FAQ](https://product-on-purpose.github.io/writing-style-catalog/concepts/faq/) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Structure

| Path | Type | Purpose |
| ------ | ---- | ------- |
| `taxonomy/voices/` | Content | Voice entries (persistent writer identity) |
| `taxonomy/tones/` | Content | Tone entries (situational register modifiers) |
| `taxonomy/styles/` | Content | Style/mode/genre entries (rhetorical patterns) |
| `taxonomy/formats/` | Content | Format/output-structure entries |
| `examples/vertical-slices/` | Content | Full worked examples for a single topic across all axes |
| `examples/horizontal-slices/` | Content | Cross-topic samples for a single axis value |
| `examples/diff-pairs/` | Content | Side-by-side pairs showing the effect of changing one axis |
| `schemas/` | Code | JSON Schema files for all entry types |
| `skills/writing-instruction-builder/` | Code | Compose a prompt from axis values you already know you want |
| `skills/style-profile/` | Code | Capture a personal default style once, for reuse |
| `skills/entry-recommender/` | Code | Recommend a combination for a described situation |
| `library.json` | Config | Canonical plugin manifest (family Standard, Section 5) |
| `site/` | Docs | Astro Starlight site app (authored pages in `src/content/docs/`; catalog pages generated at build time) |
| `docs/` | Docs | Internal governance only (ADRs, plans, specs) - not built by Astro; the site lives in `site/` |
| `tools/` | Code | Validation and index-generation scripts |
| `scripts/` | Code | Site page generator and freshness guard |
| `tests/` | Code | Pytest suites for tools and skills, plus the site-generator test (run with `node --test`) |
| `docs/internal/adr/` | Docs | Architecture Decision Records |
| `.claude-plugin/` | Config | Claude Code plugin manifest and config |
| `.github/` | Config | CI workflows and issue templates |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Status

**v0.15.0 (early / experimental).** The plugin is listed in the Product on Purpose marketplace and installable with the two commands in [Quick Start](#quick-start). The entry schema is now frozen (see [ADR 0019](docs/internal/adr/0019-schema-freeze-and-change-policy.md)), so its shape will not change without a major version and a migration. The skill interface, entry wording, and docs are all still settling. Shipped entries carry `machine-verified`: they pass every automated check, and the maintainer's line-by-line reading is in progress (see [ADR 0021](docs/internal/adr/0021-honest-middle-review-status.md)).

**What exists today:**

- 121 taxonomy entries in all: 98 shipped (16 Voice, 15 Tone, 15 Style, 52 Format), all `machine-verified`, plus 23 drafts under review: 20 format candidates (Stream-B breadth, batches 1-10) and three exemplars opening the Voice, Tone, and Style rebalance (`elder`, `grateful`, `first-principles-derivation`)
- 1176 worked examples across twelve anchor topics, plus 158 diff-pairs and 14 horizontal-slice recipes
- Three working skills: `writing-instruction-builder` (compose from known axis values), `style-profile` (capture a personal default), `entry-recommender` (recommend a combination for a described situation)
- An Astro Starlight documentation site, generated from the catalog and deployed to [GitHub Pages](https://product-on-purpose.github.io/writing-style-catalog/)
- Validation and freshness checks wired into CI

**Deliberately deferred, not planned:** a Composer web app and TypeScript/Python SDKs - the docs site already covers browsing and composing, and there is no consumer signal for the SDKs (see [ROADMAP.md](ROADMAP.md)'s "Deliberately deferred"). **Genuinely possible later:** an MCP server exposing composition to other agents, gated on a real consumer signal that has not appeared yet.

Distributed through the Product on Purpose marketplace (`product-on-purpose/agent-plugins`), with a ZIP path for Claude.ai / Claude Desktop as the fallback (see the [installation guide](https://product-on-purpose.github.io/writing-style-catalog/guides/install/)). See [ROADMAP.md](ROADMAP.md) for upcoming phases.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Writing has more voices than one maintainer knows. If the catalog is missing a voice, tone, style, or format you use, that gap is the most valuable thing you can contribute.

The easiest start is to [propose an entry](https://github.com/product-on-purpose/writing-style-catalog/issues/new?template=entry_proposal.yml). A proposal needs no code: name the entry, say which axis it belongs on, and say which existing entry it is most easily confused with. If it holds up, you or the maintainer can build it.

To build an entry, an example, or a docs fix yourself:

1. Fork the project
2. Create your feature branch (`git checkout -b feat/amazing-entry`)
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (`git commit -m 'feat(taxonomy): add amazing voice entry'`)
4. Run validation locally: `python tools/validate.py`
5. Open a Pull Request

New entries start as `draft`. Tooling promotes an entry to `machine-verified` once it passes every check, and only the maintainer moves an entry to `stable`, after reading it. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry bar, the review ladder, and the full checklist.

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
