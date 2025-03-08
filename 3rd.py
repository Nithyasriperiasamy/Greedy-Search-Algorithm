import random
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import time  # To simulate real-time updates

# Generate random delivery locations (latitude, longitude)
def generate_locations(num_locations=10):
    locations = []
    for _ in range(num_locations):
        lat = random.uniform(12.9, 13.2)  # Simulated latitude for a region (e.g., Chennai)
        lon = random.uniform(80.1, 80.3)  # Simulated longitude for a region (e.g., Chennai)
        locations.append((lat, lon))
    return locations

# Greedy algorithm to find the nearest unvisited location and deliver dynamically
def dynamic_greedy_route(locations):
    route = [locations[0]]  # Start from the first location (depot)
    unvisited = locations[1:]  # All locations except the depot
    current_location = locations[0]  # Start at the depot
    total_distance = 0

    while unvisited:
        # Calculate distances to all unvisited locations from the current location
        nearest_location = min(unvisited, key=lambda loc: geodesic(current_location, loc).kilometers)
        distance_to_nearest = geodesic(current_location, nearest_location).kilometers
        total_distance += distance_to_nearest

        # Simulate delivery by "moving" to the nearest location
        print(f"Current Location: {current_location} -> Next Location: {nearest_location} | Distance: {distance_to_nearest:.2f} km")
        route.append(nearest_location)
        unvisited.remove(nearest_location)  # Mark this location as visited
        current_location = nearest_location  # Update current location to the newly visited one
        
        # Simulate real-time progression with a small delay to visualize the dynamic movement
        time.sleep(1)  # This would simulate the time taken to move to the next location (in a real scenario, it would be real-time data)
    
    return route, total_distance

# Function to plot the locations and route
def plot_route(locations, route):
    # Plot the locations (including depot)
    plt.scatter([loc[0] for loc in locations], [loc[1] for loc in locations], c='blue', label='Delivery Locations')
    
    # Plot the route (path followed by the delivery man)
    route_latitudes = [loc[0] for loc in route]
    route_longitudes = [loc[1] for loc in route]
    plt.plot(route_longitudes, route_latitudes, color='red', marker='o', label='Optimized Route')

    # Mark the depot in green
    depot = route[0]
    plt.scatter(depot[0], depot[1], c='green', marker='*', s=200, label="Depot (Start)")

    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Dynamic Delivery Route Optimization')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
locations = generate_locations(10)  # Generate 10 random locations
route, total_distance = dynamic_greedy_route(locations)  # Get the optimized route using dynamic Greedy algorithm

print(f"Total distance traveled: {total_distance:.2f} km")
plot_route(locations, route)  # Visualize the route
