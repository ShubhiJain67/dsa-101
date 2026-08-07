from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return self.singlePositiveNumber(nums)
        # return self.singleNumber(nums)
        return self.singleNumberOptimised(nums)
    
    def singleNumberOptimised(self, nums: List[int]) -> int:
        bitStore = [0]*32
        for bitIndex in range(32):
            for i in range(len(nums)):
                num = nums[i]
                # Convert to 32-bit unsigned representation
                num = num & 0xffffffff
                if num == 0:
                    continue
                bit = num%2
                if bit:
                    bitStore[bitIndex]+=1
                nums[i] = int(num/2)
        return self.getNumFromBits(bitStore)
    
    def singleNumber(self, nums: List[int]) -> int:
        bitStore = [0]*32
        negativeBitStore = [0]*32
        for bitIndex in range(32):
            for i in range(len(nums)):
                num = nums[i]
                if num == 0:
                    continue
                bit = num%2
                if bit:
                    if num >0:
                        bitStore[bitIndex]+=1
                    else:
                        negativeBitStore[bitIndex]+=1
                nums[i] = int(num/2)
        finalNum = self.getNumFromBits(bitStore)
        if finalNum != 0:
            return finalNum
        return -self.getNumFromBits(negativeBitStore)
    
    def singlePositiveNumber(self, nums: List[int]) -> int:
        bitStore = [0]*32
        for bitIndex in range(32):
            for i in range(len(nums)):
                num = nums[i]
                if num == 0:
                    continue
                bit = num%2
                if bit:
                    bitStore[bitIndex]+=1
                nums[i] = int(num/2)
        return self.getNumFromBits(bitStore)
    
    def getNumFromBits(self, bits):
        finalNum = 0
        power2 = 1
        for i in range(32):
            if bits[i] % 3 == 1:
                finalNum += power2*1
            power2 *= 2
        return finalNum
