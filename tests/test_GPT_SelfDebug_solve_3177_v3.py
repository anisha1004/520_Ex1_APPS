"""
Test file for Problem 3177 - solve_3177_v3
Module: solutions.GPT_SelfDebug
"""

import pytest
from solutions.GPT_SelfDebug import solve_3177_v3


class Test_solve_3177_v3:
    """Test class for solve_3177_v3"""
    
    @pytest.fixture
    def test_cases(self):
        """Provide test inputs and expected outputs"""
        inputs = ['2 1\n2 1\n1 2\n', '3 2\n2 1 3\n1 3\n2 3\n', '5 5\n1 2 3 4 5\n1 5\n2 5\n1 4\n1 2\n3 5\n']
        outputs = ['1\n', '3\n', '0\n']
        return list(zip(inputs, outputs))
    
    def test_all_cases(self, test_cases):
        """Test all benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_3177_v3(inp.strip())).strip()
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
                result = str(solve_3177_v3(inp.strip())).strip()
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
