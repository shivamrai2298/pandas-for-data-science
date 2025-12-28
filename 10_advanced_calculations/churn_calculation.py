"""
churn_calculation.py
--------------------
Covers:
- Customer churn calculation
- Retention logic
- Business interpretation
"""

import pandas as pd

# Sample subscription data (business-style)
data = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "start_date": ["2024-01-01", "2024-01-05", "2024-02-01", "2024-02-10", "2024-03-01", "2024-03-15"],
    "end_date": ["2024-06-01", None, "2024-04-01", None, "2024-05-15", None]
}

df = pd.DataFrame(data)
df["start_date"] = pd.to_datetime(df["start_date"])
df["end_date"] = pd.to_datetime(df["end_date"])

# ==============================
# CHURN LOGIC
# ==============================

df["churned"] = df["end_date"].notna()

churn_rate = df["churned"].mean()
print("\nChurn Rate:", round(churn_rate * 100, 2), "%")

print("\nCustomer Status:\n", df)

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is churn rate?
# Q2: How do you handle active users in churn calculation?
# Q3: Difference between churn and attrition?
# Q4: How would cohort-based churn differ?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Calculate monthly churn.
# 2. Identify longest retained customer.
# 3. Exclude customers active less than 30 days.

