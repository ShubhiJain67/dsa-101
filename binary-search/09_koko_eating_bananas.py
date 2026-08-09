class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high-low) // 2
            hours = self.hoursNeeded(piles, mid)
            # print(f"{mid} -> {hours}")
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low
        
    def hoursNeeded(self, piles, k):
        hours = 0
        for pile in piles:
            hours += ceil(pile/k)
        return hours
        
