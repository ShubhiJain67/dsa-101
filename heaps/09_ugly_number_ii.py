class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # return self.viaMinHeap(n)
        return self.viaConstantNumbers(n)
    
    def viaConstantNumbers(self, n):
        ugly = [1] * n
        i2 = i3 = i5 = 0
        
        next2 = 2
        next3 = 3
        next5 = 5

        for i in range(1, n):
            currUgly = min(next2, next3, next5)
            ugly[i] = currUgly
            if currUgly == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if currUgly == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if currUgly == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        return ugly[-1]


    def viaMinHeap(self, n):
        # Time - O(nlogm) and Space O(m)
        minHeap = [1]
        visited = set([1])
        allowedFactors = [2,3,5]
        cur_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(minHeap)

            for factor in allowedFactors:
                nextUgly = curr_ugly*factor
                if nextUgly not in visited:
                    heapq.heappush(minHeap,nextUgly)
                    visited.add(nextUgly)
        return curr_ugly
