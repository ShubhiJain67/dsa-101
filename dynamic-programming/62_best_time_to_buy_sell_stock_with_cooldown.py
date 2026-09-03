class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.getMaxProfit(prices, 0, True)

        # memo = [[None, None] for _ in range(len(prices))]
        # return self.getMaxProfitMemo(prices, 0, True, memo)

        return self.getMaxProfitDP(prices)

    def getMaxProfit(self, prices, index, canBuy):
        if index >= len(prices):
            return 0
        if canBuy:
            bought = -prices[index] + self.getMaxProfit(prices, index + 1, False)
            skippedBuying = self.getMaxProfit(prices, index + 1, True)
            return max(bought, skippedBuying)
        else:
            sold = prices[index] + self.getMaxProfit(prices, index + 2, True)
            skippedSelling = self.getMaxProfit(prices, index + 1, False)
            return max(sold, skippedSelling)
        
    def getMaxProfitMemo(self, prices, index, canBuy, memo):
        if index >= len(prices):
            return 0
        if memo[index][int(canBuy)] is not None:
            return memo[index][int(canBuy)]
        if canBuy:
            bought = -prices[index] + self.getMaxProfitMemo(prices, index + 1, False, memo)
            skippedBuying = self.getMaxProfitMemo(prices, index + 1, True, memo)
            memo[index][int(canBuy)] = max(bought, skippedBuying)
        else:
            sold = prices[index] + self.getMaxProfitMemo(prices, index + 2, True, memo)
            skippedSelling = self.getMaxProfitMemo(prices, index + 1, False, memo)
            memo[index][int(canBuy)] = max(sold, skippedSelling)
        return memo[index][int(canBuy)]

    def getMaxProfitDP(self, prices):
        memo = [[None, None] for _ in range(len(prices)+1)]
        for index in range(len(prices), -1, -1):
            for canBuy in (True, False):
                if index == len(prices):
                    memo[index][int(canBuy)] = 0
                elif canBuy:
                    bought = -prices[index] + (memo[index + 1][int(False)] if index + 1 <= len(prices) else 0)
                    skippedBuying = (memo[index + 1][int(True)] if index + 1 <= len(prices) else 0)
                    memo[index][int(canBuy)] = max(bought, skippedBuying)
                else:
                    sold = prices[index] + (memo[index + 2][int(True)] if index + 2 <= len(prices) else 0)
                    skippedSelling = (memo[index + 1][int(False)] if index + 1 <= len(prices) else 0)
                    memo[index][int(canBuy)] = max(sold, skippedSelling)
        return memo[0][int(True)]

