from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return self.combineRec(n, k)
        # return self.combineDP(n, k)
        return self.combineDPOptimised(n, k)
    
    def combineRec(self, n, k):
        if k == 0:
            return [[]]
        if n == 0:
            return []
        withoutCurr = self.combineRec(n-1, k)
        combinations = withoutCurr
        withCurr = self.combineRec(n-1, k-1)
        for curr in withCurr:
            combinations.append([n]+curr)
        # print(f"From n={n} k={k} combinations={combinations}")
        return combinations

    def combineDP(self, N, K):
        dp = [[None]*(K+1) for _ in range(N+1)]
        for n in range(0, N+1):
            for k in range(0, K+1):
                if k == 0:
                    combinations = [[]]
                elif n == 0:
                    combinations = []
                else:
                    combinations = []
                    withoutCurr = dp[n-1][k]
                    withCurr = dp[n-1][k-1]
                    for curr in withCurr:
                        combinations.append([n]+curr)
                    for curr in withoutCurr:
                        combinations.append(curr)
                dp[n][k] = combinations
        return dp[N][K]
    
    def combineDPOptimised(self, N, K):
        prevDP = [None]*(K+1)
        for n in range(0, N+1):
            currDP = [None]*(K+1)
            for k in range(0, K+1):
                if k == 0:
                    combinations = [[]]
                elif n == 0:
                    combinations = []
                else:
                    combinations = []
                    withoutCurr = prevDP[k]
                    withCurr = prevDP[k-1]
                    for curr in withCurr:
                        combinations.append([n]+curr)
                    for curr in withoutCurr:
                        combinations.append(curr)
                currDP[k] = combinations
            prevDP = currDP
        return currDP[K]

