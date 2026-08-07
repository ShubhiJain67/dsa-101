from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        p1 = 0
        p2 = 1
        count = 1
        while p2 < len(nums):
            while p2 < len(nums) and nums[p1] == nums[p2]:
                p2 += 1
            if p2 == len(nums):
                return count
            p1 += 1
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            count += 1
            p2 += 1
            # print(nums)
        return count
            
        
