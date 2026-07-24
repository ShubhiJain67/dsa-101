class Solution(object):
    def checkSubarraySum(self, nums, k):
        # return self.bruteForce(nums, k)
        # return self.prefixSum(nums, k)
        return self.prefixSumOptimised(nums, k)
    
    def prefixSumOptimised(self, nums, k):
        remainderIndex = {0: -1}
        prefixSum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            remainder = prefixSum % k

            if remainder in remainderIndex:
                if i - remainderIndex[remainder] >= 2:
                    return True
            else:
                remainderIndex[remainder] = i

        return False
    
    def prefixSum(self, nums, k):
        prefixSumStore = [0] * (len(nums) + 1)

        i = 0
        while i < len(nums):
            prefixSumStore[i + 1] = prefixSumStore[i] + nums[i]
            i += 1

        i = 0
        while i < len(nums):
            j = i + 2
            while j <= len(nums):
                currSum = prefixSumStore[j] - prefixSumStore[i]
                if currSum % k == 0:
                    return True
                j += 1
            i += 1

        return False
    
    def bruteForce(self, nums, k):
        n = len(nums)

        for i in range(n):
            currSum = nums[i]
            for j in range(i + 1, n):
                currSum += nums[j]
                if currSum % k == 0:
                    return True

        return False
