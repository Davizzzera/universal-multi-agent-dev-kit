# Documentation Rules

> Guidelines for writing, maintaining, and formatting documentation.

---

## Purpose

High-quality documentation is critical for a multi-agent system, as both humans and agents rely on it. This document establishes the standards for all documentation generated or maintained within the repository.

---

## Documentation Language

- **All repository documentation must be written in English.** This ensures universal readability for all agents and contributors.
- Translations or localized readmes may only be added if explicitly requested by the user, but the core repository content remains English.

---

## Truthfulness Requirement

- Documentation must precisely match the actual behavior and architecture of the repository.
- **No invented features:** Agents must not document features, APIs, or scripts that do not currently exist in the codebase.
- If documenting a planned feature, it must be explicitly marked as `(Planned)` or added to the roadmap.

---

## Markdown Style

- Use standard GitHub Flavored Markdown (GFM).
- **Headings:** Use `#` for the title, `##` for major sections, `###` for subsections.
- **Lists:** Use `-` or `*` consistently for bullet points.
- **Code Blocks:** Always specify the language for syntax highlighting (e.g., ````javascript ````).
- **TODOs:** Incomplete sections must be explicitly marked with `> **TODO:** [description]`. Do not leave placeholder text that looks like final content.

---

## Required Documentation

### 1. README Quality
The root `README.md` must contain:
- Project title and brief description.
- Status badges.
- Core concepts overview.
- Quick start/installation instructions.
- Architecture summary.

### 2. Architecture Documentation
Architecture documents (like `.agent/ARCHITECTURE.md`) must clearly explain the system's design, file ownership, and execution models.

### 3. Usage Documentation
Instructions on how to run, build, test, and use the project must be kept up to date.

### 4. Examples
- Examples must be realistic, syntax-error free, and safe.
- Do not use real credentials or sensitive data in examples.

---

## Changelog Rules

- Maintain the `CHANGELOG.md` using the [Keep a Changelog](https://keepachangelog.com/) format.
- Group changes under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security`.
- Unreleased changes should be tracked under an `[Unreleased]` heading.

---

## Documentation Review Checklist

Before finalizing documentation changes, agents must verify:
- [ ] Is it written in English?
- [ ] Does it accurately reflect the code?
- [ ] Are code examples correct and safe?
- [ ] Are all TODOs explicitly marked?
- [ ] Are there any broken Markdown links?
