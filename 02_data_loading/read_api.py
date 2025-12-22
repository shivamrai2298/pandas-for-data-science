"""
05_read_api.py
--------------
Covers:
- Reading data from APIs
"""

import pandas as pd
import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch API data
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df_api = pd.DataFrame(data)
print(df_api.head())

# ==================================================
# INTERVIEW QUESTIONS
# ==================================================
# Q1: Difference between API data and CSV data?
# Q2: How do you handle API failures?
# Q3: How do you paginate large API responses?

# ==================================================
# PRACTICE EXERCISES
# ==================================================
# 1. Filter posts for userId = 1.
# 2. Count number of posts per user.
# 3. Save API data to JSON file.

