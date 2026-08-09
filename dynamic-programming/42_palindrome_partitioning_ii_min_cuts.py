class Solution:
    def minCut(self, s: str) -> int:
        # return self.minCutDPAll(s)

        # return self.minCutDP(s)

        return self.minCutDPOptimised(s)
    
    def minCutDPOptimised(self, s):
        memo = [None]*(len(s)+1)
        palindromeMemo = {}
        for start in range(len(s), -1, -1):
            ans = len(s)
            if start == len(s):
                ans = -1
            else:
                for end in range(start, len(s)):
                    if self.isPalindromeMemo(s, start, end, palindromeMemo):
                        ans = min(ans, 1+memo[end + 1])
            memo[start] = ans
        return memo[0]

    def minCutDP(self, s):
        memo = [None]*(len(s)+1)
        for start in range(len(s), -1, -1):
            ans = len(s)
            if start == len(s):
                ans = -1
            else:
                for end in range(start, len(s)):
                    if self.isPalindrome(s, start, end):
                        ans = min(ans, 1+memo[end + 1])
            memo[start] = ans
        return memo[0]

    def minCutDPAll(self, s):
        memo = [None]*(len(s)+1)
        for start in range(len(s), -1, -1):
            ans = []
            if start == len(s):
                ans = [[]]
            else:
                for end in range(start, len(s)):
                    if self.isPalindrome(s, start, end):
                        for suffix in memo[end + 1]:
                            ans.append([s[start:end+1]] + suffix)
            memo[start] = ans
        minParts = len(s)
        for parts in memo[0]:
            minParts = min(minParts, len(parts) - 1)
        return minParts

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def isPalindromeMemo(self, s, i, j, memo):
        if i >= j:
            return True
        ident = f"{i}-{j}"
        if ident in memo:
            return memo[ident]
        memo[ident] = s[i] == s[j] and self.isPalindromeMemo(s, i+1, j-1, memo)
        return memo[ident]
