# CI Validation

This document explains the Continuous Integration (CI) process used by the Universal Multi-Agent Development Kit to ensure repository integrity.

## What it Does

The repository uses GitHub Actions to run the complete automated validation pipeline every time code is pushed. This ensures that any changes—whether made by humans or AI agents—strictly adhere to the required architectures, agent contracts, and security rules.

## When it Runs

The workflow `.github/workflows/verify.yml` is triggered automatically on:
- Any `push` to the `main` branch.
- Any `pull_request` targeting the `main` branch.
- Manually via `workflow_dispatch`.

## Runtime Environment

To ensure a stable and consistent check, the CI environment uses:
- **Ubuntu Latest**
- **Python 3.11**
- **Node.js 20**

## Commands Executed

The CI pipeline runs the exact same commands used for local validation:

1. `npm run generate:index` - Regenerates internal indexes to ensure they are up to date.
2. `npm run verify` - Executes the full suite of Python validation scripts.

No external Python dependencies (e.g., via `pip`) are required. The entire validation suite relies exclusively on the Python Standard Library.

## Reading CI Failures

If the CI pipeline fails, you will see a red X on your GitHub commit or PR. Check the GitHub Actions logs for specific error messages.

### Common Failure Causes

- **Agent Contract Validation Failure:** An agent file is missing mandatory sections (like `# Responsibilities` or `# Boundaries`) or frontmatter properties.
- **Skill/Workflow Contract Validation Failure:** A skill or workflow file lacks required structured metadata.
- **Markdown Validation Failure:** A document contains prohibited filler phrases, lacks required sections, or is fundamentally malformed.
- **Security Check Failure:** The defensive scanner detected a hardcoded secret, a realistic-looking credential, or prohibited terms.
- **Index Generation Failure:** The indexes are corrupt or inaccessible.

## Warnings and Non-Blocking Issues

The validation scripts may emit warnings (e.g., for Markdown lines exceeding 160 characters). **Remaining Markdown long-line warnings are non-blocking.** If the final log output displays `[OK] ALL VALIDATIONS PASSED.` and the script exits with code `0`, the CI run will succeed.

## What NOT to Do

To maintain the safety and reliability of this kit:
- **Do not disable validation to make CI pass.** Fix the root cause instead.
- **Do not remove security checks casually.** If a false positive occurs, explicitly ignore it locally within the scanner or use safer terminology in your files.
- **Do not force-push release tags.** Treat release tags as immutable.
- **Do not upload secrets as artifacts.** The CI workflow explicitly uploads generated indexes only. Never modify it to upload logs containing sensitive tokens.
