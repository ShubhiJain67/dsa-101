from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        allTogether = 0
        for num in nums:
            allTogether = allTogether ^ num
        firstSetBit = allTogether & -allTogether
        firstNum = 0
        for num in nums:
            if num & firstSetBit:
                firstNum = firstNum ^ num
        secondNum = allTogether ^ firstNum
        return [firstNum, secondNum]
