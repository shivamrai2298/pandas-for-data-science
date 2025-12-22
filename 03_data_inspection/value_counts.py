"""
04_value_counts.py
------------------
Covers:
- value_counts()
- Unique value inspection
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Count unique values in Sex column
print("\nSex distribution:\n", df["Sex"].value_counts())

# Normalize counts (percentage)
print("\nSex distribution (%):\n", df["Sex"].value_counts(normalize=True) * 100)

# Include NaN values
print("\nEmbarked (including NaN):\n", df["Embarked"].value_counts(dropna=False))

# Number of unique values per column
unique_counts = df.nunique()
print("\nUnique values per column:\n", unique_counts)

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Difference between value_counts() and groupby().count()?
# Q2: What does normalize=True do?
# Q3: Why include NaN values in counts?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Find most common passenger class.
# 2. Calculate survival rate by gender.
# 3. Identify columns that behave like categorical variables.

