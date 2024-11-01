from sys import argv
from graph import Graph

n = int(argv[1])
set_a = []
set_b = []
k_n_n = Graph()
for i in range(1, n + 1):
    k_n_n.add_vertex(f"V{n}a")
    set_a.append(f"V{i}a")
    k_n_n.add_vertex(f"V{n}b")
    set_b.append(f"V{i}b")
for v_from in set_a:
    for v_to in set_b:
        k_n_n.add_edge(v_from, v_to)
pos = {}
colors = {}
for i, vertex in enumerate(set_a):
    j = i + 1
    pos[vertex] = (j / n * 2 - 1, 1)
    colors[vertex] = '#FFFF00'
for i, vertex in enumerate(set_b):
    j = i + 1
    pos[vertex] = (j / n * 2 - 1, -1)
    colors[vertex] = '#FF00FF'
print(f"K{n},{n}")
print(k_n_n)
k_n_n.visualize(pos, colors)
