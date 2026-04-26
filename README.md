# design.md
Convesio's design.md

## Scope & Source of Truth

- `design.md` (repo root): **Brand-level** system. Sources are **static site first** and **selective Figma** (logos/brand styling only). This file should not use Storybook as a source.
- `products/design.md`: **Product-level** system. **Storybook is the sole source of truth** for product tokens, components, and variants.
- `legacy/design.md`: **Legacy brand snapshot**. **Figma legacy file is the sole source of truth** for historical styles and migration reference.

## Updating `design.md`

1. Curate source evidence into `sources/` (no bulk dumps).
2. Update canonical tokens and section prose in `design.md`.
3. Keep section order aligned to spec:
   - Overview
   - Colors
   - Typography
   - Layout
   - Elevation & Depth
   - Shapes
   - Components
   - Do's and Don'ts
4. Maintain inline source refs and update `## Sources Mapping`.
5. Run official validation:

   ```bash
   npx @google/design.md lint design.md
   npx @google/design.md lint products/design.md
   npx @google/design.md lint legacy/design.md
   ```
