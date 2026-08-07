class Solution:
    directions = [[0,1],[1,0]]
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # return self.minPath(grid, 0, 0)

        # memo = [[None]*len(grid[0]) for _ in range(len(grid))]
        # return self.minPathMemo(grid, 0, 0, memo)

        return self.minPathDP(grid)
    
    def minPath(self, grid, i, j):
        if grid[i][j] == 1:
            return 0
        if i == len(grid)-1 and j == len(grid[0])-1:
            return 1
        paths = 0
        for dirc in self.directions:
            ni = i + dirc[0]
            nj = j + dirc[1]
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                paths += self.minPath(grid, ni, nj)
        return paths


    def minPathMemo(self, grid, i, j, memo):
        if memo[i][j] is not None:
            return memo[i][j]
        paths = 0
        if grid[i][j] == 1:
            paths = 0
        elif i == len(grid)-1 and j == len(grid[0])-1:
            paths = 1
        else:
            for dirc in self.directions:
                ni = i + dirc[0]
                nj = j + dirc[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    paths += self.minPathMemo(grid, ni, nj, memo)
        memo[i][j] = paths
        return memo[i][j]

    def minPathDP(self, grid):
        memo = [[None]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                paths = 0
                if grid[i][j] == 1:
                    paths = 0
                elif i == len(grid)-1 and j == len(grid[0])-1:
                    paths = 1
                else:
                    for dirc in self.directions:
                        ni = i + dirc[0]
                        nj = j + dirc[1]
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            paths += self.minPathMemo(grid, ni, nj, memo)
                memo[i][j] = paths
        return memo[0][0]
