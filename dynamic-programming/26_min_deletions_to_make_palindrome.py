class Solution:
    def minDeletions(self,s):
        # code here 
        # longest = self.longestSubsequence(s, 0, len(s)-1)
        
        # memo = [[0]*len(s) for _ in range(len(s))]
        # longest = self.longestSubsequenceMemo(s, 0, len(s)-1, memo)
        
        # longest = self.longestSubsequenceDP(s)
        
        longest = self.longestSubsequenceDPV2(s)
        return len(s) - longest
    
    def longestSubsequence(self, s, i, j):
        longest = 0
        if i > j:
            longest = 0
        elif i == j:
            longest = 1
        elif s[i] == s[j]:
            longest = 2 + self.longestSubsequence(s, i+1, j-1)
        else:
            longest = max(self.longestSubsequence(s, i+1, j), self.longestSubsequence(s, i, j-1))
        return longest
            
    def longestSubsequenceMemo(self, s, i, j, memo):
        if i > j:
            return 0
        longest = 0
        if i == j:
            longest = 1
        elif s[i] == s[j]:
            longest = 2 + self.longestSubsequenceMemo(s, i+1, j-1, memo)
        else:
            longest = max(self.longestSubsequenceMemo(s, i+1, j, memo), self.longestSubsequenceMemo(s, i, j-1, memo))
        memo[i][j] = longest
        return longest
        
    def longestSubsequenceDP(self, s):
        memo = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                longest = 0
                if i == j:
                    longest = 1
                elif s[i] == s[j]:
                    longest = 2 + memo[i+1][j-1]
                else:
                    longest = max(memo[i+1][j], memo[i][j-1])
                memo[i][j] = longest
        return memo[0][len(s)-1]
        
        
    def longestSubsequenceDPV2(self, s):
        prev = [0]*len(s)
        for i in range(len(s)-1, -1, -1):
            curr = [0]*len(s)
            for j in range(i, len(s)):
                longest = 0
                if i == j:
                    longest = 1
                elif s[i] == s[j]:
                    longest = 2 + prev[j-1]
                else:
                    longest = max(prev[j], curr[j-1])
                curr[j] = longest
            prev = curr
        return curr[len(s)-1]    
        
    
        
        
