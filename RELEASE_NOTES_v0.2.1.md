# Universal Multi-Agent Dev Kit v0.2.1

**Release Type:** CI Validation Release
**Tag:** v0.2.1

## Release Summary

The v0.2.1 release adds automated Continuous Integration (CI) validation to the repository via GitHub Actions.
This ensures that every push and pull request to `main` is automatically verified using the same validation
pipeline that runs locally, providing an additional quality gate for the project.

## What Changed Since v0.2.0

### GitHub Actions Workflow
- Added `.github/workflows/verify.yml` — a complete CI workflow that runs on every push and pull request
  targeting the `main` branch, as well as on manual `workflow_dispatch` triggers.

### Validation Commands Used
The CI pipeline executes the same commands used for local validation:
1. `npm run generate:index` — Regenerates repository indexes.
2. `npm run verify` — Runs the full validation suite (structure, agents, skills, workflows, markdown, security).

### CI Trigger Details
The workflow is triggered on:
- **Push** to `main`.
- **Pull request** targeting `main`.
- **Manual dispatch** via `workflow_dispatch`.

### Runtime Details
- **Python 3.11** — Used for validation scripts.
- **Node.js 20** — Used for npm script execution.
- **Ubuntu Latest** — CI runner environment.

### CI Documentation
- Added `docs/ci-validation.md` explaining how CI works, common failure causes, and best practices.

### Artifact Upload
- Generated index files (`.agent/indexes/*.json`) are uploaded as CI artifacts for inspection.

## Known Remaining Warnings
- **Markdown Line Lengths:** The validation output reports warnings for lines exceeding 160 characters.
  These are confined to generated agent and workflow templates and are non-blocking (exit code 0).
  The CI pipeline and `npm run verify` both pass successfully.

## Known Limitations
- **CLI Installer:** Not yet implemented. Planned for a future release.
- **Adapters:** Antigravity remains the only officially implemented adapter.
  Adapters for Claude Code, Cursor, Codex, etc., are planned for future releases.

## Upgrade Notes from v0.2.0

No architectural changes or dependency additions were made. Simply pull the latest `main` branch.
The GitHub Actions workflow will activate automatically on your next push or pull request.

To verify locally:

```bash
npm run verify
```

If your environment has Python 3.10+ installed, you should see `[OK] ALL VALIDATIONS PASSED.`
