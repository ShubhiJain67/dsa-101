# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # return self.bruteForce(root)
        return self.getSum(root, 0)
        
    def getSum(self, root, curr):
        if root == None:
            return 0
        # Sending number prefixes to bottom
        curr = curr * 10 + root.val
        if not root.left and not root.right:
            return curr
        return self.getSum(root.left, curr) + self.getSum(root.right, curr)

    def bruteForce(self, root):
        allNums = self.getAllPaths(root)
        total = 0
        for num in allNums:
            total += int(num)
        return total

    def getAllPaths(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [f"{root.val}"]
        leftNums = self.getAllPaths(root.left)
        rightNums = self.getAllPaths(root.right)
        allNums = []
        for num in leftNums:
            allNums.append(f"{root.val}{num}")
        for num in rightNums:
            allNums.append(f"{root.val}{num}")
        return allNums
