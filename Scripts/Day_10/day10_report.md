# Day 10 Report – Non-Linear Models & Overfitting

##  Technical Summary

Today, I explored how Machine Learning models handle non-linear relationships and learned about the concept of overfitting.

- Generated synthetic "curvy" data using NumPy
- Used PolynomialFeatures to transform linear data into non-linear form
- Trained a Linear Regression model on polynomial features to capture curved patterns
- Implemented a DecisionTreeRegressor to model data using rule-based splits
- Compared models by visualizing predictions
- Performed a depth test using Decision Trees with different `max_depth` values (2, 5, 20)

This helped me understand how different models behave when handling complex data patterns.

## The "Bug" Log

### Issue: Understanding Overfitting Behavior

- Problem: Initially, the Decision Tree with higher depth seemed better because it fit the data perfectly
- Observation: The prediction line became very "jittery"
- Insight: Realized that the model was overfitting by memorizing noise instead of learning patterns
- Solution: Learned to control model complexity using 'max_depth' to improve generalization

## ◈ Conceptual Reflection

A "jittery" model that hits every training point is worse for future predictions because it is overfitting.

Overfitting occurs when a model memorizes the training data, including noise, instead of learning the true underlying pattern.

Such a model performs well on training data but fails on unseen data because it cannot generalize.

In contrast, a smooth "curvy" model captures the overall trend and ignores noise, making it more reliable for real-world predictions.

## Additional Insight

Decision Trees are powerful but prone to overfitting if not controlled. Techniques like limiting depth help balance model complexity and performance.