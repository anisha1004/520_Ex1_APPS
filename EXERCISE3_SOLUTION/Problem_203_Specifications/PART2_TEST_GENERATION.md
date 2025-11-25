# Exercise 3 - Part 2: Spec-Guided Test Generation for Problem 203

## LLM Prompt for Test Generation

**Prompt:**

```
You are given the following formal specifications for a senate voting simulation function:

SPECIFICATIONS:
1. Result must be either "D\n" or "R\n" (valid output domain)
2. Single senator case: if input has only one senator, that senator's party wins
3. Homogeneous party: if all senators are from the same party, that party wins
4. Two-senator cases: first senator always wins with optimal play (DR → D wins, RD → R wins)
5. Majority with first position: if a party has strict majority AND their senator is first, they win

Function signature: def solve_203_v2(input_str: str) -> str

Input format:
- Line 1: integer n (number of senators)
- Line 2: string of 'D' and 'R' characters

Based on these specifications, generate test cases that:
1. Verify each specification
2. Cover edge cases implied by the specifications
3. Test boundary conditions
4. Test combinations of specifications

For each test, provide:
- Test name
- Input (n and senate string)
- Expected output
- Which specification(s) it tests

Generate 10-12 test cases.
```

---

## Generated Spec-Guided Test Cases

### Test 1: Single D Senator (Spec 2)
**Input:**
```
1
D
```
**Expected Output:** `D\n`  
**Tests:** Specification 2 - single senator wins

---

### Test 2: Single R Senator (Spec 2)
**Input:**
```
1
R
```
**Expected Output:** `R\n`  
**Tests:** Specification 2 - single senator wins

---

### Test 3: All D Senators (Spec 3)
**Input:**
```
5
DDDDD
```
**Expected Output:** `D\n`  
**Tests:** Specification 3 - homogeneous party

---

### Test 4: All R Senators (Spec 3)
**Input:**
```
4
RRRR
```
**Expected Output:** `R\n`  
**Tests:** Specification 3 - homogeneous party

---

### Test 5: Two Senators DR (Spec 4)
**Input:**
```
2
DR
```
**Expected Output:** `D\n`  
**Tests:** Specification 4 - two-senator case, first wins

---

### Test 6: Two Senators RD (Spec 4)
**Input:**
```
2
RD
```
**Expected Output:** `R\n`  
**Tests:** Specification 4 - two-senator case, first wins

---

### Test 7: D Majority with D First (Spec 5)
**Input:**
```
5
DDDRR
```
**Expected Output:** `D\n`  
**Tests:** Specification 5 - majority party with first position

---

### Test 8: R Majority with R First (Spec 5)
**Input:**
```
6
RRRDDD
```
**Expected Output:** `R\n`  
**Tests:** Specification 5 - majority party with first position

---

### Test 9: D Majority, D First (Longer) (Spec 5)
**Input:**
```
9
DDDDRRRRR
```
**Expected Output:** `D\n`  
**Tests:** Specification 5 - equal split with D first (D goes first and wins)

---

### Test 10: Equal Split D First (Spec 4, 5 Combined)
**Input:**
```
4
DDRR
```
**Expected Output:** `D\n`  
**Tests:** Equal count but D is first - first position advantage

---

### Test 11: Equal Split R First (Spec 4, 5 Combined)
**Input:**
```
4
RRDD
```
**Expected Output:** `R\n`  
**Tests:** Equal count but R is first - first position advantage

---

### Test 12: Alternating Pattern D First (Spec 5)
**Input:**
```
6
DRDRDRD
```
**Expected Output:** `D\n`  
**Tests:** Alternating with D first and D majority

---

### Test 13: Alternating Pattern R First (Spec 5)
**Input:**
```
5
RDRDR
```
**Expected Output:** `R\n`  
**Tests:** Alternating with R first

---

### Test 14: Clustered D Majority (Spec 5)
**Input:**
```
7
DDDRRDR
```
**Expected Output:** `D\n`  
**Tests:** Clustered majority with first position

---

### Test 15: Minimal D Majority (Spec 5)
**Input:**
```
3
DDR
```
**Expected Output:** `D\n`  
**Tests:** Minimal majority case (2 vs 1)

---

## Test Implementation

See file: `test_spec_guided_203.py`

---

## Test Case Summary

| Test # | Specification Tested | Test Type | Input Pattern |
|--------|---------------------|-----------|---------------|
| 1-2 | Spec 2 | Single senator | D, R |
| 3-4 | Spec 3 | Homogeneous | DDDDD, RRRR |
| 5-6 | Spec 4 | Two-senator | DR, RD |
| 7-8 | Spec 5 | Majority + First | DDDRR, RRRDDD |
| 9-11 | Spec 5 | Equal/Majority | DDRR, RRDD, DDDDDDDRRR |
| 12-13 | Spec 5 | Alternating | DRDRDRD, RDRDR |
| 14-15 | Spec 5 | Clustered/Minimal | DDDRRDR, DDR |

**Total Tests**: 15 spec-guided tests

---

## Comparison with Exercise 2 Approach

### Exercise 2 (Iterative LLM)
- Started with 75 baseline tests (72% coverage)
- Added 33 targeted tests through 7 iterations
- Focused on: edge cases, queue mechanics, wraparound logic
- Final: 108 tests, 96% coverage

### Exercise 3 (Specification-Guided)
- Start with 75 baseline tests (72% coverage)
- Generate 15 tests based on formal specifications
- Focus on: specification coverage, logical properties, boundary conditions
- Expected: Different test patterns, may or may not improve coverage

### Key Differences
1. **Exercise 2**: Bottom-up, coverage-driven (find uncovered lines)
2. **Exercise 3**: Top-down, specification-driven (verify logical properties)
3. **Exercise 2**: More tests, targeted at specific lines
4. **Exercise 3**: Fewer tests, targeted at specifications


