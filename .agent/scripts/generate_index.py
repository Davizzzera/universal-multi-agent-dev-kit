import sys
from datetime import datetime, timezone
from pathlib import Path
from common import (
    get_agent_root, list_files, read_text_file, extract_yaml_frontmatter,
    simple_frontmatter_to_dict, write_json_file, ValidationResult, relative_path, get_repo_root
)

def generate_index():
    agent_root = get_agent_root()
    index_dir = agent_root / 'indexes'
    index_dir.mkdir(exist_ok=True)
    
    passed = True
    messages = []
    
    # 1. Agents
    agents = []
    agent_files = list_files(agent_root / 'agents', '*.agent.md')
    agent_categories = set()
    for f in agent_files:
        text = read_text_file(f)
        fm_text = extract_yaml_frontmatter(text)
        if fm_text:
            fm = simple_frontmatter_to_dict(fm_text)
            cat = fm.get('category', '')
            if cat:
                agent_categories.add(cat)
            agents.append({
                "name": fm.get('name', ''),
                "type": fm.get('type', ''),
                "category": cat,
                "description": fm.get('description', ''),
                "risk_level": fm.get('risk_level', ''),
                "path": str(relative_path(f)).replace('\\', '/'),
                "required_skills": fm.get('required_skills', []),
                "optional_skills": fm.get('optional_skills', [])
            })
    
    # deterministic ordering
    agents.sort(key=lambda x: x['name'])
    write_json_file(index_dir / 'agents.index.json', agents)
    
    # 2. Skills
    skills = []
    skill_files = list_files(agent_root / 'skills', 'SKILL.md')
    skill_categories = set()
    for f in skill_files:
        text = read_text_file(f)
        fm_text = extract_yaml_frontmatter(text)
        if fm_text:
            fm = simple_frontmatter_to_dict(fm_text)
            cat = fm.get('category', '')
            if cat:
                skill_categories.add(cat)
            skills.append({
                "name": fm.get('name', ''),
                "type": fm.get('type', ''),
                "category": cat,
                "description": fm.get('description', ''),
                "risk_level": fm.get('risk_level', ''),
                "validation_level": fm.get('validation_level', ''),
                "path": str(relative_path(f)).replace('\\', '/'),
                "owner_agents": fm.get('owner_agents', [])
            })

    skills.sort(key=lambda x: x['name'])
    write_json_file(index_dir / 'skills.index.json', skills)

    # 3. Workflows
    workflows = []
    workflow_files = list_files(agent_root / 'workflows', '*.workflow.md')
    for f in workflow_files:
        text = read_text_file(f)
        fm_text = extract_yaml_frontmatter(text)
        if fm_text:
            fm = simple_frontmatter_to_dict(fm_text)
            workflows.append({
                "name": fm.get('name', ''),
                "type": fm.get('type', ''),
                "description": fm.get('description', ''),
                "risk_level": fm.get('risk_level', ''),
                "validation_required": fm.get('validation_required', ''),
                "primary_agent": fm.get('primary_agent', ''),
                "path": str(relative_path(f)).replace('\\', '/'),
                "required_agents": fm.get('required_agents', []),
                "required_skills": fm.get('required_skills', []),
                "trigger": fm.get('trigger', [])
            })

    workflows.sort(key=lambda x: x['name'])
    write_json_file(index_dir / 'workflows.index.json', workflows)

    # 4. Repository Index
    rules_count = len(list_files(agent_root / 'rules', '*.md'))
    templates_count = len(list_files(agent_root / 'templates', '*.md'))
    docs_count = len(list_files(get_repo_root() / 'docs', '*.md'))
    
    repo_index = {
        "project_name": "universal-multi-agent-dev-kit",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "counts": {
            "agents": len(agents),
            "skills": len(skills),
            "workflows": len(workflows),
            "rules": rules_count,
            "templates": templates_count,
            "docs": docs_count
        },
        "categories": {
            "agent_categories": sorted(list(agent_categories)),
            "skill_categories": sorted(list(skill_categories))
        },
        "index_files": [
            ".agent/indexes/agents.index.json",
            ".agent/indexes/skills.index.json",
            ".agent/indexes/workflows.index.json"
        ],
        "notes": "These indexes are generated from Markdown frontmatter. Do not edit directly."
    }

    write_json_file(index_dir / 'repository.index.json', repo_index)
    
    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Generate Index", generate_index)
    sys.exit(0 if res.passed else 1)
