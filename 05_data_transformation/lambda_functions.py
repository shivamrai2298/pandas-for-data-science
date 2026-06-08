
"""
lambda_functions.py 
-------------------  
Covers: 
- lambda functions
- Inline transformations
""" 

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ----------------------------------
# TRAIL CODE
# ----------------------------------

# Lambda inside apply
df["Fare_category"] = df["Fare"].apply(
    lambda x: "High" if x > 50 else "Low"
)

print("\nFare categories:\n", df[["Fare", "Fare_category"]].head())

# Lambda in conditional column
df["Age_group"] = df["Age"].apply(
    lambda x: "Child" if x < 12 else ("Adult" if x < 60 else "Senior")
    if pd.notnull(x) else "Unknown"
)

print("\nAge groups:\n", df[["Age", "Age_group"]].head())

# ----------------------------------
# INTERVIEW QUESTIONS
# ----------------------------------
# Q1: Why are lambdas called anonymous functions?
# Q2: When should lambda be avoided?
# Q3: Performance impact of lambda in apply?
# Q4: Lambda vs def function?
# Q5: Can lambda return multiple values?

# ----------------------------------
# PRACTICE EXERCISES
# ----------------------------------
# 1. Create a column identifying expensive tickets.
# 2. Categorize passengers by family size.
# 3. Replace missing Age using lambda.
# 4. Use lambda with multiple conditions.
# 5. Rewrite lambda logic using def function.
