# Exercise 3 - Coverage Comparison Report


## Problem 203: Senate Voting Simulation

### Function Details
- **Function**: `solve_203_v2` (Claude_SelfDebug.py, lines 409-433)
- **Algorithm**: Dual-queue simulation with index-based elimination
- **Complexity**: 25 lines, moderate branching logic

### Coverage Results

| Approach | Line Coverage | Branch Coverage | Tests | Improvement |
|----------|---------------|-----------------|-------|-------------|
| **Exercise 2 - Baseline** | 72.0% | 57.6% | 75 | - |
| **Exercise 2 - Final (Iterative)** | 96.0% | 92.0% | 108 | +24.0% line |
| **Exercise 3 - Spec-Guided** | 72.0% | ~57.6% | 30 | +0.0% line |

### Analysis


The specification-guided tests achieved **exactly the same coverage** as the Exercise 2 baseline (72%). This is because:

1. **Baseline Already Had Many Tests**: The baseline included 75 tests from the benchmark suite, which covered basic scenarios.

2. **Specifications Capture High-Level Properties**: The formal specifications we generated focused on:
   - Valid output domain ("D\n" or "R\n")
   - Single senator cases
   - Homogeneous party cases
   - Two-senator optimal play
   - Majority with first position advantage

3. **These Properties Were Already Tested**: The baseline tests already covered these high-level behaviors. The spec-guided tests validated **correctness** but didn't discover **new code paths**.

4. **Missing Coverage Requires Low-Level Analysis**: The uncovered lines (28%) in Exercise 2 baseline were:
   - Specific queue wraparound mechanics (lines 429, 431)
   - Edge cases in index comparison logic
   - Specific branch conditions in the elimination loop
   
   These require **code-level analysis** (as done in Exercise 2 iterative approach), not specification-level reasoning.

### Key Insight

**Specification-guided testing validates correctness guarantees but doesn't necessarily improve coverage.**

The 30 spec-guided tests successfully validated that the function:
- Returns valid outputs
- Handles edge cases (single senator, homogeneous party)
- Implements correct elimination logic for simple cases

However, they didn't target the **specific uncovered lines** that Exercise 2's iterative approach found through coverage feedback.

---

## Problem 3177: BFS Permutation Sorting

### Function Details
- **Function**: `solve_3177_v2` (Claude_SelfDebug.py, lines 507-539)
- **Algorithm**: BFS state-space search for minimum swaps
- **Complexity**: 33 lines, complex state exploration

### Coverage Results

| Approach | Line Coverage | Branch Coverage | Tests | Improvement |
|----------|---------------|-----------------|-------|-------------|
| **Exercise 2 - Baseline** | 69.7% | 55.76% | 3 | - |
| **Exercise 2 - Final (Iterative)** | 97.0% | 93.9% | 31 | +27.3% line |
| **Exercise 3 - Spec-Guided** | 72.73% | ~58.18% | 28 | +3.0% line |

### Analysis

**Small Coverage Increase (+3%)**

The specification-guided tests achieved a **slight improvement** of 3% over the baseline. Here's why:

1. **Baseline Had Only 3 Tests**: Unlike Problem 203, the baseline had minimal test coverage, leaving many paths unexplored.

2. **Specifications Added Basic Coverage**: The spec-guided tests covered:
   - Already sorted cases (immediate return)
   - Format validation
   - Boundary conditions (n=2)
   - Simple swap patterns
   
   These added **some** coverage that the baseline missed.

3. **Still Missing BFS Internals**: The remaining uncovered code (27%) includes:
   - Visited set collision handling
   - Empty return path (unreachable states)
   - Complex state space exploration
   - Queue management edge cases
   
   These require **targeted test generation** based on coverage analysis, not specifications.

### Key Insight

**Specifications help when baseline is weak, but still fall short of coverage-driven approaches.**

The 28 spec-guided tests improved coverage slightly by adding fundamental test cases (sorted, minimal swaps, boundary conditions). However, to reach 97% coverage (like Exercise 2), we would need:
- Coverage-guided iteration
- Targeted tests for BFS mechanics
- Edge cases for state space exploration

---

## Overall Comparison


### Coverage Achievement

| Problem | Exercise 2 Final | Exercise 3 Final | Difference |
|---------|------------------|------------------|------------|
| **203** | 96.0% line | 72.0% line | **-24.0%** |
| **3177** | 97.0% line | 72.73% line | **-24.3%** |

### Key Findings

1. **Specification-guided testing alone cannot match coverage-driven iteration.**
   - Exercise 2: 96-97% coverage
   - Exercise 3: 72-73% coverage
   - Gap: ~24%

2. **Specifications validate correctness, not completeness.**
   - Spec-guided tests ensure the function behaves correctly for specified properties
   - They don't necessarily explore all code paths

3. **Baseline matters.**
   - Problem 203: 75 baseline tests → no improvement from specs
   - Problem 3177: 3 baseline tests → small improvement from specs

4. **Combined approach would be ideal.**
   - Use specifications to define correctness properties
   - Use coverage-guided iteration to ensure completeness
   - Best of both worlds: correct AND comprehensive

