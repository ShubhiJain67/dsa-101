class Solution:
    def minInsertions(self, s: str) -> int:
        # longestPalindrome = self.longestSubSeqRec(s, 0, len(s)-1)

        # memo = [[None]*len(s) for _ in range(len(s))]
        # longestPalindrome = self.longestSubSeqRecMemo(s, 0, len(s)-1, memo)

        # longestPalindrome = self.longestSubSeqDP(s)

        longestPalindrome = self.longestSubSeqDPV2(s)
        
        return len(s) - longestPalindrome
    
    def longestSubSeqRec(self, s, start, end):
        longest = 0
        if start > end:
            longest = 0
        elif start == end:
            longest = 1
        elif s[start] == s[end]:
            longest = 2 + self.longestSubSeqRec(s, start + 1, end - 1)
        else:
            longest = max(self.longestSubSeqRec(s, start+1, end), self.longestSubSeqRec(s, start, end-1))
        return longest

    def longestSubSeqRecMemo(self, s, start, end, memo):
        if memo[start][end] is not None:
            return memo[start][end]
        longest = 0
        if start > end:
            longest = 0
        elif start == end:
            longest = 1
        elif s[start] == s[end]:
            longest = 2 + self.longestSubSeqRecMemo(s, start + 1, end - 1, memo)
        else:
            longest = max(self.longestSubSeqRecMemo(s, start+1, end, memo), self.longestSubSeqRecMemo(s, start, end-1, memo))
        memo[start][end] = longest
        return memo[start][end]

    def longestSubSeqDP(self, s):
        memo = [[None]*len(s) for _ in range(len(s))]
        for start in range(len(s)-1, -1, -1):
            for end in range(len(s)):
                longest = 0
                if start > end:
                    longest = 0
                elif start == end:
                    longest = 1
                elif s[start] == s[end]:
                    if start + 1 < len(s) and end - 1 >= 0:
                        longest = 2 + memo[start + 1][end - 1]
                else:
                    if start + 1 < len(s):
                        longest = max(longest, memo[start + 1][end])
                    if end - 1 >= 0:
                        longest = max(longest, memo[start][end - 1])
                memo[start][end] = longest
        return memo[start][end]

    def longestSubSeqDPV2(self, s):
        prev = [0]*len(s)
        for start in range(len(s)-1, -1, -1):
            curr = [0]*len(s)
            for end in range(len(s)):
                longest = 0
                if start > end:
                    longest = 0
                elif start == end:
                    longest = 1
                elif s[start] == s[end]:
                    if start + 1 < len(s) and end - 1 >= 0:
                        longest = 2 + prev[end - 1]
                else:
                    if start + 1 < len(s):
                        longest = max(longest, prev[end])
                    if end - 1 >= 0:
                        longest = max(longest, curr[end - 1])
                curr[end] = longest
            prev = curr
        return curr[end]
