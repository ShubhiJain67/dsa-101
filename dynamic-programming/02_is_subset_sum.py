class Solution:
    def isSubsetSum (self, arr, sum):
        # return self.isSubsetSumRecursion(arr, sum, 0)
        
        # memory = [[None]*(sum+1) for _ in range(len(arr)+1)]
        # return self.isSubsetSumMemoisation(arr, sum, 0, memory)
        
        return self.isSubsetSumDP(arr, sum)
        
    def isSubsetSumRecursion(self, arr, sum, index):
        if sum == 0:
            return True
        elif index == len(arr):
            return False
        elif sum < arr[index]:
            return self.isSubsetSumRecursion(arr, sum, index+1)
        else:
            withItem = self.isSubsetSumRecursion(arr, sum-arr[index], index+1)
            if not withItem:
                withoutItem = self.isSubsetSumRecursion(arr, sum, index+1)
                return withoutItem
            else:
                return withItem
                
    def isSubsetSumMemoisation(self, arr, sum, index, memory):
        if sum == 0:
            return True
        elif index == len(arr):
            return False
        elif memory[index][sum] != None:
            return memory[index][sum]
        elif sum < arr[index]:
            memory[index][sum] = self.isSubsetSumMemoisation(arr, sum, index+1, memory)
            return memory[index][sum]
        else:
            withItem = self.isSubsetSumMemoisation(arr, sum-arr[index], index+1, memory)
            if not withItem:
                withoutItem = self.isSubsetSumMemoisation(arr, sum, index+1, memory)
                memory[index][sum] = withoutItem
            else:
                memory[index][sum] = withItem
            return memory[index][sum]
    
    def isSubsetSumDP(self, arr, s):
        memory = [[None]*(s+1) for _ in range(len(arr)+1)]
        for index in range(len(arr), -1, -1):
            for sum in range(s+1):
                if sum == 0:
                    memory[index][sum] = True
                elif index == len(arr):
                    memory[index][sum] = False
                elif sum < arr[index]:
                    memory[index][sum] = memory[index+1][sum]
                else:
                    memory[index][sum] = memory[index+1][sum-arr[index]] or memory[index+1][sum]
        return memory[0][s]
            
