"""
time_based_groupby.py
---------------------
Covers:
- Grouper
- Time-based groupby in pandas
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Create datetime column
df["BookingDate"] = pd.date_range(
    start="2020-01-01",
    periods=len(df),
    freq="D"
)

# ==============================
# TRAIL CODE
# ==============================

# Group by month using Grouper
monthly_survival = df.groupby(
    pd.Grouper(key="BookingDate", freq="M")
)["Survived"].mean()

print("\nMonthly Survival Rate:\n", monthly_survival.head())

# Group by month and class
monthly_class_fare = df.groupby(
    [pd.Grouper(key="BookingDate", freq="M"), "Pclass"]
)["Fare"].mean()

print("\nMonthly Fare by Class:\n", monthly_class_fare.head())

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: What is pd.Grouper?
# Q2: Difference between Grouper and resample?
# Q3: When is time-based groupby preferred?
# Q4: Can Grouper be used with non-time columns?
# Q5: Real-world examples of time-based aggregation?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Group by quarter and calculate mean Fare.
# 2. Group by week and count passengers.
# 3. Combine time-based groupby with categorical columns.
# 4. Reset index after time-based grouping.
# 5. Sort grouped output chronologically.

