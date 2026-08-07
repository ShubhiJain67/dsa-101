from typing import List
import math
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        adj = self.getAdjList(heights)
        n = len(heights)
        m = len(heights[0])
        return self.minimumEffort(adj, [0,0], n,m, [n-1, n-1])

    def minimumEffort(self, adj, source, n,m, dest):
        minEffort = [[math.inf]*m for _ in range(n)]
        minHeap = []
        heapq.heappush(minHeap, (0, source))
        minEffort[source[0]][source[1]] = 0
        while minHeap:
            effort, node = heapq.heappop(minHeap)
            if effort > minEffort[node[0]][node[1]]:
                continue
            for neigh, neighEffort in adj[node[0]][node[1]]:
                newEffort = neighEffort if neighEffort > effort else effort
                if newEffort < minEffort[neigh[0]][neigh[1]]:
                    minEffort[neigh[0]][neigh[1]] = newEffort
                    heapq.heappush(minHeap, (newEffort, neigh))
        if minEffort[dest[0]][dest[1]] == math.inf:
            return -1
        return minEffort[dest[0]][dest[1]]

    
    def getAdjList(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        adj = [[[] for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                directions = [
                            [-1, 0],
                    [0, -1],        [0, +1],
                            [+1, 0]
                ]
                for dirI, dirJ in directions:
                    newI = i + dirI
                    newJ = j + dirJ

                    if 0 <= newI < n and 0 <= newJ < n:
                        weight = heights[i][j] - heights[newI][newJ]
                        if weight < 0:
                            weight = weight * -1
                        adj[i][j].append([[newI, newJ], weight])
        return adj
