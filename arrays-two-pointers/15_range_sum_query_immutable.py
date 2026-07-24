class NumArray(object):
    prefixSumStore = []

    def __init__(self, nums):
        prefixSum = 0
        self.prefixSumStore = [0] * (len(nums))
        i = 0
        while i < len(nums):
            prefixSum += nums[i]
            self.prefixSumStore[i] = prefixSum
            i += 1

    def sumRange(self, left, right):
        total = self.prefixSumStore[right]
        if left - 1 >= 0:
            total -= self.prefixSumStore[left - 1]
        return total
