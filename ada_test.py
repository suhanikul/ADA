import pytest
from ada_pbl import Graph, dijkstra  # replace 'your_module' with your actual file name

# Test Kosaraju's SCC algorithm
def test_kosaraju_scc():
    airports = ['A', 'B', 'C', 'D', 'E']
    flight_routes = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E')]
    
    g = Graph(airports)
    for u, v in flight_routes:
        g.add_edge(u, v)
    
    sccs = g.kosaraju_scc()
    
    assert len(sccs) == 3  # Assuming 3 SCCs in this simple example

# Test Dijkstra's algorithm
def test_dijkstra():
    flight_routes = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    source = 'A'
    destination = 'D'
    
    result = dijkstra(flight_routes, source, destination)
    
    assert result == ['A', 'B', 'C', 'D']
