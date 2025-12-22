"""
01_head_tail_info.py
-------------------
Covers:
- head()
- tail()
- info()
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Preview first rows
print("Head:\n", df.head())

# Preview last rows
print("\nTail:\n", df.tail())

# Structural information
print("\nDataFrame Info:")
df.info()

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is the difference between head() and sample()?
# Q2: Why is info() preferred over describe() for schema inspection?
# Q3: What does non-null count in info() indicate?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Display only first 3 rows.
# 2. Display last 2 rows.
# 3. Check how many columns have missing values.

