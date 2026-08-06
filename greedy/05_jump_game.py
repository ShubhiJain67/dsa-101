class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return self.jump(nums, 0)
        
        # memo = [None]*len(nums)
        # return self.jumpMemo(nums, 0, memo)
        
        # return self.jumpDP(nums)

        return self.jumpGreedy(nums)
    
    def jumpGreedy(self, nums):
        goal = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] >= (goal - index):
                goal = index
        return goal == 0
    
    def jump(self, nums, index):
        if index == len(nums)-1:
            return True
        if index >= len(nums):
            return False
        canReach = False
        for i in range(1, nums[index]+1):
            if self.jump(nums, index + i):
                return True
        return False

    def jumpMemo(self, nums, index, memo):
        if index == len(nums)-1:
            return True
        if index >= len(nums):
            return False
        if memo[index] is not None:
            return memo[index]
        canReach = False
        for i in range(1, nums[index]+1):
            if self.jumpMemo(nums, index + i, memo):
                canReach = True
                break
        memo[index] = canReach
        return memo[index]

    def jumpDP(self, nums):
        memo = [None]*len(nums)
        for index in range(len(nums)-1, -1, -1):
            canReach = False
            if index == len(nums)-1:
                canReach = True
            else:
                for i in range(1, nums[index]+1):
                    if index + i < len(nums) and memo[index + i]:
                        canReach = True
                        break
            memo[index] = canReach
        return memo[0]
