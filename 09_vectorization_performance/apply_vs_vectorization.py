"""
apply_vs_vectorization.py
-------------------------
Covers:
- apply() vs vectorized operations
- Performance difference
- When apply() should be avoided in this
"""

import pandas as pd
import time

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Fill missing Age for fair comparison
df["Age"] = df["Age"].fillna(df["Age"].median())

# ==============================
# USING apply()
# ==============================

start = time.time()

def age_category(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup_apply"] = df["Age"].apply(age_category)

end = time.time()
print(f"\napply() time: {end - start:.6f} seconds")

# ==============================
# USING VECTORIZATION
# ==============================

start = time.time()

df["AgeGroup_vectorized"] = pd.cut(
    df["Age"],
    bins=[0, 18, 60, 100],
    labels=["Child", "Adult", "Senior"]
)

end = time.time()
print(f"Vectorized time: {end - start:.6f} seconds")

print("\nSample Output:\n", df[["Age", "AgeGroup_apply", "AgeGroup_vectorized"]].head())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Why are vectorized operations faster than apply()?
# Q2: Is apply() always slower?
# Q3: When is apply() unavoidable?
# Q4: How does Pandas use NumPy internally?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Create FareCategory using apply().
# 2. Convert FareCategory to a vectorized solution.
# 3. Measure execution time for both approaches.

