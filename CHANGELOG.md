# Changelog

All notable changes to this repository are documented in this file.

## 2026-04-26

### Added
- Added `products/design.md` for product-level design system guidance with Storybook as the sole source of truth.
- Added `legacy/design.md` for legacy Figma-only brand snapshot guidance.
- Added `new/design.md` as the current brand-level canonical DESIGN.md location.
- Added `.gitignore` entry to ignore local `docs/` workspace artifacts.
- Added README directory guide for repository structure and authority boundaries.

### Changed
- Aligned repository workflows to use official Google lint commands for all DESIGN.md files.
- Split authority model by scope:
  - `new/design.md` for brand (static site + selective Figma)
  - `products/design.md` for product (Storybook-only)
  - `legacy/design.md` for historical legacy (Figma-only)

### Removed
- Removed custom local validator/test workflow files:
  - `tools/validate_design_md.py`
  - `tests/test_validate_design_md.py`
