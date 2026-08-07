from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # self.sortColorsAnyCount(nums)
        self.sortDutchNationalFlag(nums)

    def sortDutchNationalFlag(self, nums):
        p1 = 0
        p2 = 0
        p3 = len(nums) - 1
        while p2 <= p3:
            if nums[p2] == 0:
                nums[p2] = nums[p1]
                nums[p1] = 0
                p1 += 1
                p2 += 1
            elif nums[p2] == 1:
                p2 += 1
            else:
                nums[p2] = nums[p3]
                nums[p3] = 2
                p3 -= 1
            



    def sortColorsAnyCount(self, nums: List[int]) -> None:
        colorCount = 3
        colors = [0] * colorCount
        for num in nums:
            colors[num]+=1
        color = 0
        index = 0
        for color in range(3):
            while colors[color] > 0:
                nums[index] = color
                index += 1
                colors[color] -= 1
