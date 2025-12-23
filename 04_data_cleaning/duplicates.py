"""
02_duplicates.py
----------------
Covers:
- Identifying duplicates
- Understanding duplicate rows
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# -------------------------------
# TRAIL CODE
# -------------------------------

print("\nTotal duplicate rows:", df.duplicated().sum())

print("\nDuplicates based on Name & Ticket:",
      df.duplicated(subset=["Name", "Ticket"]).sum())

# -------------------------------
# INTERVIEW QUESTIONS
# -------------------------------
# Q1: What does duplicated() return?
# Q2: What is the default behavior of drop_duplicates()?
# Q3: Difference between full-row and subset duplicates?
# Q4: Why should duplicates be inspected before deletion?
# Q5: Can duplicates ever represent valid data?

# -------------------------------
# PRACTICE EXERCISES
# -------------------------------
# 1. Identify all duplicate rows.
# 2. Remove duplicate rows.
# 3. Keep only the last occurrence of duplicates.
# 4. Verify duplicates are removed.
# 5. Find duplicates using a subset of columns.

