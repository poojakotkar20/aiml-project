import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Hours': [1,2,3,4,5,6,7,8,9,10],
    'Score': [35,40,55,60,68,72,81,88,92,95]
}

df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Score']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test.values)
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions) # 1.0 is a perfect score!
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-Squared Score: {r2:.2f}")



import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue') # Real data
plt.plot(X, model.predict(X), color='red') # AI's best-fit line
plt.title("Hours vs Score: AI Prediction Line")
plt.show()