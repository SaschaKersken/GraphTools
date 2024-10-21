import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph

# Wertebereich von Zahlen in Dict oder Liste anpassen
def adjust_range(numbers, index=100):
    if type(numbers) is dict:
        max_value = abs(max(numbers.values()))
        return {key: value / max_value * index for (key, value) in numbers.items()}
    max_value = abs(max(numbers, key=abs))
    return [number / max_value * index for number in numbers]


# Kantengewichteter Graph
class WeightedGraph(Graph):

    def __init__(self): 
        super().__init__()
        self.edges = {}

    # Kante hinzufügen
    # Kann auch zur Änderung des Gewichts vorhandener Kanten verwendet werden
    def add_edge(self, vertex_from, vertex_to, weight):
        # Knoten hinzufügen, falls noch nicht vorhanden
        self.add_vertex(vertex_from, vertex_to)
        # Kanten in beide Richtungen mit angegebenem Gewicht
        self.edges[(vertex_from, vertex_to)] = weight
        self.edges[(vertex_to, vertex_from)] = weight

    # Mehrere Kanten hinzufügen (Dict)
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edges[edge])

    # Kanten aus einer Adjazenzmatrix hinzufügen
    def add_edges_by_adjacency_matrix(self, matrix):
        cv = len(self.vertices)
        if matrix.ndim == 2 and matrix.shape == (cv, cv):
            for col in range(cv):
                for row in range(cv):
                    if matrix[col, row] != 0:
                        self.add_edge(
                            self.vertices[col], self.vertices[row], matrix[col, row]
                        )
        else:
            raise ValueError(f"Form des Arrays muss ({cv}, {cv}) sein.")

    # Alle von einem Knoten ausgehenden Kanten mit Gewichten ermitteln
    def edges_from_vertex_with_weights(self, vertex):
        result = []
        if vertex in self.vertices:
            result = [
                (vertices, self.edges[vertices])
                for vertices in self.edges if vertices[0] == vertex
            ]
        return result

    # Kante entfernen
    def remove_edge(self, edge):
        # In beide Richtungen
        if edge in self.edges:
            del self.edges[edge]
        reverse = (edge[1], edge[0])
        if reverse in self.edges:
            del self.edges[reverse]

    # Alle direkt mit einem Knoten verbundenen Nachbarn
    # und die zu ihnen führenden Gewichte ermitteln
    def neighbors_with_weights(self, vertex):
        result = []
        for (edge, weight) in self.edges_from_vertex_with_weights(vertex):
            result.append((edge[1], weight))
        return result

    #Adjazenzmatrix-Darstellung
    @property
    def adjacency_matrix(self):
        matrix = np.zeros(
            (len(self.vertices),
            len(self.vertices))
        )
        for i, v_from in enumerate(self.vertices):
            for j, v_to in enumerate(self.vertices):
                if (v_from, v_to) in self.edges:
                    matrix[i, j] = self.edges[(v_from, v_to)]
        return matrix

    # Visualisierung
    def visualize(self, pos = None):
        # Eindeutige Listen der Kanten und ihrer Gewichte erstellen
        used_edges = set()
        edge_list = []
        weight_list = []
        for edge in self.edges:
            unique = frozenset(edge)
            if unique not in used_edges:
                used_edges.add(unique)
                edge_list.append(edge)
                weight_list.append(self.edges[edge])
        # Die Visualisierung erzeugen und zeichnen
        plot = nx.Graph()
        plot.add_nodes_from(self.vertices)
        plot.add_edges_from(edge_list)
        nx.draw(plot, pos, with_labels = True, width = adjust_range(weight_list, 10))
        plt.show()

    # String-Darstellung
    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += f"{vertex}: {self.neighbors_with_weights(vertex)}\n"
        return result

    # Hash
    def __hash__(self):
        return hash((
            tuple(self.edges.items()),
            tuple(self.vertices)
        ))
