## Technical Summary
Today I implemented Logistic Regression for binary classification using the Breast Cancer dataset. I also learned the importance of feature scaling and how classification models output probabilities using the sigmoid function.

## ◈ Task Inventory
- Loaded the Breast Cancer dataset using sklearn
- Split data into training and testing sets
- Applied StandardScaler for feature normalization
- Trained a Logistic Regression model
- Generated predictions using model.predict()
- Calculated model accuracy
- Visualized performance using a Confusion Matrix heatmap
- Used model.predict_proba() to analyze prediction probabilities
- Documented the difference between class predictions and probabilities

## Conceptual Reflection
In medical diagnosis, a False Negative is more dangerous than a False Positive because it fails to detect a disease, potentially leading to delayed treatment and serious consequences.