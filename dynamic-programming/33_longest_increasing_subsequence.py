from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.longestRec(nums, -1)

        # memo = [None]*(len(nums))
        # return self.longestRecMemo(nums, -1, memo)

        return self.longestDP(nums)
    
    def longestRec(self, nums, index):
        if index >= len(nums):
            return 0
        maxLen = 0
        currHeight = -10001
        if index >= 0:
            currHeight = nums[index]
        for nextGreater in range(index+1, len(nums)):
            if nums[nextGreater] > currHeight:
                currLen = 1 + self.longestRec(nums, nextGreater)
                maxLen = max(maxLen, currLen)
        return maxLen

    def longestRecMemo(self, nums, index, memo):
        if index >= len(nums):
            return 0
        if index >= 0 and memo[index] is not None:
            return memo[index]
        maxLen = 0
        currHeight = -10001
        if index >= 0:
            currHeight = nums[index]
        for nextGreater in range(index+1, len(nums)):
            if nums[nextGreater] > currHeight:
                currLen = 1 + self.longestRecMemo(nums, nextGreater, memo)
                maxLen = max(maxLen, currLen)
        if index >= 0:
            memo[index] = maxLen
        return maxLen
    
    def longestDP(self, nums):
        memo = [None]*(len(nums)+2)
        for index in range(len(nums), -2, -1):
            maxLen = 0
            if index == len(nums):
                maxLen = 0
            else:
                currHeight = -10001
                if index >= 0:
                    currHeight = nums[index]
                for nextGreater in range(index+1, len(nums)):
                    if nums[nextGreater] > currHeight:
                        currLen = 1 + memo[nextGreater+1]
                        maxLen = max(maxLen, currLen)
                memo[index+1] = maxLen
        return memo[0]
