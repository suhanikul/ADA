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
}

flight_routes = [
    #These form SSC
    ('GOI', 'BOM'), ('DEL', 'BLR'), ('BOM', 'HYD'), ('BLR', 'MAA'),
    ('MAA', 'CCU'), ('HYD', 'CCU'), ('CCU', 'DEL'),('BLR', 'DEL'),
    # PNQ and AMD are connected in a way that doesn't form an SCC
    ('PNQ', 'AMD'), ('AMD', 'PNQ'),('DEL','BOM'),('DEL','PNQ')
]

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)



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
    
# Streamlit Interface
st.title("Airport Route Analyzer")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "SCC Analysis", "Graph Visualization"])
