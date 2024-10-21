from weighted_graph import WeightedGraph
from weighted_graph_tools import mst
from graph_tools import eulerian_cycle
from salesman import create_graph, get_distance, get_start

cities = create_graph()
start = get_start(cities.vertices)
total_distance = 0
current = start
visited = [start]

while len(visited) < len(cities.vertices):
    neighbors = cities.neighbors_with_weights(current)
    neighbors.sort(key = lambda record: record[1])
    for (next, next_distance) in neighbors:
        if next not in visited:
            break
    visited.append(next)
    total_distance += next_distance
    current = next

visited.append(start)
total_distance += cities.edges[(current, start)]
print(visited, total_distance)
cities.visualize()
cities_mst_data = mst(cities)
print(f"Minimaler Spannbaum: {cities_mst_data} ({sum(cities_mst_data.values())})")
cities_mst = WeightedGraph()
cities_mst.add_edges(cities_mst_data)
cities_mst.visualize()
