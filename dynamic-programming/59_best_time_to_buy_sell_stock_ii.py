class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.maxProfRec(prices, 0)

        # memo = [None]*(len(prices)+1)
        # return self.maxProfMemo(prices, 0, memo)

        # return self.maxProfDP(prices)

        return self.maxProfDPV2(prices)
    
    def maxProfRec(self, prices, index):
        if index >= len(prices) - 1:
            return 0
        profit = 0
        stock = prices[index]
        for i in range(index+1, len(prices)):
            if prices[i]>stock:
                # print(f"Bought on {index} and sold on {i}")
                profit = max(profit, prices[i]-stock+self.maxProfRec(prices, i+1))
        profit = max(profit, self.maxProfRec(prices, index+1))
        return profit

    def maxProfMemo(self, prices, index, memo):
        if memo[index] is not None:
            return memo[index]
        profit = 0
        if index >= len(prices) - 1:
            profit = 0
        else:
            stock = prices[index]
            for i in range(index+1, len(prices)):
                if prices[i]>stock:
                    # print(f"Bought on {index} and sold on {i}")
                    profit = max(profit, prices[i]-stock+self.maxProfMemo(prices, i+1, memo))
            profit = max(profit, self.maxProfMemo(prices, index+1, memo))
        memo[index] = profit
        return memo[index]

    def maxProfDP(self, prices):
        memo = [None]*(len(prices)+1)
        for index in range(len(prices), -1, -1):
            profit = 0
            if index >= len(prices) - 1:
                profit = 0
            else:
                stock = prices[index]
                for i in range(index+1, len(prices)):
                    if prices[i]>stock:
                        # print(f"Bought on {index} and sold on {i}")
                        profit = max(profit, prices[i]-stock+memo[i+1])
                profit = max(profit, memo[index+1])
            memo[index] = profit
        return memo[0]

    def maxProfDPV2(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
