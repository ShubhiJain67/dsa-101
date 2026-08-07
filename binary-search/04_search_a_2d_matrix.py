from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)*len(matrix[0]) - 1
        while low <= high:
            mid = low + (high-low)//2
            x, y = self.getCoordinates(mid, matrix)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
    
    def getCoordinates(self, index, matrix):
        r = len(matrix)
        c = len(matrix[0])
        x = int(index/c)
        y = index - x*c
        return x, y
