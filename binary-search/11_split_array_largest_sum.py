class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefixSum = self.getPrefixSum(nums)

        # prefixSum = self.getPrefixSum(nums)
        # return self.split(nums, 0, k, prefixSum)

        # prefixSum = self.getPrefixSum(nums)
        # memo = [[None]*(k+1) for _ in range(len(nums))]
        # return self.splitMemo(nums, 0, k, prefixSum, memo)

        # prefixSum = self.getPrefixSum(nums)
        # return self.splitDP(nums, k, prefixSum)

        return self.splitGreedy(nums, k)


    
    def getPrefixSum(self, nums):
        prefixSum = []
        prevSum = 0
        for num in nums:
            prevSum += num
            prefixSum.append(prevSum)
        return prefixSum

    def split(self, nums, index, k, prefixSum):
        if k == 1:
            preSum = prefixSum[-1] - (prefixSum[index - 1] if index > 0 else 0)
            return preSum
        minSplit = math.inf
        for part in range(index + 1, len(nums)):
            minLeft = prefixSum[part-1] - (prefixSum[index-1] if index > 0 else 0)
            minRight = self.split(nums, part, k-1, prefixSum)
            minSplit = min(minSplit, max(minLeft, minRight))
        return minSplit

    def splitMemo(self, nums, index, k, prefixSum, memo):
        if memo[index][k] is not None:
            return memo[index][k]
        minSplit = math.inf
        if k == 1:
            minSplit = prefixSum[-1] - (prefixSum[index - 1] if index > 0 else 0)
        else:
            for part in range(index + 1, len(nums)):
                minLeft = prefixSum[part-1] - (prefixSum[index-1] if index > 0 else 0)
                minRight = self.splitMemo(nums, part, k-1, prefixSum, memo)
                minSplit = min(minSplit, max(minLeft, minRight))
        memo[index][k] = minSplit
        return memo[index][k]
    
    def splitDP(self, nums, K, prefixSum):
        memo = [[None]*(K+1) for _ in range(len(nums))]
        for k in range(1, K+1):
            for index in range(len(nums)-1, -1, -1):
                minSplit = math.inf
                if k == 1:
                    minSplit = prefixSum[-1] - (prefixSum[index - 1] if index > 0 else 0)
                else:
                    for part in range(index + 1, len(nums)):
                        minLeft = prefixSum[part-1] - (prefixSum[index-1] if index > 0 else 0)
                        minRight = memo[part][k-1]
                        minSplit = min(minSplit, max(minLeft, minRight))
                memo[index][k] = minSplit
        return memo[0][K]
    
    def splitGreedy(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            if self.canSplit(nums, mid, k):
                high = mid
            else:
                low = mid + 1

        return low

    def canSplit(self, nums, maxSum, k):
        partitions = 1
        currSum = 0

        for num in nums:
            if currSum + num <= maxSum:
                currSum += num
            else:
                partitions += 1
                currSum = num

        return partitions <= k
