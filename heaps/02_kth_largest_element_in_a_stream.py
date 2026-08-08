from bisect import bisect_left

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


# from bisect import bisect_left

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         nums.sort()
#         self.elements = nums
#         self.k = k

#     def add(self, val: int) -> int:
#         idx = bisect_left(self.elements, val)
#         self.elements.insert(idx, val)
#         return self.elements[-self.k]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
