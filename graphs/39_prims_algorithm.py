import heapq
class Solution:
    def spanningTree(self, V, edges):
        adjList = [[] for _ in range(V)]
        for start, end, weight in edges:
            adjList[start].append([end, weight])
            adjList[end].append([start, weight])
        # code here
        minHeap = []
        heapq.heappush(minHeap, (0, 0, -1))
        vertextVisited = [False]*V
        parent = [None]*V
        edgeCount = V
        sumWeight = 0
        while edgeCount>0:
            weight, end, start = heapq.heappop(minHeap)
            if vertextVisited[end]:
                continue
            sumWeight += weight
            edgeCount -= 1
            vertextVisited[end] = True
            parent[end] = start
            for n, w in adjList[end]:
                if not vertextVisited[n]:
                    heapq.heappush(minHeap, (w, n, end))
                    
        return sumWeight
