from typing import List
import heapq
class Solution:
    def spanningTree(self, V, edges):
        adjList = self.getAdjList(V, edges)
        minHeap = [[edge[2], edge[0], edge[1]] for edge in edges]
        heapq.heapify(minHeap)

        nodesVisited = [False]*V
        edgeCount = 0
        parents = [i for i in range(V)]
        ranks = [0]*V
        sumCount = 0
        
        while edgeCount + 1 < V:
            weight, source, dest = heapq.heappop(minHeap)
            sourceParent = self.find(source, parents)
            destParent = self.find(dest, parents)
            if sourceParent == destParent:
                continue
            edgeCount += 1
            sumCount += weight
            self.union(source, dest, parents, ranks)
        return sumCount
    
    def getAdjList(self, V, edges):
        adjList = [[] for _ in range(V)]
        for edge in edges:
            adjList[edge[0]].append([edge[1], edge[2]])
            adjList[edge[1]].append([edge[0], edge[2]])
    
    def union(self, node1, node2, parents, ranks):
        parent1 = self.find(node1, parents)
        parent2 = self.find(node2, parents)
        if parent1 == parent2:
            return
        rank1 = ranks[parent1]
        rank2 = ranks[parent2]
        if rank1 == rank2:
            parents[parent1] = parent2
            ranks[parent2] += 1
        elif rank1 > rank2:
            parents[parent2] = parent1
        else:
            parents[parent1] = parent2
            
    def find(self, node, parents):
        if node == parents[node]:
            return node
        parents[node] = self.find(parents[node], parents)
        return parents[node]
