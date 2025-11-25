"""
Specification-Guided Tests for Problem 203 (Senate Voting)
Exercise 3 - Part 2

These tests are generated based on formal specifications, not coverage analysis.
They verify logical properties of the senate voting algorithm.
"""

import pytest
import sys
sys.path.append('/Users/anpandey/Documents/Doll/520_LLM/solutions')
from Claude_SelfDebug import solve_203_v2


class TestSpecification1_ValidOutput:
    """Spec 1: Result must be either 'D\\n' or 'R\\n'"""
    
    def test_output_is_valid_d(self):
        result = solve_203_v2("1\nD")
        assert result in ["D\n", "R\n"], "Output must be D\\n or R\\n"
        
    def test_output_is_valid_r(self):
        result = solve_203_v2("1\nR")
        assert result in ["D\n", "R\n"], "Output must be D\\n or R\\n"


class TestSpecification2_SingleSenator:
    """Spec 2: Single senator - that senator's party wins"""
    
    def test_single_d_senator(self):
        """Single D senator should result in D winning"""
        result = solve_203_v2("1\nD")
        assert result == "D\n", "Single D senator should win"
    
    def test_single_r_senator(self):
        """Single R senator should result in R winning"""
        result = solve_203_v2("1\nR")
        assert result == "R\n", "Single R senator should win"


class TestSpecification3_HomogeneousParty:
    """Spec 3: All senators from same party - that party wins"""
    
    def test_all_d_senators_small(self):
        """All D senators (n=3) should result in D winning"""
        result = solve_203_v2("3\nDDD")
        assert result == "D\n", "All D senators should win"
    
    def test_all_d_senators_medium(self):
        """All D senators (n=5) should result in D winning"""
        result = solve_203_v2("5\nDDDDD")
        assert result == "D\n", "All D senators should win"
    
    def test_all_r_senators_small(self):
        """All R senators (n=3) should result in R winning"""
        result = solve_203_v2("3\nRRR")
        assert result == "R\n", "All R senators should win"
    
    def test_all_r_senators_medium(self):
        """All R senators (n=4) should result in R winning"""
        result = solve_203_v2("4\nRRRR")
        assert result == "R\n", "All R senators should win"


class TestSpecification4_TwoSenatorCases:
    """Spec 4: Two senators - first senator wins with optimal play"""
    
    def test_two_senators_dr(self):
        """DR: D goes first and eliminates R"""
        result = solve_203_v2("2\nDR")
        assert result == "D\n", "D should win when first in DR"
    
    def test_two_senators_rd(self):
        """RD: R goes first and eliminates D"""
        result = solve_203_v2("2\nRD")
        assert result == "R\n", "R should win when first in RD"


class TestSpecification5_MajorityWithFirstPosition:
    """Spec 5: Party with majority and first position wins"""
    
    def test_d_majority_d_first_3v2(self):
        """D has 3 senators, R has 2, D is first"""
        result = solve_203_v2("5\nDDDRR")
        assert result == "D\n", "D with majority and first position should win"
    
    def test_r_majority_r_first_3v2(self):
        """R has 3 senators, D has 2, R is first"""
        result = solve_203_v2("5\nRRRDD")
        assert result == "R\n", "R with majority and first position should win"
    
    def test_d_majority_d_first_4v3(self):
        """D has 4 senators, R has 3, D is first"""
        result = solve_203_v2("7\nDDDDRRR")
        assert result == "D\n", "D with majority and first position should win"
    
    def test_r_majority_r_first_4v2(self):
        """R has 4 senators, D has 2, R is first"""
        result = solve_203_v2("6\nRRRRDD")
        assert result == "R\n", "R with majority and first position should win"


class TestSpecification5_EqualCountFirstPosition:
    """Spec 5 Extension: Equal count - first position wins"""
    
    def test_equal_count_d_first_2v2(self):
        """Equal count 2v2, D is first"""
        result = solve_203_v2("4\nDDRR")
        assert result == "D\n", "D first with equal count should win"
    
    def test_equal_count_r_first_2v2(self):
        """Equal count 2v2, R is first"""
        result = solve_203_v2("4\nRRDD")
        assert result == "R\n", "R first with equal count should win"
    
    def test_equal_count_d_first_3v3(self):
        """Equal count 3v3, D is first"""
        result = solve_203_v2("6\nDDDRRR")
        assert result == "D\n", "D first with equal count should win"
    
    def test_equal_count_r_first_3v3(self):
        """Equal count 3v3, R is first"""
        result = solve_203_v2("6\nRRRDDD")
        assert result == "R\n", "R first with equal count should win"


class TestSpecificationCombined_AlternatingPatterns:
    """Combined: Test alternating patterns with different first positions"""
    
    def test_alternating_d_first_4_senators(self):
        """Alternating DRDR pattern"""
        result = solve_203_v2("4\nDRDR")
        assert result == "D\n", "D first in alternating pattern should win"
    
    def test_alternating_r_first_4_senators(self):
        """Alternating RDRD pattern"""
        result = solve_203_v2("4\nRDRD")
        assert result == "R\n", "R first in alternating pattern should win"
    
    def test_alternating_d_first_5_senators(self):
        """Alternating DRDRD pattern (D has majority)"""
        result = solve_203_v2("5\nDRDRD")
        assert result == "D\n", "D first with majority in alternating should win"
    
    def test_alternating_r_first_5_senators(self):
        """Alternating RDRDR pattern (R has majority)"""
        result = solve_203_v2("5\nRDRDR")
        assert result == "R\n", "R first with majority in alternating should win"


class TestSpecificationBoundary_MinimalMajority:
    """Boundary: Test minimal majority cases (2v1, 3v2, etc.)"""
    
    def test_minimal_d_majority_2v1(self):
        """D has 2, R has 1, D is first"""
        result = solve_203_v2("3\nDDR")
        assert result == "D\n", "D with minimal majority should win"
    
    def test_minimal_r_majority_2v1(self):
        """R has 2, D has 1, R is first"""
        result = solve_203_v2("3\nRRD")
        assert result == "R\n", "R with minimal majority should win"
    
    def test_minimal_d_majority_3v2(self):
        """D has 3, R has 2, D is first"""
        result = solve_203_v2("5\nDDDRR")
        assert result == "D\n", "D with minimal majority should win"


class TestSpecificationBoundary_ClusteredPatterns:
    """Boundary: Test clustered senator patterns"""
    
    def test_clustered_d_majority_at_start(self):
        """D senators clustered at start: DDDRRR"""
        result = solve_203_v2("6\nDDDRRR")
        assert result == "D\n", "D clustered at start with equal count should win"
    
    def test_clustered_r_majority_at_start(self):
        """R senators clustered at start: RRRDDD"""
        result = solve_203_v2("6\nRRRDDD")
        assert result == "R\n", "R clustered at start with equal count should win"
    
    def test_mixed_clustering_d_first(self):
        """Mixed clustering with D first: DDDRRDR"""
        result = solve_203_v2("7\nDDDRRDR")
        assert result == "D\n", "D with majority and first position should win"


# Summary of spec-guided tests
def test_summary():
    """
    Summary of Specification-Guided Tests:
    
    Total: 30 tests
    - Spec 1 (Valid Output): 2 tests
    - Spec 2 (Single Senator): 2 tests
    - Spec 3 (Homogeneous): 4 tests
    - Spec 4 (Two Senators): 2 tests
    - Spec 5 (Majority + First): 4 + 4 = 8 tests
    - Combined (Alternating): 4 tests
    - Boundary (Minimal Majority): 3 tests
    - Boundary (Clustered): 3 tests
    
    Focus: Logical properties and specifications
    Goal: Verify correctness based on formal specs, compare coverage with Exercise 2
    """
    assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

