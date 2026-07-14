class Solution:
    def equalPartition(self, arr):
        # code here
        sum = 0
        for num in arr:
            sum += num
        if sum % 2 == 1:
            return False
        
        # return self.findRecursion(arr, sum, 0, 0)
        
        # memory = [[None]*(sum+1) for _ in range(len(arr)+1)]
        # return self.findRecursionMemoisation(arr, sum, 0, 0, memory)
        
        return self.findDP(arr, sum)
        
    
    def findRecursion(self, arr, total, currSum, index):
        if currSum*2 == total:
            return True
        if index >= len(arr):
            return False
        withCurrent = self.findRecursion(arr, total, currSum + arr[index], index + 1)
        if withCurrent:
            return True
        return self.findRecursion(arr, total, currSum, index + 1)
        
        
    def findRecursionMemoisation(self, arr, total, currSum, index, memory):
        if currSum*2 == total:
            return True
        if currSum*2 > total:
            return False
        if index >= len(arr):
            return False
        if memory[index][currSum] != None:
            return memory[index][currSum]
        withCurrent = self.findRecursionMemoisation(arr, total, currSum + arr[index], index + 1, memory)
        if withCurrent:
            memory[index][currSum] = withCurrent
        else:
            memory[index][currSum] = self.findRecursionMemoisation(arr, total, currSum, index + 1, memory)
        return memory[index][currSum]
        
    def findDP(self, arr, sum):
        memory = [[None]*(sum+1) for _ in range(len(arr)+1)]
        
        for index in range(len(arr), -1, -1):
            for currSum in range(sum, -1, -1):
                if currSum*2 > sum:
                    memory[index][currSum] = False
                elif currSum*2 == sum:
                    memory[index][currSum] = True
                elif index >= len(arr):
                    memory[index][currSum] = False
                else:
                    if currSum + arr[index] <= sum:
                        withCurrent = memory[index + 1][currSum + arr[index]]
                    else:
                        withCurrent = False
                    withoutCurrent = memory[index + 1][currSum]
                    memory[index][currSum] = withCurrent or withoutCurrent
        return memory[0][0]
        
        
        
