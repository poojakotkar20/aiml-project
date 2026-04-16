# Day 11 Report – Ensemble Learning with Random Forest


## Technical Summary

Today, I learned about Ensemble Learning using Random Forests.

- Implemented RandomForestRegressor on California Housing dataset
- Understood Bagging (Bootstrap Aggregation)
- Trained multiple decision trees and combined their predictions
- Evaluated model using R² score
- Visualized Feature Importance
- Conducted Tree Count experiment (10, 50, 200 trees)
- Measured performance vs training time

This helped me understand how combining multiple models improves stability and accuracy.


##  The "Bug" Log

### Issue: Understanding Training Time vs Accuracy

- Problem: Initially assumed more trees always improve performance
- Observation: Accuracy improvement slowed down after certain number of trees
- Insight: Identified diminishing returns
- Solution: Learned to balance performance and computational cost

##  Conceptual Reflection

As the number of trees increases, model performance improves initially due to reduced variance.

However, after a certain point, the improvement becomes minimal while training time increases significantly.

This is known as diminishing returns, where adding more trees does not justify the computational cost.

##  Additional Insight

Random Forest provides built-in feature importance, making it both powerful and interpretable for real-world applications.