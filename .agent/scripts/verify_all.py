import sys
from common import print_info, print_ok, print_fail

def main():
    print_info("Starting Universal Multi-Agent Dev Kit Validation...\n")
    
    # Import validation modules
    from validate_structure import validate_structure
    from validate_agents import validate_agents
    from validate_skills import validate_skills
    from validate_workflows import validate_workflows
    from validate_markdown import validate_markdown
    from security_check import security_check
    from generate_index import generate_index
    from common import run_validation

    validations = [
        ("Structure Validation", validate_structure),
        ("Agent Validation", validate_agents),
        ("Skill Validation", validate_skills),
        ("Workflow Validation", validate_workflows),
        ("Markdown Validation", validate_markdown),
        ("Security Check", security_check),
        ("Index Generation", generate_index)
    ]

    all_passed = True

    for name, func in validations:
        res = run_validation(name, func)
        if not res.passed:
            all_passed = False
        print("") # newline for readability

    if all_passed:
        print_ok("ALL VALIDATIONS PASSED.")
        sys.exit(0)
    else:
        print_fail("ONE OR MORE VALIDATIONS FAILED. SEE OUTPUT ABOVE.")
        sys.exit(1)

if __name__ == "__main__":
    main()
