"""
04_string_cleaning.py
--------------------
Covers:
- String normalization
- Text extraction
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# -------------------------------
# TRAIL CODE
# -------------------------------

print("\nOriginal Name:", df["Name"].iloc[0])
print("Lowercase Name:", df["Name"].iloc[0].lower())

titles = df["Name"].str.extract(r",\s*([^\.]+)\.")
print("\nExtracted titles:\n", titles.head())

# -------------------------------
# INTERVIEW QUESTIONS
# -------------------------------
# Q1: Why is string normalization important?
# Q2: Difference between replace() and str.replace()?
# Q3: Why are vectorized string operations faster?
# Q4: When should regex be avoided?
# Q5: How does dirty text affect ML models?

# -------------------------------
# PRACTICE EXERCISES
# -------------------------------
# 1. Convert all names to lowercase.
# 2. Remove leading and trailing spaces from Name.
# 3. Extract passenger titles from Name.
# 4. Standardize titles (Mlle, Ms → Miss).
# 5. Count number of passengers per title.

