import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://product-on-purpose.github.io',
  base: '/writing-style-library',
  integrations: [
    // astro-mermaid must come BEFORE starlight (integration-order rule).
    mermaid({ theme: 'default', autoTheme: true }),
    starlight({
      title: 'Writing Style Library',
      description: 'Composable writing instructions on four orthogonal axes: Voice, Tone, Style, Format.',
      editLink: { baseUrl: 'https://github.com/product-on-purpose/writing-style-library/edit/main/' },
      customCss: ['./src/styles/custom.css'],
      // Starlight 0.39: autogenerate must be wrapped in items: [].
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
  ],
});
