# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        rootStr = f"({left}):{root.val}:({right})"
        return rootStr
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None

        left, root, right = self.parse(data)

        rootNode = TreeNode(root)
        rootNode.left = self.deserialize(left)
        rootNode.right = self.deserialize(right)

        return rootNode

    def parse(self, s):
        depth = 0
        first = second = -1

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            elif ch == ':' and depth == 0:
                if first == -1:
                    first = i
                else:
                    second = i
                    break

        left = s[:first][1:-1]
        root = int(s[first+1:second])
        right = s[second+1:][1:-1]

        return left, root, right

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
