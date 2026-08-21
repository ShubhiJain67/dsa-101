import math
class Solution:
    def matrixMultiplication(self, arr):
        # return self.minOp(arr, 0, len(arr) - 1)
        
        # memo = [[None]*len(arr) for _ in range(len(arr))]
        # return self.minOpMemo(arr, 0, len(arr) - 1, memo)
        
        return self.minOpDP(arr)

    def minOp(self, arr, low, high):
        if low + 1 == high:
            return 0
            
        minOperations = math.inf
        for part in range(low+1, high):
            cost = (
                self.minOp(arr, low, part)
                + self.minOp(arr, part, high)
                + arr[low] * arr[part] * arr[high]
            )

            minOperations = min(minOperations, cost)

        return minOperations
        
    def minOpMemo(self, arr, low, high, memo):
        if low + 1 == high:
            return 0
        
        if memo[low][high] is not None:
            return memo[low][high]
            
        minOperations = math.inf
        for part in range(low+1, high):
            cost = (
                self.minOpMemo(arr, low, part, memo)
                + self.minOpMemo(arr, part, high, memo)
                + arr[low] * arr[part] * arr[high]
            )

            minOperations = min(minOperations, cost)
        memo[low][high] = minOperations
        return minOperations
        
    def minOpDP(self, arr):
        memo = [[None]*len(arr) for _ in range(len(arr))]
        for low in range(len(arr)-1, -1, -1):
            for high in range(low+1, len(arr)):
                minOperations = math.inf
                if low + 1 == high:
                    minOperations = 0
                else:
                    for part in range(low+1, high):
                        cost = (
                            memo[low][part]
                            + memo[part][high]
                            + arr[low] * arr[part] * arr[high]
                        )
            
                        minOperations = min(minOperations, cost)
                memo[low][high] = minOperations
        return memo[0][len(arr)-1]
        
          
