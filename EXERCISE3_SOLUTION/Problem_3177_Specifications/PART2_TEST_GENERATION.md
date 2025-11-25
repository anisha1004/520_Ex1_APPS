# Exercise 3 - Part 2: Spec-Guided Test Generation for Problem 3177

## LLM Prompt for Test Generation

**Prompt:**

```
You are given the following formal specifications for a permutation sorting function using BFS:

SPECIFICATIONS:
1. Result format is numeric (non-negative integer followed by "\n")
2. Non-negative result: minimum swaps ≥ 0
3. Already sorted requires 0 swaps: if permutation is [1,2,3,...,n], result is 0
4. Reasonable upper bound: result ≤ 50 (since n ≤ 11)
5. Input validation: permutation length equals n, contains 1 to n exactly once
6. Valid permutation: sorted(perm) == [1, 2, ..., n]

Function signature: def solve_3177_v2(input_str: str) -> str

Input format:
- Line 1: n (length) and m (number of allowed swaps)
- Line 2: permutation of 1 to n
- Lines 3 to m+2: allowed swap positions (1-indexed)

Based on these specifications, generate test cases that:
1. Verify each specification
2. Cover edge cases (already sorted, single swap needed, minimum n=2, maximum n=11)
3. Test different allowed swap patterns (adjacent only, non-adjacent, complete graph)
4. Test boundary conditions

For each test, provide:
- Test name
- Full input (n, m, permutation, allowed swaps)
- Expected output
- Which specification(s) it tests

Generate 12-15 test cases.
```

---

## Generated Spec-Guided Test Cases

### Test 1: Already Sorted (Spec 3)
**Input:**
```
3 2
1 2 3
1 2
2 3
```
**Expected Output:** `0\n`  
**Tests:** Specification 3 - already sorted requires 0 swaps

---

### Test 2: Single Swap Needed (Specs 2, 4)
**Input:**
```
2 1
2 1
1 2
```
**Expected Output:** `1\n`  
**Tests:** Specifications 2, 4 - minimal non-zero result

---

### Test 3: Two Swaps Needed (Specs 2, 4)
**Input:**
```
3 2
3 2 1
1 2
2 3
```
**Expected Output:** `2\n`  
**Tests:** Specifications 2, 4 - multiple swaps

---

### Test 4: Minimum N=2 Already Sorted (Specs 3, 5)
**Input:**
```
2 1
1 2
1 2
```
**Expected Output:** `0\n`  
**Tests:** Boundary: minimum n, already sorted

---

### Test 5: Minimum N=2 One Swap (Specs 2, 5)
**Input:**
```
2 1
2 1
1 2
```
**Expected Output:** `1\n`  
**Tests:** Boundary: minimum n, one swap needed

---

### Test 6: Adjacent Swaps Only (Spec 4)
**Input:**
```
4 3
4 3 2 1
1 2
2 3
3 4
```
**Expected Output:** ≤ 6 (depends on BFS)  
**Tests:** Adjacent swaps constraint

---

### Test 7: Non-Adjacent Swaps (Spec 4)
**Input:**
```
4 2
2 1 4 3
1 3
2 4
```
**Expected Output:** `2\n`  
**Tests:** Non-adjacent swap pattern

---

### Test 8: Complete Graph (All Swaps Allowed) (Spec 4)
**Input:**
```
3 3
3 1 2
1 2
1 3
2 3
```
**Expected Output:** `2\n`  
**Tests:** All possible swaps allowed

---

### Test 9: Single Element Out of Place (Spec 2, 4)
**Input:**
```
4 3
1 2 4 3
1 2
2 3
3 4
```
**Expected Output:** `1\n`  
**Tests:** Minimal disorder

---

### Test 10: Cyclic Permutation (Spec 4)
**Input:**
```
5 4
2 3 4 5 1
1 2
2 3
3 4
4 5
```
**Expected Output:** `4\n`  
**Tests:** Cyclic shift pattern

---

### Test 11: Reverse Order (Spec 4)
**Input:**
```
4 3
4 3 2 1
1 2
2 3
3 4
```
**Expected Output:** Multiple swaps needed  
**Tests:** Maximum disorder with adjacent swaps

---

### Test 12: Sparse Allowed Swaps (Spec 2, 4)
**Input:**
```
5 2
2 1 3 4 5
1 2
3 4
```
**Expected Output:** `1\n`  
**Tests:** Limited swap options

---

### Test 13: Large N (Spec 4, 5)
**Input:**
```
8 7
2 1 3 4 5 6 7 8
1 2
2 3
3 4
4 5
5 6
6 7
7 8
```
**Expected Output:** `1\n`  
**Tests:** Larger n with simple fix

---

### Test 14: Multiple Swaps Same Positions (Spec 4)
**Input:**
```
4 4
3 4 1 2
1 2
1 3
2 4
3 4
```
**Expected Output:** `3\n`  
**Tests:** Complex swap dependencies

---

### Test 15: Already Sorted Large (Spec 3, 5)
**Input:**
```
6 5
1 2 3 4 5 6
1 2
2 3
3 4
4 5
5 6
```
**Expected Output:** `0\n`  
**Tests:** Larger n already sorted

---

## Test Implementation

See file: `test_spec_guided_3177.py`

---

## Test Case Summary

| Test # | Specification Tested | Test Type | Permutation Type |
|--------|---------------------|-----------|------------------|
| 1 | Spec 3 | Already sorted | [1,2,3] |
| 2 | Spec 2, 4 | Single swap | [2,1] |
| 3 | Spec 2, 4 | Multiple swaps | [3,2,1] |
| 4-5 | Spec 3, 5 | Boundary (n=2) | Sorted, swapped |
| 6-8 | Spec 4 | Swap patterns | Adjacent, non-adj, complete |
| 9 | Spec 2, 4 | Minimal disorder | One element wrong |
| 10-11 | Spec 4 | Special patterns | Cyclic, reverse |
| 12 | Spec 2, 4 | Sparse swaps | Limited options |
| 13 | Spec 4, 5 | Large n | n=8 |
| 14 | Spec 4 | Complex | Multiple dependencies |
| 15 | Spec 3, 5 | Large sorted | n=6 sorted |

**Total Tests**: 15 spec-guided tests

---

## Comparison with Exercise 2 Approach

### Exercise 2 (Iterative LLM)
- Started with 3 baseline tests (69.7% coverage)
- Added 28 targeted tests through 7 iterations
- Focused on: BFS mechanics, state space exploration, edge cases
- Final: 31 tests, 97% coverage

### Exercise 3 (Specification-Guided)
- Start with 3 baseline tests (69.7% coverage)
- Generate 15 tests based on formal specifications
- Focus on: specification validation, boundary conditions, swap patterns
- Expected: Different test patterns, focus on logical correctness

### Key Differences
1. **Exercise 2**: Coverage-driven, targets specific uncovered lines
2. **Exercise 3**: Specification-driven, validates logical properties
3. **Exercise 2**: More tests, fine-grained coverage improvement
4. **Exercise 3**: Fewer tests, validates correctness guarantees


