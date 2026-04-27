---
version: "alpha"
name: "Convesio Design System"
description: "Canonical visual and component guidance with curated provenance."
colors:
  primary: "#0D2743"
  secondary: "#2D85D8"
  tertiary: "#FF6A5B"
  neutral: "#F2F5F7"
  surface: "#FFFFFF"
  surface-alt: "#FAFAFA"
  surface-dark: "#0D2743"
  surface-dark-deep: "#0B111E"
  on-surface: "#1A1A1A"
  on-surface-secondary: "#4A4A4A"
  on-surface-tertiary: "#7A7A7A"
  on-surface-inverse: "#FFFFFF"
  border: "#ECECEC"
  border-strong: "#C3C9CE"
  border-1: "#E5EBEF"
  border-2: "#D9D9D9"
  success: "#2BB673"
  warning: "#F5A623"
  error: "#FF4040"
  link: "#2D85D8"
  link-hover: "#005EC4"
  link-dark: "#FFFFFF"
  link-aa: "#005EC4"
  link-aa-hover: "#0C2B4D"
  tertiary-hover: "#F89A8F"
  tertiary-aa: "#C24135"
typography:
  display-lg:
    fontFamily: "Inter"
    fontSize: "72px"
    fontWeight: 700
    lineHeight: "1.05"
    letterSpacing: "-0.03em"
  display-md:
    fontFamily: "Inter"
    fontSize: "40px"
    fontWeight: 800
    lineHeight: "1.05"
    letterSpacing: "-0.02em"
  headline-lg:
    fontFamily: "Inter"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.02em"
  headline-md:
    fontFamily: "Inter"
    fontSize: "25px"
    fontWeight: 600
    lineHeight: "1.2"
    letterSpacing: "0em"
  title-lg:
    fontFamily: "Inter"
    fontSize: "21px"
    fontWeight: 600
    lineHeight: "1.2"
  title-md:
    fontFamily: "Inter"
    fontSize: "18px"
    fontWeight: 500
    lineHeight: "1.4"
  body-lg:
    fontFamily: "Inter"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: "1.55"
  body-md:
    fontFamily: "Inter"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.55"
  body-sm:
    fontFamily: "Inter"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: "1.4"
  label-md:
    fontFamily: "Inter"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: "1.2"
    letterSpacing: "0.16em"
  label-sm:
    fontFamily: "Inter"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: "16px"
    letterSpacing: "0.18em"
  caption:
    fontFamily: "Inter"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: "16px"
    letterSpacing: "0.04em"
  h1:
    fontFamily: "Inter"
    fontSize: "40px"
    fontWeight: 800
    lineHeight: "1.05"
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Inter"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.02em"
  h3:
    fontFamily: "Inter"
    fontSize: "25px"
    fontWeight: 600
    lineHeight: "1.2"
  h4:
    fontFamily: "Inter"
    fontSize: "21px"
    fontWeight: 600
    lineHeight: "1.2"
  h5:
    fontFamily: "Inter"
    fontSize: "18px"
    fontWeight: 500
    lineHeight: "1.4"
rounded:
  xs: "4px"
  sm: "6px"
  md: "10px"
  lg: "16px"
  xl: "24px"
  full: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section-md: "72px"
  section-lg: "96px"
  section-xl: "120px"
  container-sm: "980px"
  container-lg: "1240px"
  grid-gap-sm: "20px"
  grid-gap-md: "24px"
  grid-gap-xl: "80px"
shadows:
  xs: "0 1px 2px rgba(13,39,67,0.06)"
  sm: "0 2px 6px rgba(13,39,67,0.08)"
  md: "0 8px 20px rgba(13,39,67,0.10)"
  lg: "0 20px 48px rgba(13,39,67,0.14)"
  inset: "inset 0 1px 0 rgba(255,255,255,0.06)"
motion:
  ease-out: "cubic-bezier(.2,.6,.2,1)"
  ease-in-out: "cubic-bezier(.4,0,.2,1)"
  dur-fast: "120ms"
  dur-base: "200ms"
  dur-slow: "360ms"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.lg}"
    padding: "14px"
  button-primary-hover:
    backgroundColor: "{colors.link-aa-hover}"
    textColor: "{colors.surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.lg}"
    padding: "14px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.lg}"
    padding: "14px"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.lg}"
    padding: "14px"
  link-inline-aa:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.link-aa}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  link-inline-aa-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.link-aa-hover}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  link-dark-inline:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.link-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  link-dark-inline-muted:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-inverse}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  nav-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  nav-link-muted:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  header-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.lg}"
    padding: "14px"
  hero-kicker:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-secondary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "8px"
  hero-status-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  eyebrow-aa:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.tertiary-aa}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "0px"
  card-light:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "28px"
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-inverse}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  section-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-inverse}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.section-lg}"
---

## Overview
This file is the canonical brand-level `design.md` reference for Convesio design decisions. Static-site visuals are the primary authority for overall look, feel, layout rhythm, color usage, imagery direction, and visual conflict resolution.

Future UI generation should favor the lighter static-site direction and avoid inheriting legacy dark-background bias unless that treatment is directly evidenced in the static site.

Canonical authority model:
- Static site is canonical for page-level visual direction and conflict resolution.
- Figma is allowed only for logo and icon assets.
- When base token declarations and rendered page usage diverge, follow rendered page usage as the canonical mapping.
- Source-specific capture rules live in each source README; shared authority decisions are defined here.

Source refs: `static-site:home-hero`, `static-site:page-surface`, `figma:logo-brand`, `figma:icon-set`

## Colors
Color roles are derived from static-site usage only.

Background treatments from the static site are part of the canonical palette: use `surface` and `surface-alt` for light backgrounds, `surface-dark`/`surface-dark-deep` for dark sections, and `on-surface-inverse` for text on dark backgrounds. Use `tertiary` for CTA emphasis and `primary` for strong navy anchors.

Static-source mapping note: dark navy (`primary`) is the canonical primary button fill for `new/`. Coral tokens (`tertiary`, `tertiary-hover`) are accent/text treatments only and should not be used as section backgrounds.

Accessibility guardrails (v1): [contrast status: proposed, not yet verified end-to-end] body text and essential UI text should target WCAG AA contrast (4.5:1 minimum against its surface). Large text (18px regular or 14px bold and above) should not drop below 3:1. Non-text interactive UI indicators such as borders, icons, and controls should maintain at least 3:1 contrast against adjacent surfaces.

Canonical accessibility defaults:
- Use `link-inline-aa` / `link-inline-aa-hover` for body-text link treatment.
- Use `eyebrow-aa` for eyebrow/kicker text on light surfaces.
- Use `link-dark-inline` (or muted dark-link treatment) for links in dark sections; avoid coral links on dark backgrounds unless explicitly called out as accent content.

Source refs: `static-site:navigation`, `static-site:page-surface`, `static-site:body-copy`

## Typography
Typography should preserve the static site's reading rhythm and approachable product-marketing tone.

`body-md` is the baseline text role for product UI copy and component labels until verified source captures justify a fuller type scale.

Source refs: `static-site:body-copy`

## Layout
Spacing and composition follow static-site page patterns: clear section rhythm, generous breathing room, and reusable grid spacing that can translate into product screens without becoming dense or dark by default.

Use `container-lg` (`1240px`) and `container-sm` (`980px`) for content width constraints. Use section spacing tokens (`section-md`, `section-lg`, `section-xl`) for vertical rhythm and `grid-gap-sm`/`grid-gap-md`/`grid-gap-xl` for composition-level spacing.

Header/hero layout pattern from static upload:
- Top navigation uses a wide horizontal container with lightweight inline nav links and a compact dark primary CTA at top-right.
- Hero uses a left-heavy headline/content column with a right status/metrics panel card.
- Keep the hero backdrop predominantly light/neutral; avoid coral section fills.

Focus visibility (v1): [focus status: proposed, partially verified] all keyboard-focusable controls must render a clearly visible focus indicator that is not color-only and remains present against light surfaces; prefer an outline or ring with at least 3:1 contrast from adjacent colors. Do not suppress focus styles without an equivalent, clearly perceivable replacement.

Motion restraint (v1): [motion status: proposed, verification pending] keep motion subtle and functional, reflecting static-site behavior. Avoid autoplay, parallax-heavy movement, and long decorative animations in baseline experiences. For transitions, use short durations and support reduced motion by minimizing or removing non-essential animation when `prefers-reduced-motion` is enabled.

Use `motion.ease-out`/`motion.ease-in-out` with `motion.dur-fast`/`motion.dur-base`/`motion.dur-slow` as default timing primitives.

Source refs: `static-site:feature-grid`, `static-site:cta-section`

## Elevation & Depth
Depth cues should mirror observable static-site hierarchy and interaction patterns. Do not introduce a broad shadow system until curated source evidence shows repeated elevation behavior across static-site or current Storybook surfaces.

Prefer contrast, spacing, and border treatment before adding heavy shadows. When shadows are needed, match static-site tiers: subtle (`shadows.xs`/`shadows.sm`) for light cards, moderate (`shadows.md`) for elevated content blocks, and restrained large (`shadows.lg`) only for hero-level emphasis. Use `shadows.inset` for gentle highlight layering on dark surfaces where appropriate.

Source refs: `static-site:cards`

## Shapes
Shape language should align to static-site surfaces. Use modest radii for controls and cards, and avoid sharp changes in radius scale without visible source evidence.

`rounded.sm` is the initial control radius for buttons and compact UI surfaces.

Source refs: `static-site:cards`

## Components
Canonical component guidance in this brand file is grounded in static-site component patterns. Figma can supply logo/icon assets only. Product component contracts live in `products/design.md`.

Core component treatments are now grounded in static-site evidence:
- `button-primary` and `button-primary-hover` map to dark primary CTA treatment.
- `button-secondary` and `button-secondary-hover` map to light/outlined secondary treatment with dark hover inversion.
- `link-inline-aa` and `link-inline-aa-hover` are canonical for inline links in body-text contexts.
- `link-dark-inline` and muted dark-link treatment are canonical for navigation/footer links on dark surfaces.
- `eyebrow-aa` is canonical for eyebrow/kicker text on light backgrounds.
- Brighter coral treatments are accent-only and should not be used as section background fills.
- `card-light` and `card-dark` map to static-site surface cards in light and dark sections.
- `section-dark` maps to dark background section blocks with inverse typography.
- `nav-link`, `nav-link-muted`, and `header-cta` represent the top header/navigation pattern shown in the static upload.
- `hero-kicker` and `hero-status-panel` represent the front-page hero badge + right-side status panel pattern.

Logo and icon asset mapping (explicit):
- **Primary logo (light surfaces):** `assets/convesio-logo.svg` (provided from Figma export package `Logo.svg.zip`).
- **Inverse logo (dark surfaces):** `assets/convesio-logo-white.svg` (fetched from `https://convesio.com/wp-content/uploads/2025/06/convesio-logo-white.svg`).
- **Icon set source:** `assets/host-menu-icon.svg`, `assets/convert-menu-icon.svg`, `assets/pay-menu-icon.svg`, `assets/service-menu-icon.svg` (fetched from `convesio.com`).
- **Favicon/source mark:** `assets/convesio-favicon.png` (fetched from `https://convesio.com/wp-content/uploads/2024/05/convesio-favicon.png`).
- **Repository note:** dark-surface logo and core header icons are now stored locally under `assets/`.
- **Usage rule:** use primary logo on light backgrounds and inverse logo on dark backgrounds; do not recolor logos beyond approved brand assets.

Card styling note: light cards use white surfaces, `16px` corners, and `28px` inner padding with subtle hairline borders (`#ECECEC`) as seen in the static page card grid.

Where the static site uses border-driven ghost styles, explicit borders, focus rings, and shadow nuances are captured in prose guidance until component property support expands.

Source refs: `static-site:cta-section`, `figma:logo-brand`, `figma:icon-set`

## Do's and Don'ts
- Do treat static-site visuals as final authority when sources conflict.
- Do use Figma only for logo and icon assets.
- Do prefer rendered page usage over generic/base token defaults when they differ.
- Do keep short source IDs near non-obvious token, layout, and component decisions.
- Do preserve WCAG-oriented contrast and focus visibility guardrails for v1 defaults.
- Do keep baseline motion restrained and respect reduced-motion preferences.
- Don't inherit historical dark-theme bias unless explicit static-site evidence supports it.
- Don't ingest broad exports from static-site or Storybook into canonical tokens.
- Don't use Figma for layout, spacing, or section background decisions in this file.
- Don't canonize deprecated or experimental Storybook components in v1.
- Don't remove keyboard focus indicators without an accessible replacement.
- Don't introduce decorative motion patterns that exceed static-site behavior.
- Don't expand the token taxonomy beyond currently evidenced needs.
- Don't use coral tokens as section background colors.
- Don't use Storybook as a source in this top-level brand file; keep product-level Storybook sourcing in `products/design.md`.

## Sources Mapping
- Use short source IDs in `design.md` entries and keep detailed mappings canonical in `sources/mapping.md`.
- Current IDs used in this file: `static-site:*`, `figma:logo-brand`, `figma:icon-set`.
