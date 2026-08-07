from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return list(self.getParRec(n))
        # return list(self.getParDP(n))
        return list(self.getParIter(n))
    
    def getParRec(self, n):
        if n == 0:
            return set([""])
        combinations = set()
        restCombinations = self.getParRec(n-1)
        for comb in restCombinations:
            for i in range(len(comb)+1):
                newPar = comb[:i]+"()"+comb[i:]
                combinations.add(newPar)
        return combinations
    
    def getParDP(self, N):
        dp = [None]*(N+1)
        for n in range(N+1):
            if n == 0:
                combinations = set([""])
            else:
                combinations = set()
                restCombinations = dp[n-1]
                for comb in restCombinations:
                    for i in range(len(comb)+1):
                        newPar = comb[:i]+"()"+comb[i:]
                        combinations.add(newPar)
            dp[n] = combinations
        return dp[N]
    
    def getParIter(self, N):
        totalCombinations = []
        for n in range(N+1):
            if n == 0:
                combinations = set([""])
            else:
                combinations = set()
                for comb in totalCombinations:
                    for i in range(len(comb)+1):
                        newPar = comb[:i]+"()"+comb[i:]
                        combinations.add(newPar)
            totalCombinations = combinations
        return totalCombinations
