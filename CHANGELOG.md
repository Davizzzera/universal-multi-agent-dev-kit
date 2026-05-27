# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added inline registry evidence rules.
- Added inline registry evidence template.
- Strengthened Execution Trace requirements.
- Required exact registry paths for workflows, packs, agents and skills.
- Required inline final response trace.
- Improved Antigravity adapter trace enforcement.

## [0.2.2] - 2026-05-25

### Added
- Added Execution Trace rules.
- Added Execution Trace template.
- Added Orchestration Plan template.
- Added Agent Activity Report template.
- Added documentation for agent visibility.
- Updated Antigravity adapter to require visible Execution Trace.
- Added distinction between selected agents, actually used agents and recommended agents.
- Added distinction between tool-visible subagents and orchestrated agent roles.
- Confirmed validation through `npm run verify`.

## [0.2.1] - 2026-05-25

### Added
- Added GitHub Actions workflow for repository validation (`.github/workflows/verify.yml`).
- Added CI validation on push to `main`.
- Added CI validation on pull requests to `main`.
- Added manual `workflow_dispatch` support.
- Added CI documentation in `docs/ci-validation.md`.
- Added generated index artifact upload for inspection.
- Confirmed local validation through `npm run verify`.
- Confirmed CI validation as part of the quality pipeline.

## [0.2.0] - 2026-05-25

### Fixed
- Fixed orchestration agent validation issues.
- Fixed missing required agent sections.
- Fixed documentation validation failure caused by unfinished filler wording.
- Fixed security scanner self-detection false positives.
- Improved defensive security scan reliability.
- Improved Antigravity troubleshooting example safety.
- Confirmed real Python validation through `npm run verify`.
- Regenerated repository indexes.
- Reduced Markdown long-line warnings from 239 to 210.
- Confirmed all validations pass with remaining warnings treated as non-blocking.

## [0.1.0] - 2026-05-25

### Added

- Initial repository structure with core directories.
- `.agent/` directory with `AGENTS.md`, `ARCHITECTURE.md`, and `INDEX.md`.
- Subdirectories for agents, skills, workflows, rules, memory, templates, scripts, and indexes.
- `adapters/` directory with placeholders for Antigravity, Claude Code, Cursor, Codex, and generic adapters.
- `packs/` directory with placeholders for web-app, landing-page, API, data-bi, automation, ai-agent, n8n, ecommerce, and enterprise packs.
- `docs/` directory with initial documentation files.
- `README.md` with project overview, core concepts, and architecture summary.
- `LICENSE` (MIT).
- `CONTRIBUTING.md` with contribution guidelines.
- `package.json` with project metadata and validation scripts.
- `.gitignore` with professional exclusion rules.
- `.gitkeep` files in empty directories to preserve structure.
- Added global rules (`.agent/rules/`).
- Added reusable templates (`.agent/templates/`).
- Added file ownership model.
- Added handoff and output contract standards.
- Added core orchestration agents.
- Added orchestration agent documentation.
- Added orchestration lifecycle documentation.
- Added agent coordination model.
- Added core specialist agent categories.
- Added product, architecture, frontend, backend, database, AI automation, QA, security, DevOps, documentation and marketing agents.
- Added specialist agent documentation.
- Added specialist agent category model.
- Added core skills library.
- Added 18 skill categories.
- Added 104 reusable skills.
- Added skill category documentation.
- Added agent-to-skill execution model.
- Added operational workflows layer.
- Added 18 reusable workflows.
- Added workflow documentation.
- Added workflow-to-agent and workflow-to-skill execution model.
- Added validation-first workflow standards.
- Added validation scripts.
- Added generated repository indexes.
- Added structure validation.
- Added agent, skill and workflow validation.
- Added Markdown validation.
- Added basic defensive security checks.
- Added package scripts for validation.
- Added Antigravity adapter.
- Added Antigravity AGENTS.md entrypoint.
- Added Antigravity installation and usage documentation.
- Added Antigravity prompt examples.
- Added Antigravity troubleshooting guide.
- Added adapter manifest.
- Added 9 project packs for domain-specific agent configuration.
- Added web-app-pack, landing-page-pack, api-pack, data-bi-pack, automation-pack, ai-agent-pack, n8n-pack, ecommerce-pack, enterprise-pack.
- Updated INDEX.md, ARCHITECTURE.md, and AGENTS.md to include packs.
- Updated examples.md with pack usage scenarios.
