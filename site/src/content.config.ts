import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Pattern S: rendered website content lives in src/content/docs/ and is read by
// the stock Starlight docsLoader(). The generated catalog (reference/, examples/,
// recipes/, templates/) is emitted here by scripts/gen-site.mjs and gitignored
// (rebuilt each build); the hand-authored narrative pages are committed.
export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
};
