"""
resampling.py
------------- 
Covers:
- resample()
- Frequency conversion
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Create datetime index
df["Date"] = pd.date_range(
    start="2020-01-01",
    periods=len(df),
    freq="D"
)

df = df.set_index("Date")

# ==============================
# TRAIL CODE
# ==============================

# Daily to monthly resampling
monthly_fare = df["Fare"].resample("M").mean()

print("\nMonthly Average Fare:\n", monthly_fare.head())

# Weekly passenger count
weekly_count = df["PassengerId"].resample("W").count()
print("\nWeekly Passenger Count:\n", weekly_count.head())

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: Difference between resample and groupby?
# Q2: What is upsampling vs downsampling?
# Q3: How does resample handle missing periods?
# Q4: Difference between 'M' and 'MS'?
# Q5: Common resampling use cases?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Resample Fare using sum and median.
# 2. Change frequency to quarterly.
# 3. Forward-fill missing resampled values.
# 4. Compare daily vs monthly trends.
# 5. Plot resampled output.

