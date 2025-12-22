"""
03_missing_values.py
--------------------
Covers:
- Missing value detection
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Check missing values per column
missing_counts = df.isnull().sum()
print("\nMissing values per column:\n", missing_counts)

# Percentage of missing values
missing_percentage = (df.isnull().mean() * 100).round(2)
print("\nMissing values percentage:\n", missing_percentage)

# Columns with missing values
missing_columns = missing_counts[missing_counts > 0]
print("\nColumns with missing data:\n", missing_columns)

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Difference between isnull() and notnull()?
# Q2: Why checking percentage of missing values is important?
# Q3: When would you drop a column due to missing data?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Identify columns with more than 30% missing values.
# 2. Count total missing values in the dataset.
# 3. Sort columns by missing percentage.

