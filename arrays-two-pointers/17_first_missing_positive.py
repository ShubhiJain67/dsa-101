class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # return self.firstMissingPositiveMemo(nums)
        return self.firstMissingCyclicSort(nums)
    
    def firstMissingCyclicSort(self, nums):
        n = len(nums)
        index = 0
        while index < len(nums):
            correctIndex = nums[index]-1
            # print(f"At {index} {correctIndex} {nums}")
            if 0 <= correctIndex < n and nums[index] != nums[correctIndex]:
                nums[correctIndex], nums[index] = nums[index], nums[correctIndex]
            else:
                index += 1
        
        for index in range(len(nums)):
            if index != nums[index]-1:
                return index+1
        return len(nums)+1


    def firstMissingPositiveMemo(self, nums: List[int]) -> int:
        seen = [False]*len(nums)
        for num in nums:
            if num <= 0 or num>len(nums):
                continue
            seen[num-1] = True
        for i in range(len(nums)):
            if not seen[i]:
                return i+1
        return len(nums)+1
