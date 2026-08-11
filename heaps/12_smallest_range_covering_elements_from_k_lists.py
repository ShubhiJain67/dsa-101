class Solution:
    def smallestRange(self, numsList: List[List[int]]) -> List[int]:
        nums = self.getNumbers(numsList)
        numCount = len(nums)

        listCount = len(numsList)
        store = {i: 1 for i in range(listCount)}

        minRange = None
        start = 0
        end = 0
        count = 0
        while start < numCount and end < numCount:
            currValue, currIndex = nums[end]
            if store[currIndex] > 0:
                count += 1
            store[currIndex] -= 1

            while count == listCount:
                if (minRange is None or
                    (currValue - nums[start][0] < minRange[1] - minRange[0])):
                    minRange = [nums[start][0], currValue]
                _, startIndex = nums[start]
                store[startIndex] += 1
                if store[startIndex] > 0:
                    count -= 1
                start += 1
            end += 1
        return minRange
    
    def getNumbers(self, numsList):
        nums = []
        for index in range(len(numsList)):
            for num in numsList[index]:
                nums.append([num, index])
        nums.sort()
        return nums
