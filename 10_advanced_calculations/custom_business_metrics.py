"""
custom_business_metrics.py 
--------------------------
Covers:
- KPI creation
- Custom metrics
- Business logic in Pandas
"""

import pandas as pd

# Sample sales data
data = {
    "order_id": [1,2,3,4,5],
    "revenue": [1000, 1500, 500, 3000, 2500],
    "cost": [600, 900, 300, 1800, 1500]
}

df = pd.DataFrame(data)

# ==============================
# CUSTOM METRICS
# ==============================

df["profit"] = df["revenue"] - df["cost"]
df["margin_pct"] = (df["profit"] / df["revenue"]) * 100

print("\nBusiness Metrics:\n", df)

print("\nAverage Margin:", round(df["margin_pct"].mean(), 2), "%")

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is contribution margin?
# Q2: Why percentages are better than raw profit?
# Q3: How do you validate business metrics?
# Q4: What causes misleading KPIs?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Add cumulative revenue.
# 2. Identify loss-making orders.
# 3. Create ROI metric.
