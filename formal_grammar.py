from digraph import Digraph

grammar = Digraph()
grammar.add_vertex('S')
grammar.add_vertex('0T')
grammar.add_vertex('1T')
grammar.add_vertex('+U')
grammar.add_vertex('0V')
grammar.add_vertex('1V')
grammar.add_vertex('ε')
grammar.add_edge('S', '0T')
grammar.add_edge('S', '1T')
grammar.add_edge('0T', '0T')
grammar.add_edge('0T', '1T')
grammar.add_edge('1T', '0T')
grammar.add_edge('0T', '+U')
grammar.add_edge('1T', '+U')
grammar.add_edge('+U', '0V')
grammar.add_edge('+U', '1V')
grammar.add_edge('0V', '0V')
grammar.add_edge('0V', '1V')
grammar.add_edge('1V', '0V')
grammar.add_edge('1V', '1V')
grammar.add_edge('0V', 'ε')
grammar.add_edge('1V', 'ε')
pos = {'S': (-1, 0), '0T': (-0.5, 0.2), '1T': (-0.5, -0.2), '+U': (0, 0), '0V': (0.5, 0.2), '1V': (0.5, -0.2), 'ε': (1, 0)}
grammar.visualize(pos)
