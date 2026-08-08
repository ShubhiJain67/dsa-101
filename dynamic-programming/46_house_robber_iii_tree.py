# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return self.robRec(root)
        
        # memory = {}
        # return self.robMemo(root, memory, "R")

        # memoryWith = {}
        # memoryWithout = {}
        # return self.robMemoV2(root, memoryWith, memoryWithout, "R")


        # withRoot, withoutRoot = self.robRecSimple(root)
        # return max(withRoot, withoutRoot)

        # memory = {}
        # withRoot, withoutRoot = self.robMemoSimple(root, memory, "R")
        # return max(withRoot, withoutRoot)

        withRoot, withoutRoot = self.robDP(root)
        return max(withRoot, withoutRoot)


    def robRec(self, root):
        if not root:
            return 0
        withCurr = root.val
        withoutCurr = 0
        if root.left:
            withoutCurr += self.robRec(root.left)
            withCurr += self.robRec(root.left.left)
            withCurr += self.robRec(root.left.right)
        if root.right:
            withoutCurr += self.robRec(root.right)
            withCurr += self.robRec(root.right.left)
            withCurr += self.robRec(root.right.right)
        return max(withoutCurr, withCurr)

    def robMemo(self, root, memory, identifier):
        if not root:
            return 0
        if identifier in memory:
            return memory[identifier]
        withCurr = root.val
        withoutCurr = 0
        if root.left:
            withoutCurr += self.robMemo(root.left, memory, identifier+"L")
            withCurr += self.robMemo(root.left.left, memory, identifier+"LL")
            withCurr += self.robMemo(root.left.right, memory, identifier+"LR")
        if root.right:
            withoutCurr += self.robMemo(root.right, memory, identifier+"R")
            withCurr += self.robMemo(root.right.left, memory, identifier+"RL")
            withCurr += self.robMemo(root.right.right, memory, identifier+"RR")
        memory[identifier] = max(withoutCurr, withCurr)
        return memory[identifier]

    def robMemoV2(self, root, identifier):
        memoryWith = {}
        memoryWithout = {}
        que = deque((root, identifer))
        if not root:
            return 0
        if identifier in memoryWith and identifier in memoryWithout:
            return max(memoryWith[identifier], memoryWithout[identifier])
        withCurr = root.val
        withoutCurr = 0
        if root.left:
            withoutCurr += self.robMemoV2(root.left, memoryWith, memoryWithout, identifier+"L")
            withCurr += self.robMemoV2(root.left.left, memoryWith, memoryWithout, identifier+"LL")
            withCurr += self.robMemoV2(root.left.right, memoryWith, memoryWithout, identifier+"LR")
        if root.right:
            withoutCurr += self.robMemoV2(root.right, memoryWith, memoryWithout, identifier+"R")
            withCurr += self.robMemoV2(root.right.left, memoryWith, memoryWithout, identifier+"RL")
            withCurr += self.robMemoV2(root.right.right, memoryWith, memoryWithout, identifier+"RR")
        memoryWith[identifier] = withCurr
        memoryWithout[identifier] = withoutCurr
        return max(memoryWith[identifier], memoryWithout[identifier])

    def robRecSimple(self, root):
        if not root:
            return 0, 0
        
        wihLeft, withoutLeft = self.robRecSimple(root.left)
        withRight, withoutRight = self.robRecSimple(root.right)

        withCurr = root.val + withoutLeft + withoutRight
        withoutCurr = max(wihLeft, withoutLeft) + max(withRight, withoutRight)
        return withCurr, withoutCurr

    def robMemoSimple(self, root, memo, identifier):
        if not root:
            return 0, 0
        if identifier in memo:
            return memo[identifier]
        wihLeft, withoutLeft = self.robMemoSimple(root.left, memo, identifier+"L")
        withRight, withoutRight = self.robMemoSimple( root.right, memo, identifier+"R")

        withCurr = root.val + withoutLeft + withoutRight
        withoutCurr = max(wihLeft, withoutLeft) + max(withRight, withoutRight)
        memo[identifier] = [withCurr, withoutCurr]
        return memo[identifier]


    def robDP(self, root):
        if not root:
            return 0
        # recursion call initiate
        stack = [(root, False)]
        memo = {}
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                # recursion call completion
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                withLeft, withoutLeft = memo[node.left] if node.left in memo else [0,0]
                withRight, withoutRight = memo[node.right] if node.right in memo else [0,0]

                withCurr = node.val + withoutLeft + withoutRight
                withoutCurr = max(withLeft, withoutLeft) + max(withRight, withoutRight)
                memo[node] = [withCurr, withoutCurr]
        return memo[root]


    
    
