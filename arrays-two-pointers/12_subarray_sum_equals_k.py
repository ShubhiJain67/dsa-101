class Solution(object):
    def subarraySum(self, nums, k):
        # return self.bruteForce(nums, k)
        return self.optimised(nums, k)
        
    
    def bruteForce(self, nums, k):
        count = 0
        i = 0
        while i < len(nums):
            currSum = 0
            j = i
            while j < len(nums):
                currSum += nums[j]
                j+=1
                if currSum == k:
                    count += 1
            i+=1
        return count
    
    def optimised(self, nums, k):
        prefixSumMap = {0:1}
        count = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixSumMap:
                count += prefixSumMap[prefixSum - k]
            if prefixSum not in prefixSumMap:
                prefixSumMap[prefixSum] = 0
            prefixSumMap[prefixSum] += 1
        return count
