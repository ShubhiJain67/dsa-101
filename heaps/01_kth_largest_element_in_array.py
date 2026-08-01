import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapLen = len(nums)
        num = 0
        heapq.heapify(nums)
        while k <= heapLen:
            num = heapq.heappop(nums)
            k += 1
        return num
