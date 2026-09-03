class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.maxBruteForce(prices)
        return self.optimised(prices)

    def optimised(self, prices):
        maxProfit = 0

        profitFromEnd = [0]*len(prices)
        greaterOnRight = 0
        maxCurrProfit = 0
        for index in range(len(prices)-1, -1, -1):
            currProfit = max(0, greaterOnRight - prices[index])
            greaterOnRight = max(greaterOnRight, prices[index])
            maxCurrProfit = max(maxCurrProfit, currProfit)
            profitFromEnd[index] = maxCurrProfit

        profitFromStart = [0]*len(prices)
        leastOnLeft = math.inf
        maxCurrProfit = 0
        for index in range(len(prices)):
            currProfit = max(0, prices[index] - leastOnLeft)
            leastOnLeft = min(leastOnLeft, prices[index])
            maxCurrProfit = max(maxCurrProfit, currProfit)
            profitFromStart[index] = maxCurrProfit

        for partition in range(len(prices)):
            firstProfit = profitFromStart[partition]
            secondProfit = profitFromEnd[partition + 1] if partition + 1 < len(prices) else 0
            # print(f"{firstProfit} | {secondProfit}")
            maxProfit = max(maxProfit, firstProfit + secondProfit)
        return maxProfit
    
    def maxBruteForce(self, prices):
        maxProfit = 0
        for partition in range(len(prices)):
            firstProfit = self.maxProfitInRange(prices, 0, partition)
            secondProfit = self.maxProfitInRange(prices, partition + 1, len(prices)-1)
            # print(f"{firstProfit} | {secondProfit}")
            maxProfit = max(maxProfit, firstProfit + secondProfit)
        return maxProfit

    def maxProfitInRange(self, prices, start, end):
        greaterOnRight = 0
        maxProfit = 0
        for index in range(end, start-1, -1):
            currProfit = max(0, greaterOnRight - prices[index])
            greaterOnRight = max(greaterOnRight, prices[index])
            maxProfit = max(maxProfit, currProfit)
        return maxProfit
