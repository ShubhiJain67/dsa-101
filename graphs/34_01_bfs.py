from collections import deque

class Solution:
    def bfs01(self, V, edges, targetSource):
        adj = self.getAdjList(V, edges)
        minDist = [float("inf")] * V
        
        minDist[targetSource] = 0
        que = deque([(0, targetSource)])
        
        while len(que) != 0:
            weight, currNode = que.popleft()
            if weight > minDist[currNode]:
                continue
            for n, w in adj[currNode]:
                if weight + w < minDist[n]:
                    minDist[n] = weight + w
                    if w == 0:
                        que.appendleft((weight + w, n))
                    else:
                        que.append((weight + w, n))
                        
        return minDist

        
    # returns list of [node, wieght] for every node
    def getAdjList(self, V, edges):
        adj = [[] for i in range(V)]
        for source, dest, weight in edges:
            adj[dest].append([source, weight])
            adj[source].append([dest, weight])
        return adj
