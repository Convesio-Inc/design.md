---
version: "alpha"
name: "Convesio Product Design System"
description: "Product-level DESIGN.md with Storybook as the sole source of truth."
colors:
  primary: "#FF6A5B"
  secondary: "#0D2743"
  tertiary: "#3459E6"
  neutral: "#F2F5F7"
  surface: "#FFFFFF"
  on-surface: "#212529"
  on-surface-secondary: "#495057"
  border: "#DAD9DE"
  border-light: "#E5E7EB"
  success: "#2EBA55"
  info: "#527DEB"
  warning: "#F8BA1D"
  error: "#F65454"
  primary-tint: "#FFE9E7"
  card-surface: "#F8F9FA"
typography:
  heading-lg:
    fontFamily: "Inter"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "1"
    letterSpacing: "-0.02em"
  heading:
    fontFamily: "Inter"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: "1"
  body-md:
    fontFamily: "Inter"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: "1.5"
  body-lg:
    fontFamily: "Inter"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.5"
  body-sm:
    fontFamily: "Inter"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "1.5"
  label:
    fontFamily: "Inter"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: "1.4"
  caption:
    fontFamily: "Inter"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "1.4"
rounded:
  sm: "4px"
  md: "6px"
  lg: "8px"
  full: "999px"
spacing:
  xs: "0.25rem"
  sm: "8px"
  form-label: "0.2rem"
  md: "16px"
  button-y: "0.45rem"
  button-x: "1rem"
  input-y: "9px"
  input-x: "13px"
  lg: "24px"
  navbar-y: "20px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-secondary-hover:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.button-y}"
  button-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0px"
  badge-primary:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  badge-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  badge-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  badge-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  alert-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  alert-primary:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  alert-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  alert-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  alert-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  card-default:
    backgroundColor: "{colors.card-surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  input-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.input-y}"
---

## Overview
This file is the product-level `design.md` for Convesio product UI work. Storybook is the sole source of truth for tokens, component behavior, and variant contracts in this file.

The root brand `design.md` may provide context, but this product file governs implementation decisions for product surfaces whenever there is any conflict.

Source refs: `storybook:src/stories/DesignSystem.stories.jsx`, `storybook:src/styles/tokens.css`, `storybook:tokens/design-tokens.json`

## Colors
Color roles are product-defined from Storybook component usage and product UI states. Product tokens prioritize legibility, consistency across interactive states, and alignment to current Storybook stories.

Source refs: `storybook:tokens/design-tokens.json#color`, `storybook:src/styles/tokens.css`

## Typography
Typography levels are product-oriented and reflect Storybook component contracts for labels, body copy, and headline usage in product contexts.

Source refs: `storybook:tokens/design-tokens.json#typography`, `storybook:src/styles/tokens.css`

## Layout
Layout spacing is guided by product component spacing contracts in Storybook, emphasizing predictable density and reusable spacing steps across forms, cards, and lists.

Source refs: `storybook:tokens/design-tokens.json#spacing`, `storybook:src/styles/tokens.css`

## Elevation & Depth
Use restrained depth treatment and prioritize hierarchy through spacing, border, and contrast first. Any elevation usage should mirror Storybook component variants for cards, popovers, or surfaced controls.

Source refs: `storybook:tokens/design-tokens.json#boxShadow`, `storybook:src/stories/DesignSystem.stories.jsx#Cards`

## Shapes
Corner radius usage follows Storybook components: small and medium radii for controls/surfaces, and full radius for pill-style interactive elements.

Source refs: `storybook:tokens/design-tokens.json#borderRadius`, `storybook:src/stories/DesignSystem.stories.jsx#Buttons`

## Components
Component tokens in this file represent current product-level Storybook contracts only. Add variants as separate component keys and keep naming consistent with Storybook story/state naming.

Source refs: `storybook:src/stories/DesignSystem.stories.jsx#Buttons`, `storybook:src/stories/DesignSystem.stories.jsx#Badges`, `storybook:src/stories/DesignSystem.stories.jsx#Cards`, `storybook:src/stories/DesignSystem.stories.jsx#Alerts`

## Do's and Don'ts
- Do treat Storybook as the sole authority for product token and component decisions.
- Do add or update component variants only when represented in current Storybook stories.
- Do keep component naming aligned with Storybook state/variant naming.
- Don't import brand-only or marketing-only style overrides into this file.
- Don't add tokens/components not represented by current product Storybook usage.
- Don't allow conflicts with Storybook to persist; reconcile this file to Storybook.
