"""
01_series_basics.py
-------------------
Topics Covers:
- Creating Pandas Series
- Indexing qq
- Vectorized operations
"""

import pandas as pd

# Creating a Series from a list
scores = pd.Series([85, 90, 78, 92, 88])
print("Series:\n", scores)

#to print single element
print(scores[0]) # works similarly to list


# Series with custom index
scores_with_names = pd.Series(
    [85, 90, 78],
    index=["Alice", "Bob", "Charlie"]
)
print("\nSeries with index:\n", scores_with_names)

# Accessing elements
print("\nScore of Bob:", scores_with_names["Bob"])

# Vectorized operation (no loops needed)
updated_scores = scores + 5
print("\nUpdated Scores:\n", updated_scores)

# Series attributes
print("\nData type:", scores.dtype)
print("Shape:", scores.shape)


#Below are the list of questions for interview and for practice
# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is the difference between a Pandas Series and a NumPy array?
# Q2: Can a Pandas Series have duplicate indexes?
# Q3: Why are vectorized operations faster than loops in Pandas?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Create a Series of 5 city names as index and their temperatures as values.
# 2. Increase all temperatures by 2 degrees using vectorized operation.
# 3. Find the maximum temperature from the Series.

