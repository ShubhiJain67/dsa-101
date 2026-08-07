class Solution:
    def perfectSum(self, arr, target):
        return self.perfectSumRecursionDPV2(arr, target)
    
    def perfectSumRecursion(self, arr, target):
        subArrays = []
        self.getPerfectSumRecursion(arr, target, 0, [], subArrays)
        uniqueSubArrays = set(map(tuple, subArrays))
        result = []
        for array in uniqueSubArrays:
            result.append([arr[index] for index in array])
        return len(result)
    
    def getPerfectSumRecursion(self, arr, target, index, subArray, subArrays):
        if target == 0:
            subArrays.append(subArray)
        if index == len(arr):
            return
        if target >= arr[index]:
            self.getPerfectSumRecursion(arr, target - arr[index], index + 1, subArray + [index], subArrays)
            self.getPerfectSumRecursion(arr, target, index + 1, subArray , subArrays)
        else:
            self.getPerfectSumRecursion(arr, target, index + 1, subArray , subArrays)
        
    def perfectSumRecursion2(self, arr, target):
        subArrays = []
        self.getPerfectSumRecursion(arr, target, 0, [], subArrays)
        uniqueSubArrays = set(map(tuple, subArrays))
        result = []
        for array in uniqueSubArrays:
            result.append([arr[index] for index in array])
    
    def getPerfectSumRecursion2(self, arr, target, index):
        if target == 0:
            return [[]], True
        if index == len(arr):
            return None, False
        allSubArrays = []
        if target >= arr[index]:
            withIndexSubArrays, hasSubsetsWithIndex = self.getPerfectSumRecursion2(arr, target-arr[index], index+1)
            if hasSubsetsWithIndex:
                for withIndexSubArray in withIndexSubArrays:
                    allSubArrays.append(withIndexSubArray+[index])

        withoutIndexSubArrays, hasSubsetsWithoutIndex = self.getPerfectSumRecursion2(arr, target, index+1)
        if hasSubsetsWithoutIndex:
            for withoutIndexSubArray in withoutIndexSubArrays:
                allSubArrays.append(withoutIndexSubArray+[index])
        
        return allSubArrays, hasSubsetsWithoutIndex or hasSubsetsWithIndex
        
        
    def perfectSumRecursionMemoisation(self, arr, target):
        memory = [[None] * (len(arr) + 1) for _ in range(target + 1)]
        subArrays, found = self.getPerfectSumRecursionMemoisation(arr, target, 0, memory)
        if not found:
            return 0
        uniqueSubArrays = set(map(tuple, subArrays))
        result = []
        for array in uniqueSubArrays:
            result.append([arr[index] for index in array])
        return len(result)
    
    def getPerfectSumRecursionMemoisation(self, arr, target, index, memory):
        if target < 0:
            return [], False

        if index == len(arr):
            memory[target][index] = ([[]] if target == 0 else [], target == 0)
            return memory[target][index]
    
        if memory[target][index] is not None:
            return memory[target][index]
    
        allSubArrays = []
        hasSubsetsWithIndex = False
        hasSubsetsWithoutIndex = False
    
        if target >= arr[index]:
            withIndexSubArrays, hasSubsetsWithIndex = (self.getPerfectSumRecursionMemoisation(arr, target - arr[index], index + 1, memory))
    
            if hasSubsetsWithIndex:
                for subset in withIndexSubArrays:
                    allSubArrays.append(subset + [index])
    
        withoutIndexSubArrays, hasSubsetsWithoutIndex = (self.getPerfectSumRecursionMemoisation(arr, target, index + 1, memory))
     
        if hasSubsetsWithoutIndex:
            for subset in withoutIndexSubArrays:
                allSubArrays.append(subset)
    
        memory[target][index] = (allSubArrays, hasSubsetsWithIndex or hasSubsetsWithoutIndex)
    
        return memory[target][index]
        

    def perfectSumRecursionDP(self, arr, Target):
        memory = [[None] * (len(arr) + 1) for _ in range(Target + 1)]
        for target in range(Target+1):
            for index in range(len(arr), -1, -1):
                if index == len(arr):
                    memory[target][index] = ([[]] if target == 0 else [], target == 0)
                else:
                    allSubArrays = []
                    hasSubsetsWithIndex = False
                    hasSubsetsWithoutIndex = False
                    if target >= arr[index]:
                        withIndexSubArrays, hasSubsetsWithIndex = memory[target - arr[index]][index + 1]
    
                        if hasSubsetsWithIndex:
                            for subset in withIndexSubArrays:
                                allSubArrays.append([index] + subset)
                
                    withoutIndexSubArrays, hasSubsetsWithoutIndex = memory[target][index + 1]
                 
                    if hasSubsetsWithoutIndex:
                        for subset in withoutIndexSubArrays:
                            allSubArrays.append(subset)
                
                    memory[target][index] = (allSubArrays, hasSubsetsWithIndex or hasSubsetsWithoutIndex)
        
        if not memory[Target][0][1]:
            return 0
        uniqueSubArrays = set(map(tuple, memory[Target][0][0]))
        result = []
        for array in uniqueSubArrays:
            result.append([arr[index] for index in array])
        return len(result)
    
    

    def perfectSumRecursionDPV2(self, arr, Target):
        prev = [None] * (Target + 1)
        curr = [None] * (Target + 1)
        for target in range(Target + 1):
            prev[target] = ([[]] if target == 0 else [], target == 0)
        
        for index in range(len(arr) - 1, -1, -1):
            for target in range(Target + 1):
                allSubArrays = []
        
                if target >= arr[index]:
                    subsets, ok = prev[target - arr[index]]
                    if ok:
                        for subset in subsets:
                            allSubArrays.append([index] + subset)
        
                subsets, ok = prev[target]
                if ok:
                    allSubArrays.extend(subsets)
        
                curr[target] = (allSubArrays, len(allSubArrays) > 0)
        
            prev, curr = curr, [None] * (Target + 1)
        
        subsets, found = prev[Target]
        if not found:
            return 0
#       uniqueSubArrays = set(map(tuple, subsets))
        return len(subsets)
    
