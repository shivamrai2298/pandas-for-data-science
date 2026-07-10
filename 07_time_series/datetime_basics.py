""" 
datetime_basics.py file 
------------------
Covers:
- pd.to_datetime() 
- DateTime properties
"""

import pandas as pd
import numpy as np

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ==============================
# TRAIL CODE
# ==============================

# Create artificial datetime column
df["BookingDate"] = pd.date_range(
    start="2020-01-01",
    periods=len(df),
    freq="D"
)

# Convert to datetime
df["BookingDate"] = pd.to_datetime(df["BookingDate"])

# Extract datetime components
df["Year"] = df["BookingDate"].dt.year
df["Month"] = df["BookingDate"].dt.month
df["Day"] = df["BookingDate"].dt.day
df["Weekday"] = df["BookingDate"].dt.day_name()

print("\nDatetime components:\n",
      df[["BookingDate", "Year", "Month", "Weekday"]].head())

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: Why use pd.to_datetime()?
# Q2: Difference between datetime64 and object?
# Q3: What does .dt accessor do?
# Q4: How does pandas handle timezone-aware dates?
# Q5: Common datetime pitfalls in data pipelines?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Extract quarter and week number.
# 2. Create IsWeekend column.
# 3. Convert BookingDate to string format.
# 4. Filter rows for a specific month.
# 5. Sort DataFrame by BookingDate.

