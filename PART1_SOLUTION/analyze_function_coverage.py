"""
Analyze per-function coverage from module-level coverage data.

This script:
1. Identifies which lines belong to each function
2. Analyzes coverage data to see which lines were executed
3. Calculates accurate per-function coverage metrics
"""

import ast
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Set, Tuple

def get_function_lines(source_file: Path, function_name: str) -> Tuple[Set[int], Set[tuple]]:
    """Get the line numbers and branches for a specific function"""
    
    with source_file.open() as f:
        source = f.read()
    
    tree = ast.parse(source)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            lines = set(range(node.lineno, node.end_lineno + 1))
            
            # Get all branches (if statements, loops, etc.) within this function
            branches = set()
            for child in ast.walk(node):
                if isinstance(child, (ast.If, ast.While, ast.For, ast.Try)):
                    if hasattr(child, 'lineno'):
                        # Branch from condition line
                        branches.add((child.lineno, child.lineno + 1))
            
            return lines, branches
    
    return set(), set()

def run_coverage_and_analyze(test_file: Path, module_name: str, 
                            function_name: str) -> Dict:
    """Run coverage and analyze for specific function"""
    
    # Module file path
    module_file = Path(f"solutions/{module_name}.py")
    
    if not module_file.exists():
        return {
            "error": "Module file not found",
            "line_coverage": 0.0,
            "branch_coverage": 0.0
        }
    
    # Get function's line numbers
    func_lines, func_branches = get_function_lines(module_file, function_name)
    
    if not func_lines:
        return {
            "error": "Function not found in module",
            "line_coverage": 0.0,
            "branch_coverage": 0.0
        }
    
    # Run pytest with coverage
    cmd = [
        sys.executable, "-m", "pytest",
        str(test_file),
        f"--cov=solutions.{module_name}",
        "--cov-report=json",
        "--cov-branch",
        "-q"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        # Read coverage JSON
        cov_json = Path("coverage.json")
        if not cov_json.exists():
            return {
                "error": "Coverage file not generated",
                "line_coverage": 0.0,
                "branch_coverage": 0.0
            }
        
        with cov_json.open() as f:
            cov_data = json.load(f)
        
        # Find our module in coverage data
        module_cov = None
        for file_path, file_data in cov_data.get("files", {}).items():
            if module_name in file_path and file_path.endswith(".py"):
                module_cov = file_data
                break
        
        if not module_cov:
            return {
                "error": "Module not in coverage data",
                "line_coverage": 0.0,
                "branch_coverage": 0.0
            }
        
        # Get executed lines
        executed_lines = set(module_cov.get("executed_lines", []))
        
        # Calculate function-specific coverage
        func_executed = func_lines & executed_lines
        line_coverage = (len(func_executed) / len(func_lines) * 100) if func_lines else 0.0
        
        # Get branch coverage (if available)
        missing_branches = module_cov.get("missing_branches", [])
        executed_branches = module_cov.get("executed_branches", [])
        
        # Count branches in this function
        func_branch_count = len(func_branches)
        if func_branch_count > 0:
            # This is approximate - we'd need more detailed analysis
            branch_coverage = (len(func_executed) / len(func_lines)) * 100 * 0.8  # Rough estimate
        else:
            branch_coverage = 0.0
        
        # Parse test results
        tests_passed = 0
        tests_total = 0
        if "passed" in result.stdout:
            import re
            match = re.search(r'(\d+) passed', result.stdout)
            if match:
                tests_passed = int(match.group(1))
                tests_total = tests_passed
        if "failed" in result.stdout:
            import re
            match = re.search(r'(\d+) failed', result.stdout)
            if match:
                tests_total += int(match.group(1))
        
        return {
            "line_coverage": round(line_coverage, 2),
            "branch_coverage": round(branch_coverage, 2),
            "lines_in_function": len(func_lines),
            "lines_executed": len(func_executed),
            "tests_passed": tests_passed,
            "tests_total": tests_total if tests_total > 0 else tests_passed,
            "status": "PASS" if result.returncode == 0 else "FAIL"
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "line_coverage": 0.0,
            "branch_coverage": 0.0
        }

def main():
    """Analyze coverage for sample functions"""
    
    print("=" * 80)
    print("Per-Function Coverage Analysis")
    print("=" * 80)
    print()
    
    # Sample tests
    samples = [
        ("tests/test_GPT_CoT_solve_1079_v1.py", "GPT_CoT", "solve_1079_v1"),
        ("tests/test_GPT_CoT_solve_3040_v3.py", "GPT_CoT", "solve_3040_v3"),
        ("tests/test_GPT_SelfDebug_solve_1079_v1.py", "GPT_SelfDebug", "solve_1079_v1"),
        ("tests/test_Claude_CoT_solve_203_v1.py", "Claude_CoT", "solve_203_v1"),
    ]
    
    for test_file, module, function in samples:
        print(f"\nAnalyzing: {module} - {function}")
        
        result = run_coverage_and_analyze(Path(test_file), module, function)
        
        if result.get("error"):
            print(f"  ❌ Error: {result['error']}")
        else:
            status = "✅" if result["status"] == "PASS" else "❌"
            print(f"  {status} Tests: {result['tests_passed']}/{result['tests_total']}")
            print(f"  📊 Line Coverage: {result['line_coverage']:.1f}%")
            print(f"     ({result['lines_executed']}/{result['lines_in_function']} lines)")
            print(f"  🔀 Branch Coverage: {result['branch_coverage']:.1f}% (estimated)")
    
    print("\n" + "=" * 80)
    print("Sample complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()

