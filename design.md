---
version: "alpha"
name: "Convesio Design System"
description: "Canonical visual and component guidance with curated provenance."
authority:
  visual: "static-site"
  components: "storybook"
  brand: "figma-selective"
rules:
  static-site-canonical-visual-authority: true
  storybook-current-components-only: true
  figma-selective-logos-style-only: true
  avoid-dark-bias-inheritance: true
colors:
  primary:
    value: "#0A66FF"
    status: "proposed"
    sources:
      - "static-site:navigation"
      - "figma:logo-brand"
  surface:
    value: "#FFFFFF"
    status: "proposed"
    sources:
      - "static-site:page-surface"
  on-surface:
    value: "#111111"
    status: "proposed"
    sources:
      - "static-site:body-copy"
typography:
  body-md:
    fontFamily: "Inter"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
    status: "proposed"
    sources:
      - "static-site:body-copy"
      - "storybook:button-primary"
spacing:
  md:
    value: "16px"
    status: "proposed"
    sources:
      - "static-site:feature-grid"
radii:
  sm:
    value: "6px"
    status: "proposed"
    sources:
      - "static-site:cards"
      - "storybook:button-primary"
components:
  button-primary:
    status: "proposed"
    source: "storybook:button-primary"
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.body-md}"
    radius: "{radii.sm}"
    paddingBlock: "12px"
    paddingInline: "16px"
---

## Overview
This file is the canonical `design.md` reference for Convesio design decisions. Static-site visuals are the canonical authority for overall look, feel, layout rhythm, color usage, imagery direction, and visual conflict resolution. Storybook describes current product component behavior and variants. Figma is used selectively for logos and brand styling references only.

Future UI generation should favor the lighter static-site direction and avoid inheriting legacy dark-background bias unless that treatment is directly evidenced in the static site.

Canonical authority model:
- Static site is canonical for page-level visual direction and conflict resolution.
- Storybook is canonical for current component behavior and variant contracts.
- Figma is selective for logos and brand styling references only.
- Source-specific capture rules live in each source README; shared authority decisions are defined here.

Status lifecycle:
- `proposed`: candidate value with curated evidence linked by short source IDs.
- `validated`: reviewed by a maintainer with evidence quality confirmed.
- `canonical`: approved default for broad production use across the system.

Promotion requires passing the curated evidence checklist in `sources/mapping.md`.

Source refs: `static-site:home-hero`, `static-site:page-surface`, `storybook:button-primary`, `figma:logo-brand`

## Colors
Color roles are derived from static-site usage first, then reconciled with Storybook where current components depend on an explicit token. Figma color cues are limited to logo and brand styling context; they do not override static-site page direction.

Use `surface` and `on-surface` for the default light UI baseline. Use `primary` for core interactive emphasis and brand-forward calls to action.

Accessibility guardrails (v1): [contrast status: proposed, not yet verified end-to-end] body text and essential UI text should target WCAG AA contrast (4.5:1 minimum against its surface). Large text (18px regular or 14px bold and above) should not drop below 3:1. Non-text interactive UI indicators such as borders, icons, and controls should maintain at least 3:1 contrast against adjacent surfaces.

Source refs: `static-site:navigation`, `static-site:page-surface`, `static-site:body-copy`, `figma:logo-brand`

## Typography
Typography should preserve the static site's reading rhythm and approachable product-marketing tone. Current Storybook components may clarify component-level type contracts, but broad type scale choices should remain aligned to static-site behavior.

`body-md` is the baseline text role for product UI copy and component labels until verified source captures justify a fuller type scale.

Source refs: `static-site:body-copy`, `storybook:button-primary`

## Layout
Spacing and composition follow static-site page patterns: clear section rhythm, generous breathing room, and reusable grid spacing that can translate into product screens without becoming dense or dark by default.

Use `spacing.md` as a portable baseline for component and page layout decisions. Additional spacing tokens should be added only when curated source evidence shows a repeated need.

Focus visibility (v1): [focus status: proposed, partially verified] all keyboard-focusable controls must render a clearly visible focus indicator that is not color-only and remains present against light surfaces; prefer an outline or ring with at least 3:1 contrast from adjacent colors. Do not suppress focus styles without an equivalent, clearly perceivable replacement.

Motion restraint (v1): [motion status: proposed, verification pending] keep motion subtle and functional, reflecting static-site behavior. Avoid autoplay, parallax-heavy movement, and long decorative animations in baseline experiences. For transitions, use short durations and support reduced motion by minimizing or removing non-essential animation when `prefers-reduced-motion` is enabled.

Source refs: `static-site:feature-grid`, `static-site:cta-section`

## Elevation & Depth
Depth cues should mirror observable static-site hierarchy and interaction patterns. Do not introduce a broad shadow system until curated source evidence shows repeated elevation behavior across static-site or current Storybook surfaces.

Prefer contrast, spacing, and border treatment before adding heavy shadows.

Source refs: `static-site:cards`

## Shapes
Shape language should align to static-site surfaces and current Storybook components. Use modest radii for controls and cards, and avoid sharp changes in radius scale without visible source evidence.

`radii.sm` is the initial proposed control radius for buttons and compact UI surfaces.

Source refs: `static-site:cards`, `storybook:button-primary`

## Components
Canonical component guidance comes from current Storybook product components only. Deprecated, legacy, or speculative components are excluded from v1 unless explicitly labeled as proposed and tied to curated source evidence.

`button-primary` is the initial proposed component entry because it links visible static-site brand direction with current Storybook component behavior.

Source refs: `storybook:button-primary`, `static-site:cta-section`

## Do's and Don'ts
- Do treat static-site visuals as final authority when sources conflict.
- Do use Storybook to describe current product component contracts and variants.
- Do use Figma selectively for logos and brand styling references only.
- Do keep short source IDs near non-obvious token, layout, and component decisions.
- Do preserve WCAG-oriented contrast and focus visibility guardrails for v1 defaults.
- Do keep baseline motion restrained and respect reduced-motion preferences.
- Don't inherit historical dark-background bias from Figma or legacy artifacts unless static-site evidence supports it.
- Don't ingest broad static-site, Storybook, or Figma exports into canonical tokens.
- Don't include deprecated or legacy Storybook components in v1.
- Don't remove or hide keyboard focus indicators without an accessible replacement.
- Don't introduce decorative motion patterns that exceed static-site behavior.
- Don't treat the following as in scope for v1: automated bulk ingestion from static-site, Storybook, or Figma exports.
- Don't restore legacy dark-theme patterns without explicit static-site evidence.
- Don't canonize deprecated or experimental Storybook components.
- Don't expand the token taxonomy beyond currently evidenced needs.

## Sources Mapping
- Use short source IDs in `design.md` entries and keep detailed mappings canonical in `sources/mapping.md`.
- Current IDs used in this file: `static-site:*`, `storybook:button-primary`, `figma:logo-brand`.
