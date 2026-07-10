import heapq
import math

class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = self.getAdjList(V, edges)
        bestPath, minDist = self.getAllShortestPathsFromSrc(V, adj, src)

        if minDist[dest] == math.inf:
            return [-1]

        return list(bestPath[dest])

    def getAllShortestPathsFromSrc(self, V, adj, src):
        minHeap = []

        minDist = [math.inf] * (V + 1)
        bestPath = [None] * (V + 1)

        minDist[src] = 0
        bestPath[src] = (src,)

        heapq.heappush(minHeap, (0, (src,), src))

        while minHeap:
            dist, path, node = heapq.heappop(minHeap)

            if dist > minDist[node]:
                continue

            if dist == minDist[node] and path != bestPath[node]:
                continue

            for nei, wt in adj[node]:
                newDist = dist + wt
                newPath = path + (nei,)

                if newDist < minDist[nei]:
                    minDist[nei] = newDist
                    bestPath[nei] = newPath
                    heapq.heappush(minHeap, (newDist, newPath, nei))

                elif newDist == minDist[nei] and newPath < bestPath[nei]:
                    bestPath[nei] = newPath
                    heapq.heappush(minHeap, (newDist, newPath, nei))

        return bestPath, minDist

    def getAdjList(self, V, edges):
        adj = [[] for _ in range(V + 1)]

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        for neighbours in adj:
            neighbours.sort()

        return adj
