# Day 4 Report – Pre-processing Protocol


## Technical Summary

Today, I worked on Data Pre-processing, specifically focusing on Data Imputation and Feature Scaling.

- Used Pandas to identify missing values using `.isnull()`
- Applied mean imputation to fill missing values in the "Age" column
- Replaced missing "Score" values with a default value (0)
- Learned feature scaling using MinMaxScaler from Scikit-learn
- Generated a heatmap visualization using Seaborn to understand feature relationships

This process is critical because raw data is often incomplete and needs cleaning before being used in Machine Learning models.

---

## The "Bug" Log

### Error: KeyError: 'Age'

- Cause: The column name contained extra spaces (e.g., " Age") in the CSV file
- Issue: Pandas could not locate the column using `df['Age']`
-  Solution: Cleaned column names using:

```python
df.columns = df.columns.str.strip()

## The "Bug" Log

Filling missing values with the mean is better than using 0 because 0 is not a realistic value for features like age.

Using 0 introduces incorrect data and can distort the dataset, leading to inaccurate model predictions. It creates false patterns and reduces model performance.

On the other hand, mean imputation provides a balanced estimate based on existing data and helps maintain the overall distribution of the dataset.

Therefore, filling missing values with the mean improves data quality and ensures better results in Machine Learning models.