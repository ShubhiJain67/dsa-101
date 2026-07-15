class Solution:
    def countPartitions(self, arr, diff):
        # code here
        totalSumCount = sum(arr)
        if (totalSumCount - diff) % 2 == 1:
            return 0
        if totalSumCount - diff < 0:
            return 0
        mid = int((totalSumCount - diff)/2)
        
        # return self.getSubsetCountRec(arr, 0, mid)
        
        # memory = [[None]*(mid+1) for _ in range(len(arr)+1)]
        # return self.getSubsetCountRecMemo(arr, 0, mid, memory)
        
        return self.getSubsetCountDP(arr, mid)
    
    def getSubsetCountRec(self, arr, index, currSum):
        subsetCount = 0
        if currSum == 0:
            subsetCount = 1
        elif currSum < 0:
            return subsetCount
        
        if index == len(arr):
            return subsetCount
        else:
            withCurrentCount = self.getSubsetCountRec(arr, index+1, currSum-arr[index])
            withoutCurrentCount = self.getSubsetCountRec(arr, index+1, currSum)
            subsetCount = withCurrentCount + withoutCurrentCount
        return subsetCount
        
    def getSubsetCountRecMemo(self, arr, index, currSum,memory):
        subsetCount = 0
        if currSum == 0:
            subsetCount = 1
        elif currSum < 0:
            return subsetCount
        if index == len(arr):
            return subsetCount
        elif memory[index][currSum] != None:
            return memory[index][currSum]
        else:
            withCurrentCount = self.getSubsetCountRecMemo(arr, index+1, currSum-arr[index], memory)
            withoutCurrentCount = self.getSubsetCountRecMemo(arr, index+1, currSum, memory)
            memory[index][currSum] = withCurrentCount + withoutCurrentCount
        return memory[index][currSum]
    
    
    def getSubsetCountDP(self, arr, targetSum):
        memory = [[None]*(targetSum+1) for _ in range(len(arr)+1)]
        
        for index in range(len(arr), -1, -1):
            for currSum in range(targetSum + 1):
                subsetCount = 0
                if currSum == 0:
                    subsetCount = 1
                if index == len(arr):
                    memory[index][currSum] = subsetCount
                    continue
                else:
                    withCurrentCount = 0
                    if (currSum-arr[index]) >= 0:
                        withCurrentCount = memory[index+1][currSum-arr[index]]
                    withoutCurrentCount = memory[index+1][currSum]
                    memory[index][currSum] = withCurrentCount + withoutCurrentCount
        # print(memory)
        return memory[0][targetSum]
        
        
        
