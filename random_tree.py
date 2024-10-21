from random import randrange
from sys import argv
from tree import Branch, Tree

def branching_factor(tree):
    branches = []
    frontier = [tree.root]
    visited = set()
    while len(frontier) > 0:
        current = frontier.pop(0)
        visited.add(current)
        if len(current.successors) > 0:
            branches.append(len(current.successors))
            for successor in current.successors:
                if successor not in visited:
                    frontier.append(successor)
    if len(branches) > 0:
        return sum(branches) / len(branches)
    return 0

if __name__ == '__main__':    
    max_depth = 3
    max_successors = 4
    if len(argv) > 1:
        max_depth = int(argv[1])
        if len(argv) > 2:
            max_successors = int(argv[2])
    leaf_count = 0
    tree = Tree(leaf_count)
    nodes = [tree.root]
    for i in range(max_depth):
        next_nodes = []
        for node in nodes:
            for j in range(randrange(max_successors)):
                leaf_count += 1
                branch = Branch(leaf_count)
                next_nodes.append(branch)
                node.add_successor(branch)
        nodes = next_nodes
    print(tree)
    print(f"b = {branching_factor(tree)}, d = {tree.depth}, b ** d = {branching_factor(tree) ** tree.depth}")
    print(f"|V| = {len(tree.graph.vertices)}, |E| = {len(tree.graph.edges)}, |V| + |E| = {len(tree.graph.vertices) + len(tree.graph.edges)}")
    tree.visualize()
