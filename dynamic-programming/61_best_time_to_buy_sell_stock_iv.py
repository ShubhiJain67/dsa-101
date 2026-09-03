class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # return self.getMaxProfit(prices, 0, True, k)

        # memo = [[[None]*(k+1) for _ in range(2)] for _ in range(len(prices))]
        # return self.getMaxProfitMemo(prices, 0, True, memo, k)

        return self.getMaxProfitDP(prices, k)

    def getMaxProfit(self, prices, index, canBuy, transactions):
        if index >= len(prices):
            return 0
        if transactions == 0:
            return 0
        if canBuy:
            bought = -prices[index] + self.getMaxProfit(prices, index + 1, False, transactions)
            skippedBuying = self.getMaxProfit(prices, index + 1, True, transactions)
            return max(bought, skippedBuying)
        else:
            sold = prices[index] + self.getMaxProfit(prices, index + 1, True, transactions - 1)
            skippedSelling = self.getMaxProfit(prices, index + 1, False, transactions)
            return max(sold, skippedSelling)
        
    def getMaxProfitMemo(self, prices, index, canBuy, memo, transactions):
        if index >= len(prices):
            return 0
        if memo[index][int(canBuy)][transactions] is not None:
            return memo[index][int(canBuy)][transactions]
        if transactions == 0:
            return 0
        if canBuy:
            bought = -prices[index] + self.getMaxProfitMemo(prices, index + 1, False, memo, transactions)
            skippedBuying = self.getMaxProfitMemo(prices, index + 1, True, memo, transactions)
            memo[index][int(canBuy)][transactions] = max(bought, skippedBuying)
        else:
            sold = prices[index] + self.getMaxProfitMemo(prices, index + 1, True, memo, transactions - 1)
            skippedSelling = self.getMaxProfitMemo(prices, index + 1, False, memo, transactions)
            memo[index][int(canBuy)][transactions] = max(sold, skippedSelling)
        return memo[index][int(canBuy)][transactions]


    def getMaxProfitDP(self, prices,  transactions):
        memo = [[[0]*(transactions+1) for _ in range(2)] for _ in range(len(prices)+1)]
        for index in range(len(prices)-1, -1, -1):
            for canBuy in (True, False):
                for transaction in range(1, transactions+1):
                    if canBuy:
                        bought = -prices[index] + (memo[index + 1][int(False)][transaction] if index + 1 <= len(prices) else 0)
                        skippedBuying = (memo[index + 1][int(True)][transaction] if index + 1 <= len(prices) else 0)
                        memo[index][int(canBuy)][transaction] = max(bought, skippedBuying)
                    else:
                        sold = prices[index] + (memo[index + 1][int(True)][transaction-1] if index + 2 <= len(prices) else 0)
                        skippedSelling = (memo[index + 1][int(False)][transaction] if index + 1 <= len(prices) else 0)
                        memo[index][int(canBuy)][transaction] = max(sold, skippedSelling)
        return memo[0][int(True)][transactions]

