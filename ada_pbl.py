import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import streamlit as st

# Sample data representing Indian airports (nodes) and flight routes (edges)
airports = {
    'DEL': 'Indira Gandhi International Airport',
    'BOM': 'Chhatrapati Shivaji Maharaj International Airport',
    'BLR': 'Kempegowda International Airport',
    'MAA': 'Chennai International Airport',
    'HYD': 'Rajiv Gandhi International Airport',
    'CCU': 'Netaji Subhas Chandra Bose International Airport',
    'GOI': 'Dabolim Airport',
    'PNQ': 'Pune Airport',
    'AMD': 'Sardar Vallabhbhai Patel International Airport',
    'JAI': 'Jaipur International Airport',  # Added new airport
    'TRV': 'Trivandrum International Airport',  # Added new airport
    'LKO': 'Chaudhary Charan Singh International Airport',  # Added new airport
}

flight_routes = [
    # These form SSC
    ('GOI', 'BOM'), ('DEL', 'BLR'), ('BOM', 'HYD'), ('BLR', 'MAA'),
    ('MAA', 'CCU'), ('HYD', 'CCU'), ('CCU', 'DEL'), ('BLR', 'DEL'),
    ('PNQ', 'AMD'), ('AMD', 'PNQ'), ('DEL', 'BOM'), ('DEL', 'PNQ'),
    ('JAI', 'TRV'), ('TRV', 'LKO'), ('LKO', 'JAI') 
]

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)   

    def dfs_fill_order(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_fill_order(neighbor, visited, stack)
        stack.append(v)
        self.graph[u].append(v)     

    def dfs_collect_scc(self, v, visited, scc):
        visited[v] = True
        scc.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_collect_scc(neighbor, visited, scc)
  
    def kosaraju_scc(self):
        stack = []
        visited = {v: False for v in self.V}
        
        for v in self.V:
            if not visited[v]:
                self.dfs_fill_order(v, visited, stack)
        
        transposed_graph = self.transpose()
        visited = {v: False for v in self.V}
        sccs = []
        
        while stack:
            v = stack.pop()
            if not visited[v]:
                scc = []
                transposed_graph.dfs_collect_scc(v, visited, scc)
                sccs.append(scc)
        return sccs
      
 # Dijkstra's algorithm for shortest path
def dijkstra(graph, source, target):
    G = nx.DiGraph()
    for u, v in graph:
        G.add_edge(u, v, weight=1)  # Assuming all edges have weight 1
    
    try:
        path = nx.shortest_path(G, source=source, target=target, weight='weight')
        return path
    except nx.NetworkXNoPath:
        return None
   
# Streamlit Interface
st.title("Airport Route Analyzer")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "SCC Analysis", "Graph Visualization", "Shortest Path"])

# Page 1: Home
if page == "Home":
    st.image("AIRPORT FINDER.png", use_column_width=True)
    st.write("Navigate through the sidebar to explore different features.")


# JIRA Task ID in Jira: AP-7 - correct order of pages
# Page 2: SCC Analysis
elif page == "SCC Analysis":
    st.header("Strongly Connected Components (SCC) Analysis")

    # Dropdowns for selecting source and destination airports
    source_airport = st.selectbox("Select Source Airport", list(airports.keys()), format_func=lambda x: airports[x])
    destination_airport = st.selectbox("Select Destination Airport", list(airports.keys()), format_func=lambda x: airports[x])

    if st.button("Check"):
        # Find the SCC containing the source airport
        scc_found = None
        for scc in sccs:
            if source_airport in scc:
                scc_found = scc
                break
        
        if scc_found and destination_airport in scc_found:
            st.success(f"{airports[source_airport]} and {airports[destination_airport]} are in the same SCC.")
        else:
            st.error(f"{airports[source_airport]} and {airports[destination_airport]} are NOT in the same SCC.")

# Page 3: Graph Visualization
elif page == "Graph Visualization":
    st.header("Airport Route Graph Visualization")

    # Visualize the graph using Matplotlib and NetworkX
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for airport in airports.keys():
        G.add_node(airport)

    for u, v in flight_routes:
        G.add_edge(u, v)

    # Draw the graph with SCCs highlighted
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 10))

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=flight_routes, arrowstyle='->', arrowsize=20)

    # Draw node labels with codes only
    labels = {node: node for node in G.nodes}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, verticalalignment='center')

    # Highlight SCCs with different colors
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    for i, scc in enumerate(sccs):
        nx.draw_networkx_nodes(G, pos, nodelist=scc, node_color=colors[i % len(colors)], node_size=700)

    st.pyplot(plt)

# Page 4: Shortest Path
elif page == "Shortest Path":
    st.header("Shortest Path Finder")

    # Dropdowns for selecting source and destination airports
    source_airport = st.selectbox("Select Source Airport", list(airports.keys()), format_func=lambda x: airports[x])
    destination_airport = st.selectbox("Select Destination Airport", list(airports.keys()), format_func=lambda x: airports[x])

    if st.button("Find Shortest Path"):
        path = dijkstra(flight_routes, source_airport, destination_airport)
        
        if path:
            st.success(f"The shortest path from {airports[source_airport]} to {airports[destination_airport]} is: {' -> '.join(path)}")
        else:
            st.error(f"No path found between {airports[source_airport]} and {airports[destination_airport]}")