import math
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = self.getAdjList(times, n)
        allMinTimes = self.getAllMinTimes(n, adj, k)
        minTime = -1
        for node in range(1, len(allMinTimes)):
            time = allMinTimes[node]
            if time == math.inf and node != k:
                return -1
            elif minTime < time:
                minTime = time
        return minTime

    def getAdjList(self, times, n):
        adj = [[] for _ in range(n+1)]
        for src, dest, time in times:
            adj[src].append([dest, time])
        return adj
    
    def getAllMinTimes(self, n, adj, src):
        minTimes = [math.inf] * (n+1)
        minHeap = []

        minTimes[src] = 0
        heapq.heappush(minHeap, (0, src))

        while minHeap:
            currTime, currNode = heapq.heappop(minHeap)
            if currTime > minTimes[currNode]:
                continue
            for neigh, time in adj[currNode]:
                newTime = time + currTime
                if newTime < minTimes[neigh]:
                    minTimes[neigh] = newTime
                    heapq.heappush(minHeap, (newTime, neigh))
        return minTimes
