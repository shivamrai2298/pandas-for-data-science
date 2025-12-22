"""
03_read_json.py
---------------
Covers:
- Reading JSON files
- Handling nested data
"""

import pandas as pd

# Reading JSON from URL
json_url = "https://jsonplaceholder.typicode.com/users"
df_json = pd.read_json(json_url)

print(df_json.head())

# Normalize nested JSON
df_normalized = pd.json_normalize(df_json.to_dict(orient="records"))
print("\nFlattened JSON:\n", df_normalized.head())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Difference between read_json and json_normalize?
# Q2: What is orient parameter?
# Q3: When is JSON preferred over CSV?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Extract company name from JSON.
# 2. Count how many users belong to each city.
# 3. Save normalized data as CSV.

