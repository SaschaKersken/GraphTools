from digraph import Digraph
from node_search import get_path, dfs, bfs

graph = Digraph()
graph.add_vertex('A', 'B', 'C', 'D', 'E')
graph.add_edges([('A', 'B'), ('A', 'D')])
graph.add_edges([('B', 'C'), ('B', 'D'), ('B', 'E')])
graph.add_edges([('C', 'A'), ('C', 'E')])
graph.add_edge('D', 'E')
graph.add_edge('E', 'C')

print(graph)
a_to_c_1 = dfs(
    'A',
    lambda vertex: vertex == 'C',
    lambda vertex: graph.successors(vertex)
)
print("Von A nach C mit Tiefensuche:")
print(get_path(a_to_c_1))
a_to_c_2 = bfs(
    'A',
    lambda vertex: vertex == 'C',
    lambda vertex: graph.successors(vertex)
)
print("Von A nach C mit Breitensuche:")
print(get_path(a_to_c_2))
graph.visualize()
