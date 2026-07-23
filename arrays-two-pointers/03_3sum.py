class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        index = 0
        while index < len(nums) - 2:
            if index > 0 and nums[index] == nums[index-1]:
                index += 1
                continue
            curr = nums[index]
            otherIndexes = self.twoSum(index+1, nums, 0 - curr)
            for indexes in otherIndexes:
                result.append([nums[index], nums[indexes[0]], nums[indexes[1]]])
            index += 1
        return result


    def twoSum(self, i, nums, target):
        p1 = i
        p2 = len(nums) - 1
        result = []
        while p1 < p2:
            currSum = nums[p1] + nums[p2]
            if currSum == target:
                result.append([p1, p2])
                p1+=1
                p2-=1
                while p1 < p2 and nums[p1] == nums[p1-1]:
                    p1+=1
                while p1 < p2 and nums[p2] == nums[p2+1]:
                    p2-=1
            elif currSum < target:
                p1 += 1
            else:
                p2 -= 1
        return result
