class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store = {}
        for ch in s:
            store[ch] = 0
        for ch in t:
            if ch not in store:
                return ""
            store[ch] += 1

        start = -1
        end = 0
        minLen = math.inf
        minStr = ""
        cut = 0
        while start < len(s) and end < len(s) and start <= end: #EXPAND
            ch = s[end]
            if store[ch] > 0:
                cut += 1
            store[ch] -= 1
            while cut == len(t): # SHRINK
                if minLen > end - start:
                    minLen = end - start
                    minStr = s[start+1:end+1]
                start += 1
                ch = s[start]
                store[ch] += 1
                if store[ch] > 0:
                    cut -= 1
            end += 1
        return minStr
        
