class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        if len(nums) < 4:
            return result
        nums.sort()
        result = []
        index = 0
        while index < len(nums) - 3:
            if index > 0 and nums[index] == nums[index-1]:
                index += 1
                continue
            curr = nums[index]
            otherIndexes = self.threeSum(index+1, nums, target - curr)
            for indexes in otherIndexes:
                result.append([nums[index], nums[indexes[0]], nums[indexes[1]], nums[indexes[2]]])
            index += 1
        return result
    
    def threeSum(self, index, nums, target):
        result = []
        start = index
        while index < len(nums) - 2:
            if index > start and nums[index] == nums[index-1]:
                index += 1
                continue
            curr = nums[index]
            otherIndexes = self.twoSum(index+1, nums, target - curr)
            for indexes in otherIndexes:
                result.append([index, indexes[0], indexes[1]])
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
