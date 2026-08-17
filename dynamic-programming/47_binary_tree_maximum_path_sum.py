# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, ans = self.maxSum(root)
        return ans
    
    def maxSum(self, root):
        if root is None:
            return (0, float("-inf"))

        withLeft, withoutLeft = self.maxSum(root.left)
        withRight, withoutRight = self.maxSum(root.right)

        # Path that can be extended to the parent
        withCurr = root.val + max(0, withLeft, withRight)

        # Best path passing through the current node
        throughCurr = (
            root.val
            + max(0, withLeft)
            + max(0, withRight)
        )

        # Best path anywhere in this subtree
        withoutCurr = max(
            withoutLeft,
            withoutRight,
            throughCurr
        )

        return withCurr, withoutCurr
