class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.robRec(nums, 0)
        # return self.robDP(nums)
        return self.robDPOptimised(nums)

    def robRec(self, nums, index):
        if index >= len(nums):
            return 0
        withCurr = nums[index] + self.robRec(nums, index+2)
        withoutCurr =  self.robRec(nums, index+1)
        return max(withCurr, withoutCurr)
    
    def robDP(self, nums):
        dp = [0]*(len(nums)+2)
        for index in range(len(nums)+1, -1, -1):
            if index >= len(nums):
                maxCount = 0
            else:
                withCurr = nums[index] + dp[index+2]
                withoutCurr =  dp[index+1]
                maxCount = max(withCurr, withoutCurr)
            dp[index] = maxCount
        return dp[0]
    
    def robDPOptimised(self, nums):
        p1 = 0
        p2 = 0
        for index in range(len(nums)+1, -1, -1):
            if index >= len(nums):
                maxCount = 0
            else:
                withCurr = nums[index] + p1
                withoutCurr = p2
                maxCount = max(withCurr, withoutCurr)
            p1 = p2
            p2 = maxCount
        return p2

    
