# Function to plot the route using Folium map
def plot_route_on_map(locations, route):
    # Initialize the map
    map_center = route[0]  # Start at the depot (first location)
    m = folium.Map(location=[map_center[0], map_center[1]], zoom_start=13)

    # Marker Cluster for locations
    marker_cluster = MarkerCluster().add_to(m)

    # Add the locations as markers on the map
    for idx, loc in enumerate(locations):
        folium.Marker([loc[0], loc[1]], popup=f"Location {idx + 1}").add_to(marker_cluster)

    # Add the route as a polyline
    route_latitudes = [loc[0] for loc in route]
    route_longitudes = [loc[1] for loc in route]
    folium.PolyLine(locations=list(zip(route_latitudes, route_longitudes)), color="red", weight=2.5, opacity=1).add_to(m)

    # Mark the depot on the map
    folium.Marker([route[0][0], route[0][1]], popup="Depot", icon=folium.Icon(color="green")).add_to(m)

    return m

# Streamlit app
def main():
    # Set up the title and description for the app
    st.title('Improved Delivery Route Optimization')
    st.write("""
        This app simulates the process of dynamically optimizing a delivery route using the greedy algorithm.
        The delivery man starts at the depot and moves to the nearest unvisited location until all deliveries are made.
        An interactive map will display the optimized route.
    """)

    # Number of locations to generate
    num_locations = st.slider("Select the number of delivery locations", min_value=5, max_value=20, value=10, step=1)

    # Generate the delivery locations
    locations = generate_locations(num_locations)

    # Show the generated locations
    st.write("Generated Delivery Locations:")
    st.write(locations)

    # Initialize the starting location (Depot)
    current_location = locations[0]  # Start from the first location (depot)
    unvisited_locations = locations[1:]  # All locations except the depot
    route = [current_location]  # The route starts with the depot
    total_distance = 0  # Track total distance
    total_time = 0  # Track total time

    # Display the starting depot
    st.write(f"Starting at Depot (Location: {current_location})")

    # Plot initial locations on the map
    map_placeholder = st.empty()

    # Dynamically update the map with the latest route
    for _ in range(len(locations) - 1):
        next_location = get_next_nearest_location(current_location, unvisited_locations)
        distance_to_next = geodesic(current_location, next_location).kilometers
        total_distance += distance_to_next
        time_to_next = estimate_time(distance_to_next)
        total_time += time_to_next
        
        route.append(next_location)
        current_location = next_location
        unvisited_locations.remove(next_location)

        # Display current location and next delivery details
        st.write(f"Current Location: {current_location} -> Next Location: {next_location} | Distance: {distance_to_next:.2f} km | Time to Next: {time_to_next:.2f} min")

        # Dynamically update the map with the latest route
        map_placeholder.markdown(plot_route_on_map(locations, route)._repr_html_(), unsafe_allow_html=True)

        # Simulate the real-time delivery movement with a pause
        time.sleep(0.5)

    # Show total distance and time after all deliveries are made
    st.write(f"Total distance traveled: {total_distance:.2f} km")
    st.write(f"Total time for the route: {total_time:.2f} minutes")

    # Plot the final route on the map
    st.write("Optimized Delivery Route:")
    final_map = plot_route_on_map(locations, route)
    st.markdown(final_map._repr_html_(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
