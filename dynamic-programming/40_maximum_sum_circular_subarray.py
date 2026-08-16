class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0

        currMax = 0
        maxSum = -math.inf

        currMin = 0
        minSum = math.inf

        for num in nums:
            totalSum += num

            # Kadane for maximum subarray
            currMax = max(num, currMax + num)
            maxSum = max(maxSum, currMax)

            # Kadane for minimum subarray
            currMin = min(num, currMin + num)
            minSum = min(minSum, currMin)

        # All numbers are negative
        if maxSum < 0:
            return maxSum
        return max(maxSum, totalSum - minSum)
