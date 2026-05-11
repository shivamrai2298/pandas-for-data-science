"""
concat_vs_merge.py
------------------
Covers:
- pd.concat() 
- pd.merge()
- Key differences between concat and merge in pandas
"""

import pandas as pd

# Load dataset 
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Create smaller DataFrames 
df_passengers = df[["PassengerId", "Name", "Sex"]]
df_fares = df[["PassengerId", "Fare"]]

# ==============================
# CONCAT (row-wise & column-wise)
# ==============================

# Row-wise concat (stacking)
concat_rows = pd.concat([df_passengers.head(3), df_passengers.tail(3)])
print("\nRow-wise concat:\n", concat_rows)

# Column-wise concat
concat_cols = pd.concat(
    [df_passengers.head(5), df_fares.head(5)],
    axis=1
)
print("\nColumn-wise concat:\n", concat_cols)

# ==============================
# MERGE (SQL-style join)
# ==============================

merged_df = pd.merge(
    df_passengers,
    df_fares,
    on="PassengerId",
    how="inner"
)
print("\nMerged DataFrame:\n", merged

