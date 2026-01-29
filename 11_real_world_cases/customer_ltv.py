"""
customer_ltv.py
---------------
Covers:
- Customer Lifetime Value (LTV)
- Revenue-based customer importance
- Business assumptions calc
"""

import pandas as pd

# ==============================
# SAMPLE DATA
# ==============================

data = {
    "customer_id": [1, 1, 2, 2, 3, 3, 3],
    "order_value": [500, 700, 300, 400, 1000, 1200, 800]
}

df = pd.DataFrame(data)

# ==============================
# LTV CALCULATION
# ==============================

avg_order_value = df.groupby("customer_id")["order_value"].mean()
purchase_frequency = df.groupby("customer_id")["order_value"].count()

customer_lifespan_years = 3  # business assumption

ltv = avg_order_value * purchase_frequency * customer_lifespan_years

print("\nCustomer Lifetime Value:")
print(ltv)

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: What is LTV?
A: Total revenue a customer generates over their lifetime.

Q2: Why is LTV important?
A: Helps decide marketing spend, retention strategy, and pricing.

Q3: Key assumptions in LTV?
A: Lifespan, churn, and purchase behavior stability.
"""

# ==============================
# PRACTICE EXERCISES (SOLVED)
# ==============================

# Top customer by LTV
print("\nTop Customer by LTV:")
print(ltv.idxmax())

