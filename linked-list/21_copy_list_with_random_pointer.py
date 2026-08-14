"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeStore = {}
        ptr = head
        while ptr:
            node = Node(ptr.val)
            nodeStore[ptr] = node
            ptr = ptr.next
        ptr = head
        newHead = None
        while ptr:
            node = nodeStore[ptr]
            if ptr.next:
                node.next = nodeStore[ptr.next]
            if ptr.random:
                node.random = nodeStore[ptr.random]
            if newHead == None:
                newHead = node
            ptr = ptr.next
        return newHead
        
