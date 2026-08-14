"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None or (head.next is None and head.child is None):
            return head
        ptr = head
        if head.child:
            newHead = self.flatten(head.child)
            head.child = None
            temp = newHead
            while temp.next:
                temp = temp.next
            temp.next = self.flatten(head.next)
            if head.next:
                head.next.prev = temp
            newHead.prev = head
            head.next = newHead
        else:
            head.next = self.flatten(head.next)
        return head
