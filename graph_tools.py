from graph import Graph
from data_structures import Queue
from itertools import combinations

# Sammlung von Algorithmen für einfache Graphen

# Alle von einem angegebenen Knoten aus erreichbaren Knoten besuchen
# (DFS-Variante)
def traverse(graph, vertex):
    frontier = [vertex]
    visited = [vertex]
    while len(frontier) > 0:
         current = frontier.pop()
         neighbors = graph.neighbors(current)
         for neighbor in neighbors:
             if neighbor in visited:
                 continue
             visited.append(neighbor)
             frontier.append(neighbor)
    return visited

# Ist der Graph zusammenhängend?
def is_connected(graph):
    return len(graph.vertices) == len(traverse(graph, graph.vertices[0]))

# Gibt es einen Kreis vom angegebenen Knoten aus?
def circle(graph, start_vertex):
    frontier = graph.edges_from_vertex(start_vertex)
    visited = set()
    while len(frontier) > 0:
        current_edge = frontier.pop()
        current_vertex = current_edge[1]
        if current_vertex == start_vertex:
            return True
        visited.add(frozenset(current_edge))
        frontier += [
            edge for edge in graph.edges_from_vertex(current_vertex)
            if frozenset(edge) not in visited
        ]
    return False

# Ist der Graph ein Baum (enthält keine Kreise)?
def is_tree(graph):
    # Ein unzusammenhängender Graph kann kein Baum sein
    if not is_connected(graph):
        return False
    # Von jedem Knoten aus nach möglichen Kreisen suchen
    for start_vertex in graph.vertices:
        if circle(graph, start_vertex):
            # Kreis gefunden -- kein Baum
            return False
    # Hier muss es sich um einen Baum handeln
    return True

# Hilfsfunktion, um Eulerweg- oder Eulerkreis-Eigenschaft zu prüfen
def _euler_check(graph):
    odd = -1
    vertices = traverse(graph, graph.vertices[0])
    # Nur zusammenhängende Graphen näher betrachten
    if len(vertices) == len(graph.vertices):
        odd = 0
        for vertex in vertices:
            odd += len(graph.neighbors(vertex)) % 2
    return odd

# Eulerweg möglich?
def has_eulerian_path(graph):
    odd = _euler_check(graph)
    return odd >= 0 and odd <= 2

# Eulerkreis möglich?
def has_eulerian_cycle(graph):
    return _euler_check(graph) == 0

# Eulerkreis finden (Algorithmus von Hierholzer)
def eulerian_cycle(graph):
    # Kein Eulerkreis? Dann sofort beenden
    if not has_eulerian_cycle(graph):
        return None
    total_edges = len(graph.unique_edges)
    used_edges = set()
    circles = []
    start_vertex = graph.vertices[0]
    current_circle = [start_vertex]
    current_vertex = None
    next_start_vertex = None
    # Wiederholen, solange noch nicht genug Kanten gefunden wurden
    while len(used_edges) < total_edges:
        # Noch keinen Kreis gefunden?
        while current_vertex != start_vertex:
            if current_vertex is None:
                current_vertex = start_vertex
            # Noch nicht verwendete Kanten, die vom aktuellen Knoten ausgehen
            edges_to_use = [
                edge for edge in graph.edges_from_vertex(current_vertex)
                if frozenset(edge) not in used_edges
            ]
            # Falls es mehrere Kanten gibt, den aktuellen Knoten als Start
            # des nächsten Kreises vormerken
            if len(edges_to_use) > 1:
                next_start_vertex = current_vertex
            # Falls es mindestens eine Kante gibt, die erste verwenden,
            # als benutzt markieren, erreichten Knoten im aktuellen Kreis speichern
            if len(edges_to_use) > 0:
                edge = edges_to_use[0]
                used_edges.add(frozenset(edge))
                current_circle.append(edge[1])
                current_vertex = edge[1]
        # Durchlauf für den nächsten Kreis vorbereiten
        start_vertex = next_start_vertex
        next_start_vertex = None
        current_vertex = None
        circles.append(current_circle)
        current_circle = [start_vertex]
    # Die gefundenen Kreise in der richtigen Reihenfolge zusammenfügen
    result = circles.pop(0)
    for circle in circles:
        index = -1
        for i, edge in enumerate(result):
            if edge == circle[0]:
                index = i
                break
        if index >= 0:
            result[index:index + 1] = circle
    return result

# Ist der Graph bipartit?
def is_bipartite(graph):
    colors = {vertex: -1 for vertex in graph.vertices}
    # Unterfunktion: bfs-Variante
    def bfs(start):
        frontier = Queue()
        frontier.push(start)
        colors[start] = 0
        while not frontier.empty:
            vertex = frontier.pop()
            for neighbor in graph.neighbors(vertex):
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[vertex]
                    frontier.push(neighbor)
                elif colors[neighbor] == colors[vertex]:
                    return False
        return True
    for vertex in graph.vertices:
        if colors[vertex] == -1:
            if not bfs(vertex):
                return False
    return True
    
# Handelt es sich um den Graphen K5?
def is_k5(graph):
    return is_connected(graph) and len(graph.vertices) == 5 and len(graph.edges) == 20

# Handelt es sich um den Graphen K3,3?
def is_k3_3(graph):
    if not is_connected(graph):
        return False
    if len(graph.vertices) != 6:
        return False
    if len(graph.unique_edges) != 9:
        return False
    if is_bipartite(graph):
        return True
    return False   

# Ist der Graph planar (d.h. ist eine planare Darstellung möglich)?
def is_planar(graph):
    if len(graph.vertices) >= 5:
        for subvertices in combinations(graph.vertices, 5):
            if is_k5(graph.subgraph(subvertices)):
                return False
    if len(graph.vertices) >= 6:
        for subedges in combinations(graph.unique_edges, 9):
            subgraph = Graph()
            subgraph.add_edges(subedges)
            if is_k3_3(subgraph):
                return False
    return True
