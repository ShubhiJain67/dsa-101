class Solution(object):
    def matrixBlockSum(self, mat, k):
        result = [[0]*(len(mat[0])) for _ in range(len(mat))]
        self.convertPrefixSum(mat)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                x1, y1, x2, y2 = self.getCoordinates(r, c, mat, k)
                result[r][c] = self.getRangeSum(mat, x1, y1, x2, y2)
        return result

    def getCoordinates(self, x, y, mat, k):
        x1 = max(0, x-k)
        y1 = max(0, y-k)
        x2 = min(len(mat)-1, x+k)
        y2 = min(len(mat[0])-1, y+k)
        return x1, y1, x2, y2

    def convertPrefixSum(self, mat):
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r > 0:
                    mat[r][c] += mat[r-1][c]
                if c > 0:
                    mat[r][c] += mat[r][c-1]
                if r > 0 and c > 0:
                    mat[r][c] -= mat[r-1][c-1]

    def getRangeSum(self, mat, x1, y1, x2, y2):
        result = mat[x2][y2]
        if x1 > 0:
            result -= mat[x1-1][y2]
        if y1 > 0:
            result -= mat[x2][y1-1]
        if x1 > 0 and y1 > 0:
            result += mat[x1-1][y1-1]
        return result
        
