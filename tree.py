import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from digraph import Digraph

# Verzweigung eines Baums (Knoten mit Elternknoten und Nachfolgern)
class Branch:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.successors = []

    # Einen Nachfolger hinzufügen
    def add_successor(self, value):
        if type(value) is Branch:
            value.parent = self
            self.successors.append(value)
        else:
            self.successors.append(Branch(value, self))

    # Tiefe (Entfernung bis zum Wurzelknoten)
    @property
    def depth(self):
        depth = 0
        current = self
        while current.parent is not None:
            current = current.parent
            depth += 1
        return depth

    def __str__(self, indentation = 0):
        result = f"{' ' * (indentation * 4)}{self.value}\n"
        for successor in self.successors:
            if indentation < 10:
                result += successor.__str__(indentation + 1)
            else:
                return result
        return result

    def __repr__(self):
        return "Tree\n" + self.__str__()


# Baum
class Tree:
    def __init__(self, root = None):
        if root is not None and type(root) is not Branch:
            root = Branch(root, None)
        self.root = root

    # Pfad zu einem bestimmten Knoten
    def path(self, *index):
        current = self.root
        for i in index:
            if len(current.successors) >= i + 1:
                current = current.successors[i]
            else:
                return None
        return current
        
    # Tiefe des Baums (BFS-Variante)
    @property
    def depth(self):
        frontier = [self.root]
        visited = []
        result = 0
        while len(frontier) > 0:
            current = frontier.pop(0)
            visited.append(current)
            if len(current.successors) == 0:
                if current.depth > result:
                    result = current.depth
            else:
                for successor in current.successors:
                    frontier.append(successor)
        return result

    # Blätter (Nachkommen ohne Nachfolger)
    @property
    def leaves(self):
        frontier = [self.root]
        visited = []
        result = []
        while len(frontier) > 0:
            current = frontier.pop(0)
            visited.append(current)
            if len(current.successors) == 0:
                result.append(current.value)
            else:
                for successor in current.successors:
                    frontier.append(successor)
        return result
        
    # Rekursive Hilfsfunktion: Knoten/Kanten für die Graphen-Darstellung erzeugen
    def _graph(self, branch, vertices, edges):
        vertices.append(branch.value)
        for successor in branch.successors:
            edges.append((branch.value, successor.value))
            self._graph(successor, vertices, edges)

    # Graphen-Darstellung des aktuellen Baums
    @property
    def graph(self):
        vertices = []
        edges = []
        self._graph(self.root, vertices, edges)
        graph = Digraph()
        graph.add_vertices(vertices)
        graph.add_edges(edges)
        return graph

    # Plot des Baums mit vorgegebener Positionierung
    def visualize(self):
        plot = nx.DiGraph()
        plot.add_nodes_from(self.graph.vertices)
        plot.add_edges_from(self.graph.edges)
        pos = graphviz_layout(plot, prog="dot")
        nx.draw(plot, pos, with_labels = True)
        plt.show()

    def __str__(self):
        return self.root.__str__()

    def __repr__(self):
        return self.root.__repr__()

    def __hash__(self):
        return hash(self.__str__())
