"""
01_missing_values.py 
--------------------
Covers:
- Detecting missing values
- Understanding missing data patterns
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# -------------------------------
# TRAIL CODE
# -------------------------------

print("\nMissing values per column:\n", df.isnull().sum())

print("\nRows where Age is missing:\n", df[df["Age"].isnull()].head())

# -------------------------------
# INTERVIEW QUESTIONS
# -------------------------------
# Q1: What is the difference between isnull() and notnull()?
# Q2: When should missing values be dropped instead of imputed?
# Q3: Why is median preferred over mean for Age?
# Q4: How do missing values affect groupby results?
# Q5: What is forward fill and backward fill?

# -------------------------------
# PRACTICE EXERCISES
# -------------------------------
# 1. Print percentage of missing values for each column.
# 2. Fill missing values in Age using median.
# 3. Drop rows where Embarked is missing.
# 4. Create a binary column Cabin_available.
# 5. Drop columns with more than 40% missing values.

