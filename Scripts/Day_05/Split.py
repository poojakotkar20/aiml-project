from sklearn.model_selection import train_test_split
import pandas as pd
# Sample Dataset: Hours Studied vs Exam Score
data = {'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 'Score': [35, 40, 55, 60, 68, 72, 81, 88, 92, 95]}
df = pd.DataFrame(data)
X = df[['Hours']] # Features (Capital X for matrix)
y = df['Score'] # Target (Lowercase y for vector)
# Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training items: {len(X_train)} | Testing items: {len(X_test)}")