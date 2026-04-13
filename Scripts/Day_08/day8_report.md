# Day 8 Report – Regression on Real Dataset & Residual Analysis

## Technical Summary

Today, I worked with a real-world dataset using California Housing Data to build a regression model.

- Loaded dataset using `fetch_california_housing()` from Scikit-learn
- Converted data into a Pandas DataFrame for analysis
- Performed train-test split (80% training, 20% testing)
- Applied StandardScaler to normalize feature values
- Trained a Linear Regression model
- Generated predictions on unseen data
- Evaluated model performance using:
  - Mean Absolute Error (MAE)
  - R² Score
- Visualized model performance using a Residual Plot

This task helped me understand how regression works on real-world datasets and how to evaluate model reliability.


##  Conceptual Reflection

If the Residual Plot shows a clear "U" shape instead of random dots, it indicates that the Linear Regression model is not a good fit for the data.

This happens because the relationship between input features and the target variable is non-linear, while Linear Regression can only model straight-line relationships.

As a result, the model systematically makes errors, leading to a curved pattern in residuals.

To handle such cases, more advanced models like Polynomial Regression or other non-linear algorithms should be used.


##  Additional Insight

Residual analysis is a powerful diagnostic tool in Machine Learning. It helps identify whether a model is underfitting and whether a different modeling approach is required.