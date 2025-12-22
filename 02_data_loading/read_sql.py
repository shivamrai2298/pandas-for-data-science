"""
04_read_sql.py
--------------
Covers:
- Reading data from SQL databases
"""

import pandas as pd
import sqlite3

# Create SQLite connection (demo purpose)
conn = sqlite3.connect(":memory:")

# Create sample table
query = """
CREATE TABLE users (
    id INTEGER,
    name TEXT,
    age INTEGER
)
"""
conn.execute(query)

# Insert data
conn.executemany(
    "INSERT INTO users VALUES (?, ?, ?)",
    [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35)]
)

# Read SQL table into Pandas
df_sql = pd.read_sql("SELECT * FROM users", conn)
print(df_sql)

conn.close()

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Difference between read_sql and read_sql_query?
# Q2: When should SQL filtering be done instead of Pandas?
# Q3: What are advantages of pushing computation to database?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Select only users above age 30 using SQL.
# 2. Load SQL result into Pandas and calculate average age.
# 3. Save SQL data into CSV.

