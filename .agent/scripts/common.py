import os
import sys
import json
from pathlib import Path

def get_repo_root():
    # Since common.py is in .agent/scripts, repo root is 2 levels up
    return Path(__file__).resolve().parent.parent.parent

def get_agent_root():
    return get_repo_root() / '.agent'

def read_text_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_json_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def list_files(base, pattern):
    return list(base.rglob(pattern))

def has_yaml_frontmatter(text):
    return text.startswith('---\n')

def extract_yaml_frontmatter(text):
    if not has_yaml_frontmatter(text):
        return ""
    parts = text.split('---\n', 2)
    if len(parts) >= 3:
        return parts[1]
    return ""

def simple_frontmatter_to_dict(text):
    data = {}
    lines = text.splitlines()
    for line in lines:
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            # simple array extraction
            if val.startswith('[') and val.endswith(']'):
                items = val[1:-1].split(',')
                val = [item.strip().strip('"').strip("'") for item in items if item.strip()]
            else:
                val = val.strip('"').strip("'")
            data[key] = val
    return data

def contains_required_sections(text, sections):
    missing = []
    for section in sections:
        if section not in text:
            missing.append(section)
    return missing

def relative_path(path):
    try:
        return path.relative_to(get_repo_root())
    except ValueError:
        return path

def print_ok(message):
    print(f"[OK] {message}")

def print_fail(message):
    print(f"[FAIL] {message}")

def print_warn(message):
    print(f"[WARN] {message}")

def print_info(message):
    print(f"[INFO] {message}")

class ValidationResult:
    def __init__(self, passed, messages=None):
        self.passed = passed
        self.messages = messages or []

def run_validation(name, callable):
    print(f"--- Running {name} ---")
    result = callable()
    if result.passed:
        print_ok(f"{name} passed.")
    else:
        print_fail(f"{name} failed.")
        for msg in result.messages:
            print_fail(msg)
    return result

def safe_json_dump(path, data):
    try:
        write_json_file(path, data)
        return True
    except Exception as e:
        print_fail(f"Failed to write {path}: {e}")
        return False
