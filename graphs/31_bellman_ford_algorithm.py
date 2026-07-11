import math
class Solution:
    def bellmanFord(self, V, edges, src):
        minDist = [math.inf] * V
        minDist[src] = 0
        for i in range(V - 1):
            for start, end, weight in edges:
                if weight + minDist[start] < minDist[end]:
                    minDist[end] = weight + minDist[start]
        for start, end, weight in edges:
            if weight + minDist[start] < minDist[end]:
                return [-1]
        return [dist if dist != math.inf else 100000000 for dist in minDist]
