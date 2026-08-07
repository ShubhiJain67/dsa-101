from typing import List
import math
class Solution:
    directions = [[0,1],[1,0]]
    def minPathSum(self, grid: List[List[int]]) -> int:
        # return self.minPath(grid, 0, 0)

        # memo = [[None]*len(grid[0]) for _ in range(len(grid))]
        # return self.minPathMemo(grid, 0, 0, memo)

        return self.minPathDP(grid)
    
    def minPath(self, grid, i, j):
        if i == len(grid)-1 and j == len(grid[0])-1:
            return grid[i][j]
        minPathLen = math.inf
        for dirc in self.directions:
            ni = i + dirc[0]
            nj = j + dirc[1]
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                minPathLen = min(minPathLen, grid[i][j] + self.minPath(grid, ni, nj))
        return minPathLen


    def minPathMemo(self, grid, i, j, memo):
        if memo[i][j] is not None:
            return memo[i][j]
        minPathLen = math.inf
        if i == len(grid)-1 and j == len(grid[0])-1:
            minPathLen = grid[i][j]
        else:
            for dirc in self.directions:
                ni = i + dirc[0]
                nj = j + dirc[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    minPathLen = min(minPathLen, grid[i][j] + self.minPathMemo(grid, ni, nj, memo))
        memo[i][j] = minPathLen
        return memo[i][j]

    def minPathDP(self, grid):
        memo = [[None]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                minPathLen = math.inf
                if i == len(grid)-1 and j == len(grid[0])-1:
                    minPathLen = grid[i][j]
                else:
                    for dirc in self.directions:
                        ni = i + dirc[0]
                        nj = j + dirc[1]
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            minPathLen = min(minPathLen, grid[i][j] + memo[ni][nj])
                memo[i][j] = minPathLen
        return memo[0][0]
