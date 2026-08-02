# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == key:
            right = root.right
            left = root.left
            if right == None:
                return left
            if left == None:
                return right
            newRoot = right
            leftToAlign = right.left
            newRoot.left = left
            p = newRoot.left
            while p.right is not None:
                p = p.right
            p.right = leftToAlign
            return newRoot
        else:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
        return root
