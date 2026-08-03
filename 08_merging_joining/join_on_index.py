"""
join_on_index.py
----------------
Covers:
- DataFrame.join() 
- Joining on index
"""

import pandas as pd 

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Create DataFrames with index
df_names = df[["PassengerId", "Name"]].set_index("PassengerId")
df_survival = df[["PassengerId", "Survived"]].set_index("PassengerId")

# ==============================
# JOIN ON INDEX
# ==============================

joined_df = df_names.join(df_survival)
print("\nJoined on index:\n", joined_df.head())

# LEFT JOIN (default)
left_join = df_names.join(df_survival, how="left")
print("\nLeft Join:\n", left_join.head())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: How is join() different from merge()?
# Q2: Why must indexes align for join()?
# Q3: What is the default join type in join()?
# Q4: Can join() work without indexes?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Join Age column using PassengerId as index.
# 2. Perform an inner join using join().
# 3. Compare output of join() vs merge().

