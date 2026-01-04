"""
pandas_to_sklearn.py
--------------------
Covers:
- Pandas → ML pipeline
- Feature / target separation
- Model training
- Adjustment
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==============================
# SAMPLE DATA
# ==============================

data = pd.DataFrame({
    "age": [25, 35, 45, 23, 52, 40, 60],
    "income": [30000, 50000, 70000, 25000, 90000, 65000, 100000],
    "purchased": [0, 1, 1, 0, 1, 1, 1]
})

# ==============================
# ML PIPELINE
# ==============================

X = data[["age", "income"]]
y = data["purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, preds))

# ==============================
# INTERVIEW QUESTIONS
# ==============================

"""
Q1: Why pandas before sklearn?
A: Cleaning, feature engineering, and validation.

Q2: What causes data leakage?
A: Using future or target information in features.
"""

# ==============================
# PRACTICE EXERCISES
# ==============================

# Check feature importance
importance = pd.Series(
    model.coef_[0],
    index=X.columns
)

print("\nFeature Importance:")
print(importance)

