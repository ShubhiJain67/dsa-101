class Solution(object):
    def findDuplicate(self, nums):
        # return self.bruteForce(nums)
        # return self.inPlace(nums)
        return self.cycleDetection(nums)
    
    def cycleDetection(self, nums):
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
    
    def inPlace(self, nums):
        i = 0
        while i < len(nums):
            if nums[abs(nums[i])-1] < 0:
                return abs(nums[i])
            nums[nums[i]-1] *= -1
            i += 1
        return 0
    
    def bruteForce(self, nums):
        found = [False]*(len(nums)-1)
        i = 0
        while i < len(nums):
            if found[nums[i]-1]:
                return nums[i]
            found[nums[i]-1] = True
            i += 1
        return 0
