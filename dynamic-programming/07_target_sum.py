from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # totalSum = sum(nums)
        # if (totalSum-target)%2 != 0:
        #     return 0
        # if abs(target) > totalSum:
        #     return 0
        # mid = (totalSum - target) // 2
        # return self.findSubsetRec(nums, 0, mid)

        # memory = [[None]*(mid+1) for _ in range(len(nums)+1)]
        # return self.findSubsetRecMemo (nums, 0, mid, memory)

        return self.findSubsetRecDP(nums, target)
    
    def findSubsetBruteForce(self, nums, target, index):
        if index == len(nums):
            return int(target == 0)
        withMinus = self.findSubsetBruteForce(nums, target + nums[index], index+1)
        withPlus = self.findSubsetBruteForce(nums, target - nums[index], index+1)
        return withMinus + withPlus

    def findSubsetRec(self, nums, index, target):
        subsetCount = 0
        if index == len(nums):
            return 1 if target == 0 else 0
        else:
            withCurrentCount = 0
            if target-nums[index] >= 0:
                withCurrentCount = self.findSubsetRec(nums, index+1, target-nums[index])
            withoutCurrentCount = self.findSubsetRec(nums, index+1, target)
            subsetCount = withCurrentCount + withoutCurrentCount
        return subsetCount

    def findSubsetRecMemo(self, nums, index, target, memory):
        subsetCount = 0
        if index == len(nums):
            return 1 if target == 0 else 0
        if memory[index][target] != None:
            return memory[index][target]
        else:
            withCurrentCount = 0
            if target-nums[index] >= 0:
                withCurrentCount = self.findSubsetRecMemo(nums, index+1, target-nums[index], memory)
            withoutCurrentCount = self.findSubsetRecMemo(nums, index+1, target, memory)
            subsetCount += withCurrentCount + withoutCurrentCount
        memory[index][target] = subsetCount
        return memory[index][target]

    def findSubsetRecDP(self, nums, targetSum):
        totalSum = sum(nums)
        if (totalSum-targetSum)%2 != 0:
            return 0
        if abs(targetSum) > totalSum:
            return 0
        mid = (totalSum - targetSum) // 2
        memory = [[None]*(mid+1) for _ in range(len(nums)+1)]

        for index in range(len(nums), -1, -1):
            for target in range(mid, -1, -1):
                subsetCount = 0
                if index == len(nums):
                    subsetCount = 1 if target == 0 else 0
                else: 
                    withCurrentCount = 0
                    if target-nums[index] >= 0:
                        withCurrentCount = memory[index+1][target-nums[index]]
                    withoutCurrentCount = memory[index+1][target]
                    subsetCount += withCurrentCount + withoutCurrentCount
                memory[index][target] = subsetCount
        return memory[0][mid]
