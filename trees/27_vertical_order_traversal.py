# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [[(root, 0)]]
        curr = 0
        nums = {}

        while curr < len(q):
            level = q[curr]
            newLevel = []

            levelMap = {}

            for node, position in level:
                if position not in levelMap:
                    levelMap[position] = []

                levelMap[position].append(node.val)

                if node.left:
                    newLevel.append((node.left, position - 1))

                if node.right:
                    newLevel.append((node.right, position + 1))

            # Sort nodes with same row & column
            for position in levelMap:
                levelMap[position].sort()

                if position not in nums:
                    nums[position] = []

                nums[position].extend(levelMap[position])

            if newLevel:
                q.append(newLevel)

            curr += 1

        return [nums[col] for col in sorted(nums)]
