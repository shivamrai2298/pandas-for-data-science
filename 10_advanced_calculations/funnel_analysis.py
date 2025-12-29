"""
funnel_analysis.py
------------------
Covers:
- Funnel steps
- Conversion rates
- Drop-off analysis
"""

import pandas as pd

# Sample funnel data
data = {
    "step": ["Visited", "Signed Up", "Activated", "Paid"],
    "users": [1000, 600, 400, 150]
}

df = pd.DataFrame(data)

# ==============================
# FUNNEL METRICS
# ==============================

df["conversion_rate"] = df["users"] / df["users"].shift(1)
df.loc[0, "conversion_rate"] = 1.0

df["drop_off"] = 1 - df["conversion_rate"]

print("\nFunnel Analysis:\n", df)

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is funnel leakage?
# Q2: How do you improve conversion rates?
# Q3: Why top-of-funnel matters?
# Q4: How would this change by cohort?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Add cumulative conversion.
# 2. Identify weakest funnel step.
# 3. Visualize funnel.

