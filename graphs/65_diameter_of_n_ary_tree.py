"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if root is None:
            return 0
        maxWithoutCurr = 0
        for child in root.children:
            maxWithoutCurr = max(maxWithoutCurr, self.diameter(child))
        maxH1 = -1
        maxH2 = -1
        for child in root.children:
            childH = self.height(child)
            if childH >= maxH1:
                maxH2 = maxH1
                maxH1 = childH
            elif childH >= maxH2:
                maxH2 = childH
        viaCurr = 0
        if maxH1 >= 0:
            viaCurr += maxH1 + 1
        if maxH2 >= 0:
            viaCurr += maxH2 + 1
        return max(viaCurr, maxWithoutCurr)
    
    def height(self, node):
        if node is None or (node.children is None or len(node.children) == 0):
            return 0
        maxChildHeight = 0
        for child in node.children:
            maxChildHeight = max(maxChildHeight, self.height(child))
        return maxChildHeight + 1
        
