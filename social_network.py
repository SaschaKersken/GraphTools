from sys import argv, exit
from graph import Graph
from node_search import multiple_paths, get_path

def print_usage(users):
    print(f"Verwendung: python3 {argv[0]} USER1 USER2")
    print("USER1 und USER2 müssen unterschiedliche Namen aus folgender Liste sein:")
    print(users)

if __name__ == '__main__':
    users = [
        "Alex", "Betty", "Carl", "Dana", "Emil",
        "Frances", "Gary", "Hannah", "Ian", "Jenny"
    ]
    if (len(argv) <= 2 or argv[1] == argv[2]
            or argv[1] not in users or argv[2] not in users):
        print_usage(users)
        exit(1)
    network = Graph()
    network.add_vertices(users)
    network.add_edge("Alex", "Betty")
    network.add_edge("Alex", "Dana")
    network.add_edge("Alex", "Emil")
    network.add_edge("Alex", "Hannah")
    network.add_edge("Betty", "Jenny")
    network.add_edge("Betty", "Gary")
    network.add_edge("Betty", "Frances")
    network.add_edge("Carl", "Dana")
    network.add_edge("Carl", "Ian")
    network.add_edge("Carl", "Jenny")
    network.add_edge("Dana", "Gary")
    network.add_edge("Dana", "Hannah")
    network.add_edge("Dana", "Ian")
    network.add_edge("Dana", "Jenny")
    network.add_edge("Emil", "Frances")
    network.add_edge("Emil", "Hannah")
    network.add_edge("Emil", "Ian")
    network.add_edge("Frances", "Gary")
    network.add_edge("Frances", "Hannah")
    network.add_edge("Gary", "Ian")
    network.add_edge("Hannah", "Jenny")
    network.add_edge("Ian", "Jenny")
    paths = multiple_paths(
        argv[1],
        lambda user: user == argv[2],
        lambda user: network.neighbors(user),
        5,
        20
    )
    print(f"Kontaktpfade zwischen {argv[1]} und {argv[2]}:")
    for path in paths:
        print(get_path(path))
    network.visualize()
