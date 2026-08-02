# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBst(root, -math.inf, math.inf)

    def isBst(self, root, lower, upper):
        if root == None:
            return True
        if root.val <= lower:
            return False
        if root.val >= upper:
            return False
        return self.isBst(root.left, lower, root.val) and self.isBst(root.right, root.val, upper)
