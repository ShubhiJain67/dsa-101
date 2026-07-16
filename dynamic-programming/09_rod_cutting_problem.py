class Solution:
    def cutRod(self, price):
        # return self.cutRodRec(price, len(price), 0)
        
        # memory = [[None]*(len(price)+1) for _ in range(len(price)+1)]
        # return self.cutRodRecMemo(price, len(price), 0, memory)
        
        return self.cutRodDP(price)
        
    
    def cutRodRec(self, price, length, index):
        if length == 0:
            return 0
        if index == len(price):
            return 0
        maxValue = 0
        if length - (index + 1) >= 0:
            withCurrentAndStay = price[index] + self.cutRodRec(price, length-(index+1), index)
            maxValue = max(maxValue, withCurrentAndStay)
        withoutCurrentAndContinue = self.cutRodRec(price, length, index+1)
        maxValue = max(maxValue, withoutCurrentAndContinue)
        return maxValue
        
    def cutRodRecMemo(self, price, length, index, memory):
        if length == 0:
            return 0
        if index == len(price):
            return 0
        if memory[length][index] != None:
            return memory[length][index]
        maxValue = 0
        if length - (index + 1) >= 0:
            withCurrentAndStay = price[index] + self.cutRodRecMemo(price, length-(index+1), index, memory)
            maxValue = max(maxValue, withCurrentAndStay)
        withoutCurrentAndContinue = self.cutRodRecMemo(price, length, index+1, memory)
        maxValue = max(maxValue, withoutCurrentAndContinue)
        memory[length][index] = maxValue
        return memory[length][index]
        
    def cutRodDP(self, price):
        memory = [[None]*(len(price)+1) for _ in range(len(price)+1)]
        for index in range(len(price), -1, -1):
            for length in range(len(price)+1):
                if length == 0:
                    memory[length][index] = 0
                elif index == len(price):
                    memory[length][index] = 0
                else:
                    maxValue = 0
                    if length - (index + 1) >= 0:
                        withCurrentAndStay = price[index] + memory[length-(index+1)][index]
                        maxValue = max(maxValue, withCurrentAndStay)
                    withoutCurrentAndContinue = memory[length][index+1]
                    maxValue = max(maxValue, withoutCurrentAndContinue)
                    memory[length][index] = maxValue
        return memory[len(price)][0]
                
        
            
