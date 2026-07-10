from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [
                    [-1, 0],
            [0, -1],        [0, +1],
                    [+1, 0]
        ]
        freshOrangesCount = 0
        rottenOranges = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottenOranges.append([i,j])
                elif grid[i][j] == 1:
                    freshOrangesCount += 1
        if freshOrangesCount == 0:
            return 0
        level = 0
        currLevelCount = len(rottenOranges)
        levelAffected = False
        while rottenOranges:
            r, c = rottenOranges.popleft()
            currLevelCount -= 1
            for dr, dc in directions:
                nr = dr + r
                nc = dc +c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    rottenOranges.append([nr,nc])
                    grid[nr][nc] = 2
                    freshOrangesCount -= 1
                    levelAffected = True
            if currLevelCount == 0 and levelAffected:
                currLevelCount = len(rottenOranges)
                level += 1
                levelAffected = False
        return level if freshOrangesCount == 0 else -1
