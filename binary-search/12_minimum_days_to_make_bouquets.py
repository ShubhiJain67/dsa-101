class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int):
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:
            mid = low + (high - low) // 2
            bouquets = self.getBouquets(bloomDay, k, mid)
            if bouquets >= m:
                high = mid
            else:
                low = mid + 1
        return low

    def getBouquets(self, bloomDay, reqFlowerCount, days):
        bloomState = [day <= days for day in bloomDay]
        flowerStatePrefix = [1 if bloomState[0] else 0]
        for index in range(1, len(bloomState)):
            flowerStatePrefix.append(flowerStatePrefix[-1]+ 1 if bloomState[index] else 0)
        bouquets = 0
        i = 0

        while i < len(bloomDay) - reqFlowerCount + 1:
            flowers = flowerStatePrefix[i + reqFlowerCount - 1] -( 0 if i == 0 else flowerStatePrefix[i-1])
            if flowers == reqFlowerCount:
                bouquets += 1
                i += reqFlowerCount
            else:
                i += 1
        return bouquets
