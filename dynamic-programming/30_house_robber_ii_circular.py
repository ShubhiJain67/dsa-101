class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.robRec(nums, 0, 0)

        # memo = [[None]*2 for _ in range(len(nums))]
        # return self.robRecMemo(nums, 0, 0, memo)
        
        # return self.robDP(nums)
        
        return self.robDPOptimised(nums)
        
    def robRec(self, nums, index, robbedFirst):
        if index >= len(nums):
            return 0
        if robbedFirst == 1 and index == len(nums) - 1:
            return 0
        if index == 0:
            robbedFirst = 1
        withCurr = nums[index] + self.robRec(nums, index+2, robbedFirst)
        if index == 0:
            robbedFirst = 0
        withoutCurr =  self.robRec(nums, index+1, robbedFirst)
        return max(withCurr, withoutCurr)
    
    def robRecMemo(self, nums, index, robbedFirst, memo):
        if index >= len(nums):
            return 0
        if memo[index][robbedFirst] is not None:
            return memo[index][robbedFirst]
        if robbedFirst == 1 and index == len(nums) - 1:
            maxCount = 0
        else:
            withCurr = nums[index] + self.robRecMemo(nums, index+2, 1 if index == 0 else robbedFirst, memo)
            withoutCurr =  self.robRecMemo(nums, index+1, 0 if index == 0 else robbedFirst, memo)
            maxCount = max(withCurr, withoutCurr)
        memo[index][robbedFirst] = maxCount
        return memo[index][robbedFirst]
    
    def robDP(self, nums):
        dp = [[None]*2 for _ in range(len(nums)+2)]
        for index in range(len(nums)+1, -1, -1):
            for robbedFirst in range(2):
                if index >= len(nums):
                    maxCount = 0
                elif robbedFirst == 1 and index == len(nums) - 1:
                    maxCount = 0
                else:
                    withCurr = nums[index] + dp[index+2][1 if index == 0 else robbedFirst]
                    withoutCurr =  dp[index+1][0 if index == 0 else robbedFirst]
                    maxCount = max(withCurr, withoutCurr)
                dp[index][robbedFirst] = maxCount
        return dp[0][0]
    
    def robDPOptimised(self, nums):
        p1 = [0,0]
        p2 = [0,0]
        for index in range(len(nums)+1, -1, -1):
            curr = [0,0]
            for robbedFirst in range(2):
                if index >= len(nums):
                    maxCount = 0
                elif robbedFirst == 1 and index == len(nums) - 1:
                    maxCount = 0
                else:
                    withCurr = nums[index] + p1[1 if index == 0 else robbedFirst]
                    withoutCurr =  p2[0 if index == 0 else robbedFirst]
                    maxCount = max(withCurr, withoutCurr)
                curr[robbedFirst] = maxCount
            p1 = p2
            p2 = curr
        return p2[0]

    
