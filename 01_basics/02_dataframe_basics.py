"""
02_dataframe_basics.py
---------------------- 
Covers:
- Creating DataFrames
- Column access
- Basic statistics
"""

import pandas as pd 

# Creating a DataFrame using a dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing columns
print("\nAges:\n", df["age"])

# Multiple columns
print("\nName & Salary:\n", df[["name", "salary"]])

# Basic statistics
print("\nSalary statistics:\n", df["salary"].describe())

# Shape of DataFrame
print("\nRows & Columns:", df.shape)

#solution file is in the same folder
# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: How is a Pandas DataFrame different from a SQL table?
# Q2: Can a DataFrame have columns with different data types?
# Q3: What happens if you access a column that does not exist?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Add a new column called 'tax' which is 10% of salary.
# 2. Find the average age of employees.
# 3. Filter employees whose salary is greater than 55,000.

