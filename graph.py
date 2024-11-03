import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Einfacher Graph
class Graph:

    def __init__(self):
        self.vertices = []
        self.edges = []

    # Eindeutige Kanten
    @property
    def unique_edges(self):
        result = []
        for edge in self.edges:
            if edge not in result and (edge[1], edge[0]) not in result:
                result.append(edge)
        return result

    # Beliebig viele Knoten hinzufügen
    def add_vertex(self, *args):
        for vertex in args:
            if vertex not in self.vertices:
                self.vertices.append(vertex)

    # Komfort-Methode, um eine Liste von Knoten hinzuzufügen
    def add_vertices(self, vertices):
        self.add_vertex(*vertices)

    # Kante hinzufügen
    def add_edge(self, vertex_from, vertex_to):
        # Knoten hinzufügen, falls noch nicht vorhanden
        self.add_vertex(vertex_from, vertex_to)
        # Kanten in beide Richtungen, falls noch nicht vorhanden
        if (vertex_from, vertex_to) not in self.edges:
            self.edges.append((vertex_from, vertex_to))
        if (vertex_to, vertex_from) not in self.edges:
            self.edges.append((vertex_to, vertex_from))

    # Mehrere Kanten hinzufügen (Liste von Tupeln)
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    # Kanten aus einer Adjazenzmatrix hinzufügen
    def add_edges_by_adjacency_matrix(self, matrix):
        cv = len(self.vertices)
        if matrix.ndim == 2 and matrix.shape == (cv, cv):
            for col in range(cv):
                for row in range(cv):
                    if matrix[col, row] == 1:
                        self.add_edge(self.vertices[col], self.vertices[row])
        else:
            raise ValueError(f"Form des Arrays muss ({cv}, {cv}) sein.")
        
    # Alle von einem Knoten ausgehenden Kanten ermitteln
    def edges_from_vertex(self, vertex):
        return [edge for edge in self.edges if edge[0] == vertex]

    # Alle direkt mit einem Knoten verbundenen Nachbarn ermitteln
    def neighbors(self, vertex):
        result = []
        for edge in self.edges_from_vertex(vertex):
            result.append(edge[1])
        return result

    # Kante entfernen
    def remove_edge(self, edge):
        # In beide Richtungen
        if edge in self.edges:
            self.edges.remove(edge)
        reverse = (edge[1], edge[0])
        if reverse in self.edges:
            self.edges.remove(reverse)

    # Knoten (und alle mit ihm verbundenen Kanten) entfernen
    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            removable_edges = self.edges_from_vertex(vertex)
            for edge in removable_edges:
                self.remove_edge(edge)
            self.vertices.remove(vertex)

    # Einen Teilgraphen aus den angegebenen Knoten und allen sie verbindenden Kanten erzeugen
    def subgraph(self, vertices):
        subgraph_edges = [edge for edge in self.edges if edge[0] in vertices and edge[1] in vertices]
        sub = Graph()
        sub.add_vertices(vertices)
        sub.add_edges(subgraph_edges)
        return sub

    # Adjazenzmatrix-Darstellung
    @property
    def adjacency_matrix(self):
        matrix = np.zeros(
            (len(self.vertices),
            len(self.vertices)),
            dtype=np.byte
        )
        for i, v_from in enumerate(self.vertices):
            for j, v_to in enumerate(self.vertices):
                if ((v_from, v_to) in self.edges):
                    matrix[i, j] = 1
        return matrix

    # Visualisierung
    def visualize(self, pos=None, color_map=None, caption=None):
        plot = nx.Graph()
        plot.add_nodes_from(self.vertices)
        plot.add_edges_from(self.edges)
        colors = None
        if color_map is not None:
            colors = []
            for vertex in self.vertices:
                if vertex in color_map:
                    colors.append(color_map[vertex])
        if caption is not None:
            plt.figure()
            plt.title(caption)
        nx.draw(plot, pos, with_labels = True, node_color=colors)
        plt.show()

    # Repräsentation
    def __repr__(self):
        return f"""Graph(
  V={self.vertices},
  E={self.edges}
)"""
    # String-Darstellung
    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += f"{vertex}: {self.neighbors(vertex)}\n"
        return result

    # Hash
    def __hash__(self):
        return hash((tuple(self.edges), tuple(self.vertices)))

    # Gleichheit
    def __eq__(self, other):
        return self.adjacency_matrix == other.adjacency_matrix
