class NumMatrix(object):
    prefixSum = []

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.prefixSum = [[0]*(len(matrix[0])) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.prefixSum[r][c] = matrix[r][c]
                if r > 0:
                    self.prefixSum[r][c] += self.prefixSum[r-1][c]
                if c > 0:
                    self.prefixSum[r][c] += self.prefixSum[r][c-1]
                if r > 0 and c > 0:
                    self.prefixSum[r][c] -= self.prefixSum[r-1][c-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        total = self.prefixSum[row2][col2]
        if row1 > 0:
            total -= self.prefixSum[row1-1][col2]
        if col1 > 0:
            total -= self.prefixSum[row2][col1-1]
        if row1 > 0 and col1 > 0:
            total += self.prefixSum[row1-1][col1-1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
