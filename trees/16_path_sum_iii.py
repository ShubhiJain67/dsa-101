# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        totalCount = 0
        if root == None:
            return totalCount
        totalCount += self.pathSum(root.left, targetSum)
        totalCount += self.pathSum(root.right, targetSum)
        totalCount += self.countSum(root, targetSum)
        return totalCount
    
    def countSum(self, root, targetSum):
        totalCount = 0
        if root == None:
            return totalCount
        if root.val == targetSum:
            totalCount += 1
        totalCount += self.countSum(root.left, targetSum - root.val)
        totalCount += self.countSum(root.right, targetSum - root.val)
        return totalCount
