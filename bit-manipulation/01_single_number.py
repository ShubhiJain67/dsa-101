class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNum = 0
        for num in nums:
            singleNum = singleNum ^ num
        return singleNum
