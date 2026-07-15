""" 
apply_vs_map.py 
---------------
Covers:
- apply() 
- map()
- When to use which
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ----------------------------------
# TRAIL CODE
# ----------------------------------

# map(): works on Series with mapping logic
df["Sex_numeric"] = df["Sex"].map({"male": 0, "female": 1})
print("\nSex using map():\n", df[["Sex", "Sex_numeric"]].head())

# apply(): flexible, row or column-wise
df["Age_status"] = df["Age"].apply(
    lambda x: "Missing" if pd.isna(x) else "Present"
)
print("\nAge status using apply():\n", df[["Age", "Age_status"]].head())

# ----------------------------------
# INTERVIEW QUESTIONS
# ----------------------------------
# Q1: Why is map faster than apply for Series?
# Q2: Can apply work row-wise and column-wise?
# Q3: Why can't map work on DataFrames?
# Q4: What is the axis parameter in apply()?
# Q5: When should apply be avoided?

# ----------------------------------
# PRACTICE EXERCISES
# ----------------------------------
# 1. Convert Embarked values using map().
# 2. Create a column indicating Fare is high or low using apply().
# 3. Replace missing Age values with a label.
# 4. Compare execution time of apply vs map.
# 5. Identify columns where map cannot be used.

