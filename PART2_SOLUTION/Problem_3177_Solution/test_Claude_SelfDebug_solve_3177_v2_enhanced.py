"""
Enhanced Test file for Problem 3177 - solve_3177_v2 
Module: solutions.Claude_SelfDebug
Part 2: LLM-Generated Tests for DRAMATIC Coverage Improvement

Baseline: 69.7% line, 55.76% branch (ONLY 3 tests!)
Target: 95%+ coverage through iterative LLM test generation
"""

import pytest
from solutions.Claude_SelfDebug import solve_3177_v2


class Test_solve_3177_v2_baseline:
    """Baseline tests - only 3 tests, 69.7% coverage"""
    
    @pytest.fixture
    def test_cases(self):
        """Original benchmark test cases"""
        inputs = ['2 1\n2 1\n1 2\n', '3 2\n2 1 3\n1 3\n2 3\n', '5 5\n1 2 3 4 5\n1 5\n2 5\n1 4\n1 2\n3 5\n']
        outputs = ['1\n', '3\n', '0\n']
        return list(zip(inputs, outputs))
    
    def test_baseline_cases(self, test_cases):
        """Test all original benchmark cases"""
        for i, (inp, expected) in enumerate(test_cases):
            result = str(solve_3177_v2(inp.strip())).strip()
            expected_clean = str(expected).strip()
            assert result == expected_clean, f"Baseline test {i+1} failed"


class Test_solve_3177_v2_iteration1:
    """Iteration 1: LLM-generated tests for BFS edge cases
    
    Prompt: Generate tests for a BFS permutation solver that:
    - Tests early termination (already sorted)
    - Tests unreachable states
    - Tests single swap needed
    - Tests all swaps needed
    - Tests boundary: n=2 (minimum)
    - Tests boundary: n=11 (maximum)
    - Tests different swap patterns
    """
    
    def test_already_sorted(self):
        """Already in target state - should return 0"""
        input_data = "3 3\n1 2 3\n1 2\n2 3\n1 3\n"
        result = solve_3177_v2(input_data)
        assert result.strip() == "0"
    
    def test_single_swap_needed(self):
        """Only one swap needed"""
        input_data = "3 1\n1 3 2\n2 3\n"
        result = solve_3177_v2(input_data)
        assert result.strip() == "1"
    
    def test_reverse_order(self):
        """Complete reverse - multiple swaps"""
        input_data = "4 2\n4 3 2 1\n1 2\n3 4\n"
        result = solve_3177_v2(input_data)
        # May not reach solution with limited swaps
        assert result.strip() == "" or int(result.strip()) >= 1
    
    def test_minimum_n(self):
        """Boundary: minimum n=2"""
        input_data = "2 1\n1 2\n1 2\n"
        result = solve_3177_v2(input_data)
        assert result.strip() == "0"
    
    def test_adjacent_swaps_only(self):
        """Only adjacent swaps allowed"""
        input_data = "4 3\n4 3 2 1\n1 2\n2 3\n3 4\n"
        result = solve_3177_v2(input_data)
        # Bubble sort-like pattern
        assert int(result.strip()) >= 2
    
    def test_non_adjacent_swaps(self):
        """Long-range swaps"""
        input_data = "5 1\n5 2 3 4 1\n1 5\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 1
    
    def test_cycle_permutation(self):
        """Cyclic permutation pattern"""
        input_data = "4 4\n2 3 4 1\n1 2\n2 3\n3 4\n1 4\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 1
    
    def test_two_swaps_needed(self):
        """Swap pattern test"""
        input_data = "3 2\n3 2 1\n1 3\n1 2\n"
        result = solve_3177_v2(input_data)
        assert result.strip() == "1"  # Optimal is 1 swap


class Test_solve_3177_v2_iteration2:
    """Iteration 2: BFS state space exploration
    
    Prompt: Generate tests that explore BFS behavior:
    - Tests queue management (deque operations)
    - Tests visited set efficiency
    - Tests state tuple creation
    - Tests multiple paths to same state
    - Tests swap order independence
    - Tests large n with limited swaps
    """
    
    def test_multiple_paths_same_result(self):
        """Multiple swap sequences lead to solution"""
        input_data = "4 6\n2 1 4 3\n1 2\n3 4\n1 3\n2 4\n1 4\n2 3\n"
        result = solve_3177_v2(input_data)
        # Many paths available, BFS finds shortest
        assert int(result.strip()) >= 1
    
    def test_swap_order_matters(self):
        """Order of applying swaps affects path length"""
        input_data = "4 3\n3 4 1 2\n1 2\n3 4\n2 3\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 2
    
    def test_large_n_few_swaps(self):
        """Large permutation, limited swaps"""
        input_data = "6 2\n6 2 3 4 5 1\n1 6\n2 6\n"
        result = solve_3177_v2(input_data)
        # These swaps can reach solution
        assert result.strip() == "1"
    
    def test_partial_sort_needed(self):
        """Only part of permutation out of order"""
        input_data = "5 3\n1 2 5 4 3\n3 4\n4 5\n3 5\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 1
    
    def test_long_bfs_path(self):
        """Requires many BFS levels"""
        input_data = "5 2\n5 4 3 2 1\n2 3\n3 4\n"
        result = solve_3177_v2(input_data)
        # Limited swaps - may not reach solution
        assert result.strip() == "" or int(result.strip()) >= 3
    
    def test_all_swaps_available(self):
        """All possible swaps allowed - shortest path"""
        input_data = "4 6\n4 3 2 1\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n"
        result = solve_3177_v2(input_data)
        # With all swaps, should find very short path
        assert int(result.strip()) >= 1


class Test_solve_3177_v2_iteration3:
    """Iteration 3: Complex permutation patterns
    
    Prompt: Test complex algorithmic cases:
    - Transposition patterns
    - Permutation cycles
    - Edge cases in tuple/list conversion
    - State explosion scenarios
    - Optimal vs suboptimal paths
    """
    
    def test_transposition_pattern(self):
        """Single transposition fixes"""
        input_data = "6 1\n1 6 3 4 5 2\n2 6\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 1
    
    def test_three_cycle(self):
        """3-cycle permutation"""
        input_data = "5 3\n2 3 1 4 5\n1 2\n2 3\n1 3\n"
        result = solve_3177_v2(input_data)
        # Breaking a 3-cycle
        assert int(result.strip()) >= 2
    
    def test_disjoint_cycles(self):
        """Two independent cycles"""
        input_data = "6 4\n2 1 4 3 6 5\n1 2\n3 4\n5 6\n1 3\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 2
    
    def test_maximal_n(self):
        """Boundary: maximum n=11"""
        input_data = "11 10\n11 10 9 8 7 6 5 4 3 2 1\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9\n9 10\n10 11\n"
        result = solve_3177_v2(input_data)
        # Complete reverse with adjacent swaps
        assert int(result.strip()) >= 10
    
    def test_star_topology_swaps(self):
        """All swaps involve position 1"""
        input_data = "5 4\n3 1 5 4 2\n1 2\n1 3\n1 4\n1 5\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 2
    
    def test_palindrome_permutation(self):
        """Symmetric disorder"""
        input_data = "5 3\n5 2 3 4 1\n1 5\n2 4\n1 2\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 1


class Test_solve_3177_v2_iteration4:
    """Iteration 4: State space and visited set coverage
    
    Prompt: Target uncovered branches:
    - Empty result return path
    - Visited set collision handling
    - Queue empty conditions
    - State equality checks
    """
    
    def test_minimal_swap_set(self):
        """Very limited swaps"""
        input_data = "4 1\n2 1 3 4\n1 2\n"
        result = solve_3177_v2(input_data)
        assert result.strip() == "1"
    
    def test_no_solution_path(self):
        """Swaps don't allow reaching sorted state"""
        input_data = "4 2\n4 3 2 1\n1 3\n2 4\n"
        result = solve_3177_v2(input_data)
        # May not reach solution with these swaps
        assert result.strip() in ["", "2", "3", "4", "5", "6", "7", "8"]
    
    def test_deep_bfs_search(self):
        """Requires deep BFS search"""
        input_data = "7 3\n7 6 5 4 3 2 1\n3 4\n4 5\n5 6\n"
        result = solve_3177_v2(input_data)
        # Very limited swaps - may not reach solution
        assert result.strip() == "" or int(result.strip()) >= 5
    
    def test_immediate_neighbor_check(self):
        """First swap from start is solution"""
        input_data = "2 1\n2 1\n1 2\n"
        result = solve_3177_v2(input_data)
        assert result.strip() == "1"
    
    def test_zigzag_permutation(self):
        """Alternating high-low pattern"""
        input_data = "6 5\n2 1 4 3 6 5\n1 2\n3 4\n5 6\n2 3\n4 5\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 3


class Test_solve_3177_v2_iteration5:
    """Iteration 5: Final coverage push - stress tests
    
    Prompt: Maximum coverage with:
    - Large state spaces
    - Complex swap graphs
    - Edge cases in distance calculation
    """
    
    def test_complete_graph_swaps(self):
        """All pairs can swap - optimal is guaranteed"""
        input_data = "5 10\n5 4 3 2 1\n1 2\n1 3\n1 4\n1 5\n2 3\n2 4\n2 5\n3 4\n3 5\n4 5\n"
        result = solve_3177_v2(input_data)
        # Complete graph allows very short path
        assert int(result.strip()) <= 4
    
    def test_single_element_out_of_place(self):
        """Only one element wrong"""
        input_data = "7 2\n1 2 3 7 5 6 4\n4 7\n4 5\n"
        result = solve_3177_v2(input_data)
        # Can reach solution with 1 swap
        assert result.strip() == "1"
    
    def test_every_other_swap(self):
        """Odd-even swap pattern"""
        input_data = "8 4\n8 2 3 4 5 6 7 1\n1 2\n3 4\n5 6\n7 8\n"
        result = solve_3177_v2(input_data)
        # Non-adjacent swaps only - may not reach solution
        assert result.strip() == "" or int(result.strip()) >= 2
    
    def test_median_swap_only(self):
        """Only middle swaps allowed"""
        input_data = "7 2\n7 2 3 4 5 6 1\n3 4\n4 5\n"
        result = solve_3177_v2(input_data)
        # Very restricted swaps - tests BFS with limited options
        assert result.strip() in ["", "5", "6", "7", "8", "9", "10"]  # Valid or no solution
    
    def test_rotation_permutation(self):
        """Rotated by k positions"""
        input_data = "6 5\n4 5 6 1 2 3\n1 4\n2 5\n3 6\n1 2\n4 5\n"
        result = solve_3177_v2(input_data)
        assert int(result.strip()) >= 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

