class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        # return self.prefixSumBruteForce(matrix, target)
        return self.prefixSum1DConversion(matrix, target)
    
    def prefixSum1DConversion(self, matrix, target):
        numbers = [0]*(len(matrix[0]))
        self.getRowPrefixSum(matrix)
        count = 0
        for r1 in range(len(matrix)):
            for r2 in range(r1, len(matrix)):
                for c in range(len(matrix[0])):
                    numbers[c] = matrix[r2][c]
                    if r1 > 0:
                        numbers[c] -= matrix[r1-1][c]
                currCount = self.numSubmatrixSumTarget1D(numbers, target)
                count += currCount
                # print("From {} to {} -> {}".format(r1, r2, currCount))
        return count
    
    def getRowPrefixSum(self, matrix):
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                if r > 0:
                    matrix[r][c] += matrix[r-1][c]

    def numSubmatrixSumTarget1D(self, numbers, target):
        targetMap = {0:1}
        prefixSum = 0
        count = 0
        for num in numbers:
            prefixSum += num
            if (prefixSum-target) in targetMap:
                currCount = targetMap[prefixSum-target]
                count += currCount
            if prefixSum not in targetMap:
                targetMap[prefixSum] = 0
            targetMap[prefixSum] += 1
        return count

    def prefixSumBruteForce(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        self.getPrefixSum(matrix)
        count = 0
        for sr in range(0, m):
            for sc in range(0, n):
                for er  in range(sr, m):
                    for ec in range(sc, n):
                        if self.getSum(matrix, sr, sc, er, ec) == target:
                            count += 1
        return count
    
    def getPrefixSum(self, matrix):
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                if r > 0:
                    matrix[r][c] += matrix[r-1][c]
                if c > 0:
                    matrix[r][c] += matrix[r][c-1]
                if r > 0 and c > 0:
                    matrix[r][c] -= matrix[r-1][c-1]
    
    def getSum(self, matrix, x1, y1, x2, y2):
        totalSum = matrix[x2][y2]
        if x1 > 0:
            totalSum -= matrix[x1-1][y2]
        if y1 > 0:
            totalSum -= matrix[x2][y1-1]
        if x1 > 0 and y1 > 0:
            totalSum += matrix[x1-1][y1-1]
        return totalSum
