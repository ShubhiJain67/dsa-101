class Solution(object):
    def permute(self, nums):
        return self.getPermutations(nums, 0)
    
    def getPermutations(self, nums, index):
        if index == len(nums):
            return [[]]
        restPermutations = self.getPermutations(nums, index+1)
        allPermutations = []
        for perm in restPermutations:
            for i in range(len(perm)+1):
                allPermutations.append(perm[:i]+[nums[index]]+perm[i:])
        return allPermutations
        
