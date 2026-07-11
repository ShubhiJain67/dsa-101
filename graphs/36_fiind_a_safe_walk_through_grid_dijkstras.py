class Solution:
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        return self.walkDijakstras(grid, health, 0, 0, len(grid)-1, len(grid[0])-1)
    
    def walkDijakstras(self, grid: List[List[int]], health: int, sourceI: int, sourceJ: int, targetI: int, targetJ: int) -> bool:
        minHeap = []
        bestHealth = [[math.inf]*(len(grid[0])) for _ in range(len(grid))]

        heapq.heappush(minHeap, (grid[sourceI][sourceJ], (sourceI,sourceJ)))
        bestHealth[sourceI][sourceJ] = grid[sourceI][sourceJ]
        while minHeap:
            # print(minHeap)
            currHealth, (currI, currJ) = heapq.heappop(minHeap)
            if currHealth > bestHealth[currI][currJ]:
                continue
            for di, dj in self.directions:
                ni = currI + di
                nj = currJ + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    newHealth = currHealth + grid[ni][nj]
                    # print(f"Comparing {newHealth} {bestHealth[ni][nj]}")
                    if newHealth < bestHealth[ni][nj]:
                        bestHealth[ni][nj] = newHealth
                        heapq.heappush(minHeap, (bestHealth[ni][nj], (ni, nj)))
        # print(bestHealth)
        # print(bestHealth[targetI][targetJ])
        # print(health)
        return bestHealth[targetI][targetJ] < health
