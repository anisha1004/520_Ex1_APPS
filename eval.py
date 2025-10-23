import importlib
import json
import re
from math import comb
from pathlib import Path

# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------
DATASET_PATH = Path("data/apps_10.jsonl")
SOLUTION_MODULES = [
    "solutions.GPT_CoT",
    "solutions.GPT_SelfDebug",
    "solutions.Claude_CoT",
    "solutions.Claude_SelfDebug",
]
K_VALUES = [1, 2, 3]          # compute pass@1, pass@2, pass@3
OUT_CSV = Path("reports/eval_passk.csv")

# -----------------------------------------------------------------------------
# UTILS
# -----------------------------------------------------------------------------
def load_records(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def discover_variants(module, problem_id: int):
    """
    Return a list of (name, callable) for all functions that match:
      solve_<pid> OR solve_<pid>_v<digits>
    """
    pid = str(problem_id)
    pat = re.compile(rf"^solve_{re.escape(pid)}(?:_v\d+)?$")
    variants = []
    for name in dir(module):
        if pat.match(name):
            fn = getattr(module, name)
            if callable(fn):
                variants.append((name, fn))
    # sort so v1, v2, v3 come in order; plain (no suffix) first if present
    def keyfn(x):
        name = x[0]
        if name == f"solve_{pid}":
            return (0, 0)
        m = re.search(r"_v(\d+)$", name)
        return (1, int(m.group(1)) if m else 999999)
    variants.sort(key=keyfn)
    return variants

def run_one_variant(fn, inputs, outputs):
    """Return True if this variant passes ALL test cases."""
    passed = 0
    total = len(inputs)
    for inp, exp in zip(inputs, outputs):
        try:
            got = str(fn(inp.strip())).strip()
            exp_clean = str(exp).strip()
            if got == exp_clean:
                passed += 1
        except Exception:
            return False
    return passed == total and total > 0

def pass_at_k_from_counts(c, n, k):
    """
    Standard pass@k estimator (without replacement):
      pass@k = 1 - C(n-c, k)/C(n, k)   if n >= k and c > 0
    Edge handling:
      - if c == 0 -> 0
      - if k > n  -> treat as k = n
    """
    if c == 0:
        return 0.0
    if k > n:
        k = n
    if k == 0:
        return 0.0
    return 1.0 - (comb(n - c, k) / comb(n, k))

# -----------------------------------------------------------------------------
# MAIN EVAL
# -----------------------------------------------------------------------------
def main():
    records = load_records(DATASET_PATH)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    # Collect rows for CSV
    csv_rows = []
    for mod_name in SOLUTION_MODULES:
        print(f"\n=== Evaluating {mod_name} ===")
        try:
            mod = importlib.import_module(mod_name)
        except Exception as e:
            print(f"💥 Failed to import {mod_name}: {e}")
            continue

        per_problem_stats = []  # [(pid, n_variants, n_pass, {k: pass@k})]

        for rec in records:
            pid = rec["problem_id"]
            io = rec["input_output"]
            if isinstance(io, str):
                try:
                    io = json.loads(io)
                except Exception:
                    io = {}
            inputs = io.get("inputs", [])
            outputs = io.get("outputs", [])

            variants = discover_variants(mod, pid)
            if not variants:
                print(f"⚠️  {mod_name}: no variants for problem {pid}")
                continue

            # test all variants
            passed_flags = []
            for vname, vfn in variants:
                ok = run_one_variant(vfn, inputs, outputs)
                passed_flags.append((vname, ok))
                status = "PASS" if ok else "FAIL"
                print(f"{pid} :: {vname} → {status}")

            # summarize for this problem
            n = len(passed_flags)
            c = sum(1 for _, ok in passed_flags if ok)
            passk = {k: pass_at_k_from_counts(c, n, k) for k in K_VALUES}

            # print compact per-problem summary line
            k_display = " ".join([f"p@{k}={passk[k]:.2f}" for k in K_VALUES])
            print(f"→ Problem {pid}: {c}/{n} variants passed | {k_display}")

            per_problem_stats.append((pid, n, c, passk))

            # add rows for CSV (per problem)
            csv_row = {
                "module": mod_name,
                "problem_id": pid,
                "n_variants": n,
                "n_pass": c,
            }
            for k in K_VALUES:
                csv_row[f"pass@{k}"] = passk[k]
            csv_rows.append(csv_row)

        # module-level averages
        if per_problem_stats:
            for k in K_VALUES:
                avg = sum(p[3][k] for p in per_problem_stats) / len(per_problem_stats)
                print(f"{mod_name} :: mean pass@{k} = {avg:.3f}")
        else:
            print(f"{mod_name}: no problems evaluated.")

    # write CSV
    # (avoid pandas dependency to keep things light)
    if csv_rows:
        headers = ["module", "problem_id", "n_variants", "n_pass"] + [f"pass@{k}" for k in K_VALUES]
        with OUT_CSV.open("w", encoding="utf-8") as f:
            f.write(",".join(headers) + "\n")
            for row in csv_rows:
                f.write(",".join(str(row[h]) for h in headers) + "\n")
        print(f"\nSaved → {OUT_CSV}")

if __name__ == "__main__":
    main()

