"""
01_read_csv.py
-------------- 
Covers:
- Reading CSV files 
- Common parameters
- Basic validation
"""

import pandas as pd

# Reading CSV from local path
df = pd.read_csv("datasets/raw/titanic.csv")
print(df.head())

# Reading CSV from URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df_url = pd.read_csv(url)
print("\nLoaded from URL:\n", df_url.head())

# Common useful parameters
df_selected = pd.read_csv(
    url,
    usecols=["Survived", "Pclass", "Sex", "Age"],
    parse_dates=False
)

print("\nSelected Columns:\n", df_selected.head())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: What is the default delimiter in read_csv?
# Q2: Difference between usecols and dtype?
# Q3: When would you use chunksize in read_csv?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Load only 'Name' and 'Fare' columns from the dataset.
# 2. Count total number of rows.
# 3. Check memory usage of the DataFrame.

