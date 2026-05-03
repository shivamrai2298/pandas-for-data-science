"""
transform_vs_apply.py
---------------------
Covers:
- transform()
- apply()
- Differences and use cases
"""  

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url) 

# ==============================
# TRAIL CODE
# ==============================

# transform keeps original shape
df["AvgFareByClass"] = df.groupby("Pclass")["Fare"].transform("mean")

# apply can change shape
fare_deviation = df.groupby("Pclass")["Fare"].apply(
    lambda x: x - x.mean()
)

print("\nTransform Output:\n",
      df[["Fare", "AvgFareByClass"]].head())

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: Why does transform return same length output?
# Q2: When should apply be avoided?
# Q3: Performance comparison: transform vs apply?
# Q4: Can transform use custom functions?
# Q5: What happens if apply returns different shapes?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Add mean Age per Sex using transform.
# 2. Normalize Fare within each Pclass.
# 3. Use apply to calculate Fare range.
# 4. Compare shapes of outputs.
# 5. Drop derived columns after analysis.

