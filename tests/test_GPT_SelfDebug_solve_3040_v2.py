"""
Test file for Problem 3040 - solve_3040_v2
Module: solutions.GPT_SelfDebug
"""

import pytest
from solutions.GPT_SelfDebug import solve_3040_v2


class Test_solve_3040_v2:
    """Test class for solve_3040_v2"""
    
    @pytest.fixture
    def test_cases(self):
        """Provide test inputs and expected outputs"""
        inputs = ['abcefgabc\n', 'abcbabcba\n', 'aaaa\n', 'bbcaadbbeaa\n']
        outputs = ['abc\n', 'abcba\n', 'aaa\n', 'aa\n']
        return list(zip(inputs, outputs))
    
    def test_all_cases(self, test_cases):
        """Test all benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_3040_v2(inp.strip())).strip()
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
                result = str(solve_3040_v2(inp.strip())).strip()
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
