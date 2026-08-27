class Solution:
    def longestBitonicSequence(self, n, nums):
        # return self.solve(nums, 0, -1, True)
        
        # memo = [[[None] * 2 for _ in range(n + 1)] for _ in range(n)]
        # return self.solveMemo(nums, 0, -1, True, memo)
        
        return self.solveDP(nums)
        
    
    def solve(self, nums, index, prev, increasing):
        if index == len(nums):
            return 0
        ans = self.solve(nums, index + 1, prev, increasing)
        if increasing:
            if prev == -1 or nums[index] > nums[prev]:
                ans = max(ans,1 + self.solve(nums, index + 1, index, True))
            if prev != -1 and nums[index] < nums[prev]:
                ans = max(ans,1 + self.solve(nums, index + 1, index, False))
        else:
            if prev == -1 or nums[index] < nums[prev]:
                ans = max(ans,1 + self.solve(nums, index + 1, index, False))
        return ans
        
    def solveMemo(self, nums, index, prev, increasing, memo):
        if index == len(nums):
            return 0
    
        if memo[index][prev + 1][int(increasing)] is not None:
            return memo[index][prev + 1][int(increasing)]
        ans = self.solveMemo(nums, index + 1, prev, increasing, memo)
    
        if increasing:
            if prev == -1 or nums[index] > nums[prev]:
                ans = max(ans, 1 + self.solveMemo(nums, index + 1, index, True, memo))
            if prev != -1 and nums[index] < nums[prev]:
                ans = max(ans, 1 + self.solveMemo(nums, index + 1, index, False, memo))
        else:
            if prev == -1 or nums[index] < nums[prev]:
                ans = max(ans, 1 + self.solveMemo(nums, index + 1, index, False, memo))
    
        memo[index][prev + 1][int(increasing)] = ans
        return ans
        
    def solveDP(self, nums):
        n = len(nums)
        dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
    
        for index in range(n - 1, -1, -1):
            for prev in range(index - 1, -2, -1):
                ans = dp[index + 1][prev + 1][0]
                if prev == -1 or nums[index] < nums[prev]:
                    ans = max(ans, 1 + dp[index + 1][index + 1][0])
                dp[index][prev + 1][0] = ans
    
                ans = dp[index + 1][prev + 1][1]
                if prev == -1 or nums[index] > nums[prev]:
                    ans = max(ans, 1 + dp[index + 1][index + 1][1])
    
                if prev != -1 and nums[index] < nums[prev]:
                    ans = max(ans, 1 + dp[index + 1][index + 1][0])
    
                dp[index][prev + 1][1] = ans
    
        return dp[0][0][1]
