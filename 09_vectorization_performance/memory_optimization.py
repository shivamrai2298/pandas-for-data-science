"""
memory_optimization.py
----------------------
Covers:
- Memory usage analysis
- Data type optimization
- Category dtype
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ==============================
# MEMORY BEFORE OPTIMIZATION
# ==============================

print("\nMemory usage before optimization:")
print(df.memory_usage(deep=True))
print("Total:", df.memory_usage(deep=True).sum() / 1024**2, "MB")

# ==============================
# OPTIMIZATION STEPS
# ==============================

df["Sex"] = df["Sex"].astype("category")
df["Embarked"] = df["Embarked"].astype("category")
df["Pclass"] = df["Pclass"].astype("int8")
df["Survived"] = df["Survived"].astype("int8")

# ==============================
# MEMORY AFTER OPTIMIZATION
# ==============================

print("\nMemory usage after optimization:")
print(df.memory_usage(deep=True))
print("Total:", df.memory_usage(deep=True).sum() / 1024**2, "MB")

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Why does category dtype reduce memory?
# Q2: When should category NOT be used?
# Q3: What is deep=True in memory_usage()?
# Q4: How does dtype affect performance?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Optimize Name column memory.
# 2. Compare object vs category memory usage.
# 3. Downcast numeric columns using pandas methods.

