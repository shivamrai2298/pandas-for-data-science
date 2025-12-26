"""
merge_inner_left_right.py
------------------------
Covers:
- inner, left, right, outer joins
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Create DataFrames
df_basic = df[["PassengerId", "Name"]]
df_extra = df[["PassengerId", "Fare", "Pclass"]]

# ==============================
# INNER JOIN
# ==============================
inner_join = pd.merge(df_basic, df_extra, on="PassengerId", how="inner")
print("\nInner Join:\n", inner_join.head())

# ==============================
# LEFT JOIN
# ==============================
left_join = pd.merge(df_basic, df_extra, on="PassengerId", how="left")
print("\nLeft Join:\n", left_join.head())

# ==============================
# RIGHT JOIN
# ==============================
right_join = pd.merge(df_basic, df_extra, on="PassengerId", how="right")
print("\nRight Join:\n", right_join.head())

# ==============================
# OUTER JOIN
# ==============================
outer_join = pd.merge(df_basic, df_extra, on="PassengerId", how="outer")
print("\nOuter Join:\n", outer_join.head())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is the difference between inner and outer join?
# Q2: When would a left join create NaN values?
# Q3: Which join is safest for data retention?
# Q4: How does SQL join mapping work in pandas?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Remove PassengerId from one DataFrame and try merge.
# 2. Identify rows created only in outer join.
# 3. Compare row counts for each join type.

