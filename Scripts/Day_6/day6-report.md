# Day 6 Report – Logistic Regression & Classification Metrics

---

##  Technical Summary

Today, I transitioned from Regression to Classification by implementing a Logistic Regression model.

- Built a binary classification model to predict outcomes (Pass/Fail)
- Used `train_test_split` to divide data into training and testing sets
- Trained the model using `LogisticRegression()` and `.fit()`
- Generated predictions using `.predict()`
- Evaluated model performance using:
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-score)
- Visualized errors using a heatmap
- Analyzed feature importance using model coefficients

This helped me understand how models make decisions based on probabilities using the sigmoid function.

---

## ◈ The "Bug" Log

### Warning: X does not have valid feature names

- Cause: The model was trained using a DataFrame with column names, but prediction was made using a plain list [[3, 7]]
- Solution: Converted input into a DataFrame with proper column names:

import pandas as pd
new_data = pd.DataFrame([[3, 7]], columns=['Hours_Sleep', 'Coffee_Cups'])
model.predict(new_data)

## Conceptual Reflection

In a cancer detection system, a False Negative is more dangerous than a False Positive.

A False Negative means the model predicts that a person is healthy when they actually have cancer. This can delay treatment and lead to serious consequences or even death.

On the other hand, a False Positive may cause temporary stress and additional medical tests, but it does not miss the actual disease.

Therefore, minimizing False Negatives is more critical in medical applications.