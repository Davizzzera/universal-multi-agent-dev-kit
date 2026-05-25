import sys
from pathlib import Path
from common import (
    get_agent_root, list_files, read_text_file, extract_yaml_frontmatter,
    simple_frontmatter_to_dict, contains_required_sections, ValidationResult, print_warn, relative_path
)

def validate_workflows():
    agent_root = get_agent_root()
    workflow_files = list_files(agent_root / 'workflows', '*.workflow.md')
    passed = True
    messages = []

    if len(workflow_files) != 18:
        passed = False
        messages.append(f"Expected exactly 18 workflows, found {len(workflow_files)}.")

    required_frontmatter = [
        'name', 'type', 'description', 'trigger', 'primary_agent',
        'required_agents', 'optional_agents', 'required_skills',
        'validation_required', 'risk_level', 'related_rules'
    ]

    required_sections = [
        '# Workflow Purpose', '# Trigger Conditions', '# Required Inputs',
        '# Agents Involved', '# Skills Involved', '# Execution Steps',
        '# Parallelization Strategy', '# File Ownership Strategy', '# Validation Steps',
        '# Output Contract', '# Failure Handling', '# Example Run'
    ]

    for wf_file in workflow_files:
        text = read_text_file(wf_file)
        rel = relative_path(wf_file)
        
        if len(text) < 150:
            print_warn(f"Workflow file is unusually short: {rel}")

        fm_text = extract_yaml_frontmatter(text)
        if not fm_text:
            passed = False
            messages.append(f"No YAML frontmatter in {rel}")
            continue

        fm = simple_frontmatter_to_dict(fm_text)
        for req in required_frontmatter:
            if req not in fm:
                passed = False
                messages.append(f"Missing frontmatter key '{req}' in {rel}")

        wf_type = fm.get('type', '')
        if wf_type != 'workflow':
            passed = False
            messages.append(f"Invalid type '{wf_type}' in {rel}")

        risk = fm.get('risk_level', '')
        if risk not in ['low', 'medium', 'high', 'critical']:
            passed = False
            messages.append(f"Invalid risk_level '{risk}' in {rel}")

        val_req = fm.get('validation_required', '')
        if val_req not in ['none', 'manual', 'automated', 'manual-and-automated']:
            passed = False
            messages.append(f"Invalid validation_required '{val_req}' in {rel}")

        missing_sections = contains_required_sections(text, required_sections)
        for ms in missing_sections:
            passed = False
            messages.append(f"Missing section '{ms}' in {rel}")

    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Workflow Validation", validate_workflows)
    sys.exit(0 if res.passed else 1)
