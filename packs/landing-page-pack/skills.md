# Landing Page Pack: Skills

## Purpose
This document defines the core procedures and techniques required to build high-converting landing pages.

## Core Skills
| Skill | Usage |
|-------|-------|
| `landing-page-structure` | Defining sections (Hero, Features, Testimonials, CTA) |
| `landing-page-copy` | Writing persuasive content |
| `hero-copywriting` | Crafting strong headlines |
| `cta-copywriting` | Designing actionable buttons |
| `seo-title-description` | Optimizing meta tags |
| `conversion-audit` | Reviewing user flow |
| `tone-of-voice-definition` | Aligning copy with brand |
| `ux-flow-audit` | Checking user journey |
| `visual-consistency-review` | Ensuring brand alignment |
| `responsive-layout-audit` | Checking mobile views |
| `accessibility-contrast-check` | Ensuring readability |
| `build-validation` | Running static generators |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Planning phase: Load `landing-page-structure`, `tone-of-voice-definition`.
- Copy phase: Load `landing-page-copy`, `hero-copywriting`, `cta-copywriting`, `seo-title-description`.
- Frontend phase: Load `visual-consistency-review`.
- QA phase: Load `responsive-layout-audit`, `accessibility-contrast-check`, `conversion-audit`.

## Progressive Loading Notes
Do not load copywriting skills if the task is only a CSS bug fix.

## Validation Notes
`responsive-layout-audit` and `accessibility-contrast-check` must be completed before delivery.
