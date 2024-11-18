from graph import Graph

pos = {'A': (-1, 0.5), 'B': (-1, -0.5), 'C': (-0.5, 0), 'D': (0.5, 0), 'E': (1, 0.5), 'F': (1, -0.5), 'N': (0, 0)}
g = Graph()
g.add_vertices(['A', 'B', 'C', 'D', 'E', 'F'])
g.add_edges([('A', 'B'), ('B', 'C'), ('C', 'A')])
g.add_edge('C', 'D')
g.add_edges([('D', 'E'), ('E', 'F'), ('F', 'D')])
g.visualize(pos)
g.remove_edge(('C', 'D'))
g.visualize(pos)
g = Graph()
g.add_vertices(['A', 'B', 'N', 'E', 'F'])
g.add_edges([('A', 'B'), ('B', 'N'), ('N', 'A')])
g.add_edges([('N', 'E'), ('E', 'F'), ('F', 'N')])
g.visualize(pos)

