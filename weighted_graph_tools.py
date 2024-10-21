from weighted_graph import WeightedGraph
from graph import Graph
from graph_tools import circle
from queue import PriorityQueue

# Sammlung von Algorithmen für kantengewichtete Graphen

# Hilfsfunktion: Eindeutige, nach Gewicht sortierte Kanten
def _unique_edges(w_graph):
    unique_edges = {}
    for edge in w_graph.edges:
        if frozenset(edge) not in unique_edges:
            unique_edges[frozenset(edge)] = w_graph.edges[edge]
    # Nach Gewicht sortieren
    unique_edges = list(unique_edges.items())
    unique_edges.sort(key = lambda item: item[1])
    return unique_edges

# Hilfsfunktion: Irgendein Kreis vorhanden?
def _has_any_circle(graph):
    for vertex in graph.vertices:
        if circle(graph, vertex):
            return True
    return False

# Minimaler Spannbaum (Algorithmus von Kruskal)
def mst(w_graph):
    result = {}
    # Eindeutige, nach Gewicht sortierte Kanten
    unique_edges = _unique_edges(w_graph)
    # Kanten mit dem geringsten Gewicht beginnend untersuchen
    while len(unique_edges) > 0:
        edge, weight = unique_edges.pop(0)
        test_edges = dict(result)
        test_graph = WeightedGraph()
        test_edges[tuple(edge)] = weight
        test_graph.add_edges(test_edges)
        # Falls Graph keinen Kreis bildet, aktuelle Kante ins Ergebnis übernehmen
        if not(_has_any_circle(test_graph)):
            result = test_edges
    return result

# Kürzeste Pfade zu allen Knoten vom Startknoten aus (Algorithmus von Dijkstra)
def dijkstra(w_graph, start):
    # Entfernungen sind zunächst unbekannt
    distances = {vertex: None for vertex in w_graph.vertices}
    # Entfernung des Startknotens zu sich selbst ist 0
    distances[start] = 0
    # Noch keine Pfade vorhanden
    paths = {}
    # Startknoten mit Gewicht 0 in Prioritätswarteschlange speichern
    pq = PriorityQueue()
    pq.put((0, start))
    # Solange die Prioritätswarteschlange nicht leer ist
    while not pq.empty():
        # Knoten mit niedrigstem Gewicht entnehmen und seine Nachbarn durchgehen
        (dist, vertex) = pq.get()
        for (neighbor, weight) in w_graph.neighbors_with_weights(vertex):
             old_dist = distances[neighbor]
             new_dist = dist + weight
             if old_dist is None or old_dist > new_dist:
                 # Wenn Nachbar noch unbekannt oder Entfernung günstiger
                 # In den Ergebnis-Dicts speichern und zur PW hinzufügen
                 distances[neighbor] = new_dist
                 paths[neighbor] = (vertex, neighbor, weight)
                 pq.put((new_dist, neighbor))
    # Entfernungen und Verbindungen zurückgeben
    return distances, paths
    
# Pfad vom Startort zum gewünschten Ziel ermitteln
def get_dijkstra_path(from_vertex, to_vertex, paths):
    edge = paths[to_vertex]
    result = [edge]
    while edge[0] != from_vertex:
        edge = paths[edge[0]]
        result.append(edge)
    return list(reversed(result))
    

if __name__ == '__main__':
    w_graph = WeightedGraph()
    w_graph.add_vertex('A', 'B', 'C', 'D', 'E')
    w_graph.add_edges(
        {('A', 'B'): 7, ('B', 'C'): 2, ('C', 'A'): 9, ('B', 'D'): 1,
        ('C', 'D'): 4, ('D', 'E'): 8, ('B', 'E'): 6}
    )
    print(w_graph)
    mst_result = mst(w_graph)
    print(f"Minimaler Spannbaum: {mst_result}")
    print(f"Summe der Kantengewichte: {sum(mst_result.values())}")
    distances, paths = dijkstra(w_graph, 'A')
    print("Dijkstra von A aus:")
    print(f"Entfernungen der günstigsten Routen: {distances}")
    print(f"Günstigste Routen: {paths}")
    path = get_dijkstra_path('A', 'E', paths)
    total = sum([item[2] for item in path])
    print(f"Günstigste Route von A nach E: {path}, Gesamt: {total}")
    w_graph.visualize()
    mst_graph = WeightedGraph()
    mst_graph.add_edges(mst_result)
    mst_graph.visualize()
    dijkstra_edges = {(vertex, neighbor): weight
        for (vertex, neighbor, weight) in paths.values()
    }
    dijkstra_graph = WeightedGraph()
    dijkstra_graph.add_edges(dijkstra_edges)
    dijkstra_graph.visualize()
