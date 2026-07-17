import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';
import mdx from '@astrojs/mdx';
import remarkGfm from 'remark-gfm';
import { unified } from '@astrojs/markdown-remark';

// Integration order matters here:
//  - astro-mermaid must come BEFORE starlight (its own rule).
//  - @astrojs/mdx must come AFTER starlight, because Starlight registers
//    astro-expressive-code internally and expressive-code must precede mdx
//    (otherwise the build errors with "move astroExpressiveCode() before
//    mdx()"). @astrojs/mdx applies GFM to .mdx files so pipe tables on the
//    homepage and the generated .mdx entry/diff-pair pages render as real
//    tables instead of literal text.
export default defineConfig({
  site: 'https://product-on-purpose.github.io',
  base: '/writing-style-catalog',
  // Apply GFM (tables, strikethrough, autolinks) explicitly via the unified
  // processor (required in astro 7, which switched the default to Satteri).
  // .mdx files inherit this via @astrojs/mdx's extendMarkdownConfig (on by
  // default). Without an explicit remark-gfm here, GFM tables in .mdx pages
  // render as literal text (CommonMark features like bold and links still
  // work, but the GFM table extension is not applied to the .mdx pipeline in
  // this Starlight + astro-mermaid + mdx setup).
  markdown: {
    processor: unified({ remarkPlugins: [remarkGfm] }),
  },
  integrations: [
    mermaid({
      theme: 'default',
      autoTheme: true,
      // Family branding (SITE-STANDARD 14.2): accent #5C7CFA, system-ui, 14px.
      // Mirrors the pm-skills / thinking-framework-skills mermaid theme.
      mermaidConfig: {
        themeVariables: {
          lineColor: '#5C7CFA',
          fontFamily:
            'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif',
          fontSize: '14px',
        },
      },
    }),
    starlight({
      // Display title is deliberately "Writing Style Library" per ADR 0014: the
      // 2026-06-02 rename changed only the slug/identifiers to writing-style-catalog
      // and retained the human display name. (The astro-sites conformance packet's
      // "fix the stale title" item was based on the rename alone and did not account
      // for ADR 0014; the title is intentional, not stale.)
      title: 'Writing Style Library',
      description: 'Composable writing instructions on four orthogonal axes: Voice, Tone, Style, Format.',
      // Pattern S: the Astro app lives in site/, so the source path Starlight
      // appends is relative to site/ - the baseUrl carries the site/ prefix.
      // Generated pages set editUrl:false (their source is gitignored), so this
      // only applies to the committed hand-authored narrative pages.
      editLink: { baseUrl: 'https://github.com/product-on-purpose/writing-style-catalog/edit/main/site/' },
      customCss: ['./src/styles/custom.css'],
      // Starlight 0.41: autogenerate must be wrapped in items: [].
      // Pattern S: content lives in src/content/docs/ read by the stock
      // docsLoader(), so autogenerate directories are bare section names (no
      // 'docs/' prefix).
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Concepts', items: [{ autogenerate: { directory: 'concepts' } }] },
        { label: 'Guides', items: [{ autogenerate: { directory: 'guides' } }] },
        { label: 'Reference', items: [{ autogenerate: { directory: 'reference' } }] },
        { label: 'Examples', items: [{ autogenerate: { directory: 'examples' } }] },
        { label: 'Recipes', items: [{ autogenerate: { directory: 'recipes' } }] },
        { label: 'Templates', items: [{ autogenerate: { directory: 'templates' } }] },
        { label: 'Design Standards', items: [{ autogenerate: { directory: 'design-standards' } }] },
        { label: 'Contributing', items: [{ autogenerate: { directory: 'governance' } }] },
      ],
    }),
    // After starlight (see integration-order note above).
    mdx(),
  ],
});
