
"""
weighted_metrics.py
-------------------
Covers:
- Weighted average
- Importance weighting
- Business-adjusted metrics
"""

import pandas as pd
import numpy as np

# Sample rating data
data = {
    "customer_id": [1,2,3,4,5],
    "rating": [4, 5, 3, 5, 2],
    "orders": [50, 5, 2, 20, 1]
}

df = pd.DataFrame(data)

# ==============================
# WEIGHTED METRICS
# ==============================

weighted_avg_rating = np.average(
    df["rating"],
    weights=df["orders"]
)

print("\nWeighted Average Rating:", round(weighted_avg_rating, 2))

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Why weighted averages matter?
# Q2: What happens if weights are skewed?
# Q3: When NOT to use weighted metrics?
# Q4: Difference between mean and weighted mean?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Calculate weighted revenue per customer.
# 2. Compare weighted vs simple average.
# 3. Identify customers dominating the metric.
