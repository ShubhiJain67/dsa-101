class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        minHeap = [intervals[0][1]]
        heapq.heapify(minHeap)
        for index in range(1, len(intervals)):
            start, end = intervals[index]
            if minHeap[0] <= start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return len(minHeap)
