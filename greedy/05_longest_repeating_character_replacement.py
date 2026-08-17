class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.slidingWindow(s, k)

    def slidingWindow(self, s, k):
        chFreq = {}
        for ch in s:
            if ch not in chFreq:
                chFreq[ch] = 0
            chFreq[ch] += 1
        maxLen = 0
        for ch in chFreq:
            # print(f"Doing for {ch}")
            p0 = 0
            p1 = 0
            replacements = k
            while p0 < len(s) and p1 < len(s):
                # print(f"From {p0} to {p1} '{s[p0:p1+1]}' with {replacements}")
                if s[p1] == ch:
                    p1 += 1
                elif replacements > 0:
                    replacements -= 1
                    p1 += 1
                else:
                    if s[p0] != ch:
                        replacements += 1
                    p0 += 1
                maxLen = max(maxLen, p1-p0)
            # print(f"For {ch} -> {maxLen}")
        return maxLen
