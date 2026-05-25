import sys
from pathlib import Path
from common import (
    get_agent_root, list_files, read_text_file, extract_yaml_frontmatter,
    simple_frontmatter_to_dict, contains_required_sections, ValidationResult, print_warn, relative_path
)

def validate_agents():
    agent_root = get_agent_root()
    agent_files = list_files(agent_root / 'agents', '*.agent.md')
    passed = True
    messages = []

    if len(agent_files) < 60:
        passed = False
        messages.append(f"Expected at least 60 agents, found {len(agent_files)}.")

    required_frontmatter = [
        'name', 'type', 'category', 'description', 'when_to_use', 'do_not_use_when',
        'risk_level', 'allowed_operations', 'disallowed_operations', 'required_skills',
        'optional_skills', 'input_contract', 'output_contract', 'owner', 'reviewers'
    ]

    required_sections = [
        '# Role', '# Mission', '# Responsibilities', '# Boundaries',
        '# Output Contract', '# Failure Handling', '# Examples'
    ]

    for agent_file in agent_files:
        text = read_text_file(agent_file)
        rel = relative_path(agent_file)
        
        if len(text) < 200:
            print_warn(f"Agent file is unusually short: {rel}")

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

        agent_type = fm.get('type', '')
        if agent_type not in ['orchestration-agent', 'specialist-agent']:
            passed = False
            messages.append(f"Invalid type '{agent_type}' in {rel}")

        risk = fm.get('risk_level', '')
        if risk not in ['low', 'medium', 'high', 'critical']:
            passed = False
            messages.append(f"Invalid risk_level '{risk}' in {rel}")

        missing_sections = contains_required_sections(text, required_sections)
        for ms in missing_sections:
            passed = False
            messages.append(f"Missing section '{ms}' in {rel}")

    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Agent Validation", validate_agents)
    sys.exit(0 if res.passed else 1)
