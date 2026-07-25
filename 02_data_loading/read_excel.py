"""
02_read_excel.py
----------------
Covers: 
- Reading Excel files 
- Multiple sheets
"""

import pandas as pd

# Reading Excel file
df_excel = pd.read_excel("datasets/raw/sample.xlsx")
print(df_excel.head())

# Reading a specific sheet
df_sheet = pd.read_excel(
    "datasets/raw/sample.xlsx",
    sheet_name="Sheet1"
)

print("\nSpecific Sheet:\n", df_sheet.head())

# Reading multiple sheets
sheets = pd.read_excel(
    "datasets/raw/sample.xlsx",
    sheet_name=None
)

print("\nSheets Loaded:", sheets.keys())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What data type is returned when sheet_name=None?
# Q2: How do you load only a specific range of rows from Excel?
# Q3: Difference between read_csv and read_excel performance?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Load only first 10 rows from Excel.
# 2. Read a sheet by index instead of name.
# 3. Convert Excel data into CSV.

