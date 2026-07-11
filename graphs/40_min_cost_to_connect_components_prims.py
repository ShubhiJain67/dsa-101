class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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
        minHeap = []
        pointAdded = [False]*count
        heapq.heappush(minHeap, [0,0])
        distSum = 0
        edgeCount = 0
        while edgeCount < count:
            dist, point = heapq.heappop(minHeap)
            if pointAdded[point]:
                continue
            pointAdded[point] = True
            distSum += dist
            edgeCount += 1
            for neigh, neighDist in edges[point]:
                if pointAdded[neigh]:
                    continue
                heapq.heappush(minHeap, [neighDist, neigh])
        return distSum
            
