class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p0 = 0
        p1 = 0
        currSum = 0
        minDist = math.inf
        while p1 < len(nums):
            currSum += nums[p1]
            while currSum >= target:
                minDist = min(minDist, p1-p0+1)
                currSum -= nums[p0]
                p0 += 1
            p1 += 1
        return minDist if minDist != math.inf else 0
        
