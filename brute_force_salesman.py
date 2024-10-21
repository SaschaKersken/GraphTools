from itertools import permutations
from time import time
from salesman import create_graph, get_distance, get_start

cities = create_graph()
start = get_start(cities.vertices)
list_of_cities = cities.vertices[:]
list_of_cities.remove(start)
routes = permutations(list_of_cities)
shortest = 100000
result = []

for i, route in enumerate(routes):
    route_with_start = [start] + list(route)
    current_distance = get_distance(cities, route_with_start)
    if current_distance < shortest:
        shortest = current_distance
        result = route_with_start

print(result, shortest)
