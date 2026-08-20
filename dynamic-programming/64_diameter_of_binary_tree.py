# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        viaCurr = self.maxHeight(root.left) + self.maxHeight(root.right)
        if root.left:
            viaCurr += 1
        if root.right:
            viaCurr += 1
        leftDia = self.diameterOfBinaryTree(root.left)
        rightDia = self.diameterOfBinaryTree(root.right)
        return max(max(leftDia, rightDia), viaCurr)

    def maxHeight(self, root):
        if root == None or (root.left == None and root.right == None):
            return 0
        return max(self.maxHeight(root.left), self.maxHeight(root.right)) + 1
