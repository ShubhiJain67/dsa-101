class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # return self.changeRec(amount, coins, 0)

        # memory = [[None]*(len(coins)+1) for _ in range(amount+1)]
        # return self.changeRecMemo(amount, coins, 0, memory)

        return self.changeDP(amount, coins)
    
    def changeRec(self, amount, coins, index):
        if amount == 0:
            return 1
        if index == len(coins):
            return 1 if amount == 0 else 0
        noOfWays = 0
        if amount - coins[index] >= 0:
            withCurrentAndStay = self.changeRec(amount - coins[index], coins, index)
            noOfWays = noOfWays + withCurrentAndStay
        withoutCurrentAndContinue = self.changeRec(amount, coins, index+1)
        noOfWays = noOfWays + withoutCurrentAndContinue
        return noOfWays

    def changeRecMemo(self, amount, coins, index, memory):
        if amount == 0:
            return 1
        if index == len(coins):
            return 1 if amount == 0 else 0
        if memory[amount][index] != None:
            return memory[amount][index]
        noOfWays = 0
        if amount - coins[index] >= 0:
            withCurrentAndStay = self.changeRecMemo(amount - coins[index], coins, index, memory)
            noOfWays = withCurrentAndStay
        withoutCurrentAndContinue = self.changeRecMemo(amount, coins, index+1, memory)
        noOfWays = noOfWays + withoutCurrentAndContinue
        memory[amount][index] = noOfWays
        return noOfWays

    def changeDP(self, Amount, coins):
        memory = [[None]*(len(coins)+1) for _ in range(Amount+1)]
        for index in range(len(coins), -1, -1):
            for amount in range(Amount+1):
                if amount == 0:
                    memory[amount][index] = 1
                elif index == len(coins):
                    memory[amount][index] = 1 if amount == 0 else 0
                else:
                    noOfWays = 0
                    if amount - coins[index] >= 0:
                        withCurrentAndStay = memory[amount - coins[index]][index]
                        noOfWays = withCurrentAndStay
                    withoutCurrentAndContinue = memory[amount][index+1]
                    noOfWays = noOfWays + withoutCurrentAndContinue
                    memory[amount][index] = noOfWays
        return memory[Amount][0]

