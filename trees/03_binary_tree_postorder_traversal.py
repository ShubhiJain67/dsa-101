from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = self.postorderTraversal(root.left)
        result = result + self.postorderTraversal(root.right)
        result = result + [root.val]
        return result
