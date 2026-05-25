import sys
import re
from pathlib import Path
from common import (
    get_repo_root, list_files, read_text_file, ValidationResult, print_warn, relative_path
)

def is_ignored(path):
    parts = path.parts
    ignores = ['.git', 'node_modules', 'dist', 'build', '.venv', '__pycache__']
    for ig in ignores:
        if ig in parts:
            return True
    return False

def security_check():
    root = get_repo_root()
    passed = True
    messages = []
    
    # regexes
    aws_pattern = re.compile(r'AKIA[0-9A-Z]{16}')
    gh_pattern = re.compile(r'ghp_[a-zA-Z0-9_]{20,}')
    private_key_markers = [
        '-----BEGIN PRIVATE KEY-----',
        '-----BEGIN RSA PRIVATE KEY-----',
        '-----BEGIN OPENSSH PRIVATE KEY-----'
    ]

    # Assignment patterns
    assign_patterns = [
        re.compile(r'(?i)(password|token|secret|api_key|private_key)\s*=\s*["\']([^"\']{5,})["\']')
    ]

    offensive_terms = [
        'credential harvesting guide',
        'malware persistence',
        'evade detection',
        'unauthorized access playbook',
        'exploit target system'
    ]

    all_files = root.rglob('*')
    
    for f in all_files:
        if not f.is_file():
            continue
        if is_ignored(f) or f.name == 'security_check.py':
            continue
        if f.suffix in ['.jpg', '.png', '.gif', '.zip', '.exe', '.pdf', '.bin', '.index']:
            continue
            
        try:
            text = read_text_file(f)
        except Exception:
            # Skip unreadable files (likely binary)
            continue
            
        rel = relative_path(f)
        lines = text.splitlines()

        for i, line in enumerate(lines):
            # AWS
            if aws_pattern.search(line):
                passed = False
                messages.append(f"Likely AWS Key found at {rel}:{i+1}")
            
            # Github
            if gh_pattern.search(line):
                passed = False
                messages.append(f"Likely GitHub Token found at {rel}:{i+1}")
            
            # PK
            for pk in private_key_markers:
                if pk in line:
                    passed = False
                    messages.append(f"Private Key marker found at {rel}:{i+1}")

            # Assignments (only warn/fail if it looks like a real secret, skip if it has 'example', 'dummy')
            line_lower = line.lower()
            if 'example' not in line_lower and 'dummy' not in line_lower and 'your_' not in line_lower:
                for ap in assign_patterns:
                    match = ap.search(line)
                    if match:
                        val = match.group(2)
                        # if it's very short or looks like a placeholder, skip
                        if len(val) > 8 and 'xxx' not in val:
                            print_warn(f"Suspicious assignment found at {rel}:{i+1}")

            # Offensive terms
            for ot in offensive_terms:
                if ot in line_lower:
                    passed = False
                    messages.append(f"Prohibited offensive term '{ot}' found at {rel}:{i+1}")

    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Security Check", security_check)
    sys.exit(0 if res.passed else 1)
