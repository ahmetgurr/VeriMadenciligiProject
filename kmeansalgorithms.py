# -*- coding: utf-8 -*-
"""
@author: Ahmet
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_data(n_samples=200, n_features=2, n_centers=5, random_state=None):
    np.random.seed(random_state)
    data = []

    for _ in range(n_centers):
        center = np.random.rand(n_features) * 10  # Rastgele bir merkez oluştur
        cluster = center + np.random.randn(n_samples // n_centers, n_features)  # Merkez etrafında rastgele veri noktaları oluştur
        data.append(cluster)

    return np.vstack(data)

def visualize_data(data):
    plt.scatter(data[:, 0], data[:, 1])
    plt.title('Oluşturulan Veri Noktaları')
    plt.show()

def k_means(data, k=5, max_iters=100, tolerance=1e-4):
    centroids = data[np.random.choice(len(data), k, replace=False)]
    
    iteration = 0
    while iteration < max_iters:
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        if np.linalg.norm(new_centroids - centroids) < tolerance:
            breakgit
        centroids = new_centroids
        iteration += 1
    
    return labels, centroids

def visualize_results(data, labels, centroids):
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='red')
    plt.title('K-Means Kümeleme Sonuçları')
    plt.show()

# Veri oluşturma
data = generate_data(n_samples=200, n_features=2, n_centers=5, random_state=42)

# Veriyi görselleştirme
visualize_data(data)

# K-Means modelini kullanma
labels, centroids = k_means(data, k=5)

# Sonuçları görselleştirme
visualize_results(data, labels, centroids)
