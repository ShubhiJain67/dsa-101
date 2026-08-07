from typing import List
import math
import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        adj = self.getAdjList(n, grid)
        source = self.getNodeId(0, 0, n)
        dest = self.getNodeId(n-1, n-1, n)
        minPaths = self.getMinPaths(adj, n, source)
        if minPaths[dest] == math.inf:
            return -1
        return  minPaths[dest]

    def getMinPaths(self, adj, n, source):
        minPaths = [math.inf]*(n*n)
        minHeap = []

        heapq.heappush(minHeap, (1, source))
        minPaths[source] = 1

        while minHeap:
            pathLength, currNode = heapq.heappop(minHeap)
            if pathLength > minPaths[currNode]:
                continue
            for neigh in adj[currNode]:
                if pathLength + 1 < minPaths[neigh]:
                    minPaths[neigh] = pathLength + 1
                    heapq.heappush(minHeap, (pathLength + 1, neigh))

        return minPaths

    def getAdjList(self, n, grid):
        adj = [[] for _ in range(n * n)]
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

                currNode = self.getNodeId(i, j, n)

                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        neighbour = self.getNodeId(nr, nc, n)
                        adj[currNode].append(neighbour)

        return adj
    
    def getNodeId(self, row, col, n):
        return (row)*n+col
