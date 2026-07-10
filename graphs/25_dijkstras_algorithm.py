import heapq

class Solution:
    def dijkstra(self, V, edges, targetSource):
        adj = self.getAdjList(V, edges)
        minHeap = []
        minDist = [float("inf")] * V
        
        minDist[targetSource] = 0
        heapq.heappush(minHeap, (0, targetSource))
        
        while len(minHeap) != 0:
            weight, currNode = heapq.heappop(minHeap)
            # This Ensures that if an alternate path was updated the end to this one then it is not visited again
            # Without this also works but too much extra processing TIMEWASTE
            # Without this might exceed time constraint
            if weight > minDist[currNode]:
                continue
            for n, w in adj[currNode]:
                if weight + w < minDist[n]:
                    minDist[n] = weight + w
                    heapq.heappush(minHeap, (weight + w, n))
        return minDist

        
    # returns list of [node, wieght] for every node
    def getAdjList(self, V, edges):
        adj = [[] for i in range(V)]
        for source, dest, weight in edges:
            adj[dest].append([source, weight])
            adj[source].append([dest, weight])
        return adj
