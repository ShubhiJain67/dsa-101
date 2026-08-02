# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = [root.val]
        result = result + self.preorderTraversal(root.left)
        result = result + self.preorderTraversal(root.right)
        return result
