# run_custom_eval.py
import importlib
import json
from pathlib import Path

# ---------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------
DATASET_PATH = Path("data/apps_10.jsonl")

# Fully-qualified module names (because solutions is now a package)
SOLUTION_MODULES = [
    "solutions.GPT_CoT",
    "solutions.GPT_SelfDebug",
    "solutions.Gemini_CoT",
    "solutions.Gemini_SelfDebug",
]

# ---------------------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------------------
if not DATASET_PATH.exists():
    raise FileNotFoundError(f"Dataset file not found: {DATASET_PATH}")

records = [json.loads(line) for line in open(DATASET_PATH, "r", encoding="utf-8")]

# ---------------------------------------------------------------------
# EVALUATION LOGIC
# ---------------------------------------------------------------------
def evaluate_module(module, records):
    """Run every problem in the dataset against one solution module."""
    results = []
    for rec in records:
        pid = rec["problem_id"]
        fn_name = f"solve_{pid}"

        if not hasattr(module, fn_name):
            print(f"⚠️  {module.__name__}: missing {fn_name}")
            continue

        fn = getattr(module, fn_name)
        io_field = rec["input_output"]
        if isinstance(io_field, str):
            try:
                io_field = json.loads(io_field)
            except Exception:
                io_field = {}
        inputs = io_field.get("inputs", [])
        outputs = io_field.get("outputs", [])

        total = len(inputs)
        passed_cases = 0
        for inp, exp in zip(inputs, outputs):
            try:
                out = fn(inp.strip())
                got = str(out).strip()
                exp_clean = str(exp).strip()
                ok = got == exp_clean
                passed_cases += int(ok)
                if not ok:
                    print(f"❌ {module.__name__} - {pid} failed:\n"
                          f"Input:\n{inp}\nExpected:\n{exp_clean}\nGot:\n{got}\n")
            except Exception as e:
                print(f"💥 {module.__name__} - {pid} exception: {type(e).__name__}: {e}")

        passed = passed_cases == total and total > 0
        results.append(passed)
        print(f"{pid}: {'✅ PASS' if passed else '❌ FAIL'} ({passed_cases}/{total})")

    if results:
        pass1 = sum(results) / len(results)
        print(f"\n{module.__name__} pass@1 = {pass1:.2f}")
    else:
        print(f"\n{module.__name__}: no evaluated problems.")

# ---------------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------------
def main():
    for mod_name in SOLUTION_MODULES:
        print(f"\n=== Evaluating {mod_name} ===")
        try:
            mod = importlib.import_module(mod_name)
        except Exception as e:
            print(f"💥 Failed to import {mod_name}: {e}")
            continue
        evaluate_module(mod, records)

if __name__ == "__main__":
    main()


