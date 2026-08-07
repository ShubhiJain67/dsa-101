from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
    def build(self, preorder, pi, pj, inorder, ii, ij):
        if pi > pj or ii > ij:
            return None
        index = ii
        currNode = TreeNode(preorder[pi], None, None)
        for i in range(ii, ij+1):
            if preorder[pi] == inorder[i]:
                index = i
                break
        currNode.left = self.build(preorder, pi+1, pi+index - ii, inorder, ii, index -1)
        currNode.right = self.build(preorder, pi+index-ii+1, pj, inorder, index +1, ij)
        return currNode
        
        
