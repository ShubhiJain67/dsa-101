class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return self.powerOfFourBruteForce(n)
        return self.powerOfFourBitManipulation(n)
    
    def powerOfFourBitManipulation(self, n):
        if not self.isPowerOfTwo(n):
            return False
        count = 0 
        while n > 1:
            count += 1
            n = n >> 1     # equivalent to n = n / 2
        return (count & 1) == 0     # equivalent to count % 2 == 0
    
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1) == 0)

    
    def powerOfFourBruteForce(self, n):
        if n == 0:
            return False
        while n % 4 == 0:
            n = int(n/4)
        return n == 1
