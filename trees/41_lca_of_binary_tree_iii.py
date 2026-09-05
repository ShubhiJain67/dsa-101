"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # return self.getLcaV1(p, q)
        return self.getLcaV2(p, q)

    def getLcaV2(self, p, q):
        depthP = self.getDepth(p)
        depthQ = self.getDepth(q)
        if depthP > depthQ:
            p, q = q, p
            depthP, depthQ = depthQ, depthP
        while depthP != depthQ:
            q = q.parent
            depthQ -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p
        
        
    def getDepth(self, node):
        count = 0
        while node.parent is not None:
            node = node.parent
            count += 1
        return count
    
    def getLcaV1(self, p, q):
        root = self.getRoot(p)
        return self.lca(root, p, q)

    def getRoot(self, node):
        while node.parent is not None:
            node = node.parent
        return node

    def lca(self, curr, p, q):
        if curr is None:
            return None
        if curr == p or curr == q:
            return curr
        left = self.lca(curr.left, p, q)
        right = self.lca(curr.right, p, q)
        if left and right:
            return curr
        if left:
            return left
        if right:
            return right
        return None
