class Solution:
    def minDifference(self, arr):
        # totalSum = sum(arr)
        # targetSum = totalSum // 2
    
        # for s in range(targetSum, -1, -1):
        #     if self.subsetSumsRec(arr, 0, s):
        #         return totalSum - 2 * s
        
        # memory = [[None]*(targetSum+1) for _ in range(len(arr))]
        # for s in range(targetSum, -1, -1):
        #     if self.subsetSumsRecMemo(arr, 0, s, memory):
        #         return totalSum - 2 * s
    
        # return totalSum
        
        return self.subsetSumsDP(arr)
    
    def subsetSumsRec(self, arr, index, sum):
       if sum == 0:
           return True
       if sum < 0:
           return False
       if index == len(arr):
           return False
       withCurr = self.subsetSums(arr, index + 1, sum - arr[index])
       if withCurr:
           return withCurr
       withoutCurr = self.subsetSums(arr, index + 1, sum)
       return withoutCurr

    def subsetSumsRecMemo(self, arr, index, sum, memory):
       if sum == 0:
           return True
       if sum < 0:
           return False
       if index == len(arr):
           return False
       if memory[index][sum] != None:
           return memory[index][sum]
       withCurr = self.subsetSumsRecMemo(arr, index + 1, sum - arr[index], memory)
       if withCurr:
           memory[index][sum] = withCurr
           return withCurr
       withoutCurr = self.subsetSumsRecMemo(arr, index + 1, sum, memory)
       memory[index][sum] = withoutCurr
       return memory[index][sum]
    
    def subsetSumsDP(self, arr):
        totalSum = sum(arr)
        targetSum = totalSum // 2
        memory = [[None]*(targetSum+1) for _ in range(len(arr)+1)]
        for currSum in range(targetSum+1):
            for index in range(len(arr), -1, -1):
               if currSum == 0:
                   memory[index][currSum] = True
               elif index == len(arr):
                   memory[index][currSum] = False
               else:
                   if currSum - arr[index] >= 0 and memory[index+1][currSum - arr[index]]:
                       memory[index][currSum] = True
                   else:
                       memory[index][currSum] = memory[index+1][currSum]
        
        for currSum in range(targetSum, -1, -1):
            if memory[0][currSum]:
                return totalSum - 2 * currSum
        return totalSum
                
