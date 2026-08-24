class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return self.slidingHeap(nums, k)
        return self.slidingDeque(nums, k)

    def slidingDeque(self, nums, k):
        dq = deque()
        maxSliding = []
        for index in range(len(nums)):
            while dq and dq[0] < index - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[index]:
                dq.pop()
            dq.append(index)
            if index >= k - 1:
                maxSliding.append(nums[dq[0]])
        return maxSliding


    def slidingHeap(self, nums, k):
        maxSliding = [0]*(len(nums)-k+1)
        maxHeap = []
        index = 0
        K = k
        while K > 0:
            maxHeap.append([-nums[index], index])
            index += 1
            K -= 1
        heapq.heapify(maxHeap)
        slidingIndex = 0
        maxSliding[slidingIndex] = -maxHeap[0][0]
        slidingIndex += 1
        while index < len(nums):
            while len(maxHeap) > 0 and index - k + 1 > maxHeap[0][1]:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, [-nums[index], index])
            maxSliding[slidingIndex] = -maxHeap[0][0]
            slidingIndex += 1
            index += 1
        return maxSliding
