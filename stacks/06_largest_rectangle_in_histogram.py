class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nextSmaller = self.getNextSmaller(heights)
        prevSmaller = self.getPrevSmaller(heights)
        maxArea = 0
        for index in range(len(heights)):
            height = heights[index]
            width = nextSmaller[index] - prevSmaller[index] - 1
            area = height * width
            maxArea = max(maxArea, area)
            # print(f"-> {prevSmaller[index]}:{nextSmaller[index]} -> {height * width}")

        return maxArea

    def getNextSmaller(self, heights):
        n = len(heights)
        nextSmaller = [-1]*n
        stack = [n]
        for index in range(n-1, -1, -1):
            while stack[-1] != n and heights[stack[-1]] >= heights[index]:
                stack.pop()
            nextSmaller[index] = stack[-1]
            stack.append(index)
        return nextSmaller

    def getPrevSmaller(self, heights):
        n = len(heights)
        prevSmaller = [-1]*n
        stack = [-1]
        for index in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[index]:
                stack.pop()
            prevSmaller[index] = stack[-1]
            stack.append(index)
        return prevSmaller


    def bruteForce(self, heights):
        maxArea = 0
        for start in range(len(heights)):
            prevArea = 0
            currArea = 0
            for end in range(start, len(heights)):
                prevArea = currArea
                currArea = self.getArea(heights, start, end)
                maxArea = max(maxArea, currArea)
                if prevArea > currArea:
                    break
                
        return maxArea
    
    def getArea(self, heights, start, end):
        minHeight = math.inf
        for index in range(start, end+1):
            minHeight = min(minHeight, heights[index])        
        return minHeight * (end - start + 1)

    def getMin(self, heights):
        minHeights = [-1]*len(heights)
        minHeight = 10001
        for index in range(len(heights)-1, -1, -1):
            minHeight = min(minHeight, heights[index])
            minHeights[index] = index
