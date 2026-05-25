import sys
from pathlib import Path
from common import (
    get_repo_root, list_files, read_text_file, ValidationResult, print_warn, print_info, relative_path
)

def validate_markdown():
    root = get_repo_root()
    passed = True
    messages = []
    
    # gather files
    md_files = []
    md_files.extend(list_files(root / '.agent', '*.md'))
    md_files.extend(list_files(root / 'docs', '*.md'))
    md_files.extend(list_files(root / 'adapters', '*.md'))
    md_files.extend(list_files(root / 'packs', '*.md'))
    
    for root_file in ['README.md', 'CHANGELOG.md', 'CONTRIBUTING.md']:
        f = root / root_file
        if f.is_file():
            md_files.append(f)

    checked = 0
    warnings = 0
    failures = 0

    conflict_markers = ['<<<<<<<', '=======', '>>>>>>>']
    placeholders = ['lorem ipsum', 'placeholder text', 'insert content here']

    for md in md_files:
        rel = relative_path(md)
        if md.name == '.gitkeep':
            continue
            
        checked += 1
        text = read_text_file(md)
        if not text.strip():
            passed = False
            failures += 1
            messages.append(f"Empty Markdown file: {rel}")
            continue

        lines = text.splitlines()
        has_heading = any(line.startswith('#') for line in lines)
        if not has_heading:
            warnings += 1
            print_warn(f"No heading found in: {rel}")

        for i, line in enumerate(lines):
            if len(line) > 160:
                # exclude links and tables from line length check to avoid false positives
                if 'http' not in line and '|' not in line:
                    warnings += 1
                    print_warn(f"Line {i+1} too long (>160 chars) in {rel}")

            for marker in conflict_markers:
                if line.startswith(marker):
                    passed = False
                    failures += 1
                    messages.append(f"Merge conflict marker found at line {i+1} in {rel}")

            line_lower = line.lower()
            for p in placeholders:
                if p in line_lower:
                    passed = False
                    failures += 1
                    messages.append(f"Placeholder text '{p}' found at line {i+1} in {rel}")
            
            if 'todo' in line_lower:
                # Just warn
                warnings += 1
                # print_warn(f"TODO found at line {i+1} in {rel}")

    print_info(f"Markdown validation checked {checked} files. {warnings} warnings, {failures} failures.")
    return ValidationResult(passed, messages)

if __name__ == "__main__":
    from common import run_validation
    res = run_validation("Markdown Validation", validate_markdown)
    sys.exit(0 if res.passed else 1)
