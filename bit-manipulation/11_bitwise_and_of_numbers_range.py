class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # return self.bruteForce(left, right)
        return self.optimised(left, right)
    
    def optimised(self, left, right):
        shift = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
    
    def bruteForce(self, left, right):
        result = left
        for num in range(left+1, right+1):
            result = result & num
            if result == 0:
                return 0
        return result
