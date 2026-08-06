class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        childCount = 0
        g.sort()
        s.sort()
        p1 = 0
        p2 = 0
        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2]:
                p1 += 1
                childCount += 1
            p2 += 1
        return childCount
