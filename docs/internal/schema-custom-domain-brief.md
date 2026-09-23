# Schema custom domain - decision brief

Status: for maintainer decision (drafted 2026-09-23)

## 1. The decision

Yes = register a domain (or use one the maintainer already owns) and point it at where the
catalog's JSON Schemas are served, so schema `$id` URIs stop being tied to the
`product-on-purpose` GitHub org and the `writing-style-catalog` Pages path. No = keep serving
schemas from `https://product-on-purpose.github.io/writing-style-catalog/schemas/v1/`, accept
that a future org rename or repository transfer would break every `$id`, and make sure launch
copy says "versioned and pinnable," never "permanent."

## 2. What's confirmed against the repo and against GitHub's own docs

The six frozen schemas (`entry.universal`, `voice`, `tone`, `style`, `format`, `example`) carry
`$id: https://product-on-purpose.github.io/writing-style-catalog/schemas/v1/<name>.schema.json`
(checked directly in `schemas/*.json`). The unfrozen `diff-pair` schema is served separately at
`/schemas/experimental/`. `site/astro.config.mjs` sets `site: 'https://product-on-purpose.github.io'`
and `base: '/writing-style-catalog'`, which is exactly the coupling in question. No `CNAME` file
exists in the repo today, so no custom-domain groundwork has been started.

The summary handed to me for this brief matches what's already recorded in
[ADR 0020 (versioned schema IDs)](adr/0020-versioned-schema-ids.md) and in `docs/internal/backlog.md`
(the "custom domain" row). I did not find anything in the repo that contradicts it. I did check the
underlying GitHub claim against GitHub's own documentation rather than take it on faith:

- Renaming a repository does not redirect its Pages site: "If you plan to rename a repository
  that has a GitHub Pages site, we recommend using a custom domain for your site. This ensures
  that the site's URL isn't impacted by renaming the repository" - [Renaming a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository).
- Transferring a repository does not redirect its Pages site either: GitHub's transfer docs
  state that links to the repository itself redirect, but the Pages site does not, and warn
  about DNS takeover risk if a custom domain was attached before a transfer -
  [Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).

One fact worth adding: **adding a custom domain does not 404 today's URLs; GitHub 301-redirects
them.** GitHub's docs do not state this, so it was tested directly on 2026-09-23 against two
independent project sites that use a custom domain:

- `jekyll.github.io/jekyll/docs/installation/` -> `301` to `jekyllrb.com/docs/installation/`
- `docsifyjs.github.io/docsify/_sidebar.md` -> `301` to `docsify.js.org/_sidebar.md` (a
  non-HTML file, like a schema)

The redirect preserves the path and drops the `/<repo>` segment, which is exactly what a `base`
change to `/` produces. So `.../writing-style-catalog/schemas/v1/voice.schema.json` would land on
`<domain>/schemas/v1/voice.schema.json`. Two caveats: the redirect points at `http://` (HTTPS
enforcement then adds a second hop), and it only lasts while the site stays on this repository.

What a redirect does **not** preserve is **identity**. A consumer whose own documents `$ref` the
old `$id` string, resolved against a local registry keyed by `$id` rather than by fetching, stops
matching once the schemas declare a new `$id`. That is the real compatibility event here, and it is
why the change is still class C (section 4) even though fetching keeps working.

## 3. Options

| Option | Cost | Changes in this repo | What breaks for existing pinners |
|---|---|---|---|
| (a) Custom domain on the whole Pages site | Domain registration, roughly $10-20/yr (estimate, not checked live) + ongoing renewal/DNS upkeep | `site/public/CNAME`, repo Settings > Pages custom-domain field + enforce HTTPS, `astro.config.mjs` `site` and `base` (drops to `/` since a project custom domain serves at its root, not under `/writing-style-catalog` - confirmed via [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)), the `redirects` entry that hardcodes `/writing-style-catalog/...`, all 7 `$id` values, `tests/test_schema_change_policy.py`'s `SCHEMA_BASE` constant. `scripts/site-base.mjs` already centralizes the base literal (SITE-STANDARD 14.7), so most generated pages pick the new base up automatically; nothing in `site/src/` hardcodes it. | Fetching keeps working: old URLs 301 to the same path on the new domain (tested, see section 2). What changes is the `$id` string itself, so a consumer resolving by `$id` identity rather than by fetch needs to update its references once. Setting the domain on the organization site instead would move every `product-on-purpose` project site under it at once, including the sibling Astro sites. |
| (b) Dedicated schema subdomain / separate tiny Pages repo, just for schemas | Same domain estimate as (a) if a new domain is bought; $0 incremental if it is a subdomain of a domain already owned (a subdomain costs nothing beyond the parent domain) | A new small repo (or Pages target) that publishes only `schemas/`, a DNS record for the subdomain, and a new sync mechanism (a workflow in this repo pushing to the new repo, or one there pulling from this one, needs a stored credential). The 7 `$id` values change host but can keep the same `/schemas/v1/<name>` suffix, so `gen-site.mjs`'s existing "`$id` must match the path it publishes to" check needs no logic change. `schemas/README.md` and this repo's own `gen-site.mjs` publishing into `site/public/schemas/` are untouched, so that copy keeps serving unmodified. | Nothing has to break. Because the main docs site's Pages hosting is not touched, the old `product-on-purpose.github.io/writing-style-catalog/schemas/v1/*.json` files keep being generated and served exactly as today; they become a legacy mirror whose own `$id` field now points at the new canonical host. This is the only option that can offer indefinite parallel serving of old and new URLs. |
| (c) Do nothing; word the launch copy honestly | $0 | None to `schemas/`, `astro.config.mjs`, or CI. A copy pass over README, the site's landing content, and the marketing/launch plan to make sure nothing says "permanent" or "will never move." | Nothing breaks now. The exposure ADR 0020 (versioned schema IDs) already named stays open: a future org rename or repo transfer 404s every `$id` with no redirect. |

Both (a) and (b) also add a failure mode `github.io` doesn't have: if the domain registration
lapses or is not renewed, someone else can register it and serve arbitrary content at the old
`$id` URLs (a domain takeover). That risk, and the recurring renewal obligation, is part of what
"owning a domain" commits the project to, independent of which option is chosen.

## 4. Change class under ADR 0019

[ADR 0019 (schema freeze and change policy)](adr/0019-schema-freeze-and-change-policy.md) puts
`$id` explicitly on the class C keyword list, so changing it to a new domain is class C by rule,
even though the schema's shape stays byte-identical. The rule and ADR 0019's own test ("would this
change the verdict on any conceivable document") agree here: a consumer document that `$ref`s the
old `$id` and resolves it against a registry keyed by `$id` gets a different outcome (unresolved)
once the schemas declare the new one.

Class C requires an ADR, a version bump, every affected file migrated, and `validate.py` green.
Per the ADR 0019 amendment on pre-1.0 costs: at the current version (`0.13.0`, still `0.y.z`), the
bump is minor (for example `0.13.0` to `0.14.0`) - the same shape as [ADR 0020 (versioned schema IDs)](adr/0020-versioned-schema-ids.md),
which did `v0.8.0` to `v0.9.0` for a comparable `$id` change. From `1.0.0` onward, class C means a
major bump - so a pure host change with an identical schema shape would force a `1.x` to `2.0.0`
jump. That is the cost side of the ADR 0019 amendment's own advice to "pull class C changes
forward": the same edit is cheap now and disproportionately expensive later.

**`SCHEMA_CONTRACT_VERSION` does not move for this change.** That constant tracks the schema
*shape* (`v1`), not its host. A domain change does not trigger `scripts/gen-site.mjs`'s snapshot
requirement or `test_contract_version_bump_requires_a_snapshot`, because the contract itself has
not broken, only where it is fetched from.

**Can old URLs keep working?** For fetching, yes under both (a) and (b): (a) through GitHub's
301 redirect (section 2), (b) by leaving the existing publish target serving unchanged copies.
For `$id` identity, neither option helps; the new `$id` is a new identifier under either, which is
why this is a one-time class C event whichever option is chosen.

## 5. Migration checklist, if the decision is yes

This checklist is for option (a), the cheaper structural path, to run *before* `1.0.0`:

1. Decide the domain name (or confirm an existing `product-on-purpose`-owned domain to use) - maintainer decision, see section 6.
2. Register the domain (or the subdomain) if new; this is the ~$10-20/yr recurring line item.
3. Add the DNS records GitHub's custom-domain docs specify for the chosen apex/subdomain shape.
4. Add `site/public/CNAME` (or the equivalent Astro `public/` asset) with the domain, and set the custom domain plus "Enforce HTTPS" in repo Settings > Pages. Verify whether the Actions-based deploy (`actions/deploy-pages`) needs the CNAME file present in every build artifact to keep the setting, since this was not independently confirmed for this brief.
5. Update `astro.config.mjs`: `site` to the new domain, `base` to `/` (confirm the exact base Starlight expects for a root-served site), and the hardcoded `/writing-style-catalog/...` target in `redirects`.
6. Update all 7 schema `$id` values (6 frozen under `/schemas/v1/`, 1 experimental under `/schemas/experimental/`) to the new host, keeping the existing path suffixes so `gen-site.mjs`'s path-agreement check keeps passing unmodified.
7. Update `tests/test_schema_change_policy.py`'s `SCHEMA_BASE` constant and rerun the full suite plus `node --test tests/gen-site.test.mjs`.
8. Grep the repo for the old `product-on-purpose.github.io/writing-style-catalog` string outside `schemas/contracts/` snapshots (README, `schemas/README.md`, `docs/internal/backlog.md`, the marketing/launch plan) and update live references; leave historical ADR text as-is.
9. Write the ADR this change requires under ADR 0019's class C process, and bump the plugin version's minor component.
10. Build the site locally (`cd site && npm run build`) and confirm every `$id` resolves at its published URL before merging.
11. After merge and deploy, spot-check that each old `github.io` schema URL returns a 301 to the same path on the new domain, that the new URL serves the file over HTTPS, and that nothing in the shipped site or `README.md` still links to the old host.
12. Update `docs/internal/backlog.md`'s custom-domain row to record the resolution.

## 6. Recommendation

**Decide before `1.0.0`; this is a decision with a real deadline.** The change is class C, so it
costs a minor bump today and a major bump after `1.0.0`. With GATE 1 (reviewed catalog) reframed
by ADR 0021 (machine-verified review_status) on 2026-09-23, `1.0.0` is closer than it was, so
"later" is no longer free.

The recommended default is **(c): no domain, and honest copy**, unless the maintainer already
owns a suitable domain. There is no evidence of an external consumer pinning a schema URL yet,
and a recurring domain obligation with a takeover-risk surface does not fit the project's
agentic-first, no-funded-headcount posture. Do the free part now either way: launch and README
copy say "versioned and pinnable", never "permanent", matching ADR 0019 and ADR 0020.

**If the answer is yes, choose (a), not (b).** GitHub's 301 redirect keeps today's URLs fetchable
under (a), which removes the one advantage (b) had, and (b) adds a second repository, a sync
workflow, and a stored credential. If a `product-on-purpose` domain is ever wanted for the sibling
Astro sites too, set it on the organization site and all of them move together.

The one thing only the maintainer can decide: whether to take on owning a domain at all (the
registration and DNS maintenance, and the renewal-lapse/takeover risk that comes with it), and if
yes, which domain or subdomain name to use, including whether a `product-on-purpose`-family domain
already exists that this could ride on for free.
