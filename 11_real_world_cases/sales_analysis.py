"""
sales_analysis.py
-----------------
Covers:
- Revenue trend
- Growth metrics
- Business interpretation
"""

import pandas as pd

# ==============================
# SAMPLE DATA
# ==============================

sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "revenue": [200000, 220000, 210000, 260000, 300000]
})

# ==============================
# SALES METRICS
# ==============================

sales["MoM_Growth_%"] = sales["revenue"].pct_change() * 100

print("\nSales Performance:")
print(sales)

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: Why track MoM growth?
A: Detect momentum and seasonality.

Q2: Revenue up but profit down?
A: Cost inflation, discounts, CAC increase.
"""

# ==============================
# PRACTICE EXERCISES
# ==============================

# Best month
best_month = sales.loc[sales["revenue"].idxmax()]
print("\nBest Month:")
print(best_month)

