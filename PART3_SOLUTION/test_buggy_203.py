"""
Test runner for buggy version of solve_203_v2
This temporarily replaces the correct version with the buggy one to test fault detection.
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import the buggy version
sys.path.insert(0, str(Path(__file__).parent))
from Claude_SelfDebug_Buggy import solve_203_v2_buggy

# Monkey-patch the solutions module to use buggy version
import solutions.Claude_SelfDebug as claude_module
claude_module.solve_203_v2 = solve_203_v2_buggy

# Now import and run tests - they will use the buggy version
import pytest

if __name__ == "__main__":
    test_file = project_root / "PART2_SOLUTION" / "Problem_203_Solution" / "test_Claude_SelfDebug_solve_203_v2_enhanced.py"
    exit_code = pytest.main([str(test_file), "-v", "--tb=short", "-x"])  # -x stops at first failure
    sys.exit(exit_code)

