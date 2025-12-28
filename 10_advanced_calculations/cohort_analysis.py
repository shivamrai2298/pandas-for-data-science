"""
cohort_analysis.py
------------------
Covers:
- Cohort creation
- Retention matrix
- Time-based grouping
"""

import pandas as pd

# Sample user activity data
data = {
    "user_id": [1,1,2,2,3,3,4,5,5],
    "signup_date": [
        "2024-01-01","2024-02-01",
        "2024-01-15","2024-03-01",
        "2024-02-01","2024-04-01",
        "2024-03-10",
        "2024-01-20","2024-02-20"
    ],
    "activity_date": [
        "2024-01-15","2024-02-20",
        "2024-01-25","2024-03-15",
        "2024-02-20","2024-04-10",
        "2024-03-25",
        "2024-01-25","2024-02-25"
    ]
}

df = pd.DataFrame(data)
df["signup_date"] = pd.to_datetime(df["signup_date"])
df["activity_date"] = pd.to_datetime(df["activity_date"])

# ==============================
# COHORT CREATION
# ==============================

df["cohort_month"] = df["signup_date"].dt.to_period("M")
df["activity_month"] = df["activity_date"].dt.to_period("M")

df["cohort_index"] = (
    df["activity_month"] - df["cohort_month"]
).apply(lambda x: x.n)

# Retention matrix
cohort_table = (
    df.groupby(["cohort_month", "cohort_index"])["user_id"]
    .nunique()
    .unstack(fill_value=0)
)

print("\nCohort Retention Table:\n", cohort_table)

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is a cohort?
# Q2: Why is cohort analysis better than raw churn?
# Q3: What does cohort_index represent?
# Q4: How would you visualize this data?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Convert retention counts to percentages.
# 2. Create weekly cohorts.
# 3. Identify best-performing cohort.

