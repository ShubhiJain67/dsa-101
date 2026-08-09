class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high - low) // 2
            currDays = self.daysToShip(weights, mid)
            # print(f"With {mid} -> {days} days")
            if currDays <= days:
                high = mid
            else:
                low = mid + 1
        return low
    
    def daysToShip(self, weights, capacity):
        days = 0
        currCap = capacity
        for weight in weights:
            if weight > currCap:
                days += 1
                currCap = capacity
            currCap -= weight
        if currCap < capacity:
            days += 1
        return days
