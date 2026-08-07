from collections import deque
import math
from typing import List
class Solution:
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        return self.walk01BFS(grid, health, 0, 0, len(grid)-1, len(grid[0])-1)
  
    def walk01BFS(self, grid: List[List[int]], health: int, sourceI: int, sourceJ: int, targetI: int, targetJ: int) -> bool:
        que = deque()
        bestHealth = [[math.inf]*(len(grid[0])) for _ in range(len(grid))]
        que.append((grid[sourceI][sourceJ], (sourceI,sourceJ)))
        bestHealth[sourceI][sourceJ] = grid[sourceI][sourceJ]
        while que:
            currHealth, (currI, currJ) = que.popleft()
            if currHealth > bestHealth[currI][currJ]:
                continue
            for di, dj in self.directions:
                ni = currI + di
                nj = currJ + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    newHealth = currHealth + grid[ni][nj]
                    if newHealth < bestHealth[ni][nj]:
                        bestHealth[ni][nj] = newHealth
                        if newHealth > 0:
                            que.append((bestHealth[ni][nj], (ni, nj)))
                        else:
                            que.appendleft((bestHealth[ni][nj], (ni, nj)))
        return bestHealth[targetI][targetJ] < health
