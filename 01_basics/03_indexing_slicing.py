
"""
03_indexing_slicing.py
----------------------
Covers:
- loc vs iloc
- Row & column slicing
"""

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [80, 85, 90, 95],
    "passed": [True, True, True, True]
})

print("Original DataFrame:\n", df)

# iloc -> integer-based indexing
print("\nFirst row using iloc:\n", df.iloc[0])

# Select rows 1 to 3 (excluding 3)
print("\nRows 1 to 2:\n", df.iloc[1:3])

# loc -> label-based indexing
print("\nScore column using loc:\n", df.loc[:, "score"])

# Conditional selection
high_scorers = df[df["score"] > 85]
print("\nStudents with score > 85:\n", high_scorers)

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Difference between loc and iloc?
# Q2: Which is faster: loc or iloc, and why?
# Q3: What happens if the label does not exist in loc?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Select only 'name' and 'score' columns using loc.
# 2. Get the last two rows using iloc.
# 3. Filter students who scored between 85 and 95.
