import heapq
class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        trains = sorted(zip(arr, dep))
        platforms = []
        for arrival, departure in trains:
            if platforms and platforms[0] < arrival:
                heapq.heappop(platforms)
            heapq.heappush(platforms, departure)

        return len(platforms)
