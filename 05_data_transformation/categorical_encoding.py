"""
categorical_encoding.py
-----------------------
Covers:
- Label Encoding
- One-Hot Encoding   
- get_dummies()  
""" 
 
import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ----------------------------------
# TRAIL CODE
# ----------------------------------

# Label Encoding (manual)
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})
print("\nLabel Encoded Sex:\n", df[["Sex", "Sex_encoded"]].head())

# One-Hot Encoding
embarked_dummies = pd.get_dummies(df["Embarked"], prefix="Embarked")
print("\nOne-Hot Encoded Embarked:\n", embarked_dummies.head())

# ----------------------------------
# INTERVIEW QUESTIONS
# ----------------------------------
# Q1: Difference between Label Encoding and One-Hot Encoding?
# Q2: Why can label encoding be dangerous for ML?
# Q3: What is dummy variable trap?
# Q4: How does get_dummies handle NaN?
# Q5: When should categorical encoding be done?

# ----------------------------------
# PRACTICE EXERCISES
# ----------------------------------
# 1. One-hot encode the Sex column.
# 2. Drop original categorical columns after encoding.
# 3. Use drop_first=True and observe changes.
# 4. Encode multiple categorical columns together.
# 5. Identify high-cardinality categorical features.

