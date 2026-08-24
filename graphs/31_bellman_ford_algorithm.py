import math
class Solution:
    def bellmanFord(self, V, edges, src):
        minDist = [math.inf] * V
        minDist[src] = 0
        for _ in range(V - 1):
            updated = False
            for start, end, weight in edges:
                if minDist[start] + weight < minDist[end]:
                    minDist[end] = minDist[start] + weight
                    updated = True
                if not updated:
                    break
        for start, end, weight in edges:
            if weight + minDist[start] < minDist[end]:
                return [-1]
        return [dist if dist != math.inf else 100000000 for dist in minDist]
