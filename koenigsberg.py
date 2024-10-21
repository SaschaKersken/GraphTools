from weighted_graph import WeightedGraph
from graph_tools import has_eulerian_path

koenigsberg = WeightedGraph()
koenigsberg.add_vertex('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
koenigsberg.add_edges({('A', 'B'): 1, ('A', 'D'): 4})
koenigsberg.add_edges({('B', 'C'): 1, ('B', 'E'): 4})
koenigsberg.add_edge('C', 'F', 4)
koenigsberg.add_edges({('D', 'E'): 1, ('D', 'G'):4})
koenigsberg.add_edges({('E', 'F'): 4, ('E', 'H'): 4})
koenigsberg.add_edge('F', 'I', 4)
koenigsberg.add_edge('G', 'H', 1)
koenigsberg.add_edge('H', 'I', 1)
print(koenigsberg)
print(f"Lösbar? {has_eulerian_path(koenigsberg)}")
koenigsberg.visualize()
