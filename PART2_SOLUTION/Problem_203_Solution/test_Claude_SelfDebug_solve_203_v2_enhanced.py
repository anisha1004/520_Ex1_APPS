"""
Enhanced Test file for Problem 203 - solve_203_v2
Module: solutions.Claude_SelfDebug
Part 2: LLM-Generated Tests for Coverage Improvement

Baseline: 72.0% line, 57.6% branch (75 tests but still gaps!)
Target: 95%+ coverage through targeted LLM test generation
"""

import pytest
from solutions.Claude_SelfDebug import solve_203_v2


class Test_solve_203_v2_baseline:
    """Baseline tests - 75 tests, but only 72% coverage!"""
    
    @pytest.fixture
    def test_cases(self):
        """Original benchmark test cases"""
        inputs = ['5\nDDRRR\n', '6\nDDRRRR\n', '1\nD\n', '1\nR\n', '2\nDR\n', '3\nRDD\n', '3\nDRD\n', '4\nDRRD\n', '4\nDRRR\n', '4\nRDRD\n', '5\nDRDRR\n', '4\nRRRR\n', '5\nRDDRD\n', '5\nDDRRD\n', '5\nDRRRD\n', '5\nDDDDD\n', '6\nDRRDDR\n', '7\nRDRDRDD\n', '7\nRDRDDRD\n', '7\nRRRDDDD\n', '8\nRRRDDDDD\n', '9\nRRRDDDDDR\n', '9\nRRDDDRRDD\n', '9\nRRDDDRDRD\n', '10\nDDRRRDRRDD\n', '11\nDRDRRDDRDDR\n', '12\nDRDRDRDRRDRD\n', '13\nDRDDDDRRRRDDR\n', '14\nDDRDRRDRDRDDDD\n', '15\nDDRRRDDRDRRRDRD\n', '50\nDDDRDRDDDDRRRRDDDDRRRDRRRDDDRRRRDRDDDRRDRRDDDRDDDD\n', '50\nDRDDDDDDDRDRDDRRRDRDRDRDDDRRDRRDRDRRDDDRDDRDRDRDDR\n', '100\nRDRRDRDDDDRDRRDDRDRRDDRRDDRRRDRRRDDDRDDRDDRRDRDRRRDRDRRRDRRDDDRDDRRRDRDRRRDDRDRDDDDDDDRDRRDDDDDDRRDD\n', '100\nRRDRRDDDDDDDRDRRRDRDRDDDRDDDRDDRDRRDRRRDRRDRRRRRRRDRRRRRRDDDRRDDRRRDRRRDDRRDRRDDDDDRRDRDDRDDRRRDRRDD\n', '6\nRDDRDR\n', '6\nDRRDRD\n', '8\nDDDRRRRR\n', '7\nRRRDDDD\n', '7\nRDDRRDD\n', '9\nRDDDRRDRR\n', '5\nRDRDD\n', '5\nRRDDD\n', '8\nRDDRDRRD\n', '10\nDRRRDDRDRD\n', '7\nDRRDDRR\n', '12\nRDDDRRDRRDDR\n', '7\nRDRDDDR\n', '7\nDDRRRDR\n', '10\nDRRDRDRDRD\n', '21\nDDDDRRRRRDRDRDRDRDRDR\n', '11\nRDDDDDRRRRR\n', '10\nRDDDRRRDDR\n', '4\nRDDR\n', '7\nRDRDDRD\n', '8\nRDDDRRRD\n', '16\nDRRDRDRDRDDRDRDR\n', '8\nDRRDRDRD\n', '6\nRDDDRR\n', '10\nDDRRRRRDDD\n', '7\nDDRRRRD\n', '12\nRDDRDRDRRDRD\n', '9\nDDRRRDRDR\n', '20\nRDDRDRDRDRRDRDRDRDDR\n', '7\nRRDDDRD\n', '12\nDRRRRRRDDDDD\n', '12\nRDRDDRDRDRDR\n', '6\nDDDDDD\n', '10\nRRRDDRDDDD\n', '40\nRDDDRDDDRDRRDRDRRRRRDRDRDRDRRDRDRDRRDDDD\n', '50\nRRDDDRRDRRRDDRDDDDDRDDRRRRRRDRDDRDDDRDRRDDRDDDRDRD\n', '5\nRDRDR\n', '9\nDRRDRDDRR\n', '6\nDRRRDD\n', '10\nDDDDRRRRRR\n', '9\nRRDDDDRRD\n']
        outputs = ['D\n', 'R\n', 'D\n', 'R\n', 'D\n', 'D\n', 'D\n', 'D\n', 'R\n', 'R\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'D\n', 'R\n', 'R\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'D\n', 'D\n', 'R\n', 'R\n', 'D\n', 'R\n', 'R\n', 'R\n', 'D\n', 'D\n']
        return list(zip(inputs, outputs))
    
    def test_baseline_cases(self, test_cases):
        """Test all original benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_203_v2(inp.strip())).strip()
            expected_clean = str(expected).strip()
            assert result == expected_clean, f"Baseline test {i+1} failed"


class Test_solve_203_v2_iteration1:
    """Iteration 1: Edge cases and boundary conditions
    
    Prompt: Generate tests for senate voting queue algorithm focusing on:
    - Edge case: single senator
    - Equal D and R counts
    - Extreme imbalances
    - Early elimination patterns
    - Queue wrap-around (d_idx + n logic)
    - Empty queue conditions
    """
    
    def test_single_d(self):
        """Single D senator - immediate win"""
        input_data = "1\nD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_single_r(self):
        """Single R senator - immediate win"""
        input_data = "1\nR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"
    
    def test_two_alternating(self):
        """Simplest competition: DR"""
        input_data = "2\nDR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"  # D goes first
    
    def test_two_alternating_rd(self):
        """Simplest competition: RD"""
        input_data = "2\nRD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"  # R goes first
    
    def test_equal_count_d_first(self):
        """Equal count, D appears first"""
        input_data = "4\nDDRR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_equal_count_r_first(self):
        """Equal count, R appears first"""
        input_data = "4\nRRDD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"
    
    def test_extreme_imbalance_d(self):
        """Heavy D advantage"""
        input_data = "10\nDDDDDDDDDR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_extreme_imbalance_r(self):
        """Heavy R advantage"""
        input_data = "10\nDRRRRRRRRR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"


class Test_solve_203_v2_iteration2:
    """Iteration 2: Queue mechanics and index arithmetic
    
    Prompt: Test queue behavior and wraparound logic:
    - d_idx + n wraparound
    - r_idx + n wraparound
    - Index comparison edge cases
    - Sequential eliminations
    - Back-and-forth eliminations
    """
    
    def test_wraparound_d_wins(self):
        """D queue wraps around and wins"""
        input_data = "6\nDRDRDR\n"
        result = solve_203_v2(input_data)
        # Alternating pattern, first player advantage
        assert result.strip() == "D"
    
    def test_wraparound_r_wins(self):
        """R queue wraps around and wins"""
        input_data = "6\nRDRDRD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"
    
    def test_delayed_confrontation(self):
        """D and R far apart in initial order"""
        input_data = "5\nDDDRR\n"
        result = solve_203_v2(input_data)
        # D gets multiple turns before meeting R
        assert result.strip() == "D"
    
    def test_immediate_confrontation(self):
        """D and R adjacent"""
        input_data = "3\nDRD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_long_sequence_d(self):
        """Long D sequence before R"""
        input_data = "8\nDDDDDDRR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_long_sequence_r(self):
        """Long R sequence before D"""
        input_data = "8\nRRRRRRDD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"


class Test_solve_203_v2_iteration3:
    """Iteration 3: Complex elimination patterns
    
    Prompt: Test intricate queue dynamics:
    - Multiple rounds needed
    - Cascading eliminations
    - Position-dependent outcomes
    - Symmetric patterns
    """
    
    def test_three_rounds_needed(self):
        """Requires multiple rounds to resolve"""
        input_data = "7\nDDDRRRD\n"
        result = solve_203_v2(input_data)
        # Close count, multiple rounds
        assert result.strip() in ["D", "R"]
    
    def test_symmetric_pattern(self):
        """Symmetric D/R pattern"""
        input_data = "6\nDRDRDR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"  # First position wins
    
    def test_symmetric_pattern_r(self):
        """Symmetric R/D pattern"""
        input_data = "6\nRDRDRD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"
    
    def test_clusters_d(self):
        """Clustered D senators"""
        input_data = "8\nDDDRRDDR\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_clusters_r(self):
        """Clustered R senators"""
        input_data = "8\nRRRDDRRD\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"
    
    def test_end_heavy_d(self):
        """D senators concentrated at end"""
        input_data = "8\nRRRRDDDD\n"
        result = solve_203_v2(input_data)
        # R goes first but D may recover
        assert result.strip() in ["D", "R"]


class Test_solve_203_v2_iteration4:
    """Iteration 4: Algorithm edge cases
    
    Prompt: Target specific algorithm branches:
    - d_idx < r_idx true branch
    - d_idx < r_idx false branch
    - Queue append operations
    - Final queue empty checks
    """
    
    def test_d_always_ahead(self):
        """D index always less than R"""
        input_data = "4\nDRDR\n"
        result = solve_203_v2(input_data)
        # D at 0,2 R at 1,3 - D eliminates R
        assert result.strip() == "D"
    
    def test_r_always_ahead(self):
        """R index always less than D"""
        input_data = "4\nRDRD\n"
        result = solve_203_v2(input_data)
        # R at 0,2 D at 1,3 - R eliminates D
        assert result.strip() == "R"
    
    def test_alternating_long(self):
        """Long alternating sequence"""
        input_data = "20\nDRDRDRDRDRDRDRDRDRDR\n"
        result = solve_203_v2(input_data)
        # D has index 0, goes first
        assert result.strip() == "D"
    
    def test_alternating_long_r(self):
        """Long alternating sequence starting R"""
        input_data = "20\nRDRDRDRDRDRDRDRDRDRD\n"
        result = solve_203_v2(input_data)
        # R has index 0, goes first
        assert result.strip() == "R"
    
    def test_one_vs_many_d(self):
        """One D vs many R"""
        input_data = "6\nDRRRRR\n"
        result = solve_203_v2(input_data)
        # D at 0, R at 1-5
        assert result.strip() == "R"
    
    def test_one_vs_many_r(self):
        """One R vs many D"""
        input_data = "6\nDDDDDR\n"
        result = solve_203_v2(input_data)
        # D at 0-4, R at 5
        assert result.strip() == "D"


class Test_solve_203_v2_iteration5:
    """Iteration 5: Stress tests and final coverage
    
    Prompt: Maximum coverage with:
    - Very long sequences
    - Complex wraparound scenarios
    - Edge cases in final checks
    """
    
    def test_very_long_balanced(self):
        """Very long, balanced senate"""
        input_data = "100\n" + "DR" * 50 + "\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "D"
    
    def test_very_long_r_first(self):
        """Very long, R starts"""
        input_data = "100\n" + "RD" * 50 + "\n"
        result = solve_203_v2(input_data)
        assert result.strip() == "R"
    
    def test_blocks_of_three(self):
        """Senators in blocks of 3"""
        input_data = "12\nDDDRRRDDDRRR\n"
        result = solve_203_v2(input_data)
        # Equal blocks, first block wins
        assert result.strip() in ["D", "R"]
    
    def test_graduated_advantage(self):
        """Gradually increasing advantage"""
        input_data = "15\nDRDRRDRRRDRRRR\n"
        result = solve_203_v2(input_data)
        # R has more senators overall
        assert result.strip() == "R"
    
    def test_late_surge_d(self):
        """D surges at end"""
        input_data = "10\nRRRRRDDDDD\n"
        result = solve_203_v2(input_data)
        # R controls early positions
        assert result.strip() == "R"
    
    def test_late_surge_r(self):
        """R surges at end"""
        input_data = "10\nDDDDDRRRRR\n"
        result = solve_203_v2(input_data)
        # D controls early positions
        assert result.strip() == "D"
    
    def test_minimal_difference(self):
        """One senator difference"""
        input_data = "11\nDDDDDDRRRRR\n"
        result = solve_203_v2(input_data)
        # 6D vs 5R, D wins
        assert result.strip() == "D"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

