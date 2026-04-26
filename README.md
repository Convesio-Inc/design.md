# design.md
Convesio's design.md

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
5. Run validation:

   ```bash
   python3 tools/validate_design_md.py
   ```
