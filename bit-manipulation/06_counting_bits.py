from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        # return self.countBitsBruteForce(n)
        return self.countBitsOptimised(n)

    def countBitsOptimised(self, n):
        bitArr = [0]*(n+1)
        bitArr[0] = 0
        lastPowerChange = 1
        nextPowerChange = 2
        i = 1
        while nextPowerChange <= n:
            for index in range(lastPowerChange+1, nextPowerChange+1):
                bitArr[index-1] = bitArr[index-1-lastPowerChange] + 1
            lastPowerChange = nextPowerChange
            nextPowerChange *= 2

        for index in range(lastPowerChange+1, n+2):
            bitArr[index-1] = bitArr[index-1-lastPowerChange] + 1

        return bitArr

    def countBitsBruteForce(self, n):
        bitArr = [0]*(n+1)
        for i in range(n+1):
            bitArr[i] = self.getBitCount(i)
        return bitArr

    def getBitCount(self, n):
        count = 0
        while n > 0:
            if n%2 == 1:
                count += 1
            n = n//2
        return count
