from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Using all 4 features for clustering

# Step 2: Apply K-means Clustering
# We'll set n_clusters=3 since we know there are 3 species in the dataset
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Predict cluster labels
cluster_labels = kmeans.predict(X)

# Step 3: Evaluate the clustering using inertia
print(f"Inertia (sum of squared distances to nearest cluster center): {kmeans.inertia_}")

# Step 4 (Optional): Visualize the clusters
# For visualization, we'll use only the first two features (sepal length and sepal width)
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids', marker='X')
plt.title("K-means Clustering of Iris Dataset (using Sepal Length and Sepal Width)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()
plt.show()
