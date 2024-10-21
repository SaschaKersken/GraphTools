from binary_tree import BinaryBranch, BinaryTree

# Tree Sort: Werte mithilfe eines Binärbaums sortieren
class BinaryTreeSort(BinaryTree):
    # Hilfsmethode zum rekursiven Einfügen
    def _recursive_insert(self, branch, value):
        if value < branch.value:
            if branch.left is not None:
                self._recursive_insert(branch.left, value)
            else:
                branch.add_left(value)
            return
        elif value > branch.value:
            if branch.right is not None:
                self._recursive_insert(branch.right, value)
            else:
                branch.add_right(value)
            return
        else:
            return

    # Einen Wert nach Größe einfügen
    def insert(self, value):
        if self.root is None:
            self.root = BinaryBranch(value)
        else:
            self._recursive_insert(self.root, value)

    # Hilfsmethode zum rekursiven Auslesen
    def _recursive_read(self, branch, result):
        if branch.left is not None:
            self._recursive_read(branch.left, result)
        result.append(branch.value)
        if branch.right is not None:
            self._recursive_read(branch.right, result)

    # Die sortierten Werte von links nach rechts auslesen
    def get_sorted(self):
        result = []
        if self.root is not None:
            self._recursive_read(self.root, result)
        return result
