import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';
import mdx from '@astrojs/mdx';
import remarkGfm from 'remark-gfm';

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
  // Apply GFM (tables, strikethrough, autolinks) explicitly. .mdx files inherit
  // this via @astrojs/mdx's extendMarkdownConfig (on by default). Without an
  // explicit remark-gfm here, GFM tables in .mdx pages render as literal text
  // (CommonMark features like bold and links still work, but the GFM table
  // extension is not applied to the .mdx pipeline in this Starlight +
  // astro-mermaid + mdx setup).
  markdown: {
    remarkPlugins: [remarkGfm],
  },
  integrations: [
    mermaid({ theme: 'default', autoTheme: true }),
    starlight({
      title: 'Writing Style Library',
      description: 'Composable writing instructions on four orthogonal axes: Voice, Tone, Style, Format.',
      editLink: { baseUrl: 'https://github.com/product-on-purpose/writing-style-catalog/edit/main/' },
      customCss: ['./src/styles/custom.css'],
      // Starlight 0.39: autogenerate must be wrapped in items: [].
      // The directory must be prefixed with 'docs/' because the custom glob
      // loader (src/content.config.ts) mounts ./docs in place with base '.',
      // so each entry's filePath retains the 'docs/' prefix. Starlight's
      // autogenerate matches on filePath, so it must be 'docs/<section>', not
      // '<section>'. (generateId strips 'docs/' for clean URLs, but that does
      // not change the filePath the nav logic reads.)
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Concepts', items: [{ autogenerate: { directory: 'docs/concepts' } }] },
        { label: 'Guides', items: [{ autogenerate: { directory: 'docs/guides' } }] },
        { label: 'Reference', items: [{ autogenerate: { directory: 'docs/reference' } }] },
        { label: 'Examples', items: [{ autogenerate: { directory: 'docs/examples' } }] },
        { label: 'Recipes', items: [{ autogenerate: { directory: 'docs/recipes' } }] },
        { label: 'Templates', items: [{ autogenerate: { directory: 'docs/templates' } }] },
        { label: 'Design Standards', items: [{ autogenerate: { directory: 'docs/design-standards' } }] },
        { label: 'Contributing', items: [{ autogenerate: { directory: 'docs/governance' } }] },
      ],
    }),
    // After starlight (see integration-order note above).
    mdx(),
  ],
});
