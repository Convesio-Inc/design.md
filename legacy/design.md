---
version: "alpha"
name: "Convesio Legacy Brand System (Figma)"
description: "Legacy DESIGN.md sourced only from the historical Figma brand style guide."
colors:
  primary: "#0D2743"
  secondary: "#005EC4"
  tertiary: "#FF6A5B"
  neutral: "#FFFFFF"
  surface: "#FFFFFF"
  surface-alt: "#F2F5F7"
  on-surface: "#0B111E"
  on-surface-secondary: "#3C4A5B"
  border: "#E5EBEF"
  success: "#2BB673"
  warning: "#F5A623"
  error: "#FF4040"
typography:
  display:
    fontFamily: "Inter"
    fontSize: "72px"
    fontWeight: 700
    lineHeight: "1.05"
    letterSpacing: "-0.03em"
  heading-lg:
    fontFamily: "Inter"
    fontSize: "40px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.02em"
  heading-md:
    fontFamily: "Inter"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.02em"
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
  label-sm:
    fontFamily: "Inter"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: "16px"
    letterSpacing: "0.16em"
rounded:
  sm: "6px"
  md: "10px"
  lg: "16px"
  full: "999px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "12px"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "12px"
  card-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---

## Overview
This file is a legacy brand snapshot sourced from the historical Convesio Figma brand style guide only. It is intentionally isolated from static-site and Storybook authority models.

Use this file for legacy visual reconstruction, historical comparison, and migration reference. It should not override current brand (`design.md`) or product (`products/design.md`) authority files.

Source refs: `figma:legacy-brand-guide`, `figma:legacy-logo-style`, `figma:legacy-type-scale`

## Colors
Color roles reflect the historical Figma brand guide palette, including navy-led surfaces, coral accent treatment, and legacy semantic states.

Source refs: `figma:legacy-brand-colors`

## Typography
Typography follows the legacy Figma scale and Inter-based hierarchy used in historical brand assets and marketing layouts.

Source refs: `figma:legacy-type-scale`

## Layout
Layout guidance reflects legacy Figma spacing rhythm and section density patterns. Prefer preserving historical proportional feel over introducing modern spacing overrides in this file.

Source refs: `figma:legacy-layout-rhythm`

## Elevation & Depth
Legacy depth treatment should remain restrained and style-consistent with historical Figma visuals. Favor contrast and spacing before introducing heavy elevation.

Source refs: `figma:legacy-surface-depth`

## Shapes
Shape language uses soft rounded controls/cards and pill-style primary actions as represented in historical Figma assets.

Source refs: `figma:legacy-shape-language`

## Components
Component tokens represent legacy brand component appearance only. Keep variants aligned to what is explicitly present in the legacy Figma guide.

Source refs: `figma:legacy-button-primary`, `figma:legacy-card-default`

## Do's and Don'ts
- Do treat Figma legacy artifacts as the sole authority in this file.
- Do preserve historical visual intent when using this file for migration reference.
- Don't merge static-site or Storybook decisions into this legacy file.
- Don't use this file as the default source for new product implementation.
- Don't delete legacy mappings without first reconciling migration impact.
