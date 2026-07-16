class Solution:
    def knapSack(self, val, wt, capacity):
        # return self.knapSackRec(val, wt, capacity, 0)
        
        # memory = [[None]*(capacity+1) for _ in range(len(val)+1)]
        # return self.knapSackRecMemo(val, wt, capacity, 0, memory)
        
        return self.knapSackDP(val, wt, capacity)
        
    
    def knapSackRec(self, val, wt, capacity, index):
        if capacity == 0:
            return 0
        if index == len(wt):
            return 0
        maxProfit = 0
        withCurrent = 0
        if capacity - wt[index] >= 0:
            withCurrentAndContinue = val[index] + self.knapSackRec(val, wt, capacity - wt[index], index+1)
            withCurrentAndStay = val[index] + self.knapSackRec(val, wt, capacity - wt[index], index)
            maxProfit = max(withCurrentAndContinue, withCurrentAndStay)
        withoutCurrentAndContinue = self.knapSackRec(val, wt, capacity, index+1)
        maxProfit = max(maxProfit, withoutCurrentAndContinue)
        return maxProfit
        
    def knapSackRecMemo(self, val, wt, capacity, index, memory):
        if capacity == 0:
            return 0
        if index == len(wt):
            return 0
        if memory[index][capacity] != None:
            return memory[index][capacity]
        maxProfit = 0
        withCurrent = 0
        if capacity - wt[index] >= 0:
            withCurrentAndContinue = val[index] + self.knapSackRecMemo(val, wt, capacity - wt[index], index+1, memory)
            withCurrentAndStay = val[index] + self.knapSackRecMemo(val, wt, capacity - wt[index], index, memory)
            maxProfit = max(withCurrentAndContinue, withCurrentAndStay)
        withoutCurrentAndContinue = self.knapSackRecMemo(val, wt, capacity, index+1, memory)
        maxProfit = max(maxProfit, withoutCurrentAndContinue)
        memory[index][capacity] = maxProfit
        return memory[index][capacity]
        
    def knapSackDP(self, val, wt, Capacity):
        memory = [[None]*(Capacity+1) for _ in range(len(val)+1)]
        
        for index in range(len(wt), -1, -1):
            for capacity in range(Capacity+1):
                if capacity == 0:
                    memory[index][capacity] = 0
                if index == len(wt):
                    memory[index][capacity] = 0
                else:
                    maxProfit = 0
                    withCurrent = 0
                    if capacity - wt[index] >= 0:
                        withCurrentAndContinue = val[index] + memory[index+1][capacity - wt[index]]
                        withCurrentAndStay = val[index] + memory[index][capacity - wt[index]]
                        maxProfit = max(withCurrentAndContinue, withCurrentAndStay)
                    withoutCurrentAndContinue = memory[index+1][capacity]
                    maxProfit = max(maxProfit, withoutCurrentAndContinue)
                    memory[index][capacity] = maxProfit
        
        return memory[0][Capacity]
        
