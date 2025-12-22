"""
solutions_02_data_loading.py
----------------------------
Solutions for:
02_data_loading folder
"""

import pandas as pd
import sqlite3
import requests

# ==================================================
# 01_read_csv.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: Default delimiter is comma
# Q2: usecols limits columns; dtype enforces data types
# Q3: chunksize is used for large datasets

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# PRACTICE SOLUTIONS:

# 1. Load Name and Fare
df_csv = pd.read_csv(url, usecols=["Name", "Fare"])
print("\nCSV Selected Columns:\n", df_csv.head())

# 2. Count rows
print("\nTotal rows:", df_csv.shape[0])

# 3. Memory usage
print("\nMemory usage:\n", df_csv.memory_usage(deep=True))

# ==================================================
# 02_read_excel.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: sheet_name=None returns dict of DataFrames
# Q2: Use nrows or skiprows
# Q3: CSV is faster than Excel

# NOTE: Demo logic (requires local Excel file)
# df_excel = pd.read_excel("datasets/raw/sample.xlsx", nrows=10)

# ==================================================
# 03_read_json.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: read_json loads JSON; json_normalize flattens nested JSON
# Q2: orient defines JSON structure
# Q3: JSON is good for APIs & nested data

json_url = "https://jsonplaceholder.typicode.com/users"
df_json = pd.read_json(json_url)

# PRACTICE SOLUTIONS:

# 1. Extract company names
print("\nCompany Names:\n", df_json["company"].apply(lambda x: x["name"]))

# 2. Users per city
print("\nUsers per City:\n",
      df_json["address"].apply(lambda x: x["city"]).value_counts())

# 3. Save to CSV
df_json.to_csv("users_from_api.csv", index=False)

# ==================================================
# 04_read_sql.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: read_sql works for table & query
# Q2: Filter in SQL to reduce data transfer
# Q3: DB engines are optimized for computation

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
conn.executemany(
    "INSERT INTO users VALUES (?, ?, ?)",
    [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35)]
)

# PRACTICE SOLUTIONS:

# 1. Users above age 30
df_sql = pd.read_sql("SELECT * FROM users WHERE age > 30", conn)
print("\nUsers age > 30:\n", df_sql)

# 2. Average age
print("\nAverage Age:", df_sql["age"].mean())

# 3. Save to CSV
df_sql.to_csv("users_sql.csv", index=False)

conn.close()

# ==================================================
# 05_read_api.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: API data is real-time; CSV is static
# Q2: Handle failures with retries/status codes
# Q3: Use pagination parameters

api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)
df_api = pd.DataFrame(response.json())

# PRACTICE SOLUTIONS:

# 1. Posts by userId = 1
print("\nPosts by user 1:\n", df_api[df_api["userId"] == 1])

# 2. Posts per user
print("\nPosts per user:\n", df_api["userId"].value_counts())

# 3. Save as JSON
df_api.to_json("posts.json", orient="records", indent=2)
