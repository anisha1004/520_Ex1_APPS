"""
Test file for Problem 4655 - solve_4655_v2
Module: solutions.Claude_SelfDebug
"""

import pytest
from solutions.Claude_SelfDebug import solve_4655_v2


class Test_solve_4655_v2:
    """Test class for solve_4655_v2"""
    
    @pytest.fixture
    def test_cases(self):
        """Provide test inputs and expected outputs"""
        inputs = ['4\n1 3 4\n1 10 100\n10000000000000000 10000000000000000 10000000000000000\n23 34 45\n', '1\n111 2 3\n']
        outputs = ['4\n55\n15000000000000000\n51\n', '58\n']
        return list(zip(inputs, outputs))
    
    def test_all_cases(self, test_cases):
        """Test all benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_4655_v2(inp.strip())).strip()
            expected_clean = str(expected).strip()
            assert result == expected_clean, (
                f"Test case {i+1} failed\n"
                f"Input: {inp[:100]}...\n"
                f"Expected: {expected_clean[:100]}...\n"
                f"Got: {result[:100]}..."
            )
    
    def test_individual_cases(self, test_cases):
        """Test each case individually for better error reporting"""
        passed = 0
        failed = 0
        
        for i, (inp, expected) in enumerate(test_cases):
            try:
                result = str(solve_4655_v2(inp.strip())).strip()
                expected_clean = str(expected).strip()
                if result == expected_clean:
                    passed += 1
                else:
                    failed += 1
                    print(f"Case {i+1} FAILED")
            except Exception as e:
                failed += 1
                print(f"Case {i+1} ERROR: {e}")
        
        assert passed == len(test_cases), f"Only {passed}/{len(test_cases)} passed"
