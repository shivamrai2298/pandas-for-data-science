"""
solutions_01_basics.py
----------------------
Solutions for:
01_basics folder
Includes interview answers + practice exercises
"""

import pandas as pd
import numpy as np

# ==================================================
# 01_series_basics.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: Series is a labeled 1D structure; NumPy array has no labels
# Q2: Yes, Series can have duplicate indexes
# Q3: Vectorized operations are faster because they run in C internally

# PRACTICE SOLUTIONS:

# 1. Series of city temperatures
temps = pd.Series(
    [30, 28, 32, 27, 29],
    index=["Mumbai", "Delhi", "Pune", "Bangalore", "Chennai"]
)
print("\nCity Temperatures:\n", temps)

# 2. Increase all temperatures by 2
print("\nUpdated Temperatures:\n", temps + 2)

# 3. Maximum temperature
print("\nMax Temperature:", temps.max())

# ==================================================
# 02_dataframe_basics.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: DataFrame is in-memory; SQL table is persistent
# Q2: Yes, columns can have different dtypes
# Q3: KeyError is raised if column does not exist

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)

# PRACTICE SOLUTIONS:

# 1. Add tax column (10%)
df["tax"] = df["salary"] * 0.10
print("\nDataFrame with Tax:\n", df)

# 2. Average age
print("\nAverage Age:", df["age"].mean())

# 3. Salary > 55,000
print("\nHigh Salary Employees:\n", df[df["salary"] > 55000])

# ==================================================
# 03_indexing_slicing.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: loc is label-based, iloc is position-based
# Q2: iloc is slightly faster
# Q3: loc raises KeyError if label does not exist

df_scores = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [80, 85, 90, 95]
})

# PRACTICE SOLUTIONS:

# 1. Select name and score using loc
print("\nName & Score:\n", df_scores.loc[:, ["name", "score"]])

# 2. Last two rows using iloc
print("\nLast two rows:\n", df_scores.iloc[-2:])

# 3. Score between 85 and 95
print("\nScore between 85 and 95:\n",
      df_scores[(df_scores["score"] > 85) & (df_scores["score"] < 95)])

# ==================================================
# 04_dtypes_and_memory.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: Optimizing dtypes reduces memory & speeds up computation
# Q2: category uses integer encoding internally
# Q3: Avoid optimization if dataset is small or values may overflow

df_mem = pd.DataFrame({
    "id": range(1, 6),
    "age": [25, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000],
    "city": ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"]
})

# PRACTICE SOLUTIONS:

# 1. Convert city to category
df_mem["city"] = df_mem["city"].astype("category")

# 2. Memory usage
print("\nMemory usage:\n", df_mem.memory_usage(deep=True))

# 3. Float downcast
df_mem["bonus"] = np.array([1000.5, 2000.5, 1500.5, 1800.5, 2200.5], dtype="float64")
df_mem["bonus"] = df_mem["bonus"].astype("float32")

print("\nOptimized dtypes:\n", df_mem.dtypes)
