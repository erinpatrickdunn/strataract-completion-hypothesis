"""
inspect_columns.py
==================
Prints all column names in manga_merged_with_rar.csv so we can
map them to the expected variable names before running the audit.
"""

import pandas as pd

DATA_PATH = "manga_merged_with_rar.csv"

df = pd.read_csv(DATA_PATH, low_memory=False, nrows=5)

print(f"Shape (5 rows shown): {df.shape}")
print(f"\nAll columns ({len(df.columns)} total):\n")
for i, col in enumerate(sorted(df.columns)):
    print(f"  {i+1:>3}.  {col}")

print("\nFirst row sample values:")
print(df.iloc[0].to_string())
