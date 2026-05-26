"""
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





"""
03_data_types.py
----------------
Covers:
- Inspecting data types
- Understanding memory usage
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# -------------------------------
# TRAIL CODE
# -------------------------------

print("\nColumn data types:\n", df.dtypes)

print("\nMemory usage of Pclass:",
      df["Pclass"].memory_usage(deep=True))

# -------------------------------
# INTERVIEW QUESTIONS
# -------------------------------
# Q1: Why are incorrect data types dangerous?
# Q2: Difference between astype() and to_numeric()?
# Q3: When should category dtype be used?
# Q4: How does dtype affect memory and performance?
# Q5: What does errors='coerce' do?

# -------------------------------
# PRACTICE EXERCISES
# -------------------------------
# 1. Convert Pclass to category.
# 2. Convert Fare to numeric safely.
# 3. Identify columns suitable for categorical dtype.
# 4. Compare memory usage before and after conversion.
# 5. Convert Survived to boolean.

#make sure to practice on everyday basis


