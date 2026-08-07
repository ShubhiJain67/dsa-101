from typing import List
import math

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        self.getRowPrefixSum(matrix)
        numbers = [0]*(len(matrix[0]))
        maxFound = -math.inf
        for r1 in range(len(matrix)):
            for r2 in range(r1, len(matrix)):
                for c in range(len(matrix[0])):
                    numbers[c] = matrix[r2][c]
                    if r1 > 0:
                        numbers[c] -= matrix[r1-1][c]
                maxFound = self.get1DSubArraySum(numbers, k, maxFound)
        if maxFound == -math.inf:
            return -1
        return maxFound
    
    def get1DSubArraySum(self, arr, k, maxFound):
        for start in range(len(arr)):
            currSum = 0
            for end in range(start, len(arr)):
                currSum += arr[end]
                if currSum <= k:
                    maxFound = max(maxFound, currSum)
        return maxFound

    
    def getRowPrefixSum(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > 0:
                    matrix[r][c] += matrix[r-1][c]
        return matrix
