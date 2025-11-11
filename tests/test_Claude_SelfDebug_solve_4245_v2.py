"""
Test file for Problem 4245 - solve_4245_v2
Module: solutions.Claude_SelfDebug
"""

import pytest
from solutions.Claude_SelfDebug import solve_4245_v2


class Test_solve_4245_v2:
    """Test class for solve_4245_v2"""
    
    @pytest.fixture
    def test_cases(self):
        """Provide test inputs and expected outputs"""
        inputs = ['4 10\n', '8 9\n', '8 8\n', '4 12\n', '9 12\n', '13 17\n', '3 17\n', '10 19\n', '6 11\n', '20 19\n', '10 6\n', '2 20\n', '2 1\n', '20 1\n']
        outputs = ['3\n', '2\n', '1\n', '4\n', '2\n', '2\n', '8\n', '2\n', '2\n', '1\n', '1\n', '19\n', '0\n', '0\n']
        return list(zip(inputs, outputs))
    
    def test_all_cases(self, test_cases):
        """Test all benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_4245_v2(inp.strip())).strip()
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
                result = str(solve_4245_v2(inp.strip())).strip()
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
