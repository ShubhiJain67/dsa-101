# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1)
    
    def build(self, postorder, pi, pj, inorder, ii, ij):
        if pi > pj or ii > ij:
            return None
        index = ii
        currNode = TreeNode(postorder[pj], None, None)
        for i in range(ii, ij+1):
            if postorder[pj] == inorder[i]:
                index = i
                break
        leftSize = index - ii
        currNode.left = self.build(postorder,pi,pi + leftSize - 1,inorder,ii,index - 1)
        currNode.right = self.build(postorder,pi + leftSize,pj - 1,inorder,index + 1,ij)
        return currNode
