class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            if count > 1:
                return False
            n = n //2
        return count == 1
