import math
from sys import argv
from graph import Graph

n = int(argv[1])
kn = Graph()
for i in range(1, n + 1):
    kn.add_vertex(f'V{i}')
for v_from in kn.vertices:
    for v_to in [v for v in kn.vertices if v != v_from]:
        kn.add_edge(v_from, v_to)
pos = {}
for i, vertex in enumerate(kn.vertices):
    theta = i * (2 * math.pi / n)
    pos[vertex] = (math.sin(theta), math.cos(theta))
print(f"K{n}")
print(kn)
kn.visualize(pos)
cn = Graph()
for i in range(1, n + 1):
    cn.add_vertex(f'V{i}')
for i, v_from in enumerate(cn.vertices):
    if i == n - 1:
        v_to = cn.vertices[0]
    else:
        v_to = cn.vertices[i + 1]
    cn.add_edge(v_from, v_to)
print(f"C{n}")
print(cn)
cn.visualize(pos)
