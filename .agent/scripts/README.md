# Validation Scripts

> These scripts make the Universal Multi-Agent Development Kit self-checking and validation-first.

---

## Purpose

The validation scripts ensure that the repository maintains its structure, agents adhere to their contracts, skills are properly documented, workflows are consistent, and no accidental secrets are pushed.

These scripts are **defensive** and **non-destructive**. They read repository files but do not modify them (except for generating indexes).

## Technology

All scripts use the **Python Standard Library**. They are compatible with Python 3.10+ and do not require `pip install` or external packages.

## How to Run

You can run the full validation pipeline directly with Python:
```bash
python .agent/scripts/verify_all.py
```

Or just generate the indexes:
```bash
python .agent/scripts/generate_index.py
```

If you prefer using `npm` (if you have Node.js installed), you can use the package.json shortcuts:
```bash
npm run verify
npm run generate:index
```

## Available Scripts

| Script | Purpose |
|--------|---------|
| `common.py` | Shared helper functions for parsing Markdown, Frontmatter, and JSON generation. |
| `validate_structure.py` | Validates that all required core files and directories exist in the repository. |
| `validate_agents.py` | Validates that all 60 agent files have correct frontmatter and required sections. |
| `validate_skills.py` | Validates that all 104 skill files have correct frontmatter and required sections. |
| `validate_workflows.py` | Validates that all 18 workflow files have correct frontmatter and required sections. |
| `validate_markdown.py` | Performs lightweight checks on Markdown files (conflict markers, empty files, placeholders). |
| `security_check.py` | Defensive scan for accidental secrets and unsafe content indicators. |
| `generate_index.py` | Generates JSON indexes of agents, skills, and workflows into `.agent/indexes/`. |
| `verify_all.py` | Runs all the above scripts sequentially and summarizes the results. |

## Expected Exit Codes

- `0`: Success. All required validation checks passed.
- `1`: Failure. One or more validation checks failed.

If a script returns warnings (`[WARN]`), the process will not fail and will still exit with `0`. Warnings are for informational purposes (e.g., long lines in Markdown).
