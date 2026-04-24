# Day 17: Hyperparameter Tuning with GridSearchCV

## Technical Summary

Today, I learned how to optimize machine learning models using GridSearchCV. Instead of manually selecting hyperparameters, GridSearch automates the process by testing multiple combinations and identifying the best configuration.

I implemented GridSearchCV on a Random Forest Classifier using the Breast Cancer dataset. I defined a parameter grid including `n_estimators`, `max_depth`, and `min_samples_split`, and applied 3-fold cross-validation to evaluate each combination.

The model tested multiple configurations and returned the best parameters along with the highest cross-validation score. I also saved the optimized model using `joblib` for future use.

---
## Total Model Fits

The GridSearch tested 27 parameter combinations with 3-fold cross-validation, resulting in a total of:

27 × 3 = 81 model fits.

## Conceptual Reflection

GridSearchCV tests every combination of parameters, which can become computationally expensive as the number of parameters increases.

For example, with 5 parameters having 10 values each, the total combinations become 100,000. Running cross-validation on each of these would be very slow.

This is why RandomizedSearchCV is used in large-scale systems—it randomly samples combinations, reducing time while still finding good results.

---

## Key Takeaways

* Hyperparameters control how a model learns and must be tuned carefully.
* GridSearchCV automates the tuning process using cross-validation.
* Total model training grows exponentially with more parameters.
* RandomizedSearchCV is more efficient for large datasets.
* Saving models using joblib is important for production use.
