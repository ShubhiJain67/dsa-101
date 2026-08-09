class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRight = prices[-1]
        maxProfit = 0
        for i in range(len(prices)-2, -1, -1):
            maxProfit = max(maxProfit, maxRight-prices[i])
            maxRight = max(maxRight, prices[i])
        return maxProfit
