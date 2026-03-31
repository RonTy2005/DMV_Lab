import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy import stats

# Sample dataset (you can replace this with your own CSV)
data = {
    'X': [10, 12, 13, 12, 11, 14, 15, 100],   # 100 is an outlier
    'Y': [20, 22, 21, 23, 19, 24, 25, 5]      # 5 is an outlier
}

df = pd.DataFrame(data)

# -------------------------------
# 1. Correlation
# -------------------------------
correlation = df.corr()
print("Correlation Matrix:\n", correlation)

# -------------------------------
# 2. Outlier Detection (Z-score)
# -------------------------------
z_scores = np.abs(stats.zscore(df))
outliers = (z_scores > 3)

print("\nOutliers Detected:\n", outliers)

# Remove outliers for clustering
df_clean = df[(z_scores < 3).all(axis=1)]

# -------------------------------
# 3. Clustering (K-Means)
# -------------------------------
kmeans = KMeans(n_clusters=2, random_state=0)
df_clean['Cluster'] = kmeans.fit_predict(df_clean)

# -------------------------------
# 4. Scatter Plot
# -------------------------------
plt.figure(figsize=(8, 6))

# Plot clusters
for cluster in df_clean['Cluster'].unique():
    cluster_data = df_clean[df_clean['Cluster'] == cluster]
    plt.scatter(cluster_data['X'], cluster_data['Y'], label=f'Cluster {cluster}')

# Plot outliers in red
outlier_points = df[(z_scores > 3).any(axis=1)]
plt.scatter(outlier_points['X'], outlier_points['Y'], color='red', label='Outliers', marker='x')

plt.title("Scatter Plot with Clustering and Outliers")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()

plt.show()