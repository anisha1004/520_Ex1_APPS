"""
Verification script for Part 2 - Measure actual coverage improvements
"""

import subprocess
import json
from pathlib import Path


def run_coverage_test(test_file, module, function_name):
    """Run coverage for a specific test file"""
    project_root = Path(__file__).parent
    python_path = project_root / 'venv' / 'bin' / 'python'
    
    # Clean up
    for f in [project_root / '.coverage', project_root / 'coverage.json']:
        f.unlink(missing_ok=True)
    
    # Run with coverage
    cmd = [
        str(python_path),
        '-m', 'pytest',
        test_file,
        f'--cov={module}',
        '--cov-report=json',
        '--cov-branch',
        '-v'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(project_root))
    
    # Parse results
    coverage_file = project_root / 'coverage.json'
    if not coverage_file.exists():
        return None
    
    with open(coverage_file, 'r') as f:
        data = json.load(f)
    
    # Get test count
    passed_tests = result.stdout.count(' PASSED')
    
    return {
        'tests_passed': passed_tests,
        'line_coverage': data.get('totals', {}).get('percent_covered', 0),
        'branch_coverage': data.get('totals', {}).get('percent_covered_display', 'N/A'),
        'output': result.stdout
    }


def main():
    print("="*80)
    print("Part 2 Coverage Verification")
    print("="*80)
    print()
    
    tests = [
        {
            'name': 'Problem 747 - Baseline',
            'test_file': 'tests/test_GPT_CoT_solve_747_v3.py',
            'module': 'solutions.GPT_CoT',
            'function': 'solve_747_v3'
        },
        {
            'name': 'Problem 747 - Enhanced (All Iterations)',
            'test_file': 'tests/test_GPT_CoT_solve_747_v3_enhanced.py',
            'module': 'solutions.GPT_CoT',
            'function': 'solve_747_v3'
        },
        {
            'name': 'Problem 1079 - Baseline',
            'test_file': 'tests/test_GPT_CoT_solve_1079_v2.py',
            'module': 'solutions.GPT_CoT',
            'function': 'solve_1079_v2'
        },
        {
            'name': 'Problem 1079 - Enhanced (All Iterations)',
            'test_file': 'tests/test_GPT_CoT_solve_1079_v2_enhanced.py',
            'module': 'solutions.GPT_CoT',
            'function': 'solve_1079_v2'
        }
    ]
    
    results = {}
    
    for test in tests:
        print(f"\nTesting: {test['name']}")
        print("-" * 80)
        result = run_coverage_test(test['test_file'], test['module'], test['function'])
        
        if result:
            print(f"  Tests Passed: {result['tests_passed']}")
            print(f"  Line Coverage: {result['line_coverage']:.2f}%")
            results[test['name']] = result
        else:
            print("  ERROR: Could not measure coverage")
        print()
    
    print("="*80)
    print("Summary")
    print("="*80)
    print()
    
    # Compare baseline vs enhanced
    if 'Problem 747 - Baseline' in results and 'Problem 747 - Enhanced (All Iterations)' in results:
        baseline = results['Problem 747 - Baseline']
        enhanced = results['Problem 747 - Enhanced (All Iterations)']
        print("Problem 747:")
        print(f"  Baseline:  {baseline['tests_passed']} tests, {baseline['line_coverage']:.2f}% coverage")
        print(f"  Enhanced:  {enhanced['tests_passed']} tests, {enhanced['line_coverage']:.2f}% coverage")
        print(f"  Improvement: +{enhanced['tests_passed'] - baseline['tests_passed']} tests, "
              f"+{enhanced['line_coverage'] - baseline['line_coverage']:.2f}% coverage")
        print()
    
    if 'Problem 1079 - Baseline' in results and 'Problem 1079 - Enhanced (All Iterations)' in results:
        baseline = results['Problem 1079 - Baseline']
        enhanced = results['Problem 1079 - Enhanced (All Iterations)']
        print("Problem 1079:")
        print(f"  Baseline:  {baseline['tests_passed']} tests, {baseline['line_coverage']:.2f}% coverage")
        print(f"  Enhanced:  {enhanced['tests_passed']} tests, {enhanced['line_coverage']:.2f}% coverage")
        print(f"  Improvement: +{enhanced['tests_passed'] - baseline['tests_passed']} tests, "
              f"+{enhanced['line_coverage'] - baseline['line_coverage']:.2f}% coverage")
        print()
    
    print("="*80)
    print("Verification complete!")
    print("="*80)


if __name__ == '__main__':
    main()

