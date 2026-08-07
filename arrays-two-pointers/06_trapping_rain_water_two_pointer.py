from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # return self.trapIntiution(height)
        return self.trapOptimised(height)


    def trapOptimised(self, height):
        maxRight = self.getMaxRight(height)
        index = 0
        maxSeen = 0
        water = 0
        while index < len(height):
            water += max(0, min(maxRight[index], maxSeen) - height[index])
            if height[index] > maxSeen:
                maxSeen = height[index]
            index += 1
        return water

    def trapIntiution(self, height):
        maxRight = self.getMaxRight(height)
        maxLeft = self.getMaxLeft(height)
        water = 0
        index = 0
        while index < len(height):
            water += max(0, min(maxRight[index], maxLeft[index]) - height[index])
            index += 1
        return water

    def getMaxRight(self, height):
        maxRight = [0]*len(height)
        index = len(height) - 1
        maxSeen = 0
        while index >= 0:
            maxRight[index] = maxSeen
            if height[index] > maxSeen:
                maxSeen = height[index]
            index -= 1
        return maxRight

    def getMaxLeft(self, height):
        maxLeft = [0]*len(height)
        index = 0
        maxSeen = 0
        while index < len(height):
            maxLeft[index] = maxSeen
            if height[index] > maxSeen:
                maxSeen = height[index]
            index += 1
        return maxLeft
