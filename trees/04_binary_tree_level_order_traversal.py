# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []
        if root == None:
            return levelOrder
        queue = deque([root, None])
        while len(queue)>1:
            curr = queue.popleft()
            currLevel = []
            while curr is not None:
                currLevel.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                curr = queue.popleft()
            queue.append(None)
            levelOrder.append(currLevel)
        return levelOrder
            
