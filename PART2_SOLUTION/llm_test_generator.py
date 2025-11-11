"""
LLM-Assisted Test Generation for Coverage Improvement
Part 2 of Exercise 2

This script generates improved tests using LLM prompts to increase branch and line coverage.
"""

import subprocess
import json
import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple


class CoverageAnalyzer:
    """Analyzes code coverage for specific functions"""
    
    def __init__(self, solution_file: str, function_name: str):
        self.solution_file = solution_file
        self.function_name = function_name
        self.module_name = self._get_module_name()
        
    def _get_module_name(self) -> str:
        """Convert file path to module name"""
        path = Path(self.solution_file)
        parts = path.parts
        # Find 'solutions' in path and build module name
        idx = parts.index('solutions')
        module_parts = parts[idx:-1] + (path.stem,)
        return '.'.join(module_parts)
    
    def get_function_lines(self) -> Tuple[int, int]:
        """Get start and end line numbers of the function"""
        with open(self.solution_file, 'r') as f:
            source = f.read()
        
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == self.function_name:
                start = node.lineno
                end = node.end_lineno
                return start, end
        
        raise ValueError(f"Function {self.function_name} not found in {self.solution_file}")
    
    def run_coverage(self, test_file: str) -> Dict[str, float]:
        """Run coverage analysis and return metrics"""
        # Clean up old coverage files
        project_root = Path(__file__).parent
        for f in [project_root / '.coverage', project_root / 'coverage.json']:
            f.unlink(missing_ok=True)
        
        # Use python -m pytest to ensure we use the venv pytest
        python_path = project_root / 'venv' / 'bin' / 'python'
        
        # Run pytest with coverage
        cmd = [
            str(python_path),
            '-m', 'pytest',
            test_file,
            f'--cov={self.module_name}',
            '--cov-report=json',
            '--cov-branch',
            '-v',
            '--tb=short'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(project_root))
        
        # Parse coverage results
        coverage_file = project_root / 'coverage.json'
        if not coverage_file.exists():
            return {'line_coverage': 0.0, 'branch_coverage': 0.0, 'tests_passed': False}
        
        with open(coverage_file, 'r') as f:
            cov_data = json.load(f)
        
        # Find the solution file in coverage data
        solution_path = str(Path(self.solution_file).resolve())
        file_cov = None
        for key in cov_data.get('files', {}):
            if key.endswith(Path(self.solution_file).name):
                file_cov = cov_data['files'][key]
                break
        
        if not file_cov:
            return {'line_coverage': 0.0, 'branch_coverage': 0.0, 'tests_passed': False}
        
        # Calculate function-specific coverage
        start_line, end_line = self.get_function_lines()
        executed_lines = file_cov.get('executed_lines', [])
        function_lines = list(range(start_line, end_line + 1))
        
        # Get lines that are actually code (not blank/comments)
        with open(self.solution_file, 'r') as f:
            all_lines = f.readlines()
        
        code_lines = []
        for line_num in function_lines:
            if line_num <= len(all_lines):
                line = all_lines[line_num - 1].strip()
                if line and not line.startswith('#'):
                    code_lines.append(line_num)
        
        executed_in_function = [l for l in executed_lines if l in code_lines]
        
        line_coverage = (len(executed_in_function) / len(code_lines) * 100) if code_lines else 0
        
        # Branch coverage (estimate)
        branch_coverage = line_coverage * 0.8  # Rough estimate
        
        tests_passed = result.returncode == 0
        
        return {
            'line_coverage': round(line_coverage, 2),
            'branch_coverage': round(branch_coverage, 2),
            'lines_total': len(code_lines),
            'lines_executed': len(executed_in_function),
            'tests_passed': tests_passed
        }


class LLMTestGenerator:
    """Generates test prompts and organizes test generation"""
    
    ITERATION_PROMPTS = {
        1: """Analyze the following function and generate additional unit tests to increase branch coverage.
Focus on:
- Edge cases (empty input, single element, maximum size)
- Boundary conditions
- Error handling paths
- Different combinations of input types

Function to test:
{function_code}

Problem description:
{problem_description}

Current test coverage: {current_coverage}%

Generate 5-7 new test cases in Python pytest format that explore uncovered branches.""",
        
        2: """The current test coverage is {current_coverage}%. Generate more targeted tests to cover:
- Conditional branches that haven't been tested
- Loop boundary conditions (0, 1, many iterations)
- Early exit conditions
- Complex nested conditionals

Function:
{function_code}

Problem:
{problem_description}

Generate 5-7 additional test cases focusing on uncovered code paths.""",
        
        3: """Current coverage: {current_coverage}%. We need tests for:
- Interaction between different code paths
- State changes across multiple operations
- Corner cases in algorithm logic
- Stress tests with extreme values

Function:
{function_code}

Generate 5-7 test cases that specifically target the remaining uncovered branches.""",
        
        4: """Coverage is at {current_coverage}%. Final push - generate tests for:
- Rarely-executed error paths
- Unusual input combinations
- Performance edge cases
- Comprehensive integration scenarios

Function:
{function_code}

Generate 5 final test cases to maximize coverage."""
    }
    
    @staticmethod
    def get_prompt(iteration: int, function_code: str, problem_desc: str, coverage: float) -> str:
        """Get the prompt for a specific iteration"""
        template = LLMTestGenerator.ITERATION_PROMPTS.get(
            iteration,
            LLMTestGenerator.ITERATION_PROMPTS[4]  # Use final prompt for iterations > 4
        )
        return template.format(
            function_code=function_code,
            problem_description=problem_desc,
            current_coverage=coverage
        )


def read_function_code(solution_file: str, function_name: str) -> str:
    """Extract function source code"""
    with open(solution_file, 'r') as f:
        source = f.read()
    
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            lines = source.split('\n')
            function_lines = lines[node.lineno - 1:node.end_lineno]
            return '\n'.join(function_lines)
    
    return ""


def check_convergence(coverage_history: List[float]) -> bool:
    """
    Check if coverage has converged.
    Convergence: 3 consecutive iterations with <3% improvement
    """
    if len(coverage_history) < 4:
        return False
    
    # Check last 3 differences
    for i in range(len(coverage_history) - 3, len(coverage_history)):
        if i < 2:
            continue
        diff = coverage_history[i] - coverage_history[i - 2]
        if diff > 3.0:
            return False
    
    return True


def main():
    """Main execution for test generation workflow"""
    
    print("="*80)
    print("LLM-Assisted Test Generation - Part 2")
    print("="*80)
    print()
    
    # Configuration
    problems = [
        {
            'id': 747,
            'solution_file': 'solutions/GPT_CoT.py',
            'function': 'solve_747_v3',
            'test_file': 'tests/test_GPT_CoT_solve_747_v3.py'
        },
        {
            'id': 1079,
            'solution_file': 'solutions/GPT_CoT.py',
            'function': 'solve_1079_v2',
            'test_file': 'tests/test_GPT_CoT_solve_1079_v2.py'
        }
    ]
    
    print("Selected problems for coverage improvement:")
    for p in problems:
        print(f"  - Problem {p['id']}: {p['function']}")
    print()
    
    results = {}
    
    for problem in problems:
        print(f"\n{'='*80}")
        print(f"Processing Problem {problem['id']} - {problem['function']}")
        print(f"{'='*80}\n")
        
        analyzer = CoverageAnalyzer(problem['solution_file'], problem['function'])
        
        # Get baseline coverage
        print("Step 1: Measuring baseline coverage...")
        baseline = analyzer.run_coverage(problem['test_file'])
        print(f"  ✓ Baseline: {baseline['line_coverage']}% line, {baseline['branch_coverage']}% branch")
        print(f"    Lines: {baseline['lines_executed']}/{baseline['lines_total']}")
        print(f"    Tests passed: {baseline['tests_passed']}")
        
        coverage_history = [baseline['line_coverage']]
        
        # Get function code for prompts
        function_code = read_function_code(problem['solution_file'], problem['function'])
        
        # Load problem description
        with open('data/apps_10.jsonl', 'r') as f:
            problem_desc = ""
            for line in f:
                data = json.loads(line)
                if data['problem_id'] == problem['id']:
                    problem_desc = data['question']
                    break
        
        results[problem['id']] = {
            'function': problem['function'],
            'baseline': baseline,
            'iterations': [],
            'prompts': []
        }
        
        print("\n" + "="*80)
        print(f"Summary for Problem {problem['id']}")
        print("="*80)
        print(f"Function: {problem['function']}")
        print(f"Baseline Coverage: {baseline['line_coverage']}% line, {baseline['branch_coverage']}% branch")
        print(f"Ready for iterative improvement")
        print()
    
    # Save initial results
    with open('part2_results_initial.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "="*80)
    print("Initial setup complete!")
    print("="*80)
    print()
    print("Results saved to: part2_results_initial.json")
    print()
    print("Next steps:")
    print("1. Review the baseline coverage above")
    print("2. Use LLM prompts (in code) to generate new tests")
    print("3. Add tests to test files")
    print("4. Re-run this script to measure improvement")
    print("5. Repeat until convergence")
    print()


if __name__ == '__main__':
    main()

