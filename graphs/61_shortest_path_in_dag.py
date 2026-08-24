import math

class Solution:
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        minDist = [math.inf] * V
        minDist[0] = 0
        for i in range(V - 1):
            for start, end, weight in edges:
                if minDist[start] != math.inf and weight + minDist[start] < minDist[end]:
                    minDist[end] = weight + minDist[start]
        for start, end, weight in edges:
            if weight + minDist[start] < minDist[end]:
                return [-1]
        return [dist if dist != math.inf else -1 for dist in minDist]
        
