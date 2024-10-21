import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from tree import Branch, Tree
from digraph import Digraph

# Verzweigung eines Binärbaums
class BinaryBranch:
    def __init__(self, value, parent = None, left = None, right = None):
        self.value = value
        self.parent = parent
        if left is not None:
            self.add_left(left)
        else:
            self.left = None
        if right is not None:
            self.add_right(right)
        else:
            self.right = right

    # Linken Nachfolger hinzufügen
    def add_left(self, value):
        if type(value) is BinaryBranch:
            value.parent = self
            self.left = value
        else:
            self.left = BinaryBranch(value, self)

    # Rechten Nachfolger hinzufügen
    def add_right(self, value):
        if type(value) is BinaryBranch:
            value.parent = self
            self.right = value
        else:
            self.right = BinaryBranch(value, self)

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
        result = ''
        if self.right is not None:
            result += self.right.__str__(indentation + 1)
        result += f"{' ' * ((indentation) * 4)}{self.value}\n"
        if self.left is not None:
            result += self.left.__str__(indentation + 1)
        return result

    def __repr__(self):
        result = "Binary tree\n" + self.__str__()


# Binärbaum
class BinaryTree:
    def __init__(self, root = None):
        if root is not None and type(root) is not BinaryBranch:
            root = BinaryBranch(root, None)
        self.root = root

    # Tiefe des Baums (BFS-Variante)
    @property
    def depth(self):
        frontier = [self.root]
        visited = []
        result = 0
        while len(frontier) > 0:
            current = frontier.pop(0)
            visited.append(current)
            if current.left is None and current.right is None:
                if current.depth > result:
                    result = current.depth
            else:
                if current.left and current.left not in visited:
                    frontier.append(current.left)
                if current.right and current.right not in visited:
                    frontier.append(current.right)
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
            if current.left is None and current.right is None:
                result.append(current.value)
            else:
                if current.left and current.left not in visited:
                    frontier.append(current.left)
                if current.right and current.right not in visited:
                    frontier.append(current.right)
        return result
        
    # Rekursive Hilfsfunktion: Knoten/Kanten für die Graphen-Darstellung erzeugen
    def _graph(self, branch, vertices, edges):
        if branch.left is not None:
            edges.append((branch.value, branch.left.value))
            self._graph(branch.left, vertices, edges)
        vertices.append(branch.value)
        if branch.right is not None:
            edges.append((branch.value, branch.right.value))
            self._graph(branch.right, vertices, edges)

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

    # Plot des Binärbaums mit vorgegebener Positionierung
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
