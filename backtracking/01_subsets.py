class Solution(object):
    def subsets(self, nums):
        return self.getSubstes(nums, 0)
    
    def getSubstes(self, nums, index):
        if index == len(nums):
            return [[]]
        otherSubsets = self.getSubstes(nums, index+1)
        allSubsets = []
        for subset in otherSubsets:
            allSubsets.append(subset)
            allSubsets.append([nums[index]]+subset)
        return allSubsets
        
