from typing import List
import math
import heapq
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        adj = self.getAdjList(n, grid)
        return self.getMinPaths(adj, n, [0,0], [n-1, n-1])
        
    
    def getMinPaths(self, adj, n, source, dest):
        visited = [[False] * n for _ in range(n)]
        visited[source[0]][source[1]] = True

        que = deque([(source, 1)])

        while que:
            node, pathLen = que.popleft()
            if node == dest:
                return pathLen

            for neigh in adj[node[0]][node[1]]:
                if not visited[neigh[0]][neigh[1]]:
                    visited[neigh[0]][neigh[1]] = True
                    que.append((neigh, pathLen + 1))

        return -1
 

    def getAdjList(self, n, grid):
        adj = [[[] for _ in range(n)] for _ in range(n)]
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        for i in range(n):
            for j in range(n):
                # Skip blocked cells
                if grid[i][j] == 1:
                    continue

                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        adj[i][j].append([nr, nc])

        return adj
