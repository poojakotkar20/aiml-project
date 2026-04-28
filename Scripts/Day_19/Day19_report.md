# Day 19: PCA for Feature Compression

## Technical Summary

Today, I worked on Dimensionality Reduction using Principal Component Analysis (PCA). I applied PCA on the Digits dataset, which originally contains 64 features, and reduced it to 2 components for visualization.

I calculated the Explained Variance Ratio to measure how much information is retained after reduction. I also identified the number of components required to retain 95% of the original data variance.

Additionally, I compared the performance of a Logistic Regression model trained on the original dataset versus the PCA-reduced dataset to observe the impact on training time.


## The "Bug" Log

While implementing PCA, there were no major logical errors, but I ensured:

* Correct usage of fit_transform() for dimensionality reduction
* Proper calculation of cumulative variance using NumPy
* Setting max_iter=1000 in Logistic Regression to avoid convergence warnings

These adjustments ensured smooth execution and correct results.

##  Conceptual Reflection

In MeetMux, users may have hundreds of features such as interests, activity patterns, and preferences. Processing such high-dimensional data directly can slow down algorithms like K-Means.

By applying PCA before clustering, we reduce the number of features while preserving important information. This makes the system faster and improves the efficiency of user recommendations.

##  Key Takeaways

* PCA reduces high-dimensional data into fewer meaningful components
* Explained variance helps measure information retention
* Dimensionality reduction improves model speed and efficiency
* PCA is useful before applying clustering algorithms like K-Means
* It works best for linear relationships in data