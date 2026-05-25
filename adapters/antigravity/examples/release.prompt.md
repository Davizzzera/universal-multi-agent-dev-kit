# Release Prompt

**Purpose:** Use this prompt to prepare a project release, including changelog updates, version bumps, and final validation.

---

**Copy and paste the following into Antigravity:**

```text
Goal: Prepare the project for a new release [INSERT VERSION HERE, e.g., v1.0.0].
Workflow: `release`

Scope: `CHANGELOG.md`, `package.json` (or equivalent version files), and release documentation.
Constraints:
1. Ensure the `devops-engineer` and `documentation-specialist` are involved.
2. Review recent commits and update the CHANGELOG.md following Keep a Changelog format.
3. Bump the version in package manifests.
Validation: Run a full verify check to ensure the release candidate is stable.
Commit: If successful, commit with "chore: release [VERSION]" and push. DO NOT create git tags unless explicitly asked.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```
