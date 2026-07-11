"""
groupby_basics.py
----------------- 
Covers:
- groupby() 
- Basic aggregations
"""

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ==============================
# TRAIL CODE
# ==============================

# Survival rate by passenger class
survival_rate = df.groupby("Pclass")["Survived"].mean()
print("\nSurvival Rate by Pclass:\n", survival_rate)

# Passenger count by Sex
passenger_count = df.groupby("Sex")["PassengerId"].count()
print("\nPassenger Count by Sex:\n", passenger_count)

# ==============================
# INTERVIEW QUESTIONS
# ==============================
# Q1: Explain split-apply-combine in groupby.
# Q2: Difference between size() and count()?
# Q3: How does groupby treat NaN values?
# Q4: What happens to index after groupby?
# Q5: Why is groupby considered lazy?

# ==============================
# PRACTICE EXERCISES
# ==============================
# 1. Find average Fare by Pclass.
# 2. Calculate survival rate by Sex.
# 3. Count passengers per Embarked port.
# 4. Sort groupby output by values.
# 5. Reset index after groupby.

