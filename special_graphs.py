from graph import Graph
from graph_tools import is_bipartite, is_k5, is_k3_3, is_planar
from copy import deepcopy

k5 = Graph()
k5.add_vertices(['A', 'B', 'C', 'D', 'E'])
k5.add_edges([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')])
k5.add_edges([('B', 'C'), ('B', 'D'), ('B', 'E')])
k5.add_edges([('C', 'D'), ('C', 'E')])
k5.add_edge('D', 'E')

c5 = Graph()
c5.add_vertices(['A', 'B', 'C', 'D', 'E'])
c5.add_edges([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')])

pos5 = {'A': (0, 1), 'B': (0.8, 0.2), 'C': (0.5, -1), 'D': (-0.5, -1), 'E': (-0.8, 0.2)}

k5.visualize(pos5)
c5.visualize(pos5)

k3_3 = Graph()

k3_3.add_edges([('A', 'D'), ('A', 'E'), ('A', 'F')])
k3_3.add_edges([('B', 'D'), ('B', 'E'), ('B', 'F')])
k3_3.add_edges([('C', 'D'), ('C', 'E'), ('C', 'F')])

pos3_3 = {'A': (-1, 1), 'B': (0, 1), 'C': (1, 1), 'D': (-1, -1), 'E': (0, -1), 'F': (1, -1)}

k3_3.visualize(pos3_3, colors=['#FFFF00', '#FF00FF', '#FF00FF', '#FF00FF', '#FFFF00', '#FFFF00'])

k3_3_plus_edge = deepcopy(k3_3)
k3_3_plus_edge.add_edge('A', 'B')
k3_3_plus_edge.visualize(pos3_3)

k3_3_plus_vertex = deepcopy(k3_3)
k3_3_plus_vertex.add_vertex('G')
k3_3_plus_vertex.add_edges([('A', 'G'), ('B', 'G')])
pos3_3['G'] = (-0.5, 0.75)
k3_3_plus_vertex.visualize(pos3_3)

print("Bipartit?")
print("K3,3: ", is_bipartite(k3_3), "- K3,3 mit Zusatzkante:", is_bipartite(k3_3_plus_edge), "- K5:", is_bipartite(k5), "- C5:", is_bipartite(c5))
print("K5?")
print("K5:", is_k5(k5), "- K3,3:", is_k5(k3_3))
print("K3,3?")
print("K5:", is_k3_3(k5), "- K3,3:", is_k3_3(k3_3), "- K3,3 mit Zusatzkante:", is_k3_3(k3_3_plus_edge), "- K3,3 mit Zusatzknoten:", is_k3_3(k3_3_plus_vertex))
print("Planar?")
print("C5:", is_planar(c5), "- K5:", is_planar(k5), "- K3,3:", is_planar(k3_3), "- K3,3 mit Zusatzkante:", is_planar(k3_3_plus_edge), "- K3,3 mit Zusatzknoten:", is_planar(k3_3_plus_vertex))
