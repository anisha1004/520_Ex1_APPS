
# sample_10.py
from datasets import load_dataset
import random, json, os

ds = load_dataset("codeparrot/apps", split="test", trust_remote_code=True)
items = random.sample(list(ds), 10)

os.makedirs("data", exist_ok=True)
with open("data/apps_10.jsonl", "w", encoding="utf-8") as f:
    for ex in items:
        rec = {
            "problem_id": ex["problem_id"],
            "difficulty": ex["difficulty"],
            "question": ex["question"],
            "starter_code": ex.get("starter_code",""),
            "input_output": ex.get("input_output",""),
        }
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("Saved → data/apps_10.jsonl")


