class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return self.bruteForce(s)
        # return self.memoized(s)
        # return self.dp(s)
        return self.explanONCenter(s)
    
    def bruteForce(self, s):
        longest = ""
        longestLen = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                if self.isPalindrome(s, start, end):
                    if longestLen < end -start + 1:
                        longest = s[start:end+1]
                        longestLen = end -start + 1
        return longest
    
    def isPalindrome(self, s, start, end):
        if start == end:
            return True
        if start > end:
            return True
        if s[start] != s[end]:
            return False
        return self.isPalindrome(s, start+1, end-1)
    
    def memoized(self, s):
        longest = ""
        longestLen = 0
        memo = [[None]*len(s) for _ in range(len(s))]
        for start in range(len(s)):
            for end in range(start, len(s)):
                if self.isPalindromeMemo(s, start, end, memo):
                    if longestLen < end -start + 1:
                        longest = s[start:end+1]
                        longestLen = end -start + 1
        return longest
    
    def isPalindromeMemo(self, s, start, end, memo):
        if start > end:
            return True
        if memo[start][end] is not None:
            return memo[start][end]
        if start == end:
            isPalin = True
        elif s[start] != s[end]:
            isPalin = False
        else:
            isPalin = self.isPalindromeMemo(s, start+1, end-1, memo)
        memo[start][end] = isPalin
        return memo[start][end]

    def dp(self, s):
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        longest = ""
        longestLen = 0
        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                if start == end:
                    memo[start][end] = True
                elif s[start] != s[end]:
                    memo[start][end] = False
                elif end - start == 1:
                    memo[start][end] = True
                else:
                    memo[start][end] = memo[start + 1][end - 1]

                if memo[start][end] and end - start + 1 > longestLen:
                    longest = s[start:end+1]
                    longestLen = end -start + 1

        return longest

    def explanONCenter(self, s):
        start = 0
        maxLen = 1

        def expand(left, right):
            nonlocal start, maxLen

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    start = left

                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start:start + maxLen]
