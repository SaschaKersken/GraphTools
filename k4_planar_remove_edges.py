from graph import Graph
from copy import deepcopy

k4 = Graph()
k4.add_vertices(['V1', 'V2', 'V3', 'V4'])
k4.add_edges([('V1', 'V2'), ('V1', 'V3'), ('V1', 'V4')])
k4.add_edges([('V2', 'V3'), ('V2', 'V4')])
k4.add_edge('V3', 'V4')
pos = {'V1': (0, 0), 'V2': (0, 1), 'V3': (-1, -1), 'V4': (1, -1)}
print(k4)
k4.visualize(pos)
subgraph1 = deepcopy(k4)
subgraph1.remove_edge(('V1', 'V2'))
subgraph1.visualize(pos)
subgraph1.remove_edge(('V2', 'V3'))
subgraph1.visualize(pos)
subgraph1.remove_edge(('V1', 'V4'))
subgraph1.visualize(pos)
