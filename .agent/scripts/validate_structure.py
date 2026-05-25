import sys
from pathlib import Path
from common import get_repo_root, relative_path, ValidationResult, print_warn

def validate_structure():
    root = get_repo_root()
    passed = True
    messages = []

    required_files = [
        'README.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md', 'package.json', '.gitignore',
        '.agent/AGENTS.md', '.agent/ARCHITECTURE.md', '.agent/INDEX.md',
        'docs/getting-started.md', 'docs/agent-design.md', 'docs/skill-design.md', 'docs/workflow-design.md',
        'docs/orchestration-model.md', 'docs/validation-model.md', 'docs/antigravity-setup.md',
        'docs/examples.md', 'docs/roadmap.md',
        '.agent/rules/global-rules.md', '.agent/rules/agent-boundaries.md', '.agent/rules/file-ownership.md',
        '.agent/rules/parallel-execution.md', '.agent/rules/validation-rules.md', '.agent/rules/security-rules.md',
        '.agent/rules/documentation-rules.md', '.agent/rules/memory-rules.md', '.agent/rules/handoff-rules.md',
        '.agent/rules/output-contract-rules.md',
        '.agent/templates/agent-template.md', '.agent/templates/skill-template.md', '.agent/templates/workflow-template.md',
        '.agent/templates/task-brief-template.md', '.agent/templates/implementation-plan-template.md',
        '.agent/templates/validation-report-template.md', '.agent/templates/pr-template.md', '.agent/templates/release-template.md',
        '.agent/templates/handoff-template.md', '.agent/templates/agent-output-contract-template.md'
    ]

    required_dirs = [
        '.agent/agents', '.agent/skills', '.agent/workflows', '.agent/rules', '.agent/templates',
        '.agent/scripts', '.agent/indexes', 'adapters', 'packs', 'docs'
    ]

    for f in required_files:
        if not (root / f).is_file():
            passed = False
            messages.append(f"Missing required file: {f}")

    for d in required_dirs:
        if not (root / d).is_dir():
            passed = False
            messages.append(f"Missing required directory: {d}")

    # check gitkeeps
    for d in required_dirs:
        if d.startswith('.agent'):
            gitkeep = root / d / '.gitkeep'
            if gitkeep.exists():
                # check if populated
                if len(list((root / d).iterdir())) > 1:
                    print_warn(f".gitkeep found in populated directory: {d}")

    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Structure Validation", validate_structure)
    sys.exit(0 if res.passed else 1)
