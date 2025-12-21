"""
04_dtypes_and_memory.py
-----------------------
Covers:
- Data types
- Memory optimization
"""

import pandas as pd
import numpy as np

# Creating DataFrame with default dtypes
df = pd.DataFrame({
    "id": range(1, 6),
    "age": [25, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000]
})

print("Original dtypes:\n", df.dtypes)
print("\nMemory usage (bytes):\n", df.memory_usage(deep=True))

# Optimizing data types
df["id"] = df["id"].astype("int32")
df["age"] = df["age"].astype("int8")
df["salary"] = df["salary"].astype("int32")

print("\nOptimized dtypes:\n", df.dtypes)
print("\nOptimized memory usage (bytes):\n", df.memory_usage(deep=True))

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Why is dtype optimization important in large datasets?
# Q2: What is the difference between object and category dtype?
# Q3: When should you NOT optimize dtypes?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Add a 'city' column and convert it to category dtype.
# 2. Check memory usage before and after conversion.
# 3. Create a float column and downcast it to float32.

