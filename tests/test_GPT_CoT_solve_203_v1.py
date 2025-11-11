"""
Test file for Problem 203 - solve_203_v1
Module: solutions.GPT_CoT
"""

import pytest
from solutions.GPT_CoT import solve_203_v1


class Test_solve_203_v1:
    """Test class for solve_203_v1"""
    
    @pytest.fixture
    def test_cases(self):
        """Provide test inputs and expected outputs"""
        inputs = ['5\nDDRRR\n', '6\nDDRRRR\n', '1\nD\n', '1\nR\n', '2\nDR\n', '3\nRDD\n', '3\nDRD\n', '4\nDRRD\n', '4\nDRRR\n', '4\nRDRD\n', '5\nDRDRR\n', '4\nRRRR\n', '5\nRDDRD\n', '5\nDDRRD\n', '5\nDRRRD\n', '5\nDDDDD\n', '6\nDRRDDR\n', '7\nRDRDRDD\n', '7\nRDRDDRD\n', '7\nRRRDDDD\n', '8\nRRRDDDDD\n', '9\nRRRDDDDDR\n', '9\nRRDDDRRDD\n', '9\nRRDDDRDRD\n', '10\nDDRRRDRRDD\n', '11\nDRDRRDDRDDR\n', '12\nDRDRDRDRRDRD\n', '13\nDRDDDDRRRRDDR\n', '14\nDDRDRRDRDRDDDD\n', '15\nDDRRRDDRDRRRDRD\n', '50\nDDDRDRDDDDRRRRDDDDRRRDRRRDDDRRRRDRDDDRRDRRDDDRDDDD\n', '50\nDRDDDDDDDRDRDDRRRDRDRDRDDDRRDRRDRDRRDDDRDDRDRDRDDR\n', '100\nRDRRDRDDDDRDRRDDRDRRDDRRDDRRRDRRRDDDRDDRDDRRDRDRRRDRDRRRDRRDDDRDDRRRDRDRRRDDRDRDDDDDDDRDRRDDDDDDRRDD\n', '100\nRRDRRDDDDDDDRDRRRDRDRDDDRDDDRDDRDRRDRRRDRRDRRRRRRRDRRRRRRDDDRRDDRRRDRRRDDRRDRRDDDDDRRDRDDRDDRRRDRRDD\n', '6\nRDDRDR\n', '6\nDRRDRD\n', '8\nDDDRRRRR\n', '7\nRRRDDDD\n', '7\nRDDRRDD\n', '9\nRDDDRRDRR\n', '5\nRDRDD\n', '5\nRRDDD\n', '8\nRDDRDRRD\n', '10\nDRRRDDRDRD\n', '7\nDRRDDRR\n', '12\nRDDDRRDRRDDR\n', '7\nRDRDDDR\n', '7\nDDRRRDR\n', '10\nDRRDRDRDRD\n', '21\nDDDDRRRRRDRDRDRDRDRDR\n', '11\nRDDDDDRRRRR\n', '10\nRDDDRRRDDR\n', '4\nRDDR\n', '7\nRDRDDRD\n', '8\nRDDDRRRD\n', '16\nDRRDRDRDRDDRDRDR\n', '8\nDRRDRDRD\n', '6\nRDDDRR\n', '10\nDDRRRRRDDD\n', '7\nDDRRRRD\n', '12\nRDDRDRDRRDRD\n', '9\nDDRRRDRDR\n', '20\nRDDRDRDRDRRDRDRDRDDR\n', '7\nRRDDDRD\n', '12\nDRRRRRRDDDDD\n', '12\nRDRDDRDRDRDR\n', '6\nDDDDDD\n', '10\nRRRDDRDDDD\n', '40\nRDDDRDDDRDRRDRDRRRRRDRDRDRDRRDRDRDRRDDDD\n', '50\nRRDDDRRDRRRDDRDDDDDRDDRRRRRRDRDDRDDDRDRRDDRDDDRDRD\n', '5\nRDRDR\n', '9\nDRRDRDDRR\n', '6\nDRRRDD\n', '10\nDDDDRRRRRR\n', '9\nRRDDDDRRD\n']
        outputs = ['D\n', 'R\n', 'D\n', 'R\n', 'D\n', 'D\n', 'D\n', 'D\n', 'R\n', 'R\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'D\n', 'R\n', 'R\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n']
        return list(zip(inputs, outputs))
    
    def test_all_cases(self, test_cases):
        """Test all benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_203_v1(inp.strip())).strip()
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
                result = str(solve_203_v1(inp.strip())).strip()
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
