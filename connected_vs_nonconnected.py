from graph import Graph

g = Graph()
g.add_vertices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
g.add_edges([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('C', 'D')])
g.add_edge('D', 'E')
g.add_edges([('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'H'), ('G', 'H')])
g.visualize(caption="Zusammenhängender Graph")
g.remove_edge(('D', 'E'))
g.visualize(caption="Nicht zusammenhängender Graph")
