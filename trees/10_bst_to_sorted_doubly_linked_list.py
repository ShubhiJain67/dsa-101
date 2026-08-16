"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        doublyList = self.getDoublyList(root)
        if doublyList:
            ptr = doublyList
            while ptr.right:
                ptr = ptr.right
            ptr.right = doublyList
            doublyList.left = ptr
        return doublyList
    
    def getDoublyList(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        head = None
        leftList = self.getDoublyList(root.left)
        if leftList:
            head = leftList
            ptr = leftList
            while ptr.right:
                ptr = ptr.right
            ptr.right = root
            root.left = ptr
        else:
            head = root
        rightList = self.getDoublyList(root.right)
        root.right = rightList
        if rightList:
            rightList.left = root
        return head
            
