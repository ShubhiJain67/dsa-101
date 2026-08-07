from typing import List
import math
class Solution:
    stepDist = [1,2]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # minCost = self.minCostRec(cost, -1)

        # memo = [None]*len(cost)
        # minCost = self.minCostRecMemo(cost, -1, memo)

        # minCost = self.minCostDP(cost)

        minCost = self.minCostDPOptimised(cost)

        return minCost
        
    def minCostRec(self, cost, index):
        if index == len(cost):
            return 0
        minCost = math.inf
        for step in self.stepDist:
            if index + step <= len(cost):
                furtherCost = self.minCostRec(cost, index+step)
                totalCost = furtherCost
                if index >= 0:
                    totalCost += cost[index]
                minCost = min(minCost, totalCost)
        return minCost
    
    def minCostRecMemo(self, cost, index, memo):
        if index == len(cost):
            return 0
        if memo[index] is not None:
            return memo[index]
        minCost = math.inf
        for step in self.stepDist:
            if index + step <= len(cost):
                furtherCost = self.minCostRecMemo(cost, index+step, memo)
                totalCost = furtherCost
                if index >= 0:
                    totalCost += cost[index]
                minCost = min(minCost, totalCost)
        if index >= 0:
            memo[index] = minCost
        return minCost

    def minCostDP(self, cost):
        memo = [None]*(len(cost)+1)
        for index in range(len(cost), -1, -1):
            minCost = math.inf
            if index == len(cost):
                minCost = 0
            else:
                for step in self.stepDist:
                    if index + step <= len(cost):
                        furtherCost = memo[index+step]
                        totalCost = furtherCost
                        if index >= 0:
                            totalCost += cost[index]
                        minCost = min(minCost, totalCost)
            memo[index] = minCost
        return min(memo[0], memo[1])

    def minCostDPOptimised(self, cost):
        memo = [0]*(len(self.stepDist))
        for index in range(len(cost), -1, -1):
            minCost = math.inf
            if index == len(cost):
                minCost = 0
            else:
                for step in self.stepDist:
                    if index + step <= len(cost):
                        furtherCost = memo[step-1]
                        totalCost = furtherCost
                        if index >= 0:
                            totalCost += cost[index]
                        minCost = min(minCost, totalCost)
            for i in range(len(self.stepDist)-1, 0, -1):
                memo[i] = memo[i-1]
            memo[0] = minCost
        return min(memo[0], memo[1])
        
