from datasets import load_dataset
import pandas as pd

# Step 1: Load the dataset
# You can use "train", "test", or "validation" splits
# "all" loads all splits as a dictionary


import datasets, sys
print("datasets version:", datasets.__version__)
print("python version:", sys.version)

# Verify loading
ds = load_dataset("codeparrot/apps", split="train", trust_remote_code=True)
print(len(ds), ds.column_names[:])

