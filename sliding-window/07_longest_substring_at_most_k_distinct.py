class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        characters = {}
        p0 = 0
        p1 = 0
        maxLen = 0
        while p1 < len(s):
            ch = s[p1]

            if ch not in characters:
                characters[ch] = 0
            characters[ch] += 1
            p1 += 1

            while len(characters) > k:
                left = s[p0]
                characters[left] -= 1
                if characters[left] == 0:
                    del characters[left]
                p0 += 1
            maxLen = max(maxLen, p1 - p0)
        return maxLen
