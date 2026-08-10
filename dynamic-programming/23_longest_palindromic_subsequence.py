class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # return self.find(s, 0, len(s)-1)

        # memo = [[None]*len(s) for _ in range(len(s))]
        # return self.findMemo(s, 0, len(s)-1, memo)

        # return self.findDP(s)

        return self.findDPV2(s)

    def find(self, s, si, ti):
        if si > ti or not (0 <= si < len(s) and 0 <= ti < len(s)):
            return 0
        maxLen = 0
        if si == ti:
            maxLen = 1
        else:
            maxLen = max(self.find(s, si+1, ti), self.find(s, si, ti-1))
            if s[si] == s[ti]:
                maxLen = max(maxLen, 2+self.find(s, si+1, ti-1))
        return maxLen  
    
    def findMemo(self, s, si, ti, memo):
        if si > ti or not (0 <= si < len(s) and 0 <= ti < len(s)):
            return 0
        if memo[si][ti] is not None:
            return memo[si][ti]
        maxLen = 0
        if si == ti:
            maxLen = 1
        else:
            maxLen = max(self.findMemo(s, si+1, ti, memo), self.findMemo(s, si, ti-1, memo))
            if s[si] == s[ti]:
                maxLen = max(maxLen, 2+self.findMemo(s, si+1, ti-1, memo))
        memo[si][ti] = maxLen
        return memo[si][ti]

    def findDP(self, s):
        memo = [[None]*len(s) for _ in range(len(s))]

        for si in range(len(s)-1, -1, -1):
            for ti in range(len(s)):
                maxLen = 0
                if si > ti:
                    maxLen = 0
                elif si == ti:
                    maxLen = 1
                else:
                    maxLen = max(memo[si+1][ti], memo[si][ti-1])
                    if s[si] == s[ti]:
                        maxLen = max(maxLen, 2+memo[si+1][ti-1])
                memo[si][ti] = maxLen
        return memo[0][len(s)-1]

    def findDPV2(self, s):
        prev = [None]*len(s)
        for si in range(len(s)-1, -1, -1):
            curr = [None]*len(s)
            for ti in range(len(s)):
                maxLen = 0
                if si > ti:
                    maxLen = 0
                elif si == ti:
                    maxLen = 1
                else:
                    maxLen = max(prev[ti], curr[ti-1])
                    if s[si] == s[ti]:
                        maxLen = max(maxLen, 2+prev[ti-1])
                curr[ti] = maxLen
            prev = curr
        return curr[len(s)-1]
            
