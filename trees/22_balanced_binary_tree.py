# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, isValid = self.check(root)
        return isValid
    
    def check(self, root):
        if not root:
            return 0, True
        if not root.left and not root.right:
            return 1, True
        leftHeight, isLeft = self.check(root.left)
        rightHeight, isRight = self.check(root.right)
        if isLeft and isRight and abs(leftHeight - rightHeight) <= 1:
            return max(leftHeight, rightHeight)+1, True
        return 0, False
        
