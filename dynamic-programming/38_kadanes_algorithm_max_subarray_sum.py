class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force -> Go to every sub array sum all elements and get highest - TC - O(n^3) SC - O(1)
        # Calculate Prefix sum first then go to every sub array and fin sum via prefix sum - TC - O(n^2) SC - O(n)
        # Calculate Prefix sum on the go to every sub array and find max in same loop - TC - O(n^2) SC - O(1)
        return self.greedyDP(nums)
        # return self.dnc(nums, 0, len(nums)-1)


    def greedyDP(self, nums):
        # Idea -> only check for +ve subarrays maybe using 2 pointer? O(n)
        p1 = 0
        p2 = 0
        currSum = 0
        maximumSubArray = -math.inf
        while p1 < len(nums) and p2 < len(nums):
            currSum += nums[p2]
            p2 += 1
            if maximumSubArray < currSum:
                maximumSubArray = currSum
            if currSum < 0:
                p1 = p2
                currSum = 0

        return maximumSubArray

    def dnc(self, nums, low, high):
        # Idea -> mid would be included or fully left or fully right -> O(nlog(n))
        if low > high:
            return -math.inf

        mid = low + (high - low) // 2
        # Expanding on Mid
        bestLeftSum = 0
        leftSum = 0
        for i in range(mid-1, -1, -1):
            leftSum += nums[i]
            bestLeftSum = max(bestLeftSum, leftSum)
        bestRightSum = 0
        rightSum = 0
        for i in range(mid+1, len(nums)):
            rightSum += nums[i]
            bestRightSum = max(bestRightSum, rightSum)
        
        sumIncludingCurr = bestLeftSum + nums[mid] + bestRightSum
        onlyLeft = self.dnc(nums, low, mid - 1)
        onlyRight = self.dnc(nums, mid + 1, high)
        return max(sumIncludingCurr, max(onlyLeft, onlyRight))

