from typing import List

class Solution:
    directions = [
        (-1, 0),
        (0, -1), (0, 1),
        (1, 0)
    ]

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        bestHealth = [[-1] * n for _ in range(m)]
        return self.dfs(grid, 0, 0, health, bestHealth)

    def dfs(self, grid, r, c, health, bestHealth):
        m, n = len(grid), len(grid[0])
        if not (0 <= r < m and 0 <= c < n):
            return False
        health -= grid[r][c]
        if health <= 0:
            return False
        # "I've already reached this cell before with equal or more remaining health. 
        # So exploring from here again cannot produce a better answer."
        if bestHealth[r][c] >= health:
            return False

        bestHealth[r][c] = health
        if r == m - 1 and c == n - 1:
            return True

        for dr, dc in self.directions:
            if self.dfs(grid, r + dr, c + dc, health, bestHealth):
                return True

        return False
