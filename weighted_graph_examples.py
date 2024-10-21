from weighted_graph import WeightedGraph

graph = WeightedGraph()
graph.add_vertex('A', 'B', 'C', 'D', 'E')
graph.add_edge('A', 'B', 150)
graph.add_edge('A', 'D', 220)
graph.add_edge('B', 'C', 410)
graph.add_edge('B', 'D', 650)
graph.add_edge('B', 'E', 380)
graph.add_edge('D', 'E', 190)
print(graph)
print("Adjazenzmatrix:")
print(graph.adjacency_matrix)
print("Von A ausgehende Kanten:")
print(graph.edges_from_vertex('A'))
print(graph.edges_from_vertex_with_weights('A'))
print("Nachbarknoten von A:")
print(graph.neighbors('A'))
print(graph.neighbors_with_weights('A'))
graph.visualize()
print("Entferne Knoten D")
graph.remove_vertex('D')
print(graph)
print("Adjazenzmatrix:")
print(graph.adjacency_matrix)
print("Von A ausgehende Kanten:")
print(graph.edges_from_vertex('A'))
print(graph.edges_from_vertex_with_weights('A'))
print("Nachbarknoten von A:")
print(graph.neighbors('A'))
print(graph.neighbors_with_weights('A'))
graph.visualize()

