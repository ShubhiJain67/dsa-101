class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        if len(self.leftMaxHeap) == 0 or self.leftMaxHeap[0]*-1 > num:
            heapq.heappush(self.leftMaxHeap, -num)
        else:
            heapq.heappush(self.rightMinHeap, num)
        if len(self.leftMaxHeap) > len(self.rightMinHeap) + 1:
            heapq.heappush(self.rightMinHeap, -heapq.heappop(self.leftMaxHeap))
        if len(self.rightMinHeap) > len(self.leftMaxHeap):
            heapq.heappush(self.leftMaxHeap, -heapq.heappop(self.rightMinHeap))

    def findMedian(self) -> float:
        if len(self.leftMaxHeap) == len(self.rightMinHeap):
            return (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2
        return -self.leftMaxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
