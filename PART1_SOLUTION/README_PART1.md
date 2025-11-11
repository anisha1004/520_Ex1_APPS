# Part 1 - Baseline Coverage

## 📋 Overview

This folder contains all artifacts for **Part 1: Baseline Coverage Analysis** of Exercise 2.

---

## 📂 Files

### 1. **PART1_BASELINE_COVERAGE_REPORT.md** ⭐
**THIS IS YOUR MAIN DELIVERABLE**

Contains:
- Summary table with all 120 functions
- Line and branch coverage for each
- Test pass/fail status
- One-line interpretations
- Selection of 2 problems for Parts 2-3
- Detailed analysis per problem
- Key insights about coverage vs. correctness

### 2. **reports/function_coverage_accurate.csv**
Raw coverage data for all 120 functions (10 problems × 4 modules × 3 variants each)

### 3. **analyze_function_coverage.py**
Script for per-function coverage analysis (sample mode - 4 functions)

### 4. **run_comprehensive_function_coverage.py**
Script for comprehensive coverage analysis (all 120 functions)

### 5. **HOW_TO_RUN.md**
Detailed instructions on running the coverage analysis scripts

### 6. **START_HERE.md**
Original getting started guide (historical reference)

### 7. **CORRECTED_COVERAGE_SUMMARY.md**
Technical explanation of the per-function coverage approach

### 8. **coverage.json**
Most recent coverage output (JSON format)

---

## 🚀 How to Run Coverage Analysis

### Quick Sample (4 functions, ~30 seconds):
```bash
cd /Users/anpandey/Documents/Doll/520_Ex1_APPS/PART1_SOLUTION
python analyze_function_coverage.py
```

### Full Analysis (120 functions, ~10 minutes):
```bash
cd /Users/anpandey/Documents/Doll/520_Ex1_APPS/PART1_SOLUTION
python run_comprehensive_function_coverage.py
```

**Output**: Results saved to `reports/function_coverage_accurate.csv`

---

## 📊 Key Results

### Overall Statistics:
- **Total Functions Analyzed**: 120
- **Functions Passing Tests**: 87 (72.5%)
- **Average Line Coverage**: 91.8% (passing functions)
- **Average Branch Coverage**: 73.4% (passing functions)

### Problems Selected for Parts 2-3:

**Problem 1: 3177 (Claude_SelfDebug)**
- Tests Passed: 6/6 ✅
- Line Coverage: 71.0%
- Branch Coverage: 56.8% (**lowest among passing**)
- Algorithm: BFS state-space search

**Problem 2: 203 (Claude_SelfDebug)**
- Tests Passed: 6/6 ✅
- Line Coverage: 76.0%
- Branch Coverage: 60.8% (**second lowest among passing**)
- Algorithm: Dual-queue voting simulation

---

## 📈 Summary Table (Top 10 Modules)

| Module | Problem | Tests Passed | Avg Line % | Avg Branch % |
|--------|---------|--------------|------------|--------------|
| GPT_CoT | 1303 | 6/6 ✅ | 100.0% | 80.0% |
| GPT_CoT | 4245 | 6/6 ✅ | 100.0% | 80.0% |
| GPT_SelfDebug | 4245 | 6/6 ✅ | 100.0% | 80.0% |
| Claude_CoT | 1303 | 6/6 ✅ | 97.92% | 78.33% |
| GPT_SelfDebug | 1303 | 6/6 ✅ | 96.63% | 77.31% |
| GPT_CoT | 3040 | 6/6 ✅ | 95.92% | 76.74% |
| Claude_CoT | 3177 | 6/6 ✅ | 95.74% | 76.59% |
| GPT_CoT | 3177 | 6/6 ✅ | 95.28% | 76.22% |
| GPT_SelfDebug | 3177 | 6/6 ✅ | 92.22% | 73.78% |
| **Claude_SelfDebug** | **203** | **6/6 ✅** | **76.0%** | **60.8%** ⭐ |
| **Claude_SelfDebug** | **3177** | **6/6 ✅** | **71.0%** | **56.8%** ⭐ |

⭐ = Selected for Parts 2-3

---

## 🎯 Selection Rationale

**Why these 2 problems?**

1. **All tests pass** (quality baseline to build upon)
2. **Lowest branch coverage** (maximum room for improvement)
3. **Complex algorithms** (BFS, queue logic with many conditional paths)
4. **Clear gaps** (20-25% coverage improvement potential)

**Not selected**: Problems that fail tests (need correctness fixes first) or already have high coverage (little room for improvement)

---

## 🔍 Key Insights from Part 1

### 1. Coverage ≠ Correctness
- 18 functions have 100% coverage but FAIL all tests
- Example: Problem 4655 (GPT_CoT) - perfect coverage, all tests fail
- Coverage is necessary but not sufficient

### 2. Significant Coverage Gaps
- Selected problems have 56-62% branch coverage
- Average for passing functions is 73.4%
- 15-20% below average = substantial room for improvement

### 3. Test Quality Variation
- Benchmark tests range from 55% to 80% branch coverage
- Some problems have excellent baseline (1303: 100%)
- Others have weak baselines (3177: 56%, 203: 61%)

### 4. Algorithm Complexity Matters
- Simple problems (4245): 100% coverage easy to achieve
- Complex algorithms (BFS, queues): Many untested paths
- LLM-assisted testing most valuable for complex problems

---

## 📄 For Submission

**Main Deliverable**: `PART1_BASELINE_COVERAGE_REPORT.md`

This report contains:
- ✅ Automated coverage setup description
- ✅ Tests passed for each problem
- ✅ Line and branch coverage for all functions
- ✅ One-line interpretation for each
- ✅ Comprehensive summary table
- ✅ Selection of 2 problems for Parts 2-3
- ✅ Explicit module/package names

---

## 🔗 Related

- **Part 2 (Test Generation)**: `../PART2_SOLUTION/`
- **Part 3 (Fault Detection)**: `../PART3_SOLUTION/`
- **Master Index**: `../MASTER_INDEX.md`

---

## ✅ Requirements Met

✅ Automated coverage collection (pytest-cov)  
✅ Number of tests passed (per function)  
✅ Line coverage (all 120 functions)  
✅ Branch coverage (all 120 functions)  
✅ One-line interpretations (all entries)  
✅ Summary table (comprehensive)  
✅ Problem selection (2 with room for improvement)  
✅ Module/package names (explicit)  

---

**Status**: Part 1 Complete ✅  
**Date**: November 10, 2025  
**Tool**: pytest-cov with per-function AST analysis  
**Data**: 120 functions across 10 problems and 4 modules

