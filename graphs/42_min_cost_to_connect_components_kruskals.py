import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = self.getAdjList(points)
        return self.kruskal(adjList)
    
    def getAdjList(self, points):
        count = len(points)
        edges = [[] for _ in range(count)]
        for p1 in range(count):
            for p2 in range(p1, count):
                x1, y1 = points[p1]
                x2, y2 = points[p2]
                dist = abs(x1 - x2) + abs(y1 - y2)
                # print(f"{p1} {p2} {dist}")
                edges[p1].append([p2, dist])
                if p1 != p2:
                    edges[p2].append([p1, dist])
        return edges

    def kruskal(self, adjList):
        minHeap = []
        for i in range(len(adjList)):
            for j, w in adjList[i]:
                minHeap.append([w, i, j])
        heapq.heapify(minHeap)
        edgeCount = 0
        countSum = 0
        parents = [i for i in range(len(adjList))]
        ranks = [0] * len(adjList)
        while edgeCount + 1 < len(adjList):
            weight, point1, point2 = heapq.heappop(minHeap)
            parent1 = self.find(point1, parents)
            parent2 = self.find(point2, parents)
            if parent1 == parent2:
                continue
            edgeCount += 1
            countSum += weight
            self.union(point1, point2, parents, ranks)
        return countSum
    
    def union(self, point1, point2, parents, ranks):
        parent1 = self.find(point1, parents)
        parent2 = self.find(point2, parents)
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
    
    def find(self, point, parents):
        if point == parents[point]:
            return point
        parents[point] = self.find(parents[point], parents)
        return parents[point]
