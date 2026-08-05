# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
                nums[position] = node.val
                if node.left:
                    newLevel.append((node.left, position + 1))
        
                if node.right:
                    newLevel.append((node.right, position + 1))
        
            if newLevel:
                q.append(newLevel)
        
            curr += 1
        return [nums[col] for col in sorted(nums)]
