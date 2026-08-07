from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        p2 = 0
        
        while p2 < len(nums):
            while p2 < len(nums) and nums[p2] == 0:
                p2 += 1
            if p2 == len(nums):
                return
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1 += 1
            p2 += 1
