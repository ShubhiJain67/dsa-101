class Solution:
    def calculateSpan(self, arr):
        # return self.intiution(arr)
        return self.optimised(arr)
        
    
    def optimised(self, arr):
        n = len(arr)
        ans = [1]*n
        stack = [-1]
        for index in range(n):
            while stack[-1] != -1 and arr[stack[-1]] <= arr[index]:
                stack.pop()
            ans[index] = index - stack[-1]
            stack.append(index)
        return ans
        
        
    def intiution(self, arr):
        n = len(arr)
        prevHigher = self.getPrevHigher(arr)
        ans = [1]*n
        for index in range(n):
            ans[index] = index - prevHigher[index]
        return ans
        
    def getPrevHigher(self, arr):
        n = len(arr)
        prevHigher = [-1]*n
        stack = [-1]
        for index in range(n):
            while stack[-1] != -1 and arr[stack[-1]] <= arr[index]:
                stack.pop()
            prevHigher[index] = stack[-1]
            stack.append(index)
        return prevHigher
