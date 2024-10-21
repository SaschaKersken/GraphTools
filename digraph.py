import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph

# Gerichteter Graph (Digraph)
class Digraph(Graph):

    # Kante hinzufügen (nur in die angegebene Richtung)
    def add_edge(self, vertex_from, vertex_to):
        # Knoten hinzufügen, falls noch nicht vorhanden
        self.add_vertex(vertex_from, vertex_to)
        # Kante hinzufügen, falls noch nicht vorhanden
        if (vertex_from, vertex_to) not in self.edges:
            self.edges.append((vertex_from, vertex_to))

    # Alle zu einem Knoten hinführenden Kanten ermitteln
    def edges_to_vertex(self, vertex):
        return [edge for edge in self.edges if edge[1] == vertex]

    # Alle Knoten, die vom aktuellen aus erreichbar sind
    def successors(self, vertex):
        return [edge[1] for edge in self.edges_from_vertex(vertex)]

    # Alle Knoten, von denen aus der aktuelle erreichbar ist
    def predecessors(self, vertex):
        return [edge[0] for edge in self.edges_to_vertex(vertex)]

    # Nachbarn (in jede beliebige Richtung)
    def neighbors(self, vertex):
        return list(
            set(self.successors(vertex) + self.predecessors(vertex))
        )

    # Kante entfernen (nur in die angegebene Richtung)
    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)

    # Knoten (und alle mit ihm verbundenen Kanten) entfernen    
    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            removable_edges = (
                self.edges_from_vertex(vertex) + self.edges_to_vertex(vertex)
            )
            for edge in removable_edges:
                self.remove_edge(edge)
            self.vertices.remove(vertex)

    # Visualisierung
    def visualize(self, pos = None):
        plot = nx.DiGraph()
        plot.add_nodes_from(self.vertices)
        plot.add_edges_from(self.edges)
        nx.draw(plot, pos, with_labels = True, arrowsize = 10)
        plt.show()

    # String-Darstellung
    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += f"{vertex}: {self.successors(vertex)}\n"
        return result
