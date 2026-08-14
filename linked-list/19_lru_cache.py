class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}

        self.head = None
        self.last = None

    def remove(self, node):
        if self.head == self.last:
            self.head = None
            self.last = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.last:
            self.last = self.last.prev
            self.last.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def insertLast(self, node):
        if self.head is None:
            self.head = node
            self.last = node
            return

        node.prev = self.last
        self.last.next = node
        self.last = node

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        node = self.store[key]

        self.remove(node)
        self.insertLast(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            self.remove(node)
            self.insertLast(node)
            return

        if len(self.store) == self.capacity:
            lru = self.head
            self.remove(lru)
            del self.store[lru.key]
        node = Node(key, value)
        self.insertLast(node)
        self.store[key] = node
