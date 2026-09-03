class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # return self.getMaxProfit(prices, fee, 0, True)

        # memo = [[None, None] for _ in range(len(prices))]
        # return self.getMaxProfitMemo(prices, fee, 0, True, memo)

        return self.getMaxProfitDP(prices, fee)


    def getMaxProfit(self, prices, fee, index, canBuy):
        if index >= len(prices):
            return 0
        if canBuy:
            bought = -prices[index] + self.getMaxProfit(prices, fee, index + 1, False)
            skippedBuying = self.getMaxProfit(prices, fee, index + 1, True)
            return max(bought, skippedBuying)
        else:
            sold = prices[index]-fee + self.getMaxProfit(prices, fee, index + 1, True)
            skippedSelling = self.getMaxProfit(prices, fee, index + 1, False)
            return max(sold, skippedSelling)

    def getMaxProfitMemo(self, prices, fee, index, canBuy, memo):
        if index >= len(prices):
            return 0
        if memo[index][int(canBuy)] is not None:
            return memo[index][int(canBuy)]
        if canBuy:
            bought = -prices[index] + self.getMaxProfitMemo(prices, fee, index + 1, False, memo)
            skippedBuying = self.getMaxProfitMemo(prices, fee, index + 1, True, memo)
            memo[index][int(canBuy)] = max(bought, skippedBuying)
        else:
            sold = prices[index]-fee + self.getMaxProfitMemo(prices, fee, index + 1, True, memo)
            skippedSelling = self.getMaxProfitMemo(prices, fee, index + 1, False, memo)
            memo[index][int(canBuy)] = max(sold, skippedSelling)
        return memo[index][int(canBuy)]

    def getMaxProfitDP(self, prices, fee):
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
                    sold = prices[index] - fee + (memo[index + 1][int(True)] if index + 1 <= len(prices) else 0)
                    skippedSelling = (memo[index + 1][int(False)] if index + 1 <= len(prices) else 0)
                    memo[index][int(canBuy)] = max(sold, skippedSelling)
        return memo[0][int(True)]
