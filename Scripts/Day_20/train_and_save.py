import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
# 1. Load and Split Data
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)
# 2. Create an End-to-End Pipeline
# This ensures scaling and modeling happen in one sequence
pipeline = Pipeline([('scaler', StandardScaler()),
 ('regressor', RandomForestRegressor(n_estimators=100,
random_state=42))
])
# 3. Train the Pipeline
print("Training production pipeline...")
pipeline.fit(X_train, y_train)
# 4. Save the Pipeline (The "Brain" file)
joblib.dump(pipeline, 'production_model.pkl')
print("Model and Scaler saved as production_model.pkl")
