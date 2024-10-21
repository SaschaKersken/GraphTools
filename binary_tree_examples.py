from binary_tree import BinaryTree

tree = BinaryTree(5)
tree.root.add_left(2)
tree.root.left.add_left(1)
tree.root.left.add_right(3)
tree.root.left.right.add_left(4)
tree.root.add_right(7)
tree.root.right.add_left(6)
tree.root.right.add_right(8)
print(tree)
print(f"Blätter: {tree.leaves}")
print(f"Tiefe: {tree.depth}")
print(tree.graph)
tree.graph.visualize()
tree.visualize()