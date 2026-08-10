class Solution:
    MIN_VAL = -1000000001
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nextGreater = [-1]*n
        stack = [self.MIN_VAL]
        for index in range(2*n-1, -1, -1):
            while stack[-1] != self.MIN_VAL and stack[-1] <= nums[index%n]:
                stack.pop()
            nextGreater[index%n] = stack[-1]
            stack.append(nums[index%n])

        for index in range(len(nums)):
            if nextGreater[index] == self.MIN_VAL:
                nextGreater[index] = -1
        return nextGreater
