class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        # return self.isPowerOfTwoBruteForce(n)
        return self.isPowerOfTwoBitManipulation(n)
    
    def isPowerOfTwoBitManipulation(self, n):
        return (n & (n-1) == 0)
    
    def isPowerOfTwoBruteForce(self, n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            if count > 1:
                return False
            n = n //2
        return count == 1
