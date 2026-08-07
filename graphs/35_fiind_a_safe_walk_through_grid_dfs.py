from typing import List
class Solution:
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # visited = [[False]*(len(grid[0])) for _ in range(len(grid))]
        # return self.walkDFS(grid, health-grid[0][0], 0, 0, len(grid)-1, len(grid[0])-1, visited)
        bestHealth = [[-1]*(len(grid[0])) for _ in range(len(grid))]
        return self.walkDFSMemo(grid, health-grid[0][0], 0, 0, len(grid)-1, len(grid[0])-1, bestHealth)
        
    # This traverses same path again and again hence Time Limit Exceeds
    def walkDFS(self, grid: List[List[int]], health: int, sourceI: int, sourceJ: int, taregtI: int, targetJ: int, visited: List[List[bool]]) -> bool:
        if sourceI == taregtI and sourceJ == targetJ and health >= 1:
            return True
        if health < 1:
            return False
        if visited[sourceI][sourceJ]:
            return False
        visited[sourceI][sourceJ] = True
        for di, dj in self.directions:
            ni = sourceI + di
            nj = sourceJ + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] < health:
                if self.walkDFS(grid, health-grid[ni][nj], ni, nj, taregtI, targetJ, visited):
                    return True
        visited[sourceI][sourceJ] = False
        return False
    
    def walkDFSMemo(self, grid: List[List[int]], health: int, sourceI: int, sourceJ: int, targetI: int, targetJ: int, bestHealth: List[List[int]]) -> bool:
            if sourceI == targetI and sourceJ == targetJ and health >= 1:
                return True
            if health < 1:
                return False
            if bestHealth[sourceI][sourceJ] >= health:
                return False
            bestHealth[sourceI][sourceJ] = health
            for di, dj in self.directions:
                ni = sourceI + di
                nj = sourceJ + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if self.walkDFSMemo(grid, health - grid[ni][nj], ni, nj, targetI, targetJ, bestHealth):
                        return True
            return False
