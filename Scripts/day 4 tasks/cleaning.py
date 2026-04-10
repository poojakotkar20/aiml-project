import pandas as pd
df = pd.read_csv("data.csv")
# 1. IDENTIFY: Where are the holes?
print("Missing Values:\n", df.isnull().sum())
# 2. FIX: Fill missing Age with the Average (Mean)
# This is called 'Imputation'
df['Age'] = df['Age'].fillna(df['Age'].mean())
# 3. FIX: Fill missing Score with a default value (e.g., 0)
df['Score'] = df['Score'].fillna(0)
print("\nCleaned Data:\n", df)