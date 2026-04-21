import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 1. CREATE DATASET
# -----------------------------
# Features:
# Hours studied, Sleep hours, Common interests

data = {
    'User1_Hours': [5, 2, 6, 8, 3, 7, 4, 6, 5, 9],
    'User2_Hours': [6, 8, 5, 7, 2, 6, 3, 7, 4, 8],
    'User1_Sleep': [7, 5, 6, 8, 4, 7, 5, 6, 7, 8],
    'User2_Sleep': [7, 6, 7, 7, 5, 6, 4, 7, 6, 7],
    'Common_Interests': [3, 1, 4, 5, 2, 4, 1, 3, 2, 5],
    'Compatible': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("Dataset:\n", df.head())

# -----------------------------
# 2. DEFINE FEATURES & TARGET
# -----------------------------
X = df.drop('Compatible', axis=1)
y = df['Compatible']

# -----------------------------
# 3. POLYNOMIAL FEATURES
# -----------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# -----------------------------
# 4. TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

# -----------------------------
# 5. SCALE DATA
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# 6. RANDOM FOREST MODEL
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# -----------------------------
# 7. PREDICTIONS
# -----------------------------
y_pred = model.predict(X_test_scaled)

print("\nPredictions:", y_pred)
print("Actual:", y_test.values)

# -----------------------------
# 8. EVALUATION
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")

print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# 9. CONFUSION MATRIX
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('User Compatibility Confusion Matrix')
plt.show()

# -----------------------------
# 10. FEATURE IMPORTANCE
# -----------------------------
importances = model.feature_importances_

feature_names = poly.get_feature_names_out(X.columns)

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print("\nFeature Importance:\n")
print(importance_df.head(10))

# -----------------------------
# 11. SAMPLE PREDICTION
# -----------------------------
sample = np.array([[6, 7, 7, 7, 4]])  # new user pair

sample_poly = poly.transform(sample)
sample_scaled = scaler.transform(sample_poly)

prediction = model.predict(sample_scaled)
probability = model.predict_proba(sample_scaled)

print("\nNew Pair Prediction:", "Compatible" if prediction[0] == 1 else "Not Compatible")
print("Confidence:", probability)