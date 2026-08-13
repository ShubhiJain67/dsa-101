class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicateNums = set()
        i = 0
        while i < len(nums):
            # print(f"Working for {i} -> {nums} and {duplicateNums}")
            correct = nums[i]
            if correct != i+1:
                if nums[correct-1] == nums[i]:
                    duplicateNums.add(nums[i])
                    i += 1
                else:
                    nums[i], nums[correct-1] = nums[correct-1], nums[i]
            else:
                i += 1
        return list(duplicateNums)
