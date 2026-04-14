# Day 9 Report – Hyperparameter Tuning & Model Optimization


##  Technical Summary

Today, I learned how to optimize Machine Learning models using GridSearchCV.

- Used the California Housing dataset
- Applied feature scaling using StandardScaler
- Implemented Ridge Regression
- Defined a parameter grid for alpha values
- Used GridSearchCV with 5-fold cross-validation
- Identified the best hyperparameter (alpha)
- Compared default vs optimized model using R² score

This helped me understand how to systematically improve model performance without manual trial and error.


##  The "Bug" Log

### Issue: Understanding GridSearchCV Output

- Problem: Initially unclear how to use `best_estimator_` after grid search
- Solution: Learned that `grid_search.best_estimator_` returns the optimized model which can be directly used for prediction


##  Conceptual Reflection

It is better to start with a wider range of values (e.g., [0.1, 1, 10, 100]) because it helps identify the overall trend and locate the optimal region.

Using small increments from the beginning may limit the search space and miss better parameter values.

Once the best region is found, a finer search can be performed for precise tuning.


##  Additional Insight

Cross-validation ensures that model performance is consistent and not dependent on a single train-test split, making the evaluation more reliable.