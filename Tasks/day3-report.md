# Day 3 Progress Report – Core Architecture

# Setup Status
The development environment is working properly.

- VS Code is running successfully
- Python scripts are executing without errors
- Jupyter Notebook is launching correctly
- Project files are organized in the working directory


# Task Inventory
The following tasks were completed today:

- Created and executed `basics.py` using Python fundamentals
- Implemented data containers, loops, and functions
- Generated statistical report (min, max, average)
- Performed NumPy operations:
  - Created arrays
  - Reshaped data into a 2x2 matrix
  - Applied scaling using vectorized operations
- Created dataset file `data.csv`
- Loaded dataset using Pandas
- Analyzed data using:
  - `.head()`
  - `.describe()`
  - `.mean()`
- Fixed dataset errors for correct analysis
- Launched Jupyter Notebook
- Created `Day2_Submission.ipynb`
- Added Markdown explanation for Vectorization


# Debugging Log

## 1. Error: Cannot perform reduction 'mean' with string dtype
- Cause: The Score column contained a non-numeric value (`90s`)
- Solution: Corrected the value to `90` in the dataset


## 2. Issue: Terminal not accepting input
- Cause: A background process was running in the terminal
- Solution: Stopped the process using `Ctrl + C` and restarted the terminal


# Key Insights

The most important realization today was understanding Vectorization.

Instead of using loops, NumPy allows operations on entire datasets at once. 
This improves performance and is essential for handling large-scale data in AI/ML.

I also learned that even small data errors can affect the entire analysis, 
which highlights the importance of proper data cleaning.



# Conclusion

Day 3 focused on handling and processing data using Python, NumPy, and Pandas. 
It also emphasized documenting workflows using Jupyter Notebook, which is an essential practice in real-world AI development.