"""
rolling_window.py
-----------------
Covers:
- rolling()
- Window-based calculations
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ==============================
# TRAIL CODE
# ==============================

# Sort values to simulate time/window behavior
df_sorted = df.sort_values("Fare")

# Rolling mean of Fare
df_sorted["RollingFareMean"] = (
    df_sorted["Fare"].rolling(window=5).mean()
)

print("\nRolling Fare Mean:\n",
      df_sorted[["Fare", "RollingFareMean"]].head(10))

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: What is a rolling window?
# Q2: Difference between rolling and expanding?
# Q3: What does window size control?
# Q4: How does rolling handle NaN values?
# Q5: Real-world use cases of rolling metrics?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Compute rolling median of Fare.
# 2. Try different window sizes.
# 3. Calculate rolling sum.
# 4. Combine rolling with groupby.
# 5. Remove NaN rows after rolling.


