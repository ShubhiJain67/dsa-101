# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.right and not root.left and root.val == targetSum:
            return [[root.val]]
        leftPaths = self.pathSum(root.left, targetSum - root.val)
        rightPaths = self.pathSum(root.right, targetSum - root.val)
        paths = []
        for path in leftPaths:
            paths.append([root.val]+path)
        for path in rightPaths:
            paths.append([root.val]+path)

        return paths
