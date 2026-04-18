"""
vectorized_operations.py
------------------------
Covers:
- Arithmetic vectorization
- Boolean masking
- Conditional operations 
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# ==============================
# VECTOR ARITHMETIC
# ==============================

df["FarePerYear"] = df["Fare"] / df["Age"]
print("\nFare per Age (sample):\n", df[["Fare", "Age", "FarePerYear"]].head())

# ==============================
# BOOLEAN MASKING
# ==============================

high_fare = df[df["Fare"] > df["Fare"].mean()]
print("\nPassengers with high fare:\n", high_fare.head())

# ==============================
# CONDITIONAL VECTOR OPERATIONS
# ==============================

df["FareLevel"] = "Low"
df.loc[df["Fare"] > df["Fare"].quantile(0.75), "FareLevel"] = "High"

print("\nFare Level Distribution:\n", df["FareLevel"].value_counts())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is boolean masking?
# Q2: Why is df[df["Fare"] > mean] fast?
# Q3: How does Pandas avoid Python loops?
# Q4: Difference between loc and direct indexing?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Create AgeGroup using vectorized conditions.
# 2. Filter passengers older than average age.
# 3. Create a column marking "Expensive" fares.

