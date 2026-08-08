class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 0
            store[num] += 1
        
        heap = []
        for num in store:
            heap.append([-store[num], num])

        heapq.heapify(heap)
        topK = []
        while k > 0:
            topK.append(heapq.heappop(heap)[1])
            k -= 1
        return topK
