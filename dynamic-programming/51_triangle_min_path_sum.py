from typing import List
import math
class Solution:
    directions = [[1, 0], [1, 1]]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # return self.minTotal(triangle, 0, 0)

        # memo = [[None]*len(triangle[i]) for i in range(len(triangle))]
        # return self.minTotalMemo(triangle, 0, 0, memo)

        return self.minTotalDP(triangle)
        
    def minTotal(self, triangle, i, j):
        if i == len(triangle) - 1:
            return triangle[i][j]
        minPath = math.inf
        for dirc in self.directions:
            ni = i + dirc[0]
            nj = j + dirc[1]
            if 0 <= ni < len(triangle) and 0 <= nj < len(triangle[ni]):
                minPath = min(minPath, triangle[i][j] + self.minTotal(triangle, ni, nj))
        return minPath
    
    def minTotalMemo(self, triangle, i, j, memo):
        if memo[i][j] is not None:
            return memo[i][j]
        minPath = math.inf
        if i == len(triangle) - 1:
            minPath = triangle[i][j]
        else:
            for dirc in self.directions:
                ni = i + dirc[0]
                nj = j + dirc[1]
                if 0 <= ni < len(triangle) and 0 <= nj < len(triangle[ni]):
                    minPath = min(minPath, triangle[i][j] + self.minTotalMemo(triangle, ni, nj, memo))
        memo[i][j] = minPath
        return memo[i][j]

    
    def minTotalDP(self, triangle):
        memo = [[None]*len(triangle[i]) for i in range(len(triangle))]
        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])-1, -1, -1):
                minPath = math.inf
                if i == len(triangle) - 1:
                    minPath = triangle[i][j]
                else:
                    for dirc in self.directions:
                        ni = i + dirc[0]
                        nj = j + dirc[1]
                        if 0 <= ni < len(triangle) and 0 <= nj < len(triangle[ni]):
                            minPath = min(minPath, triangle[i][j] + memo[ni][nj])
                memo[i][j] = minPath
        return memo[0][0]
