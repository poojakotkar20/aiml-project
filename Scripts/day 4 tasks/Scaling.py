from sklearn.preprocessing import MinMaxScaler
import numpy as np
# Sample data: [Age, Salary]
data = np.array([[22, 50000], [45, 120000], [30, 80000]])
# Initialize the Scaler to put everything between 0 and 1
scaler = MinMaxScaler()
# Transform the data
scaled_data = scaler.fit_transform(data)
print("Original Data:\n", data)
print("\nScaled Data (Everything is now 0 to 1):\n", scaled_data)