import random

# Generate random latitude/longitude for 10 delivery locations
def generate_locations(num_locations=10):
    locations = []
    for _ in range(num_locations):
        lat = random.uniform(40.0, 42.0)  # Latitude range (example for the U.S.)
        lon = random.uniform(-75.0, -73.0)  # Longitude range (example for the U.S.)
        locations.append((lat, lon))
    return locations

# Example usage
delivery_locations = generate_locations(10)
print(delivery_locations)
from geopy.distance import geodesic

# Function to calculate distance between two locations
def calculate_distance(loc1, loc2):
    return geodesic(loc1, loc2).kilometers

# Example usage
loc1 = (41.4583108811576, -74.28211896810873)
loc2 = (40.21221035941391, -74.39552310045156)
distance = calculate_distance(loc1, loc2)
print(f"Distance between loc1 and loc2: {distance} km")
import numpy as np

# Function to find the nearest unvisited location using a greedy approach
def greedy_route(locations):
    route = [locations[0]]  # Start from the depot (first location)
    unvisited = locations[1:]  # All locations except the depot

    while unvisited:
        last_location = route[-1]
        nearest_location = min(unvisited, key=lambda loc: calculate_distance(last_location, loc))
        route.append(nearest_location)
        unvisited.remove(nearest_location)

    return route

# Example usage
optimized_route = greedy_route(delivery_locations)
print("Optimized Route:")
for loc in optimized_route:
    print(loc)
# Function to calculate the total distance of the route
def total_route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i+1])
    # Optionally, return to the depot (closing the route loop)
    total_distance += calculate_distance(route[-1], route[0])
    return total_distance

# Example usage
route_distance = total_route_distance(optimized_route)
print(f"Total Distance: {route_distance:.2f} km")
