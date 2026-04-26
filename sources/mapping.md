# Sources Mapping

Use short source IDs in `design.md`, and map them here to curated evidence locations, capture context, and rationale. Keep this file concise; it should point to selected evidence, not become a bulk source dump.

## Static Site
- **id:** `static-site:home-hero`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `home hero page region`
  - **decision_link:** `Overview / Canonical Authority Model (page-level visual direction)`
  - **authority_fit:** `confirmed` (static-site is canonical for visual direction and conflict resolution)
  - **conflict_notes:** `No direct conflict recorded; defer to static-site if later conflicts arise.`
- **id:** `static-site:navigation`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `navigation region and interactive states`
  - **decision_link:** `colors.primary; Colors section (navigation color and interaction cues)`
  - **authority_fit:** `confirmed` (static-site is canonical for page-level visual usage)
  - **conflict_notes:** `If token use conflicts with Storybook visuals, static-site wins for visual direction.`
- **id:** `static-site:page-surface`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `default page background/surface treatment`
  - **decision_link:** `colors.surface; Colors section (default light UI baseline)`
  - **authority_fit:** `confirmed` (static-site is canonical for overall surface direction)
  - **conflict_notes:** `Reject legacy dark-bias inheritance unless static-site evidence explicitly supports it.`
- **id:** `static-site:body-copy`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `body text rhythm and readable contrast`
  - **decision_link:** `colors.on-surface; typography.body-md`
  - **authority_fit:** `confirmed` (static-site guides global typography rhythm and copy contrast)
  - **conflict_notes:** `Storybook may inform component contracts, not broad type scale authority.`
- **id:** `static-site:feature-grid`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `feature grid spacing and layout rhythm`
  - **decision_link:** `spacing.md; Layout section`
  - **authority_fit:** `confirmed` (static-site is canonical for page composition and spacing rhythm)
  - **conflict_notes:** `No direct conflict recorded; prioritize static-site if denser alternatives appear.`
- **id:** `static-site:cta-section`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `call-to-action block and primary emphasis treatment`
  - **decision_link:** `Components section (button-primary context); Layout source refs`
  - **authority_fit:** `confirmed` (static-site governs page-level emphasis and CTA visual direction)
  - **conflict_notes:** `If CTA visuals diverge from component internals, static-site controls page-level emphasis while Storybook controls behavior contract.`
- **id:** `static-site:cards`
  - **evidence_path:** `sources/static-site/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `card/surface shape and depth hierarchy cues`
  - **decision_link:** `radii.sm; Shapes section; Elevation & Depth section`
  - **authority_fit:** `confirmed` (static-site is canonical for surface hierarchy and shape direction)
  - **conflict_notes:** `Prefer contrast/spacing/border over heavy shadows unless repeated elevation evidence appears.`

## Storybook
- **id:** `storybook:button-primary`
  - **evidence_path:** `sources/storybook/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `current primary button component, variants, and interaction behavior`
  - **decision_link:** `components.button-primary; typography.body-md; radii.sm`
  - **authority_fit:** `confirmed` (Storybook is canonical for current component behavior/variant contract)
  - **conflict_notes:** `If visual styling conflicts with static-site direction, static-site wins visual conflict while Storybook remains behavior authority.`

## Figma
- **id:** `figma:logo-brand`
  - **evidence_path:** `sources/figma/README.md`
  - **captured_at:** `2026-04-26`
  - **owner:** `@tbd-owner` (provisional)
  - **scope:** `logo artwork and brand styling accents only`
  - **decision_link:** `colors.primary (brand cue only); Canonical Authority Model (selective Figma use)`
  - **authority_fit:** `confirmed` (Figma is selective for logos/brand styling and not page-level visual authority)
  - **conflict_notes:** `Figma cues do not override static-site page direction or Storybook component behavior contracts.`

## Mapping Rules
- Static-site references resolve visual conflicts first.
- Storybook references describe current product components only.
- Figma references are selective and limited to logos or brand styling.
- Legacy dark-bias inheritance is rejected unless static-site evidence explicitly supports it.

## Curated Evidence Checklist
Every new mapping entry and every `proposed -> validated -> canonical` promotion must satisfy this checklist:
- **ID format:** Use `source:artifact` short IDs (for example `static-site:home-hero`).
- **Evidence location:** Link to a concrete curated note or capture location in the source README.
- **Captured-at metadata:** Record capture date (`YYYY-MM-DD`) and actor/owner.
- **Scope metadata:** Name the page region, component, or pattern represented.
- **Decision metadata:** State what decision the evidence supports (token/component/lifecycle change).
- **Authority fit:** Confirm the evidence follows the canonical authority model in `../design.md`.
- **Conflict note:** If sources conflict, record why the chosen authority won.

Entries missing required metadata should not be used to advance lifecycle status.
