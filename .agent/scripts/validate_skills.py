import sys
from pathlib import Path
from common import (
    get_agent_root, list_files, read_text_file, extract_yaml_frontmatter,
    simple_frontmatter_to_dict, contains_required_sections, ValidationResult, print_warn, relative_path
)

def validate_skills():
    agent_root = get_agent_root()
    skill_files = list_files(agent_root / 'skills', 'SKILL.md')
    passed = True
    messages = []

    if len(skill_files) != 104:
        passed = False
        messages.append(f"Expected exactly 104 skills, found {len(skill_files)}.")

    required_frontmatter = [
        'name', 'type', 'category', 'description', 'when_to_use', 'do_not_use_when',
        'risk_level', 'owner_agents', 'required_inputs', 'expected_outputs',
        'validation_level', 'related_rules'
    ]

    required_sections = [
        '# Purpose', '# When to Use', '# When Not to Use', '# Required Inputs',
        '# Procedure', '# Decision Rules', '# Checklist', '# Validation',
        '# Expected Output', '# Common Mistakes', '# Example Usage'
    ]

    for skill_file in skill_files:
        text = read_text_file(skill_file)
        rel = relative_path(skill_file)
        
        if len(text) < 150:
            print_warn(f"Skill file is unusually short: {rel}")

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

        skill_type = fm.get('type', '')
        if skill_type != 'skill':
            passed = False
            messages.append(f"Invalid type '{skill_type}' in {rel}")

        risk = fm.get('risk_level', '')
        if risk not in ['low', 'medium', 'high', 'critical']:
            passed = False
            messages.append(f"Invalid risk_level '{risk}' in {rel}")

        val_level = fm.get('validation_level', '')
        if val_level not in ['none', 'manual', 'automated', 'manual-and-automated']:
            passed = False
            messages.append(f"Invalid validation_level '{val_level}' in {rel}")

        missing_sections = contains_required_sections(text, required_sections)
        for ms in missing_sections:
            passed = False
            messages.append(f"Missing section '{ms}' in {rel}")

    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Skill Validation", validate_skills)
    sys.exit(0 if res.passed else 1)
