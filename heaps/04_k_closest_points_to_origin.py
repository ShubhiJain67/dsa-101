class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heap = []
        for point in points:
            heap.append((self.dist(point), point))
        heapq.heapify(heap)
        while k > 0 and heap:
            closest.append(heapq.heappop(heap)[1])
            k -= 1
        return closest
    
    def dist(self, point):
        return math.sqrt(point[0]*point[0] + point[1]*point[1])
