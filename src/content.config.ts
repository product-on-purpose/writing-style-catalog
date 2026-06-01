import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Mount the top-level docs/ tree in place as the Starlight docs collection.
// The Python generator (scripts/generate_site_pages.py) writes catalog pages
// into docs/; authored narrative pages also live in docs/. Excludes the
// internal/ working notes and per-directory README landing pages.
export const collections = {
  docs: defineCollection({
    loader: glob({
      pattern: ['docs/**/*.{md,mdx}', '!docs/internal/**', '!docs/**/README.md', '!docs/superpowers/**'],
      base: '.',
      generateId: ({ entry }) => {
        let noExt = entry.replace(/\.(md|mdx)$/, '');
        if (noExt.startsWith('docs/')) noExt = noExt.slice('docs/'.length);
        if (noExt.endsWith('/index')) return noExt.slice(0, -'/index'.length);
        return noExt;
      },
    }),
    schema: docsSchema(),
  }),
};
