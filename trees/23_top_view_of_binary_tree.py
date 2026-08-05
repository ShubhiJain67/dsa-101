'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        q = [[(root, 0)]]
        curr = 0
        tops = []
        nums = {}
        while curr < len(q):
            level = q[curr]
            newLevel = []
        
            for node, position in level:
                if position not in nums:
                    nums[position] = node.data
                    tops.append([position, node.data])
                if node.left:
                    newLevel.append((node.left, position - 1))
        
                if node.right:
                    newLevel.append((node.right, position + 1))
        
            if newLevel:
                q.append(newLevel)
        
            curr += 1
        tops.sort()
        return [top[1] for top in tops]
        
