"""
02_describe_analysis.py
----------------------
Covers:
- describe()12
- Basic statistics
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url) 

# Summary statistics (numerical columns)
print("\nNumerical Summary:\n", df.describe())

# Include categorical columns
print("\nFull Summary:\n", df.describe(include="all"))

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What statistics are returned by describe() for numeric columns?
# Q2: Why does describe() ignore object columns by default?
# Q3: How do you include categorical columns in describe()?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Get summary only for Age and Fare.
# 2. Identify columns with high variance.
# 3. Find which categorical column has the most unique values.

