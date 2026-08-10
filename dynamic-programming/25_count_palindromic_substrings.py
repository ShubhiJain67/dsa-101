class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [[None]*len(s) for _ in range(len(s))]
        count = 0
        for start in range(len(s)-1, -1, -1):
            for end in range(start, len(s)):
                if start == end:
                    memo[start][end] = True
                elif s[start] != s[end]:
                    memo[start][end] = False
                elif start + 1 == end:
                    memo[start][end] = True
                else:
                    memo[start][end] = memo[start+1][end-1]
                if memo[start][end]:
                    count += 1
        return count
