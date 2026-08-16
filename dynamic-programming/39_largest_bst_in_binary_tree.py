''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
import math
class Solution:
    def largestBst(self, root: 'Node') -> int:
        
        # return self.bruteForce(root)
        
        _, size, _, _ = self.optimised(root)
        return size
        
        
    def optimised(self, root): # O(n)
        if root is None:
            return True, 0, math.inf, -math.inf
        
        leftBST, leftSize, leftMin, leftMax = self.optimised(root.left)
        rightBST, rightSize, rightMin, rightMax = self.optimised(root.right)
        
        if leftBST and rightBST and leftMax < root.data < rightMin:
            currSize = leftSize + rightSize + 1
            currMin = min(root.data, leftMin)
            currMax = max(root.data, rightMax)
            return True, currSize, currMin, currMax
        
        return False, max(leftSize, rightSize), -math.inf, math.inf
    
    
    # ----------------------------------
        
    def bruteForce(self, root): # O(n^2)
        #  For every node in tree do full tree search and count in worstcase
        currMax = 0
        if root is None:
            currMax = 0
        elif self.isValidBST(root, -math.inf, math.inf):
            currMax = self.count(root)
        else:
            currMax = max(self.bruteForce(root.left), self.bruteForce(root.right))
        return currMax
        
    
    def isValidBST(self, root, lower, upper): # O(n)
        if root is None:
            return True
        if root.data <= lower:
            return False
        if root.data >= upper:
            return False
        return self.isValidBST(root.left, lower, root.data) and self.isValidBST(root.right, root.data, upper)
        
    def count(self, root): # O(n)
        if root is None:
            return 0
        leftCount = self.count(root.left)
        rightCount = self.count(root.right)
        return leftCount + rightCount + 1
        
        
