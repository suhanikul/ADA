import pytest
from collections import defaultdict
from app import Graph, dijkstra

# Sample data for testing
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
    'JAI': 'Jaipur International Airport',
    'TRV': 'Trivandrum International Airport',
}

flight_routes = [
    ('GOI', 'BOM'), ('DEL', 'BLR'), ('BOM', 'HYD'), ('BLR', 'MAA'),
    ('MAA', 'CCU'), ('HYD', 'CCU'), ('CCU', 'DEL'), ('BLR', 'DEL'),
    ('PNQ', 'AMD'), ('AMD', 'PNQ'), ('DEL', 'BOM'), ('DEL', 'PNQ'),
    ('JAI', 'TRV'), ('IXB', 'COK'),('COK', 'STV'), ('STV', 'VGA'), ('VGA', 'IXB'),
]

# Test cases
def test_kosaraju_scc():
    g = Graph(list(airports.keys()))
    for u, v in flight_routes:
        g.add_edge(u, v)

    sccs = g.kosaraju_scc()
    assert len(sccs) > 0  

    # Check if specific airports are in the same SCC
    scc_found = None
    for scc in sccs:
        if 'DEL' in scc:
            scc_found = scc
            break
    assert 'BOM' in scc_found 

def test_dijkstra():
    graph = flight_routes
    source = 'DEL'
    target = 'BOM'
    path = dijkstra(graph, source, target)
    assert path == ['DEL', 'BOM']  

def test_no_path():
    graph = flight_routes
    source = 'PNQ'
    target = 'DEL'
    path = dijkstra(graph, source, target)
    assert path is None 

def test_scc_disconnected_nodes():
    g = Graph(['a', 'b', 'c', 'd'])  
    sccs = g.kosaraju_scc()
    
    # Check that we have 4 SCCs, each containing one node
    assert len(sccs) == 4  
    assert set(sccs[0]) == {'a'} or set(sccs[1]) == {'a'} or set(sccs[2]) == {'a'} or set(sccs[3]) == {'a'}
    assert set(sccs[0]) == {'b'} or set(sccs[1]) == {'b'} or set(sccs[2]) == {'b'} or set(sccs[3]) == {'b'}
    assert set(sccs[0]) == {'c'} or set(sccs[1]) == {'c'} or set(sccs[2]) == {'c'} or set(sccs[3]) == {'c'}
    assert set(sccs[0]) == {'d'} or set(sccs[1]) == {'d'} or set(sccs[2]) == {'d'} or set(sccs[3]) == {'d'}

def test_scc_multiple_components():
    g = Graph(['1', '2', '3', '4'])
    g.add_edge('1', '2')
    g.add_edge('2', '1')
    g.add_edge('3', '4')
    g.add_edge('4', '3')

    sccs = g.kosaraju_scc()
    assert len(sccs) == 2  
    assert set(sccs[0]) == {'1', '2'} or set(sccs[1]) == {'1', '2'}  
    assert set(sccs[0]) == {'3', '4'} or set(sccs[1]) == {'3', '4'}  

if __name__ == "__main__":
    pytest.main()
