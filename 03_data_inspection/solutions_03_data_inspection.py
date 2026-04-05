"""
solutions_03_data_inspection.py
--------------------------------
This file contains:
1. Interview question answers (as comments)
2. Solutions to all practice exercises
Related to folder: 03_data_inspection
Dataset used: Titanic dataset
""" 

import pandas as pd

# ==================================================
# LOAD DATASET
# ==================================================
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ==================================================
# 01_head_tail_info.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: head() shows first n rows, sample() shows random rows
# Q2: info() gives schema, dtypes, non-null counts, memory usage
# Q3: Non-null count indicates how many valid (non-missing) values exist

# PRACTICE SOLUTIONS:

# 1. Display only first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# 2. Display last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# 3. Check how many columns have missing values
columns_with_missing = (df.isnull().sum() > 0).sum()
print("\nNumber of columns with missing values:", columns_with_missing)

# ==================================================
# 02_describe_analysis.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: Numeric describe() returns count, mean, std, min, quartiles, max
# Q2: Object columns are ignored because stats like mean don't apply
# Q3: Use include='all' to include categorical columns

# PRACTICE SOLUTIONS:

# 1. Summary for Age and Fare
print("\nDescribe Age and Fare:")
print(df[["Age", "Fare"]].describe())

# 2. Identify columns with high variance
print("\nVariance of numeric columns:")
print(df.var(numeric_only=True).sort_values(ascending=False))

# 3. Categorical column with most unique values
print("\nUnique values in categorical columns:")
print(
    df.select_dtypes(include="object")
      .nunique()
      .sort_values(ascending=False)
)

# ==================================================
# 03_missing_values.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: isnull() detects missing values, notnull() detects valid values
# Q2: Percentage gives better decision-making than raw counts
# Q3: Drop column if missing > 40–50% and not business-critical

# PRACTICE SOLUTIONS:

# 1. Columns with more than 30% missing values
print("\nColumns with >30% missing values:")
print((df.isnull().mean() * 100)[(df.isnull().mean() > 0.30)])

# 2. Total missing values in dataset
total_missing = df.isnull().sum().sum()
print("\nTotal missing values in dataset:", total_missing)

# 3. Sort columns by missing percentage
print("\nMissing percentage by column:")
print((df.isnull().mean() * 100).sort_values(ascending=False))

# ==================================================
# 04_value_counts.py — SOLUTIONS
# ==================================================

# INTERVIEW ANSWERS:
# Q1: value_counts() is faster and simpler for single column counts
# Q2: normalize=True returns proportions instead of counts
# Q3: Including NaN helps identify data quality issues

# PRACTICE SOLUTIONS:

# 1. Most common passenger class
most_common_class = df["Pclass"].value_counts().idxmax()
print("\nMost common passenger class:", most_common_class)

# 2. Survival rate by gender
print("\nSurvival rate by gender (%):")
print(df.groupby("Sex")["Survived"].mean() * 100)

# 3. Columns behaving like categorical variables
print("\nColumns behaving like categorical variables:")
print(df.nunique()[df.nunique() < 10])

# ==================================================
# END OF SOLUTIONS
# ==================================================
