class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        store = {}
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in store:
                p1 = max(p1, store[ch] + 1)
            store[ch] = i
            p2 += 1
            maxLen = max(maxLen, p2-p1)
            # print(f"{p1} {p2}")
        return maxLen
