"""
fraud_detection_rules.py
------------------------
Covers:
- Rule-based fraud detection
- Explainability-first approach
"""

import pandas as pd

# ==============================
# SAMPLE DATA
# ==============================

transactions = pd.DataFrame({
    "user_id": [1, 1, 2, 3, 4],
    "amount": [5000, 150000, 300, 200000, 400],
    "txns_last_hour": [1, 6, 1, 2, 1]
})

# ==============================
# FRAUD RULES
# ==============================

def fraud_rule_engine(row):
    if row["amount"] > 100000:
        return "High Amount Fraud"
    if row["txns_last_hour"] > 5:
        return "Velocity Fraud"
    return "Normal"

transactions["fraud_flag"] = transactions.apply(fraud_rule_engine, axis=1)

print("\nFraud Detection Output:")
print(transactions)

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: Why rule-based systems before ML?
A: Fast deployment, explainability, regulatory compliance.

Q2: Limitation of rules?
A: Cannot catch unknown fraud patterns.
"""

# ==============================
# PRACTICE EXERCISES
# ==============================

# Count fraud cases
print("\nFraud Case Count:")
print(transactions["fraud_flag"].value_counts())

