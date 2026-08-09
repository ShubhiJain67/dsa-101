class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # return self.part(s, 0)

        # memo = [None]*len(s)
        # return self.partMemo(s, 0, memo)

        return self.partDP(s)

    def part(self, s, start):
        if start == len(s):
            return [[]]

        ans = []
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                for suffix in self.part(s, end + 1):
                    ans.append([s[start:end+1]] + suffix)
        return ans

    def partMemo(self, s, start, memo):
        if start == len(s):
            return [[]]
        if memo[start] != None:
            return memo[start]

        ans = []
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                for suffix in self.partMemo(s, end + 1, memo):
                    ans.append([s[start:end+1]] + suffix)
        memo[start] = ans
        return memo[start]

    def partDP(self, s):
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
        return memo[0]

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
