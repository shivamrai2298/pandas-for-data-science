"""
column_engineering.py 
---------------------
Covers:  
- Feature / Column Engineering
- Derived columns 
""" 

import pandas as pd 

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ----------------------------------
# TRAIL CODE
# ----------------------------------

# Family size feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Fare per person
df["FarePerPerson"] = df["Fare"] / df["FamilySize"]

print("\nEngineered columns:\n",
      df[["SibSp", "Parch", "FamilySize", "FarePerPerson"]].head())

# ----------------------------------
# INTERVIEW QUESTIONS
# ----------------------------------
# Q1: What is feature engineering?
# Q2: Why does feature engineering improve ML models?
# Q3: What are leakage risks in column engineering?
# Q4: When should engineered features be removed?
# Q5: Difference between raw and derived features?

# ----------------------------------
# PRACTICE EXERCISES
# ----------------------------------
# 1. Create IsAlone column.
# 2. Create AgeGroup feature.
# 3. Bin Fare into categories.
# 4. Create interaction features.
# 5. Drop intermediate helper columns.

