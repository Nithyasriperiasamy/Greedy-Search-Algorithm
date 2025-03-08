import random

# Generate random latitude/longitude for 20 delivery locations
def generate_locations(num_locations=20):
    locations = []
    for _ in range(num_locations):
        lat = random.uniform(40.0, 42.0)  # Latitude range (example)
        lon = random.uniform(-75.0, -73.0)  # Longitude range (example)
        locations.append((lat, lon))
    return locations

# Example usage
delivery_locations = generate_locations(20)
print(delivery_locations)
from sklearn.cluster import KMeans
import numpy as np

# Convert locations to a NumPy array for KMeans
locations_np = np.array(delivery_locations)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(locations_np)

# Get cluster centers (centroids) and labels (cluster assignments)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Output the cluster assignment for each location
for i, label in enumerate(labels):
    print(f"Location {delivery_locations[i]} is in cluster {label}")
import matplotlib.pyplot as plt

# Extract the latitudes and longitudes
latitudes = locations_np[:, 0]
longitudes = locations_np[:, 1]

# Plot the locations and the centroids
plt.scatter(latitudes, longitudes, c=labels, cmap='viridis', label='Delivery Locations')

# Plot the centroids (cluster centers)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', label='Centroids')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('K-Means Clustering of Delivery Locations')
plt.legend()
plt.show()
# Example: Function to compute the total route distance for a given set of locations
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i + 1])
    # Optionally, return to the depot (closing the loop)
    total_distance += calculate_distance(route[-1], route[0])
    return total_distance

# Now, optimize the route for each cluster
for cluster_id in range(3):
    cluster_locations = [delivery_locations[i] for i in range(len(delivery_locations)) if labels[i] == cluster_id]
    
    # Apply the Greedy algorithm or any route optimization method to each cluster
    optimized_route = greedy_route(cluster_locations)
    
    # Calculate the total distance of the optimized route for this cluster
    route_distance = calculate_total_distance(optimized_route)
    print(f"Optimized route for cluster {cluster_id}: {optimized_route}")
    print(f"Total distance: {route_distance} km")
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from geopy.distance import geodesic

# Step 1: Generate random delivery locations (latitude, longitude)
def generate_locations(num_locations=20):
    locations = []
    for _ in range(num_locations):
        lat = random.uniform(40.0, 42.0)  # Latitude range (example)
        lon = random.uniform(-75.0, -73.0)  # Longitude range (example)
        locations.append((lat, lon))
    return locations

# Step 2: Apply K-Means clustering
def apply_kmeans_clustering(locations, num_clusters=3):
    locations_np = np.array(locations)
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(locations_np)
    return kmeans.labels_, kmeans.cluster_centers_

# Step 3: Function to calculate distance between two locations
def calculate_distance(loc1, loc2):
    return geodesic(loc1, loc2).kilometers

# Generate 20 random delivery locations
delivery_locations = generate_locations(20)

# Apply K-Means to divide locations into 3 clusters
num_clusters = 3
labels, centroids = apply_kmeans_clustering(delivery_locations, num_clusters)

# Step 4: Visualize the delivery locations and K-Means clusters
def visualize_clusters(locations, labels, centroids):
    plt.figure(figsize=(10, 8))
    
    # Plot delivery locations colored by cluster
    plt.scatter([loc[0] for loc in locations], [loc[1] for loc in locations], c=labels, cmap='viridis', label='Locations')
    
    # Plot the cluster centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200, label='Centroids')
    
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Delivery Location Clusters')
    plt.legend()
    plt.grid(True)
    plt.show()

# Visualize the clusters
visualize_clusters(delivery_locations, labels, centroids)
