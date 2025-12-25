"""
multiple_aggregations.py
------------------------
Covers:
- agg()
- Multiple aggregation functions
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ==============================
# TRAIL CODE
# ==============================

# Multiple aggregations on Fare
fare_summary = df.groupby("Pclass")["Fare"].agg(
    ["mean", "median", "min", "max", "count"]
)
print("\nFare Summary by Pclass:\n", fare_summary)

# Named aggregation
age_fare_stats = df.groupby("Sex").agg(
    AvgAge=("Age", "mean"),
    MaxFare=("Fare", "max")
)
print("\nNamed Aggregations:\n", age_fare_stats)

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: What is named aggregation?
# Q2: Difference between list and dict in agg()?
# Q3: Can custom functions be used in agg()?
# Q4: How to rename aggregated columns?
# Q5: Why prefer agg() over multiple groupbys?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Aggregate Age using mean, min, max by Sex.
# 2. Aggregate Fare by Embarked and Pclass.
# 3. Create a custom aggregation (range).
# 4. Rename aggregation output columns.
# 5. Handle MultiIndex columns.

