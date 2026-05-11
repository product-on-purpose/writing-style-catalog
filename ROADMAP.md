# Roadmap

## Phase 0 - Foundation (Current)

The current phase establishes the repository structure, authoring conventions, and schema definitions. Deliverables include the directory scaffold, root documentation files, five seed entries per axis (voices, tones, styles, formats), the async-standups vertical-slice anchor topic, and the `compose-instruction` skill stub. The goal is a working, validatable repo that contributors can build on before any UI or SDK work begins.

## Phase 1 - Composer SPA and Catalog Expansion

Phase 1 adds the browser-based Composer application (`packages/composer-app/`) that lets users browse taxonomy entries, select values on each axis, preview the composed instruction, and copy it to the clipboard. The catalog grows to 15 entries per axis, with vertical-slice examples covering three anchor topics. Documentation site goes live on GitHub Pages.

## Phase 2 - SDK and MCP Server

Phase 2 publishes a TypeScript SDK (`packages/ts-sdk/`) and Python SDK (`packages/py-sdk/`) for programmatic composition, and launches an MCP server (`packages/mcp-server/`) so the library can be used as a tool by any MCP-compatible agent. API surface is stabilized with a v1.0 schema freeze and migration guide.

## Phase 3 - Community and Quality

Phase 3 opens contribution pathways to the broader community with a formal review process, entry sponsorship program, and automated quality scoring. The catalog targets 50+ entries per axis. Integration recipes cover common developer and product workflows.
