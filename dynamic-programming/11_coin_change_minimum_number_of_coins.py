from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # count, include = self.minCoinChangeRec(coins, amount, 0)
        # return count if include else -1

        # memory = [[None]*(len(coins)+1) for _ in range(amount+1)]
        # count, include = self.minCoinChangeRecMemo(coins, amount, 0, memory)
        # return count if include else -1

        return self.minCoinChangeDP(coins, amount)
    
    def minCoinChangeRec(self, coins, amount, index):
        if amount == 0:
            return 0, True
        elif index == len(coins):
            return 0, amount == 0
        minCount = math.inf
        if amount - coins[index] >= 0:
            withAndStay, include = self.minCoinChangeRec(coins, amount - coins[index], index)
            if include:
                minCount = min(minCount, withAndStay+1)
        withoutAndContinue, include = self.minCoinChangeRec(coins, amount, index+1)
        if include:
            minCount = min(minCount, withoutAndContinue)
        return minCount, minCount != math.inf

    def minCoinChangeRecMemo(self, coins, amount, index, memory):
        if amount == 0:
            return 0, True
        elif index == len(coins):
            return 0, amount == 0
        if memory[amount][index] != None:
            return memory[amount][index]
        minCount = math.inf
        if amount - coins[index] >= 0:
            withAndStay, include = self.minCoinChangeRecMemo(coins, amount - coins[index], index, memory)
            if include:
                minCount = min(minCount, withAndStay+1)
        withoutAndContinue, include = self.minCoinChangeRecMemo(coins, amount, index+1, memory)
        if include:
            minCount = min(minCount, withoutAndContinue)
        memory[amount][index] = (minCount, minCount != math.inf)
        return memory[amount][index]

    def minCoinChangeDP(self, coins, Amount):
        memory = [[None]*(len(coins)+1) for _ in range(Amount+1)]

        for amount in range(Amount+1):
            for index in range(len(coins), -1, -1):
                if amount == 0:
                    memory[amount][index] =  (0, True)
                elif index == len(coins):
                    memory[amount][index] =  (0, amount == 0)
                else:
                    minCount = math.inf
                    if amount - coins[index] >= 0:
                        withAndStay, include = memory[amount - coins[index]][index]
                        if include:
                            minCount = min(minCount, withAndStay+1)
                    withoutAndContinue, include = memory[amount][index+1]
                    if include:
                        minCount = min(minCount, withoutAndContinue)
                    memory[amount][index] = (minCount, minCount != math.inf)
        count, include = memory[Amount][0]
        return count if include else -1
