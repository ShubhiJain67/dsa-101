import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        index = 0
        closest = math.inf
        minDiff = math.inf
        while index < len(nums) - 2:
            if index > 0 and nums[index] == nums[index-1]:
                index += 1
                continue
            requiredTarget = target - nums[index]
            minDiffToTarget, closestToTarget = self.twoSum(nums, requiredTarget, index+1)
            actualSum = closestToTarget + nums[index]
            currDiff = target - actualSum if target > actualSum else actualSum - target
            if minDiff > currDiff:
                minDiff = currDiff
                closest = actualSum
            if closest == target:
                return closest
            index += 1
        return closest
    
    def twoSum(self, nums, target, index):
        left = index
        right = len(nums) - 1
        minDiff = math.inf
        closest = math.inf
        while left < right:
            currSum = nums[left] + nums[right]
            currDiff = target - currSum if target > currSum else currSum - target
            if minDiff > currDiff:
                minDiff = currDiff
                closest = currSum
            if currSum == target:
                return minDiff, closest
            elif currSum > target:
                right -= 1
            else:
                left += 1
        return minDiff, closest
