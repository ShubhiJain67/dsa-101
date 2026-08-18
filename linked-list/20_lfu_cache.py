from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -= 1

    def removeLast(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.keyToNode = {}
        self.freqToList = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        self.updateFrequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.value = value
            self.updateFrequency(node)
            return

        if self.size == self.capacity:
            node = self.freqToList[self.minFreq].removeLast()
            del self.keyToNode[node.key]
            self.size -= 1
        node = Node(key, value)
        self.keyToNode[key] = node
        self.freqToList[1].addFirst(node)
        self.minFreq = 1
        self.size += 1

    def updateFrequency(self, node):
        oldFreq = node.freq
        self.freqToList[oldFreq].remove(node)
        if oldFreq == self.minFreq and self.freqToList[oldFreq].size == 0:
            self.minFreq += 1
        node.freq += 1
        self.freqToList[node.freq].addFirst(node)
