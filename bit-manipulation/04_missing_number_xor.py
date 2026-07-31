class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n+1):
            total = total ^ i
        for num in nums:
            total = total ^ num
        return total
