class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charFirstIndex = {}
        charLastIndex = {}
        for i in range(len(s)):
            ch = s[i]
            if ch not in charFirstIndex:
                charFirstIndex[ch] = i
            charLastIndex[ch] = i
        ranges = []
        for ch in charFirstIndex:
            ranges.append([charFirstIndex[ch], charLastIndex[ch]])
        ranges.sort()
        p1 = 0
        newRanges = [ranges[0]]
        for p2 in range(1, len(ranges)):
            if newRanges[p1][1] > ranges[p2][0]:
                newRanges[p1] = [newRanges[p1][0], max(newRanges[p1][1], ranges[p2][1])]
            else:
                newRanges.append(ranges[p2])
                p1 += 1
        return [r[1]-r[0]+1 for r in newRanges]
