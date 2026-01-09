"""
pandas_sql_pipeline.py
----------------------
Covers:
- Pandas + SQL workflow
- Data extraction
- Analytical transformation
"""

import pandas as pd
import sqlite3

# ==============================
# CREATE SQLITE DB
# ==============================

conn = sqlite3.connect(":memory:")

sales = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [1, 1, 2, 3, 3],
    "revenue": [500, 700, 300, 1000, 1200]
})

sales.to_sql("sales", conn, index=False, if_exists="replace")

# ==============================
# SQL QUERY for customer details
# ==============================

query = """
SELECT
    customer_id,
    SUM(revenue) AS total_revenue,
    COUNT(order_id) AS order_count
FROM sales
GROUP BY customer_id
"""

df_sql = pd.read_sql(query, conn)

print("\nSQL Output:")
print(df_sql)

# ==============================
# PANDAS TRANSFORMATION
# ==============================

df_sql["avg_order_value"] = df_sql["total_revenue"] / df_sql["order_count"]

print("\nFinal Pandas Output:")
print(df_sql)

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: Why combine SQL and pandas?
A: SQL for aggregation on large data, pandas for flexible analytics.

Q2: When not to use pandas?
A: Very large datasets that exceed memory limits.
"""

# ==============================
# PRACTICE EXERCISES
# ==============================

# Identify high-value customers
high_value = df_sql[df_sql["total_revenue"] > 1000]
print("\nHigh Value Customers:")
print(high_value)

