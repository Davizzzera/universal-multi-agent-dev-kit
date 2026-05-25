# Roadmap

> Development roadmap for the Universal Multi-Agent Development Kit.

---

## v0.1.0 — Repository Foundation

**Status:** 🟡 In Progress

- [x] Create repository structure.
- [x] Create core directories (`.agent/`, `adapters/`, `packs/`, `docs/`).
- [x] Create root files (`README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `package.json`, `.gitignore`).
- [x] Create `.agent/AGENTS.md` — Global agent entrypoint.
- [x] Create `.agent/ARCHITECTURE.md` — Architecture document.
- [x] Create `.agent/INDEX.md` — Human-readable index.
- [x] Create initial documentation in `docs/`.
- [x] Create `.gitkeep` files in empty directories.

---

## v0.2.0 — Core Agents

**Status:** ⬜ Planned

- [ ] Implement Universal Orchestrator agent.
- [ ] Implement Context Reader agent.
- [ ] Implement Task Router agent.
- [ ] Implement Code Writer agent.
- [ ] Implement Code Reviewer agent.
- [ ] Implement Documentation Agent.
- [ ] Implement QA Agent.
- [ ] Implement Security Agent.
- [ ] Implement Final Reviewer agent.
- [ ] Define global rules in `.agent/rules/`.
- [ ] Create agent templates in `.agent/templates/`.

---

## v0.3.0 — Core Skills

**Status:** ⬜ Planned

- [ ] Implement file reading skills.
- [ ] Implement file writing skills.
- [ ] Implement analysis skills.
- [ ] Implement validation skills.
- [ ] Implement documentation skills.
- [ ] Implement refactoring skills.
- [ ] Create skill templates in `.agent/templates/`.
- [ ] Update agent definitions with skill assignments.

---

## v0.4.0 — Workflows and Validation Scripts

**Status:** ⬜ Planned

- [ ] Implement Feature Implementation workflow.
- [ ] Implement Bug Fix workflow.
- [ ] Implement Code Review workflow.
- [ ] Implement Full Validation workflow.
- [ ] Implement `verify_all.py` validation script.
- [ ] Implement `generate_index.py` index generation script.
- [ ] Create workflow templates in `.agent/templates/`.
- [ ] Generate initial indexes in `.agent/indexes/`.

---

## v0.5.0 — Antigravity Adapter

**Status:** ⬜ Planned

- [ ] Implement Antigravity adapter configuration.
- [ ] Create Antigravity entry point.
- [ ] Map kit concepts to Antigravity capabilities.
- [ ] Write Antigravity setup documentation.
- [ ] Test integration with Antigravity.
- [ ] Begin work on generic adapter template.

---

## v1.0.0 — Stable Release

**Status:** ⬜ Planned

- [ ] Complete all core agents, skills, and workflows.
- [ ] Complete all validation scripts.
- [ ] Complete Antigravity adapter.
- [ ] Complete generic adapter template.
- [ ] Full documentation review and update.
- [ ] Implement at least one project pack.
- [ ] Comprehensive testing and validation.
- [ ] Performance optimization.
- [ ] Community contribution guidelines finalized.
- [ ] Public release.

---

## Future Considerations

- Additional adapters (Claude Code, Cursor, Codex).
- Additional project packs.
- CLI tool for kit installation and configuration.
- Plugin system for community extensions.
- Metrics and reporting dashboard.
- CI/CD integration support.
