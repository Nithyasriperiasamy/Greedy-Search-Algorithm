
# Dynamic Delivery Route Optimization 🚚  

This project simulates real-time delivery route optimization using a greedy algorithm. It dynamically finds the shortest path for deliveries and visualizes the route on an interactive Folium map using Streamlit.  

## Feature 
✅ Generate random delivery locations 📍  
✅ Optimize delivery order using the nearest neighbor approach 📊  
✅ Display real-time updates on an interactive map 🗺️  
✅ Simulate real-time movement with live tracking ⏳  

## Code Overview
1. Route Optimization (`dynamic_greedy_route.py`)
   - Uses Geopy to calculate distances between locations  
   - Implements a greedy algorithm to optimize delivery order  

2. Map Visualization (`plot_route_on_map.py`)
   - Uses Folium to plot locations and route  
   - Displays the optimized path dynamically

3. Real-time Simulation (`main.py`)
   - Uses Streamlit to display updates live  
   - Simulates movement with real-time tracking

4. Supporting Functions (`utils.py`)
   - generate_locations(): Generates random delivery locations  
   - estimate_time(): Estimates time based on distance  

## Installation & Usage

pip install streamlit folium geopy
streamlit run main.py


