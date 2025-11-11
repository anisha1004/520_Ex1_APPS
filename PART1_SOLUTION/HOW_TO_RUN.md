# How to Run Tests and Check Coverage

## 📋 Prerequisites

Make sure you have the virtual environment activated:

```bash
cd /Users/anpandey/Downloads/520_Ex1_APPS
source venv/bin/activate
```

---

## 🚀 Quick Start (Recommended)

### Option 1: Quick Sample (4 functions, ~30 seconds)

```bash
python analyze_function_coverage.py
```

**Output**: Coverage results for 4 sample functions  
**Good for**: Quick verification, testing the setup

### Option 2: Full Analysis (120 functions, ~10 minutes)

```bash
python run_comprehensive_function_coverage.py
```

**Output**: 
- `reports/function_coverage_accurate.csv` - Complete results
- Console summary with statistics

**Good for**: Complete baseline coverage report

---

## 📝 Step-by-Step Guide

### Step 1: Generate Test Files (One-time Setup)

**If tests/ directory doesn't exist**, generate test files:

```bash
python generate_tests.py
```

**Output**: Creates 120 test files in `tests/` directory  
**Time**: ~5 seconds

**Verify**:
```bash
ls tests/ | wc -l
# Should show 121 (120 test files + __init__.py)
```

---

### Step 2: Run Coverage Analysis

#### Option A: Quick Sample (Recommended First)

```bash
python analyze_function_coverage.py
```

**What it does**:
- Tests 4 sample functions
- Shows accurate per-function coverage
- Displays results in console

**Example Output**:
```
Analyzing: GPT_CoT - solve_1079_v1
  ✅ Tests: 25/25
  📊 Line Coverage: 90.5%
     (19/21 lines)
  🔀 Branch Coverage: 72.4% (estimated)
```

#### Option B: Comprehensive Analysis

```bash
python run_comprehensive_function_coverage.py
```

**What it does**:
- Tests all 120 functions
- Generates CSV report
- Shows summary statistics

**Time**: ~10 minutes (1 pytest run per function)

**Output File**: `reports/function_coverage_accurate.csv`

---

### Step 3: View Results

#### Console Output

The script shows:
- Progress (every 10 functions)
- Summary statistics by module
- Overall averages
- Top 10 by coverage
- Bottom 10 by coverage

#### CSV File

```bash
# View the full CSV
cat reports/function_coverage_accurate.csv

# View just the header
head -1 reports/function_coverage_accurate.csv

# View first 10 results
head -11 reports/function_coverage_accurate.csv

# Count passing tests
grep "PASS" reports/function_coverage_accurate.csv | wc -l

# Find high coverage functions (>90%)
awk -F',' '$6 > 90 {print $0}' reports/function_coverage_accurate.csv
```

---

## 🔍 Testing Individual Functions

### Test a Single Function

```bash
# Example: Test GPT_CoT solve_1079_v1
pytest tests/test_GPT_CoT_solve_1079_v1.py \
  --cov=solutions.GPT_CoT \
  --cov-report=term-missing \
  --cov-branch \
  -v
```

**Output**: Shows which lines were executed and which were missed

### Test All Variants of One Problem

```bash
# Example: Test all Problem 1079 variants
pytest tests/test_*_solve_1079_*.py \
  --cov=solutions \
  --cov-report=term \
  --cov-branch
```

### Test One Module

```bash
# Example: Test all GPT_CoT functions
pytest tests/test_GPT_CoT_*.py \
  --cov=solutions.GPT_CoT \
  --cov-report=html \
  --cov-branch
```

**Output**: Creates `htmlcov/` directory with visual coverage report

---

## 📊 Understanding the Results

### CSV Columns

```csv
module,problem_id,variant,tests_passed,tests_total,
line_coverage,branch_coverage,lines_in_function,
lines_executed,status
```

**Example Row**:
```csv
GPT_CoT,1079,solve_1079_v1,25,25,90.5,72.4,21,19,PASS
```

**Meaning**:
- Module: `GPT_CoT`
- Problem: `1079`
- Variant: `solve_1079_v1`
- Tests: 25 passed out of 25 total
- Line Coverage: 90.5% (19 of 21 lines executed)
- Branch Coverage: 72.4% (estimated)
- Status: PASS (all tests passed)

---

## 🎯 Common Use Cases

### 1. Check Coverage for a Specific Problem

```bash
# Example: Problem 747
grep "747" reports/function_coverage_accurate.csv
```

### 2. Find Functions with Low Coverage

```bash
# Find functions with <80% coverage
awk -F',' '$6 < 80 && $10 == "PASS" {print $3, $6"%"}' \
  reports/function_coverage_accurate.csv
```

### 3. Compare Modules

```bash
# GPT_CoT results
grep "^GPT_CoT," reports/function_coverage_accurate.csv | \
  awk -F',' '{sum+=$6; count++} END {print "Avg:", sum/count "%"}'

# Claude_CoT results  
grep "^Claude_CoT," reports/function_coverage_accurate.csv | \
  awk -F',' '{sum+=$6; count++} END {print "Avg:", sum/count "%"}'
```

---

## 🔧 Troubleshooting

### Issue: "tests/ directory not found"

**Solution**: Run test generation
```bash
python generate_tests.py
```

### Issue: "ModuleNotFoundError: No module named 'pytest'"

**Solution**: Install dependencies
```bash
pip install pytest pytest-cov
```

### Issue: "Coverage file not generated"

**Solution**: Make sure you're in the project directory
```bash
cd /Users/anpandey/Downloads/520_Ex1_APPS
source venv/bin/activate
```

### Issue: Script takes too long

**Solution**: Use the quick sample first
```bash
python analyze_function_coverage.py
```

---

## 📈 Interpreting Coverage Percentages

| Coverage | Quality | Action Needed |
|----------|---------|---------------|
| **90-100%** | Excellent | Minimal - just edge cases |
| **80-90%** | Good | Add tests for uncovered branches |
| **70-80%** | Moderate | Review untested paths |
| **<70%** | Low | Significant testing gaps |

---

## 🎓 Complete Workflow

### First Time Setup

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Generate test files
python generate_tests.py

# 3. Quick verification
python analyze_function_coverage.py
```

### For Submission

```bash
# 1. Run comprehensive analysis
python run_comprehensive_function_coverage.py

# 2. View results
cat reports/function_coverage_accurate.csv

# 3. Check documentation
cat FINAL_PART1_REPORT.md
```

### For Development/Debugging

```bash
# Test specific function
pytest tests/test_GPT_CoT_solve_1079_v1.py -v

# Generate HTML coverage report
pytest tests/test_GPT_CoT_solve_1079_v1.py \
  --cov=solutions.GPT_CoT \
  --cov-report=html

# Open in browser
open htmlcov/index.html
```

---

## 📁 Output Files

| File | Purpose | When Created |
|------|---------|--------------|
| `reports/function_coverage_accurate.csv` | Main results | After comprehensive run |
| `coverage.json` | Intermediate data | After each pytest run (auto-cleaned) |
| `.coverage` | Coverage database | After each pytest run (auto-cleaned) |
| `htmlcov/` | Visual report | When using `--cov-report=html` |

---

## ⚡ Quick Commands Reference

```bash
# Quick sample
python analyze_function_coverage.py

# Full analysis
python run_comprehensive_function_coverage.py

# Single function
pytest tests/test_GPT_CoT_solve_1079_v1.py --cov=solutions.GPT_CoT --cov-report=term -v

# View results
cat reports/function_coverage_accurate.csv

# Summary statistics
tail -30 # (from comprehensive run output)
```

---

## 📚 Related Documentation

- **START_HERE.md** - Master overview
- **QUICK_REFERENCE.md** - Quick summary
- **FINAL_PART1_REPORT.md** - Complete analysis
- **CORRECTED_COVERAGE_SUMMARY.md** - Technical details

---

**Need Help?** Check START_HERE.md for troubleshooting and FAQs.

