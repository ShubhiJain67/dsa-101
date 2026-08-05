'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        q = [[(root, 0)]]
        curr = 0
        bottoms = []
        nums = {}
        while curr < len(q):
            level = q[curr]
            newLevel = []
        
            for node, position in level:
                nums[position] = node.data
                if node.left:
                    newLevel.append((node.left, position - 1))
        
                if node.right:
                    newLevel.append((node.right, position + 1))
        
            if newLevel:
                q.append(newLevel)
        
            curr += 1
        return [nums[col] for col in sorted(nums)]
        
        
