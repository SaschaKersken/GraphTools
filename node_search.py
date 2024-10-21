from data_structures import Stack, Queue, PriorityQueue

class Node:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent


# Knoten in einen Pfad umwandeln
def get_path(node):
    # Inhalt des aktuellen Knotens
    path = [node.state]
    # Inhalte der Vorfahren
    while node.parent:
        node = node.parent
        path.append(node.state)
    # Den Pfad umkehren
    path.reverse()
    return path

def dfs(start, is_goal, successors):
    # Frontier als leeren Stapel initialisieren
    frontier = Stack()
    # Den Startknoten erzeugen und auf Frontier ablegen
    frontier.push(Node(start))
    # Der Startknoten wurde bereits besucht
    visited = [start]
    # Solange es noch Elemente in Frontier gibt
    while not frontier.empty:
        # Zuletzt hinzugefügtes Element aus Frontier holen
        node = frontier.pop()
        # Ziel erreicht? Dann aktuellen Knoten zurückgeben
        if is_goal(node.state):
            return node
        # Alle Nachfolger untersuchen
        for child in successors(node.state):
            # Falls der Nachfolger schon besucht wurde, überspringen
            if child in visited:
                continue
            # Nachfolger zur Liste der besuchten Zustände hinzufügen
            visited.append(child)
            # Aus dem Nachfolger einen Knoten erzeugen und auf Frontier legen
            frontier.push(Node(child, node))
    # Nichts gefunden
    return None

def bfs(start, is_goal, successors):
    # Frontier als leere Warteschlange initialisieren
    frontier = Queue()
    # Den Startknoten erzeugen und auf Frontier ablegen
    frontier.push(Node(start))
    # Der Startknoten wurde bereits besucht
    visited = [start]
    # Solange es noch Elemente in Frontier gibt
    while not frontier.empty:
        # Zuerst hinzugefügtes Element aus Frontier holen
        node = frontier.pop()
        # Ziel erreicht? Dann aktuellen Knoten zurückgeben
        if is_goal(node.state):
            return node
        # Alle Nachfolger untersuchen
        for child in successors(node.state):
            # Falls der Nachfolger schon besucht wurde, überspringen
            if child in visited:
                continue
            # Nachfolger zur Liste der besuchten Zustände hinzufügen
            visited.append(child)
            # Aus dem Nachfolger einen Knoten erzeugen und auf Frontier legen
            frontier.push(Node(child, node))
    # Nichts gefunden
    return None


class PathLengthAwareNode:
    def __init__(self, state, parent = None, path_length = 1):
        self.state = state
        self.parent = parent
        self.path_length = path_length
        if parent is not None:
            self.path_length += parent.path_length

    def __lt__(self, other):
        return self.path_length < other.path_length


def _multiple_paths(current, is_goal, successors, results,
        visited, max_length):
    # Aktuellen Zustand zu den besuchten hinzufügen
    visited.add(current.state)
    # Falls es sich um das Ziel handelt, zur Ergebnisliste hinzufügen
    if is_goal(current.state):
        results.append(current)
    elif current.path_length < max_length:
        # Sonst Nachfolger durchsuchen, falls max. Pfadlänge nicht erreicht
        for child in successors(current.state):
            # Falls der Nachfolger schon besucht wurde, überspringen
            if child in visited:
                continue
            # Rekursiver Aufruf mit aktuellem Nacholger und Kopie von visited
            child_node = PathLengthAwareNode(child, current)
            _multiple_paths(
                child_node, is_goal, successors, results,
                set(visited), max_length
            )

def multiple_paths(start, is_goal, successors, max_length, max_paths = 0):
    # Ergebnisliste
    results = []
    # Startknoten erzeugen
    start_node = PathLengthAwareNode(start)
    # Die eigentliche, rekursive Suche durchführen
    _multiple_paths(
        start_node, is_goal, successors, results, set(), max_length
    )
    # Ergebnis nach Pfadlängen sortieren
    results.sort(key = lambda node:node.path_length)
    if max_paths > 0:
        results = results[:max_paths]
    return results


def greedy(start, is_goal, successors, heuristic):
    # Frontier als leere Warteschlange initialisieren
    frontier = Queue()
    # Den Startknoten erzeugen und auf Frontier ablegen
    frontier.push(Node(start))
    # Der Startknoten wurde bereits besucht
    visited = [start]
    # Solange es noch Elemente in Frontier gibt
    while not frontier.empty:
        # Zuerst hinzugefügtes Element aus Frontier holen
        node = frontier.pop()
        # Ziel erreicht? Dann aktuellen Knoten zurückgeben
        if is_goal(node.state):
            return node
        # Alle Nachfolger untersuchen, günstigsten zuerst
        list_successors = successors(node.state)
        list_successors.sort(key = lambda state:heuristic(state))
        for child in list_successors:
            # Falls der Nachfolger schon besucht wurde, überspringen
            if child in visited:
                continue
            # Nachfolger zur Liste der besuchten Zustände hinzufügen
            visited.append(child)
            # Aus dem Nachfolger einen Knoten erzeugen und auf Frontier legen
            frontier.push(Node(child, node))
    # Nichts gefunden
    return None


class WeightedNode:
    def __init__(self, state, parent = None, cost = 0.0, heuristic = 0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic


def a_star(start, is_goal, successors, heuristic):
    # Frontier als leere Prioritätswarteschlange initialisieren
    frontier = PriorityQueue()
    # Den Startknoten erzeugen und auf Frontier ablegen
    frontier.push(
        WeightedNode(start, cost = 0.0, heuristic = heuristic(start))
    )
    # Der Startknoten wurde bereits besucht
    visited = {start: 0.0}
    # Solange es noch Elemente in Frontier gibt
    while not frontier.empty:
        # Günstigstes Element aus Frontier holen
        node = frontier.pop()
        # Ziel erreicht? Dann aktuellen Knoten zurückgeben
        if is_goal(node.state):
            return node
        # Alle Nachfolger untersuchen
        for child in successors(node.state):
            # Kosten berechnen
            child_cost = node.cost + 1
            # Falls Nachfolger besucht und Kosten nicht geringer, überspringen
            if child in visited and visited[child] <= child_cost:
                continue
            # Nachfolger hinzufügen oder Kosten aktualisieren
            visited[child] = child_cost
            # Aus dem Nachfolger einen Knoten erzeugen und auf Frontier legen
            frontier.push(
                WeightedNode(child, node, child_cost, heuristic(child))
            )
    # Nichts gefunden
    return None
