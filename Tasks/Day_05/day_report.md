# Day 5 Report – Linear Regression & Evaluation

---

## Technical Summary

Today, I learned how to build my first Machine Learning model using **Linear Regression**.

- Performed data splitting using `train_test_split` into training (80%) and testing (20%) sets
- Trained a model using `LinearRegression()` and `.fit()` method
- Generated predictions using `.predict()`
- Evaluated model performance using:
  - **Mean Squared Error (MSE)**
  - **R² Score (Coefficient of Determination)**
- Visualized the relationship between features using a regression line with Matplotlib

This process helped me understand how a model learns relationships between input (X) and output (y).

---

## The "Bug" Log

### Error: NameError: 'X_train' / 'X' is not defined

- **Cause:** Variables like `X_train`, `y_train`, or `X` were used without being defined in the current file or notebook cell
- **Issue:** Python files and Jupyter cells do not share variables automatically
- **Solution:** Ensured that dataset creation, splitting, and model training code were executed before using these variables

```python
X = df[['Hours']]
y = df['Score']

Conceptual Reflection

If the model is trained on only 2 rows of data instead of 8, its predictions become highly inaccurate.

With very limited data, the model cannot properly learn the relationship between input and output. This may lead to overfitting or incorrect patterns.

As a result, predictions on new data will not be reliable.

Therefore, having more training data helps the model generalize better and improves prediction accuracy.