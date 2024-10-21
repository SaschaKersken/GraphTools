from weighted_graph import WeightedGraph
from weighted_graph_tools import mst, dijkstra, get_dijkstra_path

w_graph = WeightedGraph()
w_graph.add_vertex('A', 'B', 'C', 'D', 'E')
w_graph.add_edges(
    {('A', 'B'): 7, ('B', 'C'): 2, ('C', 'A'): 9, ('B', 'D'): 1,
    ('C', 'D'): 4, ('D', 'E'): 8, ('B', 'E'): 6}
)
print(w_graph)
mst_result = mst(w_graph)
print(f"Minimaler Spannbaum: {mst_result}")
print(f"Summe der Kantengewichte: {sum(mst_result.values())}")
distances, paths = dijkstra(w_graph, 'A')
print("Dijkstra von A aus:")
print(f"Entfernungen der günstigsten Routen: {distances}")
print(f"Günstigste Routen: {paths}")
path = get_dijkstra_path('A', 'E', paths)
total = sum([item[2] for item in path])
print(f"Günstigste Route von A nach E: {path}, Gesamt: {total}")
w_graph.visualize()
mst_graph = WeightedGraph()
mst_graph.add_edges(mst_result)
mst_graph.visualize()
dijkstra_edges = {(vertex, neighbor): weight
    for (vertex, neighbor, weight) in paths.values()
}
dijkstra_graph = WeightedGraph()
dijkstra_graph.add_edges(dijkstra_edges)
dijkstra_graph.visualize()
