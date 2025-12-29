"""
feature_store_creation.py
-------------------------
Covers:
- Feature engineering using pandas
- Creating a simple feature store
- Reusable ML-ready features
"""

import pandas as pd

# ==============================
# SAMPLE RAW DATA
# ==============================

transactions = pd.DataFrame({
    "customer_id": [1, 1, 2, 3, 3, 3],
    "amount": [500, 700, 300, 1000, 1200, 800],
    "transaction_date": pd.to_datetime([
        "2024-01-01", "2024-01-15",
        "2024-01-10",
        "2024-01-05", "2024-01-20", "2024-01-28"
    ])
})

# ==============================
# FEATURE ENGINEERING
# ==============================

feature_store = transactions.groupby("customer_id").agg(
    total_spend=("amount", "sum"),
    avg_spend=("amount", "mean"),
    txn_count=("amount", "count"),
    last_txn_date=("transaction_date", "max")
).reset_index()

print("\nFeature Store:")
print(feature_store)

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: What is a feature store?
A: Centralized storage of reusable, consistent features for ML models.

Q2: Why not create features inside every model?
A: Leads to duplication, inconsistency, and data leakage risks.
"""

# ==============================
# PRACTICE EXERCISES
# ==============================

# 1. Add recency feature
reference_date = pd.to_datetime("2024-02-01")
feature_store["recency_days"] = (
    reference_date - feature_store["last_txn_date"]
).dt.days

print("\nFeature Store with Recency:")
print(feature_store)

