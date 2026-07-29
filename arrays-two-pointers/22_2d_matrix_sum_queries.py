class Solution:
    def prefixSum2D(self, mat, queries):
        prefixSum = [[0]*len(mat[0]) for _ in range(len(mat))]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                prefixSum[r][c] += mat[r][c]
                if c > 0:
                    prefixSum[r][c] += prefixSum[r][c-1]
                if r > 0:
                    prefixSum[r][c] += prefixSum[r-1][c]
                if c > 0 and r > 0:
                    prefixSum[r][c] -= prefixSum[r-1][c-1]
        allResults = []
        for query in queries:
            x1, y1, x2, y2 = query
            result = prefixSum[x2][y2]
            if x1 > 0:
                result -= prefixSum[x1-1][y2]
            if y1 > 0:
                result -= prefixSum[x2][y1-1]
            if y1 > 0 and x1 > 0:
                result += prefixSum[x1-1][y1-1]
            allResults.append(result)
        return allResults 
                
        

                      
