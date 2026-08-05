'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:

    def boundaryTraversal(self, root):
        if not root:
            return []
        ans = [root.data]
        if not root.left and not root.right:
            return ans

        self.addLeftBoundary(root.left, ans)
        self.addLeaves(root, ans)
        self.addRightBoundary(root.right, ans)

        return ans

    def isLeaf(self, node):
        return node.left is None and node.right is None

    def addLeftBoundary(self, node, ans):
        while node:
            if not self.isLeaf(node):
                ans.append(node.data)

            if node.left:
                node = node.left
            else:
                node = node.right

    def addLeaves(self, node, ans):
        if not node:
            return

        if self.isLeaf(node):
            ans.append(node.data)
            return

        self.addLeaves(node.left, ans)
        self.addLeaves(node.right, ans)

    def addRightBoundary(self, node, ans):
        temp = []

        while node:
            if not self.isLeaf(node):
                temp.append(node.data)

            if node.right:
                node = node.right
            else:
                node = node.left

        while temp:
            ans.append(temp.pop())
