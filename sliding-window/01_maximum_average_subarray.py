from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        maxAvg = currSum
        for i in range(k, len(nums)):
            currSum = currSum + nums[i] - nums[i-k]
            if maxAvg < currSum:
                maxAvg = currSum

        return maxAvg / k
