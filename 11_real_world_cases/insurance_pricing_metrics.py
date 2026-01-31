"""
insurance_pricing_metrics.py
----------------------------
Topics Covers:
- Loss ratio
- Pricing health indicators
"""

import pandas as pd

# ==============================
# SAMPLE DATA
# ==============================

insurance = pd.DataFrame({
    "policy_id": [1, 2, 3, 4, 5],
    "premium": [12000, 15000, 10000, 20000, 18000],
    "claim_amount": [0, 5000, 2000, 30000, 0]
})

# ==============================
# PRICING METRICS
# ==============================

total_premium = insurance["premium"].sum()
total_claims = insurance["claim_amount"].sum()

loss_ratio = total_claims / total_premium

print("\nTotal Premium:", total_premium)
print("Total Claims:", total_claims)
print("Loss Ratio:", round(loss_ratio, 2))

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: What is loss ratio?
A: Claims divided by premium.

Q2: What is a bad loss ratio?
A: Above 70–80% indicates pricing risk.
"""

# ==============================
# PRACTICE EXERCISES
# ==============================

# Identify loss-making policies
insurance["loss_making"] = insurance["claim_amount"] > insurance["premium"]
print("\nLoss Making Policies:")
print(insurance[insurance["loss_making"]])

