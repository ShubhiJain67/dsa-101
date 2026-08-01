class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        return self.getSubsetsRec(nums, 0)

    def getSubsetsRec(self, nums, index):
        if index == len(nums):
            return [[]]
        nextIndex = index + 1
        while nextIndex < len(nums) and nums[nextIndex] == nums[index]:
            nextIndex += 1
        skip = self.getSubsetsRec(nums, nextIndex)
        take = self.getSubsetsRec(nums, index + 1)
        combinations = []
        for comb in skip:
            combinations.append(comb)
        for comb in take:
            combinations.append([nums[index]] + comb)

        return combinations
