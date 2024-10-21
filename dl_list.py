# Listenelement
class Item:
    def __init__(self, value, pred=None, succ=None):
        self.value = value
        self.pred = pred
        self.succ = succ


# Doppelt verknüpfte Liste
class DLList:
    def __init__(self):
        self.header = None
        self.len = 0

    # Element am Ende einfügen
    def push(self, value):
        if self.header is None:
            self.header = Item(value)
        else:
            current = self.header
            while current.succ is not None:
                current = current.succ
            current.succ = Item(value, current)
        self.len += 1

    # Element vom Ende entfernen und zurückgeben
    def pop(self):
        if self.header is None:
            return None
        current = self.header
        while current.succ is not None:
            current = current.succ
        if current is self.header:
            self.header = None
        else:
            current.pred.succ = None
        self.len -= 1
        return current.value

    # Element am Anfang einfügen
    def unshift(self, value):
        if self.header is None:
            self.header = Item(value)
        else:
            item = Item(value, None, self.header)
            self.header = item
        self.len += 1

    # Element vom Anfang entfernen und zurückgeben
    def shift(self):
        if self.header is None:
            return None
        result = self.header.value
        if self.header.succ is None:
            self.header = None
        else:
            self.header = self.header.succ
        self.len -= 1
        return result

    def __len__(self):
        return self.len

    def __str__(self):
        return str(self.traverse())

    def __repr__(self):
        return f"Doubly linked list ({self.len}): {str(self)}"
    

if __name__ == '__main__':
    l = DLList()
    print("Stapel")
    l.push(1)
    l.push(2)
    l.push(3)
    while len(l) > 0:
        print(l.pop())
    print("Warteschlange")
    l.push(1)
    l.push(2)
    l.push(3)
    while len(l) > 0:
        print(l.shift())
