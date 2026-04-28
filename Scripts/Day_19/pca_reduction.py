import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import pandas as pd
# 1. Load high-dimensional data (64 features)
digits = load_digits()
X = digits.data
y = digits.target
# 2. Initialize PCA
# We reduce 64 dimensions down to 2 for visualization
pca = PCA(n_components=2)
# 3. Fit and Transform
X_reduced = pca.fit_transform(X)
# 4. Check the "Explained Variance"
# This tells us how much information we kept
print(f"Variance retained by 2 components: {sum(pca.explained_variance_ratio_)*100:.2f}%")
# 5. Visualization
plt.figure(figsize=(10, 7))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='viridis',
s=20)
plt.colorbar(label='Digit Class')
plt.title("Digits Dataset Projected into 2D Space via PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()