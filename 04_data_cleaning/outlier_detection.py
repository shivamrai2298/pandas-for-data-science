"""
05_outliers.py 
--------------
Covers:
- Outlier detection
- IQR method
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# -------------------------------
# TRAIL CODE
# -------------------------------

print("\nFare summary:\n", df["Fare"].describe())

Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)
IQR = Q3 - Q1

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

high_fare = df[df["Fare"] > Q3 + 1.5 * IQR]
print("\nHigh Fare Outliers:\n", high_fare[["Fare"]].head())

# -------------------------------
# INTERVIEW QUESTIONS
# -------------------------------
# Q1: What are outliers and why are they problematic?
# Q2: Difference between IQR and Z-score?
# Q3: When should outliers be capped instead of removed?
# Q4: Why is IQR preferred for skewed data?
# Q5: How do outliers impact ML models?

# -------------------------------
# PRACTICE EXERCISES
# -------------------------------
# 1. Detect outliers in Fare using IQR.
# 2. Count how many outliers exist.
# 3. Cap Fare values using IQR bounds.
# 4. Compare statistics before and after capping.
# 5. Visualize outliers using a boxplot.

