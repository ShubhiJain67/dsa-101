# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left, root.right)
    
    def mirror(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if (tree1 and not tree2) or (not tree1 and tree2):
            return False
        if tree1.val != tree2.val:
            return False
        return self.mirror(tree1.left, tree2.right) and self.mirror(tree1.right, tree2.left)
        
