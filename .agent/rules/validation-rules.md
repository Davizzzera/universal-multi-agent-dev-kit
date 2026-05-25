# Validation Rules

> Defines the mandatory validation requirements for all agent actions.

---

## Purpose

The Validation-First Principle is central to the Universal Multi-Agent Development Kit. This document outlines how agents must validate their work to ensure quality, prevent regressions, and build trust.

---

## Validation-First Principle

- Agents must not say something works unless they ran or documented a relevant validation.
- If a validation cannot be run (e.g., requires external credentials the agent lacks), the agent must explicitly state why and what the user must do to validate it.
- Validation output must include evidence (e.g., a command output snippet) or a manual checklist.

---

## Evidence-Based Completion

Every claim of completion must be backed by evidence. "I have created the file" is a claim. "I have created the file and here is the output of `ls` or a syntax check confirming it" provides evidence.

---

## Required Validation Levels

Validation must be applied across multiple domains depending on the task:

### 1. Markdown Validation
- Check for broken links.
- Ensure correct Markdown formatting (e.g., unclosed code blocks, malformed tables).
- Verify headings follow a logical hierarchy.

### 2. File Structure Validation
- Verify the file is created in the correct directory.
- Ensure naming conventions match the surrounding project.
- Check that required boilerplate or templates are included.

### 3. Build Validation
- If applicable, run a syntax check, compilation, or build step (e.g., `tsc --noEmit`, `npm run build`).

### 4. Test Validation
- Run existing relevant unit or integration tests.
- If new code is added, ensure tests are written and run successfully.

### 5. Security Validation
- Run static analysis or linter checks for common vulnerabilities.
- Confirm no secrets or credentials were accidentally hardcoded.

### 6. Documentation Validation
- Verify that changes in code are reflected in the corresponding documentation (README, API docs).

### 7. Manual Validation
- Provide a clear, step-by-step checklist for the user to verify features that cannot be automatically tested (e.g., UI visual changes).

---

## Final Verification Report Structure

When an agent completes a major task, it must output a validation summary conforming to the following structure:

- **Validation Summary:** Brief description of what was tested.
- **Commands Run:** Exact commands executed (e.g., `npm test`).
- **Results:** Pass/Fail status.
- **Evidence:** Snippets of logs or output proving success.
- **Pending User Actions:** Any manual checks required by the user.
