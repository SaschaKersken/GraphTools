from digraph import Digraph

graph = Digraph()
graph.add_vertex('A', 'B', 'C', 'D', 'E')
graph.add_edge('A', 'A')
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('D', 'E')
graph.add_edge('B', 'A')
graph.add_edge('D', 'A')
print(graph)
print("Adjazenzmatrix:")
print(graph.adjacency_matrix)
print("Von B ausgehende Kanten:")
print(graph.edges_from_vertex('B'))
print("Zu B führende Kanten:")
print(graph.edges_to_vertex('B'))
print("Von B erreichbare Knoten:")
print(graph.successors('B'))
print("Zu B führende Knoten:")
print(graph.predecessors('B'))
print("Nachbarknoten von B:")
print(graph.neighbors('B'))
graph.visualize()
print("Entferne Knoten D")
graph.remove_vertex('D')
print(graph)
print("Adjazenzmatrix:")
print(graph.adjacency_matrix)
print("Von B ausgehende Kanten:")
print(graph.edges_from_vertex('B'))
print("Zu B führende Kanten:")
print(graph.edges_to_vertex('B'))
print("Von B erreichbare Knoten:")
print(graph.successors('B'))
print("Zu B führende Knoten:")
print(graph.predecessors('B'))
print("Nachbarknoten von B:")
print(graph.neighbors('B'))
graph.visualize()

