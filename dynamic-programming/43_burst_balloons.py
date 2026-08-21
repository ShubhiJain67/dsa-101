import math

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for part in range(left + 1, right):
                    memo[left][right] = max(
                        memo[left][right],
                        memo[left][part]
                        + memo[part][right]
                        + nums[left] * nums[part] * nums[right]
                    )
        return memo[0][n - 1]
